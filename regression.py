from sklearn.linear_model import LinearRegression
import numpy as np

# Input data
X = np.array([[1], [2], [3], [4]])
y = np.array([3, 5, 7, 9])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[5]])
print(prediction)
