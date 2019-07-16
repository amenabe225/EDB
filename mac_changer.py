#!/bin/python
import os 
import sys, re, time
import subprocess 
interface = "eth0"
new = str(sys.argv[1])
def get_current():
        if_res = subprocess.check_output(["ifconfig", interface])
        regx_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",if_res)
        if regx_search:
                return regx_search.group(0)
        else:
                print "[-] Error could not read the MAC adress."
old = get_current()
print (old)
def change_mac():
        cm1 = "ifconfig %s down" % interface 
        cm2 = "ifconfig %s hw ether %s" % (interface,new)
        cm3 = "ifconfig %s up" % interface
        time.sleep(2)
        print ("[+] Changing your MAC adress.")
        time.sleep(2)
        os.system(cm1)
        os.system(cm2)
        os.system(cm3)
change_mac()
changed = get_current()
release = str(changed)
if not old == release:
        print ("[+] Your MAC adress was successfully changed to %s" % release)
else:
        print ("[-] Error Your MAC adress could'nt be changed sorry :(")
