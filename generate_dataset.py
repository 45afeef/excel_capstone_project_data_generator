import os
import pandas as pd

from generators.departments import generate_departments
from generators.salary import generate_salary_structure
from generators.employees import generate_employees
from generators.holidays import generate_holidays
from generators.leave import generate_leave_records
from generators.attendance import generate_attendance


# ------------------------------------------
# Create Output Folder
# ------------------------------------------

os.makedirs("output", exist_ok=True)

output_path = "output/ABC_Technologies_Raw_Data.xlsx"


# ------------------------------------------
# GENERATE DATA (ORDER IS IMPORTANT)
# ------------------------------------------

print("Generating Departments...")
departments = generate_departments()

print("Generating Salary Structure...")
salary = generate_salary_structure()

print("Generating Employees...")
employees = generate_employees(600)

print("Generating Holidays...")
holidays = generate_holidays()

print("Generating Leave Records...")
leave = generate_leave_records(employees)

print("Generating Attendance (Leave + Holiday Aware)...")
attendance = generate_attendance(
    employees,
    holidays,
    leave
)


# ------------------------------------------
# WRITE TO EXCEL (WRITER BLOCK)
# ------------------------------------------

with pd.ExcelWriter(output_path, engine="openpyxl") as writer:

    # --------------------------
    # Master Data
    # --------------------------

    departments.to_excel(
        writer,
        sheet_name="Department_Master",
        index=False
    )

    salary.to_excel(
        writer,
        sheet_name="Salary_Structure",
        index=False
    )

    employees.to_excel(
        writer,
        sheet_name="Employee_Master",
        index=False
    )

    # --------------------------
    # Time & HR Events
    # --------------------------

    holidays.to_excel(
        writer,
        sheet_name="Holiday_List",
        index=False
    )

    leave.to_excel(
        writer,
        sheet_name="Leave_Records",
        index=False
    )

    attendance.to_excel(
        writer,
        sheet_name="Attendance",
        index=False
    )


# ------------------------------------------
# DONE
# ------------------------------------------

print(f"Workbook created successfully at: {output_path}")