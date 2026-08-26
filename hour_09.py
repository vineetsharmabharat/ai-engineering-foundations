# 1. We create the Blueprint (Class)
class Server:
    # The __init__ function sets up the initial data when a new server is built
    def __init__(self, hostname_input):
        self.hostname = hostname_input
        self.status = "Offline"
        self.errors = 0

    # This is an action the server can perform on itself
    def boot(self):
        print(f"[{self.hostname}] Boot sequence initiated...")
        self.status = "Active"

    def log_error(self):
        self.errors = self.errors + 1
        print(f"[{self.hostname}] Error logged. Total: {self.errors}")

print("--- Sentinel Fleet Management ---")

# 2. We use the blueprint to build a real Object
web_node = Server("Sentinel-Web-01")

print(f"Initial State: {web_node.hostname} is {web_node.status}")

# 3. We command the object to perform its actions
web_node.boot()
web_node.log_error()
web_node.log_error()

print(f"Final State: {web_node.hostname} is {web_node.status} with {web_node.errors} errors.")