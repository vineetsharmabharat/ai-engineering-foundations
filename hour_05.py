# 1. We DEFINE the function (the blueprint)
def analyze_fleet(server_dataset, error_threshold):
    print(f"\n--- Running Health Check (Threshold: {error_threshold} errors) ---")
    
    for server in server_dataset:
        if server["errors"] > error_threshold:
            print(f"CRITICAL: {server['hostname']} has {server['errors']} errors.")
        else:
            print(f"OK: {server['hostname']} is stable.")

# Our raw data
morning_logs = [
    {"hostname": "Web-01", "errors": 2},
    {"hostname": "DB-01", "errors": 15}
]

evening_logs = [
    {"hostname": "Web-01", "errors": 12},
    {"hostname": "DB-01", "errors": 1}
]

# 2. We CALL the function (executing the blueprint)
# First run with morning data and a strict threshold of 5
analyze_fleet(morning_logs, 5)

# Second run with evening data and a relaxed threshold of 10
analyze_fleet(evening_logs, 10)