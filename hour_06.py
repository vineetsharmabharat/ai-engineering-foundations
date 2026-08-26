import random
import time

print("--- Initializing Sentinel Live Sensor Feed ---")

# range(5) tells the loop to run exactly 5 times
for i in range(5):
    # Generate a random integer between 40 and 95
    cpu_temp = random.randint(40, 95)
    
    # Evaluate the simulated hardware state
    if cpu_temp > 85:
        status = "CRITICAL WARNING"
    else:
        status = "Stable"
        
    print(f"Reading {i+1}: CPU Temp is {cpu_temp}°C | Status: {status}")
    
    # Pause the program for exactly 1.5 seconds before the next reading
    time.sleep(1.5)

print("--- Sensor Feed Terminated ---")