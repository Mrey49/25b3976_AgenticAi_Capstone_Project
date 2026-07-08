from typing import TypedDict

class StudentState(TypedDict):

    semester: int

    cpi: float

    target_credits: int

    interests: list[str]

    has_core_fr: bool

    core_fr_36: bool

    earned_18_previous_two: bool

    non_core_fr_previous_two: int

    rulebook: dict

    eligibility: dict

    compulsory_courses: list

    candidate_courses: list

    recommended_courses: list

    selected_courses: list

    rejected_courses: list

    alternative_courses: list

    clashes: list

    total_credits: int

    final_plan: dict
