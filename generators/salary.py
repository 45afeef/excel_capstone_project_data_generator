import pandas as pd


def generate_salary_structure():

    salary = [

        ("Intern",18000,10,2000,1000,12,200,5),
        ("Junior Executive",25000,15,2500,1500,12,200,8),
        ("Executive",35000,20,3000,2000,12,200,10),
        ("Senior Executive",50000,25,3500,2500,12,200,12),
        ("Team Lead",70000,30,5000,3000,12,200,15),
        ("Assistant Manager",90000,35,6000,3500,12,200,18),
        ("Manager",120000,40,8000,4000,12,200,20),
        ("Senior Manager",170000,45,10000,5000,12,200,25),

    ]

    df = pd.DataFrame(
        salary,
        columns=[
            "Designation",
            "Basic Salary",
            "HRA %",
            "Transport",
            "Medical",
            "PF %",
            "Professional Tax",
            "Bonus %"
        ]
    )

    return df