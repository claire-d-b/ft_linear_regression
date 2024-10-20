import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error

# Data: kilometers and prices
km = np.array([240000, 139800, 150500, 185530, 176000, 114800, 166800, 
               89000, 144500, 84000, 82029, 63060, 74000, 97500, 67000, 
               76025, 48235, 93000, 60949, 65674, 54000, 68500, 22899, 61789])
price = np.array([3650, 3800, 4400, 4450, 5250, 5350, 5800, 
                  5990, 5999, 6200, 6390, 6390, 6600, 6800, 6800, 
                  6900, 6900, 6990, 7490, 7555, 7990, 7990, 7990, 8290])

# Normalize data (between 0 and 1)
km_min, km_max = km.min(), km.max()
price_min, price_max = price.min(), price.max()

km_norm = (km - km_min) / (km_max - km_min)  # Normalized kilometers
price_norm = (price - price_min) / (price_max - price_min)  # Normalized price

# Perform linear regression on normalized data to find slope (a) and intercept (b)
a_norm, b_norm = np.polyfit(km_norm, price_norm, 1)

# Predictions for normalized data
price_norm_pred = a_norm * km_norm + b_norm

# Perform linear regression on non-normalized data to find slope (a) and intercept (b)
a, b = np.polyfit(km, price, 1)

# Predictions for non-normalized data
price_pred = a * km + b

# R-squared and RMSE for normalized data
r2_norm = r2_score(price_norm, price_norm_pred)
rmse_norm = np.sqrt(mean_squared_error(price_norm, price_norm_pred))

# R-squared and RMSE for non-normalized data
r2_non_norm = r2_score(price, price_pred)
rmse_non_norm = np.sqrt(mean_squared_error(price, price_pred))

# Print the results
print(f"Normalized Data - R-squared: {r2_norm:.4f}, RMSE: {rmse_norm:.4f}")
print(f"Non-Normalized Data - R-squared: {r2_non_norm:.4f}, RMSE: {rmse_non_norm:.4f}")
