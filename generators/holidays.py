import pandas as pd
from datetime import datetime


def generate_holidays():

    holidays = [

        ("New Year's Day", datetime(2025, 1, 1), "National"),
        ("Republic Day", datetime(2025, 1, 26), "National"),
        ("Maha Shivaratri", datetime(2025, 2, 26), "Festival"),
        ("Holi", datetime(2025, 3, 14), "Festival"),
        ("Good Friday", datetime(2025, 4, 18), "Festival"),
        ("Labour Day", datetime(2025, 5, 1), "National"),
        ("Bakrid", datetime(2025, 6, 7), "Festival"),
        ("Independence Day", datetime(2025, 8, 15), "National"),
        ("Onam", datetime(2025, 9, 5), "Regional"),
        ("Gandhi Jayanti", datetime(2025, 10, 2), "National"),
        ("Vijayadashami", datetime(2025, 10, 2), "Festival"),
        ("Deepavali", datetime(2025, 10, 20), "Festival"),
        ("Christmas", datetime(2025, 12, 25), "National")

    ]

    df = pd.DataFrame(
        holidays,
        columns=[
            "Holiday",
            "Date",
            "Type"
        ]
    )

    return df