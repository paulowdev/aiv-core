# coding=utf-8
import random
import thread
import time

class TreadSemaphore(object):
    def __init__(self, f, t, r):
        self.f = f
        self.t = t
        self.r = r
        self.tList = list()

    def set_time(self):
        t = random.randint(3, 7)
        print "Processo dormindo por %i segundo(s)" % self.i
        time.sleep(t)

    def init_task(self, nt):
        nt = int(nt)

        while True:
            self.tList[nt].acquire()
            self.f()
            self.tList[(nt + 1) % 5].acquire()

            time.sleep(random.randint(1, 5))
            self.tList[nt].release()
            self.tList[(nt + 1) % 5].release()

            time.sleep(random.randint(1, 10))

    # get custom range by class
    def custom_range(self):
        return self.r

    range_ = custom_range()

    for i in range(range_):
        print "Counter: ", i
        if i == 50:
            thread.start_new_thread(init_task, tuple([i]))


# def newinstanceThread():
#     def new_function():
#         pass
#
#     new_task_instance = TreadSemaphore(new_function(), 5, 50)
#     new_task_instance.init_task(5)

# while 1: pass
