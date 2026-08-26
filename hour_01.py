client_name = input("Enter client's name: ")
hours = float(input("Enter hours: "))
hourly_rate = float(input("Enter hourly rate: "))

if hours > 40:
    # 1. Calculate regular pay for exactly 40 hours
    # 2. Calculate overtime pay for the hours ABOVE 40 at 1.5x rate
    # 3. Add them together to get total_revenue
    total_revenue = (40 * hourly_rate) + ((hours - 40) * (hourly_rate * 1.5))
else:
    # Standard calculation for 40 hours or less
    total_revenue = hours * hourly_rate

print(f"Client: {client_name} | Total Revenue: ₹{total_revenue}")