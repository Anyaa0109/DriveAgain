# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib

# 1. Load the Dataset
car_dataset = pd.read_csv(r"C:\Users\KIIT\Downloads\archive (2)\car data.csv")

# Inspect dataset
print("\nDataset Info:")
car_dataset.info()

# Check for missing values
print("\nNumber of missing values in each column:")
print(car_dataset.isnull().sum())

# Encode categorical variables
car_dataset.replace({'Fuel_Type': {'Petrol': 0, 'Diesel': 1, 'CNG': 2}}, inplace=True)
car_dataset.replace({'Seller_Type': {'Dealer': 0, 'Individual': 1}}, inplace=True)
car_dataset.replace({'Transmission': {'Manual': 0, 'Automatic': 1}}, inplace=True)

# Define features (X) and target (Y)
X = car_dataset.drop(['Car_Name', 'Selling_Price'], axis=1)
Y = car_dataset['Selling_Price']

# 2. Split the Data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=2)

# 3. Train Linear Regression Model
lin_reg_model = LinearRegression()
lin_reg_model.fit(X_train, Y_train)

# Save the model
joblib.dump(lin_reg_model, 'linear_reg_model.pkl')
print("\nLinear Regression model saved as 'linear_reg_model.pkl'.")

# Evaluate Linear Regression
train_pred_lin = lin_reg_model.predict(X_train)
test_pred_lin = lin_reg_model.predict(X_test)

# Metrics for Linear Regression
train_r2_lin = r2_score(Y_train, train_pred_lin)
test_r2_lin = r2_score(Y_test, test_pred_lin)
mae_lin = mean_absolute_error(Y_test, test_pred_lin)
mse_lin = mean_squared_error(Y_test, test_pred_lin)
rmse_lin = mean_squared_error(Y_test, test_pred_lin, squared=False)

print("\nLinear Regression Evaluation:")
print(f"R-squared (Train): {train_r2_lin:.4f}")
print(f"R-squared (Test): {test_r2_lin:.4f}")
print(f"Mean Absolute Error (MAE): {mae_lin:.4f}")
print(f"Mean Squared Error (MSE): {mse_lin:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse_lin:.4f}")

# Plot Actual vs Predicted (Linear Regression)
plt.figure(figsize=(6, 6))
plt.scatter(Y_test, test_pred_lin, color='blue', alpha=0.7)
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], 'r')
plt.title("Linear Regression: Actual vs Predicted (Test Data)")
plt.xlabel("Actual Selling Price")
plt.ylabel("Predicted Selling Price")
plt.show()

# 4. Train Lasso Regression Model
lasso_reg_model = Lasso(alpha=1.0)  # Alpha controls regularization strength
lasso_reg_model.fit(X_train, Y_train)

# Evaluate Lasso Regression
train_pred_lasso = lasso_reg_model.predict(X_train)
test_pred_lasso = lasso_reg_model.predict(X_test)

# Metrics for Lasso Regression
train_r2_lasso = r2_score(Y_train, train_pred_lasso)
test_r2_lasso = r2_score(Y_test, test_pred_lasso)
mae_lasso = mean_absolute_error(Y_test, test_pred_lasso)
mse_lasso = mean_squared_error(Y_test, test_pred_lasso)
rmse_lasso = mean_squared_error(Y_test, test_pred_lasso, squared=False)

print("\nLasso Regression Evaluation:")
print(f"R-squared (Train): {train_r2_lasso:.4f}")
print(f"R-squared (Test): {test_r2_lasso:.4f}")
print(f"Mean Absolute Error (MAE): {mae_lasso:.4f}")
print(f"Mean Squared Error (MSE): {mse_lasso:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse_lasso:.4f}")

# Plot Actual vs Predicted (Lasso Regression)
plt.figure(figsize=(6, 6))
plt.scatter(Y_test, test_pred_lasso, color='red', alpha=0.7)
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], 'r')
plt.title("Lasso Regression: Actual vs Predicted (Test Data)")
plt.xlabel("Actual Selling Price")
plt.ylabel("Predicted Selling Price")
plt.show()