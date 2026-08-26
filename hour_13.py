import pandas as pd
import matplotlib.pyplot as plt

# 1. The Data Pipeline
data = {
    "hostname": ["Web-01", "DB-01", "API-01", "Auth-01"],
    "errors": [2, 15, 0, 4]
}
df = pd.DataFrame(data)

print("--- Generating Error Visualization ---")

# 2. The Canvas (Define size in inches: width, height)
plt.figure(figsize=(8, 5))

# 3. The Geometry (Create a Bar Chart mapping hostnames to errors)
plt.bar(df["hostname"], df["errors"], color=['blue', 'red', 'green', 'blue'])

# 4. The Labels
plt.title("NBPO Sentinel: Daily Server Errors")
plt.xlabel("Server Name")
plt.ylabel("Number of Errors")

# 5. The Output (Save the image to the hard drive)
plt.savefig("sentinel_chart.png")
print("Success: Chart saved securely as 'sentinel_chart.png'")