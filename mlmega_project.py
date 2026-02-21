# 1️⃣ Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# import tensorflow as tf
# from tensorflow.keras.datasets import mnist
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Flatten, Dense

# ----------------------------
# 2️⃣ Dataset Creation (Synthetic)
# ----------------------------
data = pd.DataFrame({
    "CustomerID": range(1, 11),
    "Age": [25, 35, 45, 30, 50, 40, 23, 60, 33, 48],
    "Tenure": [1,5,10,3,15,7,2,20,4,12],
    "Balance": [500,1500,2000,1000,3000,2500,600,4000,1200,2800],
    "Churn": [0,0,1,0,1,1,0,1,0,1],  # Classification
    "HouseSize": [50,60,70,80,90,100,55,65,75,85],  # Regression
    "HousePrice": [1500,1800,2100,2400,2700,3000,1600,1900,2200,2500],
    "SpendingScore": [60,50,70,65,30,40,75,20,55,45],  # Clustering
    "Review": [
        "Loved the product", "Bad service", "Amazing experience",
        "Not happy", "Worst purchase", "Very satisfied",
        "Good quality", "Terrible", "Excellent", "Disappointed"
    ]  # NLP
})

# ----------------------------
# 3️⃣ Classification: Predict Churn
# ----------------------------
X_clf = data[["Age", "Tenure", "Balance"]]
y_clf = data["Churn"]
X_train, X_test, y_train, y_test = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)
clf_model = RandomForestClassifier()
clf_model.fit(X_train, y_train)
print("Churn Prediction:", clf_model.predict(X_test))

# ----------------------------
# 4️⃣ Regression: Predict House Prices
# ----------------------------
X_reg = data[["HouseSize"]]
y_reg = data["HousePrice"]
reg_model = LinearRegression()
reg_model.fit(X_reg, y_reg)
print("Predicted price for 95 sqm house:", reg_model.predict([[95]])[0])

# ----------------------------
# 5️⃣ Clustering: Market Segmentation
# ----------------------------
X_cluster = data[["Age","SpendingScore"]]
kmeans = KMeans(n_clusters=2, random_state=42)
data['Segment'] = kmeans.fit_predict(X_cluster)
print("Customer Segments:\n", data[['CustomerID','Segment']])

# ----------------------------
# 6️⃣ NLP: Sentiment Analysis of Reviews
# ----------------------------
vectorizer = CountVectorizer()
X_nlp = vectorizer.fit_transform(data["Review"])
y_nlp = np.array([1,0,1,0,0,1,1,0,1,0])  # 1=Positive, 0=Negative
nlp_model = MultinomialNB()
nlp_model.fit(X_nlp, y_nlp)
new_review = vectorizer.transform(["The product is amazing"])
print("Sentiment Prediction:", "Positive" if nlp_model.predict(new_review)[0]==1 else "Negative")

# ----------------------------
# 7️⃣ Deep Learning: MNIST Digit Recognition (Bonus)
# ----------------------------
# TensorFlow not supported in Python 3.14 yet
# (X_train_mnist, y_train_mnist), (X_test_mnist, y_test_mnist) = mnist.load_data()
# X_train_mnist, X_test_mnist = X_train_mnist/255.0, X_test_mnist/255.0
# dl_model = Sequential([
#     Flatten(input_shape=(28,28)),
#     Dense(128, activation='relu'),
#     Dense(10, activation='softmax')
# ])
# dl_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# dl_model.fit(X_train_mnist, y_train_mnist, epochs=1, batch_size=32)
# loss, acc = dl_model.evaluate(X_test_mnist, y_test_mnist)
# print("MNIST Test Accuracy:", acc)
print("Deep Learning section skipped (TensorFlow not available for Python 3.14)")

# ----------------------------
# 8️⃣ Time Series: Forecast Monthly Sales
# ----------------------------
months = np.array(range(1,13)).reshape(-1,1)
sales = np.array([50,52,55,60,65,70,72,75,78,80,85,90])
ts_model = LinearRegression()
ts_model.fit(months, sales)
print("Predicted sales for month 13:", ts_model.predict([[13]])[0])
