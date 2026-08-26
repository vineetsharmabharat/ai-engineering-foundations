# A Dictionary representing a system's status
server_profile = {
    "hostname": "Sentinel-Web-01",
    "status": "Active",
    "error_count": 4,
    "uptime_percentage": 99.9
}

# Extracting data by its Key
current_status = server_profile["status"]
errors = server_profile["error_count"]

print(f"Server {server_profile['hostname']} is currently {current_status}.")
print(f"It has logged {errors} errors today.")
print("\n--- System Alert: New Error Detected ---")

# 1. Modifying an existing key (Incrementing the error count by 1)
server_profile["error_count"] = server_profile["error_count"] + 1

# 2. Adding a completely new key-value pair dynamically
server_profile["last_maintenance_date"] = "2026-08-26"
server_profile["status"] = "Warning"

print(f"Server is now in {server_profile['status']} state.")
print(f"Total Errors: {server_profile['error_count']}")
print("Full System Profile:")
print(server_profile)