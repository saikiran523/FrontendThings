# 1️⃣ Import Libraries
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

# 2️⃣ Prepare Dataset
# X = size of house in square meters
# y = price in ₹ (thousands)
X = np.array([[50], [60], [70], [80], [90], [100], [110]])
y = np.array([1500, 1800, 2100, 2400, 2700, 3000, 3300])

# 3️⃣ Split Data (Train/Test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4️⃣ Create Model
model = LinearRegression()

# 5️⃣ Train Model
model.fit(X_train, y_train)

# 6️⃣ Make Predictions
y_pred = model.predict(X_test)

# 7️⃣ Check Predictions
print("Predicted prices:", y_pred)
print("Actual prices:", y_test)

# 8️⃣ Predict a new house price
new_house_size = np.array([[120]])
predicted_price = model.predict(new_house_size)
print(f"Predicted price for 120 sqm house: ₹{predicted_price[0]:.2f}k")
