import subprocess
import os
import signal
import time
# def executeCpp():
#     # data, temp = os.pipe()
#     temp = os.pipe()
#     # os.write(temp, bytes("5 10\n", "utf-8"))
#     # os.write(temp)
#     # os.close(temp)
#     # s = subprocess.check_output("g++ Trial.cpp -o out2;./out2", stdin = data, shell = True)
#     # s = subprocess.check_output("g++ Trial.cpp -o out2;./out2", shell = True)

#     s = subprocess.Popen("g++ Trial.cpp -o out2;./out2" , stdout = subprocess.PIPE, shell=True, preexec_fn=os.setsid)
#     print(type(s))
#     time.sleep(0.3)
#     # for line in iter(s.stdout.readline, b''):
#     #     print(line.rstrip())
#     poller = s.poll()
#     print(poller)
#     if poller is None:
#         print("Code is still running")
    
#     os.killpg(os.getpgid(s.pid), signal.SIGTERM)
#     time.sleep(1)Trial
#     polled = s.poll()
#     print(polled)
#     if polled != None:
#         print("Code has stopped running")
    

#     # print(s.decode("utf-8"))

#     print("Code has stopped")

# if __name__=="__main__":
   
#     executeCpp()


class ExectuteCPP:
    
    def __init__(self, filename: str) -> None:
        self.FileName = filename


    
    def startProgram(self) -> None:
        cmd: str = "g++ " + self.FileName + " -o out2;./out2"
        self.s = subprocess.Popen(cmd , stdout = subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        print("programme started")
        # for line in iter(self.s.stdout.readline, b''):
        #     print(line.rstrip())

    def endProgram(self) -> None:
        os.killpg(os.getpgid(self.s.pid), signal.SIGTERM)
        print("programme ended")
    
    # def RestartProgram(self):
    #     startProgram(self)
    
    

    def CheckHealth(self) -> None:
        poller = self.s.poll()
        print(poller)
        if poller is None:
            print("Code is still running")

        else:
            print("Code is not running. Restarting Code ...")
            # RestartProgram()
            # code to restart program comes here


t = ExectuteCPP("Trial.cpp")
t.startProgram()
time.sleep(0.3)
t.CheckHealth()
t.endProgram()
time.sleep(1)
t.CheckHealth()

