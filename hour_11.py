# Import the engine and give it a standard nickname 'pd'
import pandas as pd

# The raw dataset (List of Dictionaries)
server_logs = [
    {"hostname": "Sentinel-Web-01", "status": "Active", "errors": 2},
    {"hostname": "Sentinel-DB-01", "status": "Warning", "errors": 15},
    {"hostname": "Sentinel-API-01", "status": "Active", "errors": 0}
]

print("--- Converting Data into a DataFrame ---")

# Pass the data into Pandas to create a DataFrame (a high-performance table)
df = pd.DataFrame(server_logs)

print(df)