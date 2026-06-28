import random
import pandas as pd
from datetime import datetime, timedelta


YEAR = 2025


# ------------------------------------------
# Leave Configuration
# ------------------------------------------

LEAVE_TYPE_WEIGHTS = {
    "Casual Leave": 45,
    "Sick Leave": 30,
    "Earned Leave": 15,
    "Maternity Leave": 5,
    "Paternity Leave": 3,
    "Loss of Pay": 2
}


LEAVE_STATUSES = ["Approved", "Pending", "Rejected"]


STATUS_WEIGHTS = [88, 8, 4]


REASONS = {
    "Casual Leave": [
        "Personal Work",
        "Family Function",
        "Travel",
        "Wedding Attendance"
    ],
    "Sick Leave": [
        "Viral Fever",
        "Food Poisoning",
        "Medical Appointment",
        "Migraine"
    ],
    "Earned Leave": [
        "Vacation",
        "Family Trip",
        "Festival Celebration"
    ],
    "Maternity Leave": [
        "Maternity"
    ],
    "Paternity Leave": [
        "Newborn Care"
    ],
    "Loss of Pay": [
        "Unauthorized Absence"
    ]
}


# ------------------------------------------
# Helpers
# ------------------------------------------

def random_date(start_date, end_date):
    delta = end_date - start_date
    return start_date + timedelta(days=random.randint(0, delta.days))


def get_leave_type():
    return random.choices(
        list(LEAVE_TYPE_WEIGHTS.keys()),
        weights=list(LEAVE_TYPE_WEIGHTS.values()),
        k=1
    )[0]


def get_status():
    return random.choices(
        LEAVE_STATUSES,
        weights=STATUS_WEIGHTS,
        k=1
    )[0]


def get_reason(leave_type):
    return random.choice(REASONS[leave_type])


def yearly_leave_quota():
    """
    Determines how many total leave applications an employee may take in a year.
    """
    r = random.random()

    if r < 0.18:
        return random.randint(0, 2)
    elif r < 0.60:
        return random.randint(3, 6)
    elif r < 0.88:
        return random.randint(7, 12)
    elif r < 0.97:
        return random.randint(13, 18)
    else:
        return random.randint(19, 25)


# ------------------------------------------
# Main Generator
# ------------------------------------------

def generate_leave_records(employee_df):

    rows = []
    leave_id = 1

    start_year = datetime(YEAR, 1, 1)
    end_year = datetime(YEAR, 12, 31)

    for emp_id in employee_df["Employee ID"]:

        total_leaves = yearly_leave_quota()

        for _ in range(total_leaves):

            leave_type = get_leave_type()

            # maternity/paternity only for realism control
            if leave_type == "Maternity Leave" and random.random() > 0.5:
                continue

            start_date = random_date(start_year, end_year)

            duration = random.randint(1, 5)

            end_date = start_date + timedelta(days=duration)

            status = get_status()

            reason = get_reason(leave_type)

            rows.append([
                f"LV{leave_id:06}",
                emp_id,
                leave_type,
                start_date.date(),
                end_date.date(),
                duration,
                status,
                reason
            ])

            leave_id += 1

    df = pd.DataFrame(
        rows,
        columns=[
            "Leave ID",
            "Employee ID",
            "Leave Type",
            "Start Date",
            "End Date",
            "Days",
            "Status",
            "Reason"
        ]
    )

    return df