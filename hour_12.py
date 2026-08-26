import pandas as pd

# The raw dataset
server_logs = [
    {"hostname": "Sentinel-Web-01", "status": "Active", "errors": 2},
    {"hostname": "Sentinel-DB-01", "status": "Warning", "errors": 15},
    {"hostname": "Sentinel-API-01", "status": "Active", "errors": 0},
    {"hostname": "Sentinel-Auth-01", "status": "Active", "errors": 4}
]

df = pd.DataFrame(server_logs)
print("--- FULL DATAFRAME ---")
print(df)

print("\n--- AGGREGATION: Total Errors ---")
# Calculate the sum of an entire column instantly
total_errors = df["errors"].sum()
print(f"System-wide error count: {total_errors}")

print("\n--- FILTERING: Critical Servers ---")
# Filter the DataFrame to only show rows where errors > 10
critical_servers = df[df["errors"] > 10]
print(critical_servers)