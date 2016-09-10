import string 
import subprocess 
 
charset = string.digits 
 
for i in range(0, len(charset)): 
    for j in range(0, len(charset)): 
        for k in range(0, len(charset)): 
            for l in range(0, len(charset)): 
                tar= ''.join(map(lambda x: str(x), [i, j, k, l])) 
                #print tar 
                print tar, 
                try: 
                    subprocess.check_output(["./leviathan6",tar]) 
                except subprocess.CalledProcessError as e: 
                    print e.returncode 
 
 
 
#print(subprocess.check_output(["echo", "hello world"])) 
#print "hi"

