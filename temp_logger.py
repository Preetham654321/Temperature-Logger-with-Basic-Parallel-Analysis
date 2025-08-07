import csv
import time
import random
import numpy as np
from datetime import datetime

# Create or open the log file
file_name = 'temp_log.csv'
with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Temperature (°C)'])

# Simulate and log sensor readings
def get_temp():
    return round(random.uniform(20.0, 40.0), 2)

batch = []

for i in range(10):  # log 10 readings
    temp = get_temp()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, temp])

    print(f"[{timestamp}] Temperature: {temp} °C")
    batch.append(temp)

    time.sleep(1)  # Simulate delay

# Process the data like a mini GPU-style batch
print("\n--- Batch Analysis (Simulated GPU) ---")
temps = np.array(batch)
print(f"Average Temp: {np.mean(temps):.2f} °C")
print(f"Max Temp: {np.max(temps)} °C")
print(f"Min Temp: {np.min(temps)} °C")
print(f"High Temp Alerts (>35°C): {temps[temps > 35]}")
