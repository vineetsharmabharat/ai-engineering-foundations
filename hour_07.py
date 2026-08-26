print("--- Writing logs to disk ---")

# 1. Open a new file in 'w' (write) mode. 
# If the file doesn't exist, Python creates it.
with open("sentinel_system.log", "w") as log_file:
    log_file.write("TIMESTAMP: 2026-08-26 10:00:00 | EVENT: System Initialized\n")
    log_file.write("TIMESTAMP: 2026-08-26 10:05:00 | EVENT: CPU Temp 74C - Stable\n")
    log_file.write("TIMESTAMP: 2026-08-26 10:10:00 | EVENT: CPU Temp 88C - CRITICAL\n")

print("Logs successfully saved to sentinel_system.log")

print("\n--- Reading logs from disk ---")

# 2. Open the file in 'r' (read) mode to retrieve the data.
with open("sentinel_system.log", "r") as log_file:
    saved_data = log_file.read()
    print(saved_data)