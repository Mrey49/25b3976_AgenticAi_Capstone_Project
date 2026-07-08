from graph import graph

def get_yes_no(question):
    while True:
        ans = input(question).strip().lower()

        if ans in ("y", "n"):
            return ans == "y"

        print("Invalid input. Please enter only 'y' or 'n'.")


def get_float(question, minimum, maximum):
    while True:
        try:
            value = float(input(question))

            if minimum <= value <= maximum:
                return value

            print(f"Please enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Please enter a valid number.")


def get_int(question, minimum):
    while True:
        try:
            value = int(input(question))

            if value >= minimum:
                return value

            print(f"Please enter a value greater than or equal to {minimum}.")

        except ValueError:
            print("Please enter a valid integer.")


def print_line():

    print("=" * 70)


def print_heading(title):

    print()

    print_line()

    print(title.center(70))

    print_line()


def print_courses(courses):

    print()

    print(

        f"{'Code':<10}"

        f"{'Course':<40}"

        f"{'Credits':<8}"

        f"{'Type'}"

    )

    print("-" * 70)

    for course in courses:

        print(

            f"{course['code']:<10}"

            f"{course['name']:<40}"

            f"{course['credits']:<8}"

            f"{course['type']}"

        )

def main():

    print_heading(

        "IIT Bombay Semester 3 Academic Planner"

    )

    semester = 3

    print("Semester : 3 (Supported)")

    print()

    cpi = get_float(

        "Enter CPI : ",

        0,

        10

    )

    target_credits = get_int(

        "Enter Target Credits : ",

        18

    )

    print()

    interests = input(

        "Enter Interests (comma separated) : "

    ).split(",")

    interests = [

        interest.strip()

        for interest in interests

        if interest.strip()

    ]

    print()

    print_heading(

        "Academic Standing Information"

    )

    has_core_fr = get_yes_no(

        "Do you have any outstanding FR/DX/DR/W grade(s) in a CORE course? (y/n): "

    )

    core_fr_36 = get_yes_no(

        "Have you accumulated 36 or more credits worth of outstanding FR/DX grades in CORE courses? (y/n): "

    )

    earned_18_previous_two = get_yes_no(

        "Have you earned at least 18 credits in EACH of the previous two regular semesters? (y/n): "

    )

    non_core_fr_previous_two = get_int(

        "Number of outstanding FR/DX grades in NON-CORE courses during the previous two regular semesters: ",

        0

    )

    state = {

        "semester": semester,

        "cpi": cpi,

        "target_credits": target_credits,

        "interests": interests,

        "has_core_fr": has_core_fr,

        "core_fr_36": core_fr_36,

        "earned_18_previous_two": earned_18_previous_two,

        "non_core_fr_previous_two": non_core_fr_previous_two

    }

    print_heading(

        "Running Multi-Agent Workflow"

    )

    print()

    result = graph.invoke(state)

    status = result.get(

        "ranking_status",

        "success"

    )

    if status != "success":

        print_heading(

            "Academic Advisor Status"

        )

        if status == "gemini_failed":

            print(

                "The Academic Advisor Agent could not communicate "

                "with the Gemini AI service."

            )

            print()

            print("Reason:")

            print(

                "The AI recommendation service is currently unavailable "

                "due to a network issue, invalid API key, timeout, "

                "or server-side error."

            )

        elif status == "no_courses":

            print(

                "The Academic Advisor Agent successfully analysed "

                "the available elective courses."

            )

            print()

            print("Reason:")

            print(

                "No sufficiently relevant elective courses were found "

                "matching your specified academic interests."

            )

        elif status == "invalid_courses":

            print(

                "The Academic Advisor Agent generated elective "

                "recommendations that could not be verified."

            )

            print()

            print("Reason:")

            print(

                "The AI returned invalid or unsupported course codes "

                "that are not present in the institute course database."

            )

        elif status == "no_candidates":

            print(

                "No elective courses are currently available "

                "for recommendation."

            )

            print()

            print("Reason:")

            print(

                "The candidate generator did not produce any "

                "eligible elective courses."

            )

        print()

        print(

            "Therefore, the planner has generated a semester "

            "plan containing only the compulsory Semester 3 courses."

        )

        print()

        print(

            "These compulsory courses are displayed assuming "

            "you belong to Academic Category I–V."

        )

        print()

        print(

            "If you belong to Academic Category VI "

            "(Academic Rehabilitation Programme), "

            "your semester registration must be finalized "

            "in consultation with your Faculty Adviser "

            "and the Department Undergraduate Committee."

        )

        print()

    plan = result["final_plan"]

    print_heading(

        "Registration Summary"

    )

    if "category" in plan:

        print(

            f"Academic Standing  : {plan['category']}"

        )

    print(

        f"Requested Credits   : {plan['requested_credits']}"

    )

    print(

        f"Planning Credits    : {plan['planning_target']}"

    )

    print(

        f"Registered Credits  : {plan['registered_credits']}"

    )

    print(

        f"Remaining Credits   : {plan['remaining_credits']}"

    )

    print(

        f"Total Courses       : {plan['total_courses']}"

    )

    print_heading(

        "Recommended Semester Plan"

    )

    if len(

        plan["selected_courses"]

    ) == 0:

        print(

            "No automatic semester plan has been generated."

        )

    else:

        print_courses(

            plan["selected_courses"]

        )

        print()

        print(

            f"Total Registered Credits : {plan['registered_credits']}"

        )

    if len(

        plan["rejected_courses"]

    ) > 0:

        print_heading(

            "Rejected Courses"

        )

        print_courses(

            plan["rejected_courses"]

        )

    if len(

        plan["remarks"]

    ) > 0:

        print_heading(

            "Planner Remarks"

        )

        for remark in plan["remarks"]:

            print(

                f"• {remark}"

            )

    if (

        status == "success"

        and

        "advisor_reasoning" in result

    ):

        advice = result[

            "advisor_reasoning"

        ].get(

            "overall_advice",

            ""

        )

        if advice:

            print_heading(

                "AI Academic Advisor"

            )

            print(

                advice

            )

    if "rulebook" in result:

        rulebook = result["rulebook"]

        if len(

            rulebook.get(

                "important_rules",

                []

            )

        ) > 0:

            print_heading(

                "Rulebook Insights"

            )

            for rule in rulebook["important_rules"]:

                print(

                    f"• {rule}"

                )

    print()

    print_line()

    if status == "success":

        print(

            "Semester Plan Generated Successfully".center(

                70

            )

        )

    else:

        print(

            "Semester Plan Generated (Compulsory Courses Only)".center(

                70

            )

        )

    print_line()

if __name__ == "__main__":

    main()
