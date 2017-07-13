from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from re import compile as re_compile, IGNORECASE

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves import xrange
from ansible.parsing.splitter import parse_kv
from ansible.plugins.lookup import LookupBase
from copy import deepcopy
import ConfigParser

class LookupModule(LookupBase):

    def reset(self):
        self.type = None
        self.profile= None
        self.number = None
        self.configfile= None

    def expandregex(self,arg):
        if ":" in arg:
            fname=arg.split('[')[0]
            lname=arg.split(']')[1]
            start=int(arg.split('[')[1].split(":")[0])
            end=int(arg.split('[')[1].split(":")[1].strip(']').split(']')[0])
            result=[]
            for i in range(start,end+1):
                result.append(fname+str(i)+lname)
            return result
        else:
            return None

    def parse_kv_args(self,args):
        for option in ["type","profile","number","configfile"]:
            try:
                arg_raw = args.pop(option, None)
                if arg_raw is None:
                    continue
                setattr(self,option,arg_raw)
            except ValueError:
                raise AnsibleError("can't parse arg %s=%r as integer" % (arg, arg_raw))

    def instance(self,config,type,prof,number):
        dict={}
        result=[]
        for profile in prof:
            list=config.items(type+":"+profile)
            dict['profile'] = profile
            for key,value in list:
                if key.lower() == "volumes":
                    dict[key] = eval(value)
                else:
                    dict[key] = value
            name_list=self.expandregex(dict['name'])
            if name_list:
                for i in name_list:
                    tmp_dict=dict
                    tmp_dict['name'] = i
                    result.append(deepcopy(tmp_dict))
            else:
                result.append(deepcopy(dict))
        return result


    def storage(self,config,type,prof,number):
        list=config.items(type+":"+prof)
        dict={}
        result=[]
        for key,value in list:
            dict[key] = value
        

    def run(self, terms, variables, **kwargs):
        self.reset() 
        for term in terms:
            try:
                
                self.parse_kv_args(parse_kv(term))
            except AnsibleError:
                 raise
            except Exception as e:
                 raise AnsibleError("unknown error parsing with_sequence arguments: %r. Error was: %s" % (term, e))
        config = ConfigParser.RawConfigParser()
        config.read('/root/sample.ini')
        return self.instance(config,self.type,self.profile.split(','),int(self.number))
