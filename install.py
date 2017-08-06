#encoding=utf-8
'''
Created on 2016-7-29

@author: 23683
'''
import os
import subprocess
import sys

def main():
    if not os.path.exists('install.py'):
        print("Error: install.py must be run in SoniaTest directory")
        raise Exception()
    
    soniatest_path = os.path.abspath(r'.')
    print("SoniaTest path is %s" % soniatest_path)
    
    
    path_cfg = os.getenv("PATH").split(';')
    python3_path = None
    for p in path_cfg:
        if "Python3" in p: python3_path = p
    if python3_path is None: 
        print("python3.x is not installed yet, so install it now...")
        for i in range(3):
            print("Please change the 'X' icon to 'entire feature' when install python")
            print("repeat 3 times for important things.hahaha...")
        try:
            subprocess.check_call("call %s" %os.path.join(soniatest_path,'python-3.3.3.msi'), shell=True)
        except:
            print("install python failed.")
            
    
    # 安装后重新查找    
    path_cfg = os.getenv("PATH").split(';')
    python3_path = None
    for p in path_cfg:
        if "Python3" in p: python3_path = p
    if python3_path is None: 
        print("python3.x is not in environment variables. Are you sure python is installed properly?")
        return
        
        
    print("Python 3.x path is %s" %python3_path)
    pth_file = os.path.join(python3_path, 'Lib','site-packages', 'SoniaTest.pth')
    with open(pth_file, 'w') as file:
        file.write(soniatest_path)
    
    if os.path.exists(pth_file):
        print("\ninstall successful\n");
    else:
        print("\ninstall failed\n");


if __name__ == '__main__':
    main()
    print("hit any key to exit installing")
    subprocess.check_call("PAUSE", shell=True)
