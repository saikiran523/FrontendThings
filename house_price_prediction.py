from sklearn.linear_model import LinearRegression
import numpy as np

# House sizes in square meters
X = np.array([[50], [60], [70], [80], [90]])
# House prices in ₹ thousands
y = np.array([1500, 1800, 2100, 2400, 2700])

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Predict price of a 100 sqm house
predicted_price = model.predict([[100]])
print(f"Predicted price for 100 sqm house: ₹{predicted_price[0]:.2f}k")
