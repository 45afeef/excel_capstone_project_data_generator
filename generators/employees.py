from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker("en_IN")


departments = [
    "HR",
    "IT",
    "FIN",
    "MKT",
    "OPS",
    "QA",
    "ADM",
    "SALES",
    "RND",
    "SUP"
]


designation_pool = {

    "Intern":0.08,

    "Junior Executive":0.20,

    "Executive":0.28,

    "Senior Executive":0.20,

    "Team Lead":0.10,

    "Assistant Manager":0.06,

    "Manager":0.05,

    "Senior Manager":0.03

}


designation_list = []

for title, weight in designation_pool.items():
    designation_list.extend([title] * int(weight * 100))


def employee_id(i):
    return f"EMP{i:04}"


def random_join_date():

    start = datetime(2017,1,1)

    end = datetime(2025,12,31)

    delta = end - start

    return start + timedelta(days=random.randint(0, delta.days))


def generate_employees(n=600):

    employees = []

    for i in range(1, n + 1):

        name = fake.name()

        gender = random.choice(["Male","Female"])

        dob = fake.date_of_birth(
            minimum_age=21,
            maximum_age=58
        )

        join = random_join_date()

        dept = random.choice(departments)

        designation = random.choice(designation_list)

        email = (
            name.lower()
            .replace(" ",".")
            .replace("'","")
            + "@abctech.com"
        )

        phone = fake.msisdn()[-10:]

        city = fake.city()

        emp = [

            employee_id(i),

            name,

            gender,

            dob,

            join,

            dept,

            designation,

            email,

            phone,

            city,

            random.choice([
                "Permanent",
                "Contract"
            ]),

            "Active"

        ]

        employees.append(emp)

    columns = [

        "Employee ID",

        "Employee Name",

        "Gender",

        "DOB",

        "Joining Date",

        "Department",

        "Designation",

        "Email",

        "Phone",

        "City",

        "Employment Type",

        "Status"

    ]

    return pd.DataFrame(employees, columns=columns)