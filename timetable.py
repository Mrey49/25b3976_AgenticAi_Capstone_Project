
TIMETABLE = {

    
    # Theory Slots

    "1": [
        {"day": "Monday", "start": "08:30", "end": "09:25"},
        {"day": "Tuesday", "start": "09:30", "end": "10:25"},
        {"day": "Thursday", "start": "10:35", "end": "11:30"}
    ],

    "2": [
        {"day": "Monday", "start": "09:30", "end": "10:25"},
        {"day": "Tuesday", "start": "10:35", "end": "11:30"},
        {"day": "Thursday", "start": "11:35", "end": "12:30"}
    ],

    "3": [
        {"day": "Monday", "start": "10:35", "end": "11:30"},
        {"day": "Tuesday", "start": "11:35", "end": "12:30"},
        {"day": "Thursday", "start": "08:30", "end": "09:25"}
    ],

    "4": [
        {"day": "Monday", "start": "11:35", "end": "12:30"},
        {"day": "Tuesday", "start": "08:30", "end": "09:25"},
        {"day": "Thursday", "start": "09:30", "end": "10:25"}
    ],

    "5": [
        {"day": "Wednesday", "start": "09:30", "end": "10:55"},
        {"day": "Friday", "start": "09:30", "end": "10:55"}
    ],

    "6": [
        {"day": "Wednesday", "start": "11:05", "end": "12:30"},
        {"day": "Friday", "start": "11:05", "end": "12:30"}
    ],

    "7": [
        {"day": "Wednesday", "start": "08:30", "end": "09:25"},
        {"day": "Friday", "start": "08:30", "end": "09:25"}
    ],

    "8": [
        {"day": "Monday", "start": "14:00", "end": "15:25"},
        {"day": "Thursday", "start": "14:00", "end": "15:25"}
    ],

    "9": [
        {"day": "Monday", "start": "15:30", "end": "16:55"},
        {"day": "Thursday", "start": "15:30", "end": "16:55"}
    ],

    "10": [
        {"day": "Tuesday", "start": "14:00", "end": "15:25"},
        {"day": "Friday", "start": "14:00", "end": "15:25"}
    ],

    "11": [
        {"day": "Tuesday", "start": "15:30", "end": "16:55"},
        {"day": "Friday", "start": "15:30", "end": "16:55"}
    ],

    "12": [
        {"day": "Monday", "start": "17:30", "end": "18:55"},
        {"day": "Thursday", "start": "17:30", "end": "18:55"}
    ],

    "13": [
        {"day": "Monday", "start": "19:00", "end": "20:25"},
        {"day": "Thursday", "start": "19:00", "end": "20:25"}
    ],

    "14": [
        {"day": "Tuesday", "start": "17:30", "end": "18:55"},
        {"day": "Friday", "start": "17:30", "end": "18:55"}
    ],

    "15": [
        {"day": "Tuesday", "start": "19:00", "end": "20:25"},
        {"day": "Friday", "start": "19:00", "end": "20:25"}
    ],

    
    # Lab Slots
    
    "L1": [
        {"day": "Monday", "start": "14:00", "end": "16:55"}
    ],

    "L2": [
        {"day": "Tuesday", "start": "14:00", "end": "16:55"}
    ],

    "L3": [
        {"day": "Thursday", "start": "14:00", "end": "16:55"}
    ],

    "L4": [
        {"day": "Friday", "start": "14:00", "end": "16:55"}
    ],

    "L5": [
        {"day": "Wednesday", "start": "09:30", "end": "12:30"}
    ],

    "L6": [
        {"day": "Friday", "start": "09:30", "end": "12:30"}
    ],

    "LX": [
        {"day": "Wednesday", "start": "14:00", "end": "16:55"}
    ],

    
    # X Slots
    

    "X": [
        {"day": "Wednesday", "start": "14:00", "end": "17:00"}
    ],

    "X1": [
        {"day": "Wednesday", "start": "14:00", "end": "15:00"}
    ],

    "X2": [
        {"day": "Wednesday", "start": "15:00", "end": "16:00"}
    ],

    "X3": [
        {"day": "Wednesday", "start": "16:00", "end": "17:00"}
    ],

    "XC": [
        {"day": "Wednesday", "start": "17:30", "end": "18:55"}
    ],

    "XD": [
        {"day": "Wednesday", "start": "19:00", "end": "20:25"}
    ]

}
from datetime import datetime


def to_minutes(time):

    hours, minutes = map(int, time.split(":"))

    return hours * 60 + minutes


def get_slot(slot):

    return TIMETABLE.get(slot, [])


def get_course_schedule(course):

    schedule = []

    for slot in course["slot"]:

        schedule.extend(
            get_slot(slot)
        )

    return schedule


def get_all_slots():

    return TIMETABLE


def duration_overlap(duration1, duration2):

    if duration1 == "FirstHalf" and duration2 == "SecondHalf":
        return False

    if duration1 == "SecondHalf" and duration2 == "FirstHalf":
        return False

    return True


def is_overlap(slot1, slot2):

    if slot1["day"] != slot2["day"]:
        return False

    start1 = to_minutes(slot1["start"])
    end1 = to_minutes(slot1["end"])

    start2 = to_minutes(slot2["start"])
    end2 = to_minutes(slot2["end"])

    return max(start1, start2) < min(end1, end2)


def is_slot_clash(course1, course2):

    if not duration_overlap(
        course1["duration"],
        course2["duration"]
    ):

        return {
            "clash": False,
            "reason": "Courses are offered in different semester halves."
        }

    schedule1 = get_course_schedule(course1)
    schedule2 = get_course_schedule(course2)

    for s1 in schedule1:

        for s2 in schedule2:

            if is_overlap(s1, s2):

                overlap_start = max(
                    s1["start"],
                    s2["start"]
                )

                overlap_end = min(
                    s1["end"],
                    s2["end"]
                )

                return {

                    "clash": True,

                    "course1": course1["code"],

                    "course2": course2["code"],

                    "day": s1["day"],

                    "start": overlap_start,

                    "end": overlap_end,

                    "reason": (
                        f"{course1['code']} and "
                        f"{course2['code']} overlap on "
                        f"{s1['day']} "
                        f"from {overlap_start} to {overlap_end}."
                    )
                }

    return {

        "clash": False,

        "reason": "No timetable clash."
    }


def calculate_total_credits(course_list):

    total = 0

    for course in course_list:

        total += course["credits"]

    return total


def find_all_clashes(course_list):

    clashes = []

    n = len(course_list)

    for i in range(n):

        for j in range(i + 1, n):

            result = is_slot_clash(
                course_list[i],
                course_list[j]
            )

            if result["clash"]:

                clashes.append(result)

    return clashes


def print_schedule(course):

    print(f"\n{course['code']} : {course['name']}")

    for slot in course["slot"]:

        print(f"\nSlot {slot}")

        for timing in get_slot(slot):

            print(
                f"{timing['day']}  "
                f"{timing['start']} - {timing['end']}"
            )

def can_add_course(existing_courses, new_course):

    for course in existing_courses:

        result = is_slot_clash(
            course,
            new_course
        )

        if result["clash"]:

            return False, result

    return True, None
