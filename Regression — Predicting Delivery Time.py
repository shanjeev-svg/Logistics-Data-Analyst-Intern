from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
 
features = ['distance_km', 'traffic_index', 'hour_of_day', 'agent_experience_yrs']
X = df[features]
y = df['delivery_time_min']
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
preds = model.predict(X_test)
print('MAE (minutes):', mean_absolute_error(y_test, preds))
