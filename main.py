# 2. Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 3. Loading and preparing the data
# Creating the synthetic dataset directly in the code
data = {
    'SquareFootage': [1500, 1800, 2400, 3000, 3500],
    'Price': [200000, 250000, 300000, 350000, 400000]
}

df = pd.DataFrame(data)

# We separate features (X) and target (y)
# X needs to be 2D array for sklearn, hence the double brackets
X = df[['SquareFootage']]
y = df['Price']

print("--- Data Snapshot ---")
print(df)
print("\n")

# 4. Splitting the data into training and testing sets
# We use a random_state for reproducibility (so you get the same result every time)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Training the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Deriving principles: y = mx + b
# coefficient = slope (m), intercept = bias (b)
print(f"Model Coefficient (m): {model.coef_[0]:.2f}")
print(f"Model Intercept (b): {model.intercept_:.2f}")
print("\n")

# 6. Making predictions
y_pred = model.predict(X_test)

# 7. Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("--- Evaluation Metrics ---")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R²): {r2:.2f}")

# 8. Visualizing the results
# Plotting the actual data points
plt.scatter(X, y, color='blue', label='Actual Data')

# Plotting the regression line
# We predict across the whole X range to draw the line
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')

plt.title('House Prices vs Square Footage')
plt.xlabel('Square Footage')
plt.ylabel('Price')
plt.legend()
plt.show()