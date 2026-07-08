import json

from rag import get_llm
from state import StudentState

def clean_json(text):

    text = text.strip()

    if text.startswith("```json"):
        text = text[7:]

    if text.startswith("```"):
        text = text[3:]

    if text.endswith("```"):
        text = text[:-3]

    return text.strip()

def invoke_llm(llm, prompt):

    last_error = None

    for attempt in range(3):

        try:

            response = llm.invoke(prompt)

            result = json.loads(

                clean_json(

                    response.content

                )

            )

            return result

        except Exception as e:

            last_error = e

            print(
                f"\nGemini attempt {attempt + 1} failed."
            )

    raise RuntimeError(

        f"Gemini failed after 3 attempts.\n{last_error}"

    )

def ranking_agent(state: StudentState):

    llm = get_llm()

    candidate_courses = state["candidate_courses"]

    if not candidate_courses:

        state["recommended_courses"] = []

        state["ranking_status"] = "no_candidates"

        state["advisor_reasoning"] = {

            "top_recommendations": [],

            "overall_advice":

            "No elective courses are available."

        }

        return state

    catalogue = []

    for course in candidate_courses:

        catalogue.append({

            "code": course["code"],

            "name": course["name"],

            "department": course["department"],

            "credits": course["credits"],

            "tags": course["tags"]

        })

    if len(state["interests"]) == 0:

        interest_text = """

The student has not specified any academic interests.

Recommend broadly useful electives having

• good academic value
• strong career prospects
• interdisciplinary usefulness
• research relevance

"""

    else:

        interest_text = ", ".join(

            state["interests"]

        )

    prompt = f"""
You are an experienced IIT Bombay Faculty Advisor.

Your task is to recommend ONLY the most relevant elective courses
for this student.

Student CPI

{state["cpi"]}

Student Interests

{interest_text}

Available Elective Courses

{json.dumps(catalogue, indent=2)}

------------------------------------------------------------

Understand the student's interests semantically.

Use the course title and course tags to determine relevance.

A recommendation is valid ONLY if there is a strong and direct
academic relationship between the student's interests and the
course title or tags.

Examples of acceptable semantic matches

AI
→ Artificial Intelligence
→ Machine Learning
→ Deep Learning
→ Computer Vision
→ NLP

Startup
→ Entrepreneurship
→ Innovation
→ Venture Creation
→ Product Development
→ Business Strategy

Maths
→ Mathematics
→ Statistics
→ Probability
→ Optimization
→ Numerical Methods

Programming
→ Software Engineering
→ Algorithms
→ Systems
→ Programming Languages

Security
→ Cryptography
→ Information Security
→ Computer Networks

Finance
→ Economics
→ Quantitative Finance
→ Financial Engineering

------------------------------------------------------------

IMPORTANT

• Recommend UP TO 15 elective courses.

• You may recommend anywhere between 0 and 15 courses.

• Never force recommendations simply to increase the number of
  recommended courses.

• If no course has a strong academic relationship with the
  student's interests, return

{{
    "recommended_courses":[]
}}

• Do NOT recommend courses based on vague, indirect or speculative
  semantic associations.

Examples of INVALID recommendations

Student Interest:
"Sex"

Do NOT recommend Molecular Biology or Biomolecules simply because
they are loosely related to biology.

Student Interest:
"Cricket"

Do NOT recommend Probability or Statistics unless the course is
explicitly about sports analytics.

Student Interest:
"Movies"

Do NOT recommend Entrepreneurship or Economics unless the course
explicitly relates to media or film studies.

------------------------------------------------------------

Read ONLY

• Course title
• Course tags

Recommend only those electives that strongly match the student's
academic interests.

Sort recommendations from BEST to WORST.

For every recommendation provide

1. code
2. score (0–100)
3. one concise reason explaining why the course is relevant.

Return ONLY valid JSON.

Example

{{
    "recommended_courses":[

        {{
            "code":"CS419",
            "score":98,
            "reason":"Excellent match for Artificial Intelligence and Machine Learning."
        }},

        {{
            "code":"DS203",
            "score":94,
            "reason":"Strong foundation for data science and AI."
        }}

    ]
}}
"""

    try:

        result = invoke_llm(

            llm,

            prompt

        )

    except Exception as e:

        print()

        print("=" * 70)

        print("Academic Advisor Agent".center(70))

        print("=" * 70)

        print()

        print(

            "⚠ The Academic Advisor Agent could not communicate "

            "with the Gemini AI service."

        )

        print()

        print(

            "Reason:"

        )

        print(

            str(e)

        )

        print()

        print(

            "Proceeding with compulsory Semester 3 courses only."

        )

        print()

        state["ranking_status"] = "gemini_failed"

        state["recommended_courses"] = []

        return state

    recommendations = result.get(

        "recommended_courses",

        []

    )

    if not recommendations:

        print()

        print("=" * 70)

        print("Academic Advisor Agent".center(70))

        print("=" * 70)

        print()

        print(

            "⚠ No suitable electives were found "

            "matching your specified interests."

        )

        print()

        print(

            "Proceeding with compulsory Semester 3 courses only."

        )

        print()

        state["ranking_status"] = "no_courses"

        state["recommended_courses"] = []

        return state

    recommendation_map = {}

    for item in recommendations:

        code = item.get("code")

        if not code:

            continue

        recommendation_map[code] = {

            "score": item.get(

                "score",

                75

            ),

            "reason": item.get(

                "reason",

                "Recommended by the Academic Advisor."

            )

        }

    ranked_courses = []

    valid_codes = {

        course["code"]

        for course in candidate_courses

    }

    for item in recommendations:

        code = item.get("code")

        if code not in valid_codes:

            continue

        original = next(

            course

            for course in candidate_courses

            if course["code"] == code

        )

        ranked = original.copy()

        ranked["score"] = recommendation_map[

            code

        ]["score"]

        ranked["reason"] = recommendation_map[

            code

        ]["reason"]

        ranked_courses.append(

            ranked

        )

    if not ranked_courses:

        print()

        print("=" * 70)

        print("Academic Advisor Agent".center(70))

        print("=" * 70)

        print()

        print(

            "Gemini returned recommendations that "

            "could not be verified."

        )

        print()

        print(

            "Reason:"

        )

        print(

            "All recommended courses were invalid or "

            "not present in the institute database."

        )

        print()

        print(

            "Proceeding with compulsory Semester 3 courses only."

        )

        print()

        state["ranking_status"] = "invalid_courses"

        state["recommended_courses"] = []

        return state

    ranked_courses.sort(

        key=lambda course: (

            course["score"],

            course["credits"]

        ),

        reverse=True

    )

    for priority, course in enumerate(

        ranked_courses,

        start=1

    ):

        course["priority"] = priority

    state["ranking_status"] = "success"

    state["recommended_courses"] = ranked_courses

    top_recommendations = []

    for course in ranked_courses[:5]:

        top_recommendations.append({

            "code": course["code"],

            "name": course["name"],

            "score": course["score"],

            "reason": course["reason"]

        })

    summary = []

    summary.append(

        "The Academic Advisor analysed the student's interests "

        "semantically and ranked the available electives."

    )

    summary.append("")

    summary.append(

        "Top Recommendations:"

    )

    for course in top_recommendations:

        summary.append(

            f"- {course['code']} "

            f"({course['score']}/100): "

            f"{course['reason']}"

        )

    state["advisor_reasoning"] = {

        "top_recommendations": top_recommendations,

        "overall_advice": "\n".join(summary)

    }

    return state
