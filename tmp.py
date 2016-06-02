#coding=utf-8

import threading
import time

play_threading = None

class Test1(threading.Thread):
    def fun1(self, args):
        while True:
            print args
            time.sleep(1)
    
    def run(self):
        self.fun1()
        
    thread = threading.Thread(target=fun1, args='hello')
    thread.start()
    
    
t = Test1()
t.start()