# A dataset: A list containing multiple dictionaries
server_logs = [
    {"hostname": "Sentinel-Web-01", "status": "Active", "errors": 2},
    {"hostname": "Sentinel-DB-01", "status": "Warning", "errors": 15},
    {"hostname": "Sentinel-API-01", "status": "Active", "errors": 0}
]

print("--- Sentinel Fleet Status ---")

# Iterate through the list. Each 'server' is a dictionary.
for server in server_logs:
    
    # Isolate the data we care about using dictionary keys
    name = server["hostname"]
    error_count = server["errors"]
    
    # Make a decision based on the data
    if error_count > 10:
        print(f"CRITICAL ALERT: {name} has {error_count} errors. Immediate action required.")
    else:
        print(f"OK: {name} is stable.")