#!/usr/bin/env python

import os,sys,json
import yaml
from subprocess import Popen,PIPE
#import subprocess

def request_id():
    l = list()
    with open('/tmp/component_install.json') as request:
        jsonfileop = json.load(request)
    for i in jsonfileop['results']:
        try:
                data = json.loads(i['content'])
        except:
                continue
        l.append(data['Requests']['id'])
    return l

def curl_com(id_list):
    for i in id_list:
        while(1):
            cmd = 'curl -H "X-Requested-By: ambari" -u admin:admin -X GET  http://' + input_vars['AMBARI']['AMBARI_SERVER']['host'] + ':8080/api/v1/clusters/' + input_vars['CSF_CDLK_CLUSTER_CONFIG']['cluster_name'] + '/requests/' + str(i)
            p = Popen(cmd , shell = True , stdout = PIPE , stderr = PIPE)
            out,err = p.communicate()
            data = json.loads(out)
            if (data["Requests"]["request_status"] == "COMPLETED") or (data["Requests"]["request_status"] == "FAILED"):
                print(" " +  data['Requests']['request_context'] + " is " + data["Requests"]["request_status"] + "")
                break

def main():
    with open("Addhost_input.yaml", 'r') as stream:
        try:
            global input_vars
            input_vars = (yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc)
    ret = request_id()
    curl_com(ret)


main()

