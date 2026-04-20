import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv("car_data.csv")

print("Dataset:\n", data.head())

# Encode categorical columns
le = LabelEncoder()

for col in ["fuel", "transmission", "owner"]:
    data[col] = le.fit_transform(data[col])

# Features & target
X = data.drop("selling_price", axis=1)
y = data["selling_price"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

# Accuracy
print("\nR2 Score:", r2_score(y_test, pred))
