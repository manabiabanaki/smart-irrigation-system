import matplotlib.pyplot as plt

def plot_results(model, data):
    X = data[['soil_moisture', 'temperature', 'humidity']]
    y_pred = model.predict(X)
    plt.plot(data.index, y_pred, label='Predicted water')
    plt.plot(data.index, data['water_requirement'], label='Actual water')
    plt.legend()
    plt.show()
