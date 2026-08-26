client_name = input("Enter client's name: ")
hours = float(input("Enter hours: "))
hourly_rate = float(input("Enter hourly rate: "))

total_revenue = hours * hourly_rate

print(f"Client: {client_name} | Total Revenue: ₹{total_revenue}")
