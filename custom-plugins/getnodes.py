from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from re import compile as re_compile, IGNORECASE
import json
from ansible.errors import AnsibleError
from ansible.module_utils.six.moves import xrange
from ansible.parsing.splitter import parse_kv
from ansible.plugins.lookup import LookupBase
from copy import deepcopy
import ConfigParser
from ansible.configread import LookupModule
import sys
from ConfigParser import ConfigParser


file2=open('/root/aws_nodes.json','r')
json_file=json.load(file2)

class LookupModule(LookupModule):
    def reset(self):
        self.type = None
        self.profile= None
        self.property = "public_ip"
        self.configfile= "/root/sample.ini"
        

    def parse_kv_args(self,args):
        for option in ["type","profile","property","configfile"]:
            try:
                arg_raw = args.pop(option, None)
                if arg_raw is None:
                    continue
                setattr(self,option,arg_raw)
            except ValueError:
                raise AnsibleError("can't parse arg %s=%r as integer" % (arg, arg_raw))


    def get_nodes(self):
        result=[]
        for stuff in json_file['aws_data']:
            result.append(stuff['instances'][0]['tags']['Name'])
        return result

    def get_profile_dict(self,config,type,prof):
        dict={}
        list=config.items(type+":"+prof)
        dict['profile'] = prof
        for key,value in list:
            if key.lower() == "volumes":
                dict[key] = eval(value)
            else:
                dict[key] = value
        return dict

    def get_node_details(self,node,property):
        if node not in self.get_nodes():
            json.dumps("unable to get the details of"+node)
            sys.exit(10)
        for data in json_file['aws_data']:
            if data['instances'][0]['tags']['Name'] == node:
                return data['instances'][0][property]
            
            
    def run(self, terms, variables, **kwargs):
        self.reset()
        for term in terms:
            try:
                self.parse_kv_args(parse_kv(term))
            except AnsibleError:
                 raise
            except Exception as e:
                 raise AnsibleError("unknown error parsing with_sequence arguments: %r. Error was: %s" % (term, e))
        config = ConfigParser()
        config.read(self.configfile)
        result=[]
        for prof in self.profile.split(','):
            node_name=self.get_profile_dict(config,self.type,prof)
            node_list=(self.expandregex(node_name['name']))
            for node in node_list:
                tmp={}
                tmp[self.property]=self.get_node_details(node,self.property)
                tmp["profile"]=prof
                result.append(deepcopy(tmp))                
        return result
            
        
