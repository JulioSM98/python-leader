import docker
from docker.models.nodes import Node
client = docker.from_env()
nodes = client.nodes.list(filters={'role': 'manager'})
for node in nodes:
    spec_node = node.attrs["Spec"]
    if 'Leader' in node.attrs["ManagerStatus"]:
        node: Node = node
        spec_node["Labels"]["isLeader"] = "true"

    else:
        if "isLeader" in node.attrs["Spec"]["Labels"]:
            spec_node["Labels"]["isLeader"] = "false"
    node.update(spec_node)
    print(node.attrs["Spec"]["Labels"],node.attrs["Description"]["Hostname"])