import matplotlib.pyplot as plt
import seaborn as sns

# Monthly sales
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [50, 60, 55, 70, 65, 80]

# Simple line plot using Matplotlib
plt.plot(months, sales, marker='o', color='blue')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (thousands)")
plt.show()

# Optional: Seaborn bar plot
sns.barplot(x=months, y=sales)
plt.title("Monthly Sales Bar Plot")
plt.show()
