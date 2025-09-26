import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_excel("dataset_HR_ESG_Finance_2024.xlsx")

# 2. Preview
print("Columns:", df.columns.tolist())
print(df.head())

# 3. Query 1: Average salary by department
avg_salary = df.groupby("Department")["AvgSalary"].mean().reset_index()
print("\nAverage Salary by Department:")
print(avg_salary)

plt.figure(figsize=(8,5))
plt.bar(avg_salary["Department"], avg_salary["AvgSalary"], color="seagreen")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Avg Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Query 2: Total headcount by department
headcount = df.groupby("Department")["Headcount"].sum().reset_index()
print("\nHeadcount by Department:")
print(headcount)

plt.figure(figsize=(8,5))
plt.bar(headcount["Department"], headcount["Headcount"], color="orange")
plt.title("Headcount by Department")
plt.xlabel("Department")
plt.ylabel("Headcount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
