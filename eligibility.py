from database import get_compulsory_courses
from state import StudentState


def eligibility_agent(state: StudentState):

    semester = state["semester"]

    requested_credits = state["target_credits"]

    rulebook = state["rulebook"]

    compulsory_courses = get_compulsory_courses()

    compulsory_credits = sum(

        course["credits"]

        for course in compulsory_courses

    )

    category = rulebook.get(

        "category",

        "Unknown"

    )

    maximum_credits = rulebook.get(

        "maximum_credits",

        54

    )

    minimum_credits = rulebook.get(

        "minimum_credits",

        18

    )

    remarks = list(

        rulebook.get(

            "remarks",

            []

        )

    )

    planning_target = requested_credits

    credits_adjusted = False

    if requested_credits > maximum_credits:

        planning_target = maximum_credits

        credits_adjusted = True

        remarks.append(

            f"You requested {requested_credits} credits."

        )

        remarks.append(

            f"The maximum permissible registration load for {category} is {maximum_credits} credits."

        )

        remarks.append(

            f"The planner will generate the best possible semester plan using {planning_target} credits."

        )

    if planning_target < minimum_credits:

        remarks.append(

            f"Registration below {minimum_credits} credits requires Faculty Adviser approval."

        )

    eligible = True

    if planning_target < compulsory_credits:

        eligible = False

        remarks.append(

            f"Semester {semester} contains {compulsory_credits} compulsory credits."

        )

    state["compulsory_courses"] = compulsory_courses

    state["eligibility"] = {

        "eligible": eligible,

        "category": category,

        "semester": semester,

        "requested_credits": requested_credits,

        "planning_target": planning_target,

        "credits_adjusted": credits_adjusted,

        "maximum_credits": maximum_credits,

        "minimum_credits": minimum_credits,

        "compulsory_credits": compulsory_credits,

        "remaining_credits": max(

            0,

            planning_target - compulsory_credits

        ),

        "remarks": remarks

    }

    state["target_credits"] = planning_target

    return state
