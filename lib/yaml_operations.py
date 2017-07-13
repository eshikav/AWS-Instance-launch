import os
import yaml


class yaml_operations():
    def __init__(self,file=None,yaml_data=None,default_flow_style='False',encoding=('utf-8'),indent=4):
        self.file = file
        self.flow_style = default_flow_style
        self.encoding = encoding
        self.indent = indent
        self.data = yaml_data

    def yaml_read(self):
        with open(self.file,'w') as infile:
        data = yaml.load(stream)
        return data
    
    def yaml_write(self):
        with open(self.file,'w') as outfile:
        yaml.dump(self.data,outfile,encoding=self.encoding,default_flow_style=self.flow_style,indent=self.indent)
