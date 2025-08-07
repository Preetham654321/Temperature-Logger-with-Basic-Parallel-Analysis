# 🔥 Temperature Logger with Batch Analysis (Python)

This simple project simulates sensor readings (like from an embedded system), logs them to a CSV, and performs a basic batch analysis using NumPy — similar to GPU batch processing.

## 📌 Features
- Simulates 10 temperature readings
- Logs timestamped data into `temp_log.csv`
- Analyzes data using NumPy (average, min, max, high-temp alerts)

## 💡 How It Relates to Qualcomm Roles
- **Embedded Concepts**: Sensor data simulation
- **GPU Verification**: Batch processing with NumPy (vectorized analysis)
- **Software Engineering**: Logging, file handling, and reporting

## ▶️ How to Run
```bash
python temp_logger.py
```

## 📝 Output Example
```
[2025-08-07 15:40:20] Temperature: 32.54 °C
...
--- Batch Analysis (Simulated GPU) ---
Average Temp: 31.75 °C
Max Temp: 38.91 °C
...
```

## 📁 Files
- `temp_logger.py`: Main Python script
- `temp_log.csv`: Output log file
