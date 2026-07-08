from database import COURSES
from state import StudentState

def candidate_generator_agent(state: StudentState):

    compulsory_codes = {

        course["code"]

        for course in state["compulsory_courses"]

    }

    candidate_courses = []

    for course in COURSES.values():

        if course["code"] in compulsory_codes:

            continue

        if course["type"] == "Compulsory":

            continue

        candidate_courses.append(

            course.copy()

        )

    candidate_courses.sort(

        key=lambda course: (

            course["credits"],

            course["code"]

        ),

        reverse=True

    )

    state["candidate_courses"] = candidate_courses

    return state
