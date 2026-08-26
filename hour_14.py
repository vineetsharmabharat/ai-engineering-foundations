import pandas as pd
import matplotlib.pyplot as plt

print("--- Initializing Sentinel Analytics Core ---")

# 1. The Dataset: A week of CPU temperatures for the Database Server
sensor_data = {
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "temp_celsius": [42, 45, 44, 88, 85, 46, 43]
}

# 2. Structure the Data
df = pd.DataFrame(sensor_data)

# 3. Analyze the Data (Calculate the average temperature)
avg_temp = df["temp_celsius"].mean()
print(f"Weekly Average CPU Temperature: {avg_temp:.2f}°C")

# 4. Visualize the Data
plt.figure(figsize=(10, 6))

# Draw the main line chart (marker='o' adds dots at each data point)
plt.plot(df["day"], df["temp_celsius"], marker='o', color='purple', linewidth=2, label="Daily Peak Temp")

# Draw a red dashed line representing the calculated average
plt.axhline(y=avg_temp, color='red', linestyle='--', label=f"Average ({avg_temp:.1f}°C)")

# 5. Format the Canvas
plt.title("NBPO Sentinel: Weekly CPU Temperature Trend")
plt.xlabel("Day of the Week")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True) # Adds a clean grid to the background

# 6. Save the Asset
plt.savefig("sentinel_trend.png")
print("Success: Trend analysis chart saved securely as 'sentinel_trend.png'")