import numpy as np

# Monthly sales in thousands
sales = np.array([50, 60, 55, 70, 65, 80])

# Calculate average sales
average_sales = np.mean(sales)

# Calculate growth rate (difference between months)
growth = np.diff(sales)

print("Average monthly sales:", average_sales)
print("Monthly growth:", growth)
