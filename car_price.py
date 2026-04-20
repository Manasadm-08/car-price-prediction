import pandas as pd
import numpy as np

np.random.seed(42)

n = 10000

data = pd.DataFrame({
    "year": np.random.randint(2005, 2023, n),
    "km_driven": np.random.randint(5000, 200000, n),
    "fuel": np.random.choice(["Petrol", "Diesel", "CNG"], n),
    "transmission": np.random.choice(["Manual", "Automatic"], n),
    "owner": np.random.choice(["First Owner", "Second Owner", "Third Owner"], n),
    "mileage": np.random.randint(10, 25, n),
    "engine": np.random.randint(800, 3000, n),
    "max_power": np.random.randint(40, 200, n),
    "seats": np.random.randint(4, 8, n)
})

# Generate price (depends on features)
data["selling_price"] = (
    data["year"] * 5000
    - data["km_driven"] * 2
    + data["engine"] * 300
    + data["max_power"] * 1000
    + np.random.randint(-50000, 50000, n)
)

# Save file
data.to_csv("car_data.csv", index=False)

print("Dataset created successfully!")
