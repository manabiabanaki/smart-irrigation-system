from sklearn.linear_model import LinearRegression

def train_model(data):
    X = data[['soil_moisture', 'temperature', 'humidity']]
    y = data['water_requirement']
    model = LinearRegression()
    model.fit(X, y)
    return model
