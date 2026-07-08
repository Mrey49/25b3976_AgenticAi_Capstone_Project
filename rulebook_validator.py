import json

from rag import get_registration_context
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

def rulebook_validator_agent(state: StudentState):

    context = get_registration_context()

    llm = get_llm()

    prompt = f"""
You are an IIT Bombay Undergraduate Rulebook Expert.

You MUST answer ONLY using the UG Rulebook sections provided below.

Do NOT assume anything that is not explicitly stated.

--------------------------------------------------------
Student Information
--------------------------------------------------------

Semester:
{state["semester"]}

Current CPI:
{state["cpi"]}

Outstanding FR/DX/DR/W grade(s) in a CORE course:
{state["has_core_fr"]}

Has accumulated FR/DX worth 36 or more credits in CORE courses:
{state["core_fr_36"]}

Earned at least 18 credits in EACH of the previous two regular semesters:
{state["earned_18_previous_two"]}

Number of outstanding FR/DX grades in NON-CORE courses during the previous two regular semesters:
{state["non_core_fr_previous_two"]}

--------------------------------------------------------
Task
--------------------------------------------------------

Determine

1. Academic Standing (Category I–VI)

2. Maximum permissible registration credits

3. Minimum semester credits

IMPORTANT

• Use ONLY the UG Rulebook.

• Category VI supersedes every other category.

• Determine the category strictly according to the
  student's academic information.

Return ONLY valid JSON.

Example

{{
    "category":"Category I",

    "maximum_credits":54,

    "minimum_credits":18,

    "remarks":[
        "Category determined according to Section 5.1."
    ],

    "important_rules":[
        "Category I students may register for at most 54 credits."
    ]
}}

--------------------------------------------------------
UG Rulebook Sections
--------------------------------------------------------

{context}
"""

    response = llm.invoke(prompt)

    print("\n========== RULEBOOK AGENT ==========\n")
    print(response.content)
    print("\n===================================\n")

    try:

        rulebook = json.loads(

            clean_json(

                response.content

            )

        )

    except Exception:

        rulebook = {

            "category": "Unknown",

            "maximum_credits": 54,

            "minimum_credits": 18,

            "remarks": [

                "Unable to interpret the UG Rulebook."

            ],

            "important_rules": []

        }

    if not rulebook.get("category"):

        rulebook["category"] = "Unknown"

    if rulebook.get("maximum_credits") is None:

        rulebook["maximum_credits"] = 54

    if rulebook.get("minimum_credits") is None:

        rulebook["minimum_credits"] = 18

    if rulebook.get("remarks") is None:

        rulebook["remarks"] = []

    if rulebook.get("important_rules") is None:

        rulebook["important_rules"] = []

    rulebook["context"] = context

    state["rulebook"] = rulebook

    return state
