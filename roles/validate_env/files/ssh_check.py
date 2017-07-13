import sys
import io
from itertools import islice
import subprocess

def check_ssh():
    
    flag=False
    
    
    for i in sys.argv:        
        if i != sys.argv[0]:         
            host_name=subprocess.Popen(["hostname"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            current= host_name.stdout.readlines()
            ssh = subprocess.Popen(["ssh", "-oNumberOfPasswordPrompts=0", "%s"%i,"hostname"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = ssh.stdout.readlines()
            if result == []:
                error = ssh.stderr.readlines()
                flag=False
                print "########## SSH CONNECTION FAILED BETWEEN ########## :",current,"&",i
                break
            else:
                flag=True
                
                        
    if not flag:
        raise Exception('Passwordless ssh should be successful for all the hosts!!')
 

##### Main Method ####################
def main():
        try:
            
            check_ssh()
        
        except Exception, e:
            
            raise Exception(e)

if __name__ == "__main__":
    main()
