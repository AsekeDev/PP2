import json
file_path = r"C:\Users\Lenovo Gaming\Desktop\PP\PP2\Lab 4\Json\sample-data.json"
with open(file_path, "r") as file:
    data = json.load(file)
    
interfaces = data["interfaces"] 

print("Interface Status")
print("=" * 50)
print("{:<50} {:<15} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50)

for interface in interfaces:
    dn = interface["dn"]
    description = interface["description"]
    speed = interface["speed"]
    mtu = interface["mtu"]

    print("{:<50} {:15} {:<10} {:<10}".format(dn, description, speed, mtu))