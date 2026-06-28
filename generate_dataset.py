import os
import pandas as pd

from generators.departments import generate_departments
from generators.salary import generate_salary_structure
from generators.employees import generate_employees

os.makedirs("output", exist_ok=True)

with pd.ExcelWriter(
    "output/ABC_Technologies_Raw_Data.xlsx",
    engine="openpyxl"
) as writer:

    generate_departments().to_excel(
        writer,
        sheet_name="Department_Master",
        index=False
    )

    generate_salary_structure().to_excel(
        writer,
        sheet_name="Salary_Structure",
        index=False
    )

    generate_employees(600).to_excel(
        writer,
        sheet_name="Employee_Master",
        index=False
    )

print("Workbook created successfully.")