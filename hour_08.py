# A dataset simulating a malfunctioning sensor. 
# It sends numbers as strings, but one reading is completely broken.
sensor_readings = ["74", "88", "OFFLINE", "90"]

print("--- Processing Sensor Data ---")

for reading in sensor_readings:
    try:
        # We TRY to convert the string to an integer
        temp = int(reading)
        print(f"Success: Temperature logged at {temp}°C")
        
    except ValueError:
        # If the conversion fails, we CATCH the error and keep the system alive
        print(f"CRITICAL WARNING: Invalid data received -> '{reading}'. Bypassing...")

print("--- Data Processing Complete. System remains online. ---")