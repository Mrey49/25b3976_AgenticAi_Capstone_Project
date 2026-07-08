from timetable import (
    can_add_course,
    calculate_total_credits
)

from state import StudentState

def initialize_plan(state: StudentState):

    return list(

        state["compulsory_courses"]

    )


def remaining_credits(

    selected_courses,

    planning_target

):

    return (

        planning_target

        -

        calculate_total_credits(

            selected_courses

        )

    )

def find_best_alternative(

    rejected_course,

    selected_courses,

    recommended_courses

):

    for course in recommended_courses:

        if course["code"] == rejected_course["code"]:

            continue

        if any(

            c["code"] == course["code"]

            for c in selected_courses

        ):

            continue

        allowed, _ = can_add_course(

            selected_courses,

            course

        )

        if allowed:

            return course

    return None

def reject_course(

    rejected_courses,

    course,

    reason

):

    rejected = course.copy()

    rejected["reason"] = reason

    rejected_courses.append(

        rejected

    )

def add_decision(

    decision_log,

    course,

    status,

    reason

):

    decision_log.append({

        "course": course["code"],

        "status": status,

        "reason": reason

    })

def planner_step(

    state,

    selected_courses,

    rejected_courses,

    alternative_courses,

    clashes,

    decision_log

):

    planning_target = state["eligibility"]["planning_target"]

    current = calculate_total_credits(

        selected_courses

    )

    if current >= planning_target:

        return False

    for course in state["recommended_courses"]:

        if any(

            c["code"] == course["code"]

            for c in selected_courses

        ):

            continue

        if current + course["credits"] > planning_target:

            reject_course(

                rejected_courses,

                course,

                f"Adding this course would exceed the planning target "

                f"({current + course['credits']} > {planning_target})."

            )

            add_decision(

                decision_log,

                course,

                "Rejected",

                "Credit limit exceeded."

            )

            continue

        allowed, clash = can_add_course(

            selected_courses,

            course

        )

        if not allowed:

            clashes.append(

                clash

            )

            reject_course(

                rejected_courses,

                course,

                clash["reason"]

            )

            alternative = find_best_alternative(

                course,

                selected_courses,

                state["recommended_courses"]

            )

            if alternative:

                alternative_courses.append({

                    "rejected": course["code"],

                    "alternative": alternative["code"],

                    "reason":

                    "Recommended non-clashing alternative."

                })

            add_decision(

                decision_log,

                course,

                "Rejected",

                clash["reason"]

            )

            continue

        selected_courses.append(

            course

        )

        current += course["credits"]

        add_decision(

            decision_log,

            course,

            "Selected",

            course["reason"]

        )

        return True

    return False


def build_plan(state):

    selected_courses = initialize_plan(state)

    rejected_courses = []

    alternative_courses = []

    clashes = []

    decision_log = []

    decision_log.append({

        "course": "Compulsory Courses",

        "status": "Selected",

        "reason":

        "All compulsory Semester 3 courses were added automatically."

    })

    while True:

        improved = planner_step(

            state,

            selected_courses,

            rejected_courses,

            alternative_courses,

            clashes,

            decision_log

        )

        if not improved:

            break

    return {

        "selected_courses": selected_courses,

        "rejected_courses": rejected_courses,

        "alternative_courses": alternative_courses,

        "clashes": clashes,

        "decision_log": decision_log

    }

def generate_summary(

    state,

    result

):

    selected_courses = result["selected_courses"]

    registered_credits = calculate_total_credits(

        selected_courses

    )

    requested_credits = state["eligibility"]["requested_credits"]

    planning_target = state["eligibility"]["planning_target"]

    category = state["eligibility"]["category"]

    remarks = list(

        state["eligibility"]["remarks"]

    )

    compulsory_credits = calculate_total_credits(

        state["compulsory_courses"]

    )

    if (

        category != "Category VI"

        and

        requested_credits < compulsory_credits

    ):

        remarks.append(

            f"Requested credit load ({requested_credits}) is below the compulsory Semester 3 load of {compulsory_credits} credits."

        )

        remarks.append(

            "Students in Categories I-V normally require Faculty Advisor approval to register below the compulsory Semester 3 credit load."

        )

        remarks.append(

            "The planner has therefore retained all compulsory Semester 3 courses."

        )

    if (

        category != "Category VI"

        and

        registered_credits < planning_target

    ):

        remarks.append(

            f"A complete {planning_target}-credit semester plan could not be generated due to timetable clashes or course availability."

        )

        remarks.append(

            f"The best feasible semester plan contains {registered_credits} credits."

        )

    return {

        "category":

        category,

        "requested_credits":

        requested_credits,

        "planning_target":

        planning_target,

        "credits_adjusted":

        state["eligibility"]["credits_adjusted"],

        "registered_credits":

        registered_credits,

        "remaining_credits":

        max(

            0,

            planning_target

            -

            registered_credits

        ),

        "total_courses":

        len(

            selected_courses

        ),

        "selected_courses":

        sorted(

            selected_courses,

            key=lambda course: (

                course["department"],

                course["code"]

            )

        ),

        "rejected_courses":

        result["rejected_courses"],

        "alternative_courses":

        result["alternative_courses"],

        "clashes":

        result["clashes"],

        "decision_log":

        result["decision_log"],

        "remarks":

        remarks

    }

def planner_agent(

    state: StudentState

):

    category = state["eligibility"]["category"]

    compulsory_credits = calculate_total_credits(

        state["compulsory_courses"]

    )

    if category == "Category VI":

        planning_target = state["eligibility"]["planning_target"]

        remarks = list(

            state["eligibility"]["remarks"]

        )

        remarks.extend([

            "You are in Category VI (Academic Rehabilitation Programme).",

            "Maximum permissible registration is 24 credits.",

            f"Semester 3 contains {compulsory_credits} compulsory credits.",

            "The IIT Bombay UG Rules do not specify which compulsory courses should be deferred for Category VI students.",

            "Your semester registration must be finalized in consultation with your Faculty Advisor and the Department Undergraduate Committee.",

            "Automatic course planning has therefore not been performed."

        ])

        summary = {

            "category":

            category,

            "requested_credits":

            state["eligibility"]["requested_credits"],

            "planning_target":

            planning_target,

            "credits_adjusted":

            state["eligibility"]["credits_adjusted"],

            "registered_credits":

            0,

            "remaining_credits":

            planning_target,

            "total_courses":

            0,

            "selected_courses":

            [],

            "rejected_courses":

            [],

            "alternative_courses":

            [],

            "clashes":

            [],

            "decision_log":

            [],

            "remarks":

            remarks

        }

        state["selected_courses"] = []

        state["rejected_courses"] = []

        state["alternative_courses"] = []

        state["clashes"] = []

        state["total_credits"] = 0

        state["final_plan"] = summary

        return state

    result = build_plan(

        state

    )

    summary = generate_summary(

        state,

        result

    )

    state["selected_courses"] = summary["selected_courses"]

    state["rejected_courses"] = summary["rejected_courses"]

    state["alternative_courses"] = summary["alternative_courses"]

    state["clashes"] = summary["clashes"]

    state["total_credits"] = summary["registered_credits"]

    state["final_plan"] = summary

    return state
