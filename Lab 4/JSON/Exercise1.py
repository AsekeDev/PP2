import json
file_path = r"C:\Users\Lenovo Gaming\Desktop\PP\PP2\Lab 4\Json\sample-data.json"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

interfaces = data["imdata"]
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)
for interface in interfaces:
    attributes = interface["l1PhysIf"]["attributes"]

    dn = attributes["dn"]
    description = attributes.get("descr", "") 
    speed = attributes.get("speed", "inherit") 
    mtu = attributes.get("mtu", "N/A") 

    print("{:<50} {:<20} {:<10} {:<10}".format(dn, description, speed, mtu))
