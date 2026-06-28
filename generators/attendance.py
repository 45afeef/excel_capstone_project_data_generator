# generators/attendance.py

import random
import pandas as pd
from datetime import datetime, timedelta


# ------------------------------------------
# Company Configuration
# ------------------------------------------

YEAR = 2026

OFFICE_START_HOUR = 9
OFFICE_END_HOUR = 18


# ------------------------------------------
# Helper Functions
# ------------------------------------------

def random_time(base_hour, base_minute, variation):
    base = datetime(YEAR, 1, 1, base_hour, base_minute)
    delta = timedelta(minutes=random.randint(-variation, variation))
    return (base + delta).time()


def is_weekend(date):
    return date.weekday() >= 5


def is_holiday(date, holidays_df):
    return date in set(holidays_df["Date"])


def is_on_leave(emp_id, date, leave_df):
    """
    Check if employee is on approved leave on a given date
    """
    emp_leaves = leave_df[
        (leave_df["Employee ID"] == emp_id) &
        (leave_df["Status"] == "Approved")
    ]

    for _, row in emp_leaves.iterrows():
        if row["Start Date"] <= date <= row["End Date"]:
            return True

    return False


# ------------------------------------------
# Main Generator
# ------------------------------------------

def generate_attendance(employee_df, holidays_df, leave_df):

    rows = []
    attendance_id = 1

    start_date = datetime(YEAR, 3, 1)
    end_date = datetime(YEAR, 5, 31)
    

    all_dates = pd.date_range(start_date, end_date)

    # Keep only weekdays
    working_days = [d for d in all_dates if d.weekday() < 5]

    for current_date in working_days:

        date_only = current_date.date()

        for emp_id in employee_df["Employee ID"]:

            status = None
            check_in = None
            check_out = None
            remark = "Normal"

            # ------------------------------------------
            # PRIORITY CHECKS (REAL HR LOGIC)
            # ------------------------------------------

            if is_holiday(date_only, holidays_df):
                continue  # skip attendance entry on holidays

            if is_on_leave(emp_id, date_only, leave_df):
                status = "Leave"
                remark = "Approved Leave"

            else:

                # ------------------------------------------
                # Normal Attendance Probability
                # ------------------------------------------

                status = random.choices(
                    [
                        "Present",
                        "WFH",
                        "Half Day",
                        "Absent"
                    ],
                    weights=[85, 8, 5, 2],
                    k=1
                )[0]

                # ------------------------------------------
                # Present / WFH
                # ------------------------------------------

                if status in ["Present", "WFH"]:

                    check_in = random_time(9, 0, 25)
                    check_out = random_time(18, 0, 40)

                    # Late arrival
                    if random.random() < 0.08:
                        check_in = random_time(9, 45, 20)
                        remark = "Late Arrival"

                    # Overtime
                    if random.random() < 0.10:
                        check_out = random_time(20, 0, 30)
                        remark = "Overtime"

                    # Missing checkout (real HR issue)
                    if random.random() < 0.02:
                        check_out = None
                        remark = "Missing Check Out"

                # ------------------------------------------
                # Half Day
                # ------------------------------------------

                elif status == "Half Day":
                    check_in = random_time(9, 0, 20)
                    check_out = random_time(13, 0, 20)
                    remark = "Half Day"

                # ------------------------------------------
                # Absent
                # ------------------------------------------

                elif status == "Absent":
                    check_in = None
                    check_out = None
                    remark = "Absent"

            # ------------------------------------------
            # Append Row
            # ------------------------------------------
            
            rows.append([
                f"ATT{attendance_id:07}",
                date_only,
                emp_id,
                check_in,
                check_out,
                status,
                remark,

                "",  # Working Hours (Excel formula)
                "",  # Late Minutes (Excel formula)
                ""   # Overtime Hours (Excel formula)
            ])

            attendance_id += 1
   
    df = pd.DataFrame(
        rows,
        columns=[
            "Attendance ID",
            "Date",
            "Employee ID",
            "Check In",
            "Check Out",
            "Attendance Status",
            "Remarks",
            "Working Hours",
            "Late Minutes",
            "Overtime Hours"
        ]
    )

    return df