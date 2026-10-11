import pandas as pd
from pathlib import Path


# Keep the sample CSV next to this script so it runs from any working directory.
CSV_PATH = Path(__file__).with_name("employees.csv")


def print_section(title: str) -> None:
    """Print a clear heading before each pandas example."""
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main() -> None:
    # Create a Series, which is a one-dimensional labeled data structure.
    print_section("1. Series")
    employee_names = pd.Series(["Mona", "Ali", "Sara"])
    print(employee_names)

    # Read a CSV file into a DataFrame, which is a two-dimensional table.
    print_section("2. Read a CSV file")
    employees = pd.read_csv(CSV_PATH)
    print(employees)

    # Inspect the shape, column names, data types, and basic statistics.
    print_section("3. Inspect the DataFrame")
    print("First five rows:")
    print(employees.head())
    print("\nShape (rows, columns):")
    print(employees.shape)
    print("\nColumn names:")
    print(employees.columns.tolist())
    print("\nData types and non-missing values:")
    employees.info()
    print("\nStatistics for numeric columns:")
    print(employees.describe())

    # Select rows and cells by integer position with iloc.
    print_section("4. Select data with iloc")
    print("First row:")
    print(employees.iloc[0])
    print("\nValue in the first row and second column:")
    print(employees.iloc[0, 1])
    print("\nFirst two rows:")
    print(employees.iloc[0:2])

    # Select a value by its index label and column name with loc.
    print_section("5. Select data with loc")
    print("Name in the row with index label 0:")
    print(employees.loc[0, "name"])

    # Filter rows using one or more Boolean conditions.
    print_section("6. Filter rows")
    print("Employees with a salary greater than 12,000:")
    print(employees[employees["salary"] > 12000])
    print("\nEmployees in the Sales department:")
    print(employees[employees["department"] == "Sales"])
    print("\nIT employees with a salary greater than 16,000:")
    it_high_earners = employees[
        (employees["department"] == "IT")
        & (employees["salary"] > 16000)
    ]
    print(it_high_earners)

    # Make a copy before changing data so the original DataFrame stays unchanged.
    print_section("7. Edit data and create calculated columns")
    updated_employees = employees.copy()
    updated_employees.loc[
        updated_employees["name"] == "Mona", "salary"
    ] = 11000
    updated_employees["salary_plus_1000"] = updated_employees["salary"] + 1000
    updated_employees["double_salary"] = updated_employees["salary"] * 2
    print(updated_employees)

    # Drop a column by creating a new DataFrame without that column.
    print("\nDataFrame without the city column:")
    employees_without_city = employees.drop(columns=["city"])
    print(employees_without_city)

    # Find missing values, remove rows with missing salaries, or fill them with the median.
    print_section("8. Handle missing data")
    print("Missing values in each column:")
    print(employees.isna().sum())
    print("\nRows with a missing salary removed:")
    print(employees.dropna(subset=["salary"]))
    employees_filled = employees.copy()
    salary_median = employees_filled["salary"].median()
    employees_filled["salary"] = employees_filled["salary"].fillna(salary_median)
    print("\nMissing salaries filled with the median:")
    print(employees_filled)

    # Count each distinct value in a column, or show its share of all values.
    print_section("9. Count values with value_counts")
    print("Number of employees in each department:")
    print(employees["department"].value_counts())
    print("\nProportion of employees in each department:")
    print(employees["department"].value_counts(normalize=True))

    # Sort rows by a column's values in ascending or descending order.
    print_section("10. Sort rows with sort_values")
    print("Salary from lowest to highest:")
    print(employees.sort_values(by="salary", na_position="last"))
    print("\nSalary from highest to lowest:")
    print(
        employees.sort_values(
            by="salary", ascending=False, na_position="last"
        )
    )

    # Group rows by department and calculate summary statistics for each group.
    print_section("11. Group data with groupby")
    print("Average salary by department:")
    print(employees.groupby("department")["salary"].mean())
    print("\nSalary summary by department:")
    print(
        employees.groupby("department")["salary"].agg(
            ["mean", "sum", "count"]
        )
    )
    print("\nNumber of rows in each department (includes missing salaries):")
    print(employees.groupby("department").size())
    print("\nNumber of non-missing salaries in each department:")
    print(employees.groupby("department")["salary"].count())

    # Join two DataFrames using a shared key, similar to a SQL JOIN.
    print_section("12. Merge two DataFrames")
    departments = pd.DataFrame(
        {
            "department": ["Sales", "IT"],
            "manager": ["Nour", "Karim"],
        }
    )
    employees_with_managers = employees.merge(
        departments,
        on="department",
        how="left",
    )
    print(employees_with_managers)

    # Combine grouping and sorting to rank departments by average salary.
    print_section("13. Average salary by department, highest first")
    average_salary_by_department = (
        employees.groupby("department")["salary"]
        .mean()
        .sort_values(ascending=False)
    )
    print(average_salary_by_department)


if __name__ == "__main__":
    main()
