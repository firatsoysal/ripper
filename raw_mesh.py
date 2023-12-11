from fritzconnection import FritzConnection
from fritzconnection.lib.fritzhosts import FritzHosts
import json
import time

def write_to_txt(data, file_name):
    with open(file_name, 'a') as file:
        file.write(str(data) + "\n")

fritz_ip = "192.168.188.1"
fritz_user = "fritz4244"
fritz_pass = "weizen4511"

fc = FritzConnection(address=fritz_ip, user=fritz_user, password=fritz_pass)
while True:
    try:
        fritz_hosts = FritzHosts(fc=fc)
        topo = json.loads(fritz_hosts.get_mesh_topology(raw=True))
        result={}

        client_mac = "68:54:5A:DD:EF:A0"

        for node in topo["nodes"]:
            if node["device_mac_address"] == client_mac:
                for nod in node["node_interfaces"]:
                    if nod["mac_address"] == client_mac:
                        result = nod["node_links"][0]
                        print(result)
                        current_time = time.strftime("%H:%M:%S", time.localtime())
                        result["time"] = current_time
                        print(result)

        write_to_txt(result, "mesh_top.txt")
        time.sleep(20)
    except Exception as e:
        write_to_txt(e, "errors.txt")