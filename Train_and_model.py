import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib

# Dataset reading
data = pd.read_csv("Hyderabad.csv")

# Removing duplicates
data.drop_duplicates(inplace=True)

# Removing unwanted columns
data.drop(columns=['Location','RainWaterHarvesting','MaintenanceStaff','JoggingTrack','IndoorGames','Intercom','SportsFacility','ClubHouse','StaffQuarter','MultipurposeRoom','Cafeteria','VaastuCompliant','GolfCourse'], inplace=True)

# removing irrelevent databy replacing with NaN and then dropping them
data.replace(9, np.nan, inplace=True)
data.dropna(inplace=True)

row_index = data[data['Price'] == data['Price'].max()].index
data.drop(row_index, inplace=True)

# Selecting input and output variable
x = data.drop('Price', axis=1)
y = data['Price']
# Train test spliting
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Modelling
model = LinearRegression()
model.fit(x_train, y_train)

# Prediction
y_pred = model.predict(x_test)
r2 = r2_score(y_test, y_pred)
print(f"R-squared: {r2}")

# Saving the model
joblib.dump(model, 'model.joblib')