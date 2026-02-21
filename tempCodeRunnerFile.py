import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Department": ["HR", "IT", "Finance"],
    "Salary": [50000, 60000, 55000]
}

df = pd.DataFrame(data)

# Filter employees with salary > 55000
high_salary = df[df["Salary"] > 55000]

print("All Employees:\n", df)
print("\nEmployees with high salary:\n", high_salary)
