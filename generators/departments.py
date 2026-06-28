import pandas as pd


def generate_departments():

    departments = [

        ("HR", "Human Resources", "Trivandrum"),
        ("IT", "Information Technology", "Trivandrum"),
        ("FIN", "Finance", "Kochi"),
        ("MKT", "Marketing", "Bangalore"),
        ("OPS", "Operations", "Chennai"),
        ("QA", "Quality Assurance", "Hyderabad"),
        ("ADM", "Administration", "Trivandrum"),
        ("SALES", "Sales", "Mumbai"),
        ("RND", "Research & Development", "Bangalore"),
        ("SUP", "Customer Support", "Kochi"),

    ]

    df = pd.DataFrame(
        departments,
        columns=[
            "Department Code",
            "Department Name",
            "Location"
        ]
    )

    return df