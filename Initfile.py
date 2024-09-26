import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv', low_memory=False, header=None, delimiter=',', names=['measurement1', 'measurement2'])

data['measurement1'] = pd.to_numeric(data['measurement1'], errors='coerce')
data['measurement2'] = pd.to_numeric(data['measurement2'], errors='coerce')

time = np.arange(len(data))
data.dropna(inplace=True)

plt.figure(figsize=(10, 6))
plt.plot(data.index, data['measurement1'], label='Sensor 1', color='b')
plt.plot(data.index, data['measurement2'], label='Sensor 2', color='r')

plt.xlabel('Time (Line Number)')
plt.ylabel('Measurement')
plt.title('Wave Chart of Sensor Measurements')
plt.grid(True)
plt.legend()

plt.show()
