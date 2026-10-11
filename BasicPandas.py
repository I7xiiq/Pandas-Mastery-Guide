import pandas as pd
from pathlib import Path

# We use Path to get the exact location of this script.
# This ensures pandas can find 'employees.csv' in the same folder, 
# regardless of where you are running the script from in your terminal.
CSV_PATH = Path(__file__).with_name("employees.csv")


def print_section(title: str) -> None:
    """A simple helper function to print a visual divider and a heading.
    This makes the terminal output much easier to read."""
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main() -> None:
    # =====================================================================
    # 1. Series (1-Dimensional Data)
    # A Series is the simplest Pandas data structure. You can think of it 
    # as a single column in an Excel spreadsheet or a Python list with an index.
    # =====================================================================
    print_section("1. Series")
    employee_names = pd.Series(["Mona", "Ali", "Sara"])
    print(employee_names)

    # =====================================================================
    # 2. DataFrame (2-Dimensional Data)
    # A DataFrame is a 2D table with rows and columns (like a full Excel sheet).
    # The read_csv() function loads data from a CSV file directly into a DataFrame.
    # =====================================================================
    print_section("2. Read a CSV file")
    employees = pd.read_csv(CSV_PATH)
    print(employees)

    # =====================================================================
    # 3. Inspecting the Data
    # Before working with data, you need to understand its structure.
    # These functions give you quick summaries of your DataFrame.
    # =====================================================================
    print_section("3. Inspect the DataFrame")
    
    # .head() shows only the first 5 rows (useful for large datasets)
    print("First five rows:")
    print(employees.head())
    
    # .shape returns a tuple representing (number of rows, number of columns)
    print("\nShape (rows, columns):")
    print(employees.shape)
    
    # .columns gives you a list of all the column headers in your data
    print("\nColumn names:")
    print(employees.columns.tolist())
    
    # .info() shows data types (text, numbers) and if there are any missing values
    print("\nData types and non-missing values:")
    employees.info()
    
    # .describe() calculates basic math statistics (average, min, max) for numeric columns
    print("\nStatistics for numeric columns:")
    print(employees.describe())

    # =====================================================================
    # 4. Selecting Data using Integer Position (.iloc)
    # 'iloc' stands for Integer Location. It selects data based on its numerical
    # position (index), starting from 0 (just like standard Python lists).
    # =====================================================================
    print_section("4. Select data with iloc")
    print("First row:")
    print(employees.iloc[0]) # Row 0
    
    print("\nValue in the first row and second column:")
    print(employees.iloc[0, 1]) # [Row 0, Column 1]
    
    print("\nFirst two rows:")
    print(employees.iloc[0:2]) # Rows from 0 up to (but not including) 2

    # =====================================================================
    # 5. Selecting Data using Labels (.loc)
    # 'loc' stands for Location. It selects data based on the actual names 
    # of the rows (index labels) and the names of the columns.
    # =====================================================================
    print_section("5. Select data with loc")
    print("Name in the row with index label 0:")
    print(employees.loc[0, "name"]) # [Row label 0, Column named "name"]

    # =====================================================================
    # 6. Filtering Data (Conditions)
    # You can extract specific rows that meet certain True/False conditions.
    # =====================================================================
    print_section("6. Filter rows")
    
    print("Employees with a salary greater than 12,000:")
    # Returns only rows where the 'salary' column is strictly greater than 12000
    print(employees[employees["salary"] > 12000])
    
    print("\nEmployees in the Sales department:")
    # Returns only rows where the 'department' column exactly matches "Sales"
    print(employees[employees["department"] == "Sales"])
    
    print("\nIT employees with a salary greater than 16,000:")
    # Multiple conditions must be wrapped in parentheses () and connected by '&' (AND)
    it_high_earners = employees[
        (employees["department"] == "IT")
        & (employees["salary"] > 16000)
    ]
    print(it_high_earners)

    # =====================================================================
    # 7. Editing Data & Creating Columns
    # It is a good practice to create a .copy() of your data before editing 
    # to avoid modifying the original dataset accidentally.
    # =====================================================================
    print_section("7. Edit data and create calculated columns")
    updated_employees = employees.copy()
    
    # Update Mona's salary to 11000 using .loc
    updated_employees.loc[
        updated_employees["name"] == "Mona", "salary"
    ] = 11000
    
    # Create new columns by performing arithmetic operations on existing ones
    updated_employees["salary_plus_1000"] = updated_employees["salary"] + 1000
    updated_employees["double_salary"] = updated_employees["salary"] * 2
    print(updated_employees)

    # .drop() removes specific columns. We save the result to a new variable.
    print("\nDataFrame without the city column:")
    employees_without_city = employees.drop(columns=["city"])
    print(employees_without_city)

    # =====================================================================
    # 8. Handling Missing Data (NaN)
    # Real-world data is rarely perfect. Pandas represents missing data as NaN 
    # (Not a Number). We must detect and handle these gaps.
    # =====================================================================
    print_section("8. Handle missing data")
    
    # .isna().sum() counts how many missing values exist in each column
    print("Missing values in each column:")
    print(employees.isna().sum())
    
    # .dropna() removes any row that is missing data in the specified subset
    print("\nRows with a missing salary removed:")
    print(employees.dropna(subset=["salary"]))
    
    # Instead of deleting rows, we can fill missing values (.fillna) 
    # Here, we calculate the median salary and put it in the empty spots.
    employees_filled = employees.copy()
    salary_median = employees_filled["salary"].median()
    employees_filled["salary"] = employees_filled["salary"].fillna(salary_median)
    print("\nMissing salaries filled with the median:")
    print(employees_filled)

    # =====================================================================
    # 9. Counting Values
    # .value_counts() groups the data by unique values and counts them.
    # =====================================================================
    print_section("9. Count values with value_counts")
    print("Number of employees in each department:")
    print(employees["department"].value_counts())
    
    # Adding 'normalize=True' gives you the percentage (proportion) instead of the raw count
    print("\nProportion of employees in each department:")
    print(employees["department"].value_counts(normalize=True))

    # =====================================================================
    # 10. Sorting Data
    # Rearrange rows based on the values in a specific column.
    # =====================================================================
    print_section("10. Sort rows with sort_values")
    
    # Default sorting is ascending (lowest to highest). 
    # na_position="last" pushes any missing (NaN) values to the bottom.
    print("Salary from lowest to highest:")
    print(employees.sort_values(by="salary", na_position="last"))
    
    # ascending=False flips the order to descending (highest to lowest)
    print("\nSalary from highest to lowest:")
    print(
        employees.sort_values(
            by="salary", ascending=False, na_position="last"
        )
    )

    # =====================================================================
    # 11. Grouping Data (.groupby)
    # Grouping allows you to split your data into categories and calculate 
    # statistics (mean, sum, etc.) for each specific category.
    # =====================================================================
    print_section("11. Group data with groupby")
    
    # What is the average salary in each department?
    print("Average salary by department:")
    print(employees.groupby("department")["salary"].mean())
    
    # .agg() allows you to calculate multiple statistics at the exact same time
    print("\nSalary summary by department:")
    print(
        employees.groupby("department")["salary"].agg(
            ["mean", "sum", "count"]
        )
    )
    
    # .size() counts all rows in the group, including those with missing values
    print("\nNumber of rows in each department (includes missing salaries):")
    print(employees.groupby("department").size())
    
    # .count() only counts rows that actually have a value in the 'salary' column
    print("\nNumber of non-missing salaries in each department:")
    print(employees.groupby("department")["salary"].count())

    # =====================================================================
    # 12. Merging DataFrames
    # .merge() combines two different DataFrames that share a common column.
    # It works exactly like a SQL JOIN operation in databases.
    # =====================================================================
    print_section("12. Merge two DataFrames")
    
    # Create a completely separate DataFrame for Managers
    departments = pd.DataFrame(
        {
            "department": ["Sales", "IT"],
            "manager": ["Nour", "Karim"],
        }
    )
    
    # Merge the employee data with the manager data based on the 'department' column
    employees_with_managers = employees.merge(
        departments,
        on="department", # The shared column linking both tables
        how="left",      # Keep all employees, even if they don't match a manager
    )
    print(employees_with_managers)

    # =====================================================================
    # 13. Chaining Methods
    # You can combine grouping, math, and sorting into a single continuous block 
    # of code. This is very common in Pandas data analysis.
    # =====================================================================
    print_section("13. Average salary by department, highest first")
    average_salary_by_department = (
        employees.groupby("department")["salary"] # Group by department's salary
        .mean()                                   # Calculate the average
        .sort_values(ascending=False)             # Sort from highest to lowest
    )
    print(average_salary_by_department)

# This standard boilerplate ensures main() runs only if this script is executed directly.
if __name__ == "__main__":
    main()