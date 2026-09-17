import numpy as np
from sklearn.ensemble import IsolationForest

# Normal production data
normal_data = np.array([
    [25, 50, 7.0],
    [26, 52, 7.1],
    [24, 48, 6.9],
    [27, 51, 7.2],
    [25, 49, 7.0],
    [26, 50, 7.1],
    [24, 51, 6.8],
    [27, 53, 7.2]
])

# Train anomaly detection model
model = IsolationForest(
    contamination=0.1,
    random_state=42
)

model.fit(normal_data)


def detect_anomaly(temperature, humidity, ion_concentration):
    data = np.array([[temperature, humidity, ion_concentration]])

    prediction = model.predict(data)

    if prediction[0] == -1:
        return "Anomaly Detected"
    else:
        return "Normal"