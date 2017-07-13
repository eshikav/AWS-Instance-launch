#!/usr/bin/env python

import os,sys
import json
import yaml

#Reading the JSON file and exttracting the exixting hosts in the cluster and appending the hosts into the add_hosts variable file

def read_json(existing_hosts):
    for i in existing_hosts["items"]:
        print i["Hosts"]["host_name"]
        input_vars['CLUSTER_NODES']['hosts'].append(i["Hosts"]["host_name"])
        print input_vars['CLUSTER_NODES']['hosts']

def main():
    with open("/tmp/allclusternodes.json", 'r') as data:
        json_input =  json.load(data)
        data.close()
    with open("Addhost_input.yaml", 'r') as stream:
        try:
            global input_vars
            input_vars = (yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc)
    read_json(json_input)
    with open("Addhost_input.yaml", 'w') as f:
        f.write(yaml.safe_dump(input_vars,default_flow_style=False))
main()

