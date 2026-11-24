import pandas as pd
#==============================
#======1-Load Dataset============
#==============================

df=pd.read_csv(r"F:\My Downloads\cmder_mini\Libraries\employees.csv")

#==============================
#======2-Data Exploration======
#==============================
print("First Five rows :\n")
print(df.head())

print("Last Five rows:\n")
print(df.tail())

print("Dataset Information:\n")
df.info()

print("Numerical Statistics:\n")
print(df.describe())

print("Categorical Statistics:\n")
print(df.describe(include="str"))
print("All Statistics:\n")
print(df.describe(include="all"))

# =========================
# 3-Data Type Conversion
# =========================
df["Joining_Date"]=pd.to_datetime(df["Joining_Date"])

# =========================
# 4-Data Filtering
# =========================

# Employees who joined after 2020
Employees_Joined_after2020=df[df["Joining_Date"]>"2020-01-01"]
print("Employees Joined after 2020 are:\n",Employees_Joined_after2020.Name)

# Employees with salary greater than 60,000
Salarymorethan60000=df[df["Salary"]>60000][["Name","Department","Salary"]]
print(Salarymorethan60000)

# =========================
# 5. Salary Analysis
# =========================
Average_salary_fordepartment=df.groupby("Department")["Salary"].mean()
print(f"Average Salary for each department is :\n{Average_salary_fordepartment}") 

# Maximum salary
print(f'The max Salary is {df["Salary"].max()}')

# Minimum salary
print(f'The min Salary is {df["Salary"].min()}')

# =========================
# 6- Age Analysis
# =========================
AverageofAge=df.groupby("Department")["Age"].mean()
print(AverageofAge)

# =========================
# 7-Employee Sorting
# =========================
# Order of Employees from highest salary to lowest 
Order_Of_Employees=df.sort_values("Salary",ascending=False)
print(f" Order of Employees from highest salary to lowest :\n{Order_Of_Employees[["Name","Salary"]]}")


# =========================
# 8-Employee Count
# =========================
#Number of employees in each department
Number_of_Employees=df.groupby("Department")["Age"].count()
print(Number_of_Employees)

# =========================
# 9- Data Quality Checks
# =========================
print(df.isnull().sum())
print(df.duplicated().sum())


