import random
import pandas as pd


def generate_performance_reviews(employee_df, attendance_df, leave_df):

    rows = []
    review_id = 1

    # ------------------------------------------
    # Pre-calculate attendance summary
    # ------------------------------------------

    attendance_summary = attendance_df.groupby("Employee ID").agg(
        total_days=("Attendance ID", "count"),
        present_days=("Attendance Status", lambda x: (x == "Present").sum()),
        wfh_days=("Attendance Status", lambda x: (x == "WFH").sum()),
        leave_days=("Attendance Status", lambda x: (x == "Leave").sum()),
        absent_days=("Attendance Status", lambda x: (x == "Absent").sum())
    ).reset_index()

    # ------------------------------------------
    # Loop employees
    # ------------------------------------------

    for emp_id in employee_df["Employee ID"]:

        record = attendance_summary[
            attendance_summary["Employee ID"] == emp_id
        ]

        if record.empty:
            continue

        record = record.iloc[0]

        total = record["total_days"]

        present = record["present_days"] + record["wfh_days"]

        leave = record["leave_days"]

        absent = record["absent_days"]

        # Avoid division error
        attendance_pct = (present / total) * 100 if total > 0 else 0

        # ------------------------------------------
        # Performance Score Logic (REALISTIC MODEL)
        # ------------------------------------------

        score = 0

        # Attendance contribution
        if attendance_pct >= 95:
            score += 40
        elif attendance_pct >= 90:
            score += 35
        elif attendance_pct >= 80:
            score += 25
        elif attendance_pct >= 70:
            score += 15
        else:
            score += 5

        # Leave penalty
        if leave <= 5:
            score += 20
        elif leave <= 10:
            score += 15
        elif leave <= 15:
            score += 10
        else:
            score += 5

        # Absenteeism penalty
        if absent <= 2:
            score += 20
        elif absent <= 5:
            score += 15
        elif absent <= 10:
            score += 10
        else:
            score += 5

        # Random productivity factor (real-world noise)
        score += random.randint(0, 15)

        # Cap score
        score = min(score, 100)

        # ------------------------------------------
        # Rating Assignment
        # ------------------------------------------

        if score >= 85:
            rating = "Excellent"
        elif score >= 70:
            rating = "Good"
        elif score >= 50:
            rating = "Average"
        else:
            rating = "Poor"

        # ------------------------------------------
        # Manager Comments
        # ------------------------------------------

        comments_map = {
            "Excellent": "Outstanding performance. Highly recommended for promotion.",
            "Good": "Consistent performer with strong reliability.",
            "Average": "Meets expectations but needs improvement in consistency.",
            "Poor": "Performance below expectations. Requires improvement plan."
        }

        comments = comments_map[rating]

        # ------------------------------------------
        # Append row
        # ------------------------------------------

        rows.append([
            f"PR{review_id:06}",
            emp_id,
            attendance_pct,
            leave,
            absent,
            score,
            rating,
            comments
        ])

        review_id += 1

    df = pd.DataFrame(
        rows,
        columns=[
            "Review ID",
            "Employee ID",
            "Attendance %",
            "Leave Days",
            "Absent Days",
            "Performance Score",
            "Rating",
            "Manager Comments"
        ]
    )

    return df