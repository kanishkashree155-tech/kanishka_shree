import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle
df = pd.read_csv("flight_delay_dataset.csv")
print(df.columns)
X = df[["route_distance_km", "weather_score", "departure_hour", "wind_speed", "destination_traffic", "weekend"]]
y = df["delay"]
model = DecisionTreeClassifier()
model.fit(X, y)
pickle.dump(model, open("flight_delay_model.pkl", "wb"))
print("Model trained and saved as flight_delay_model.pkl")
