from threading import Thread
from time import sleep

class Sample(Thread):
    def m1(self):
        print("m1")
    def run(self):
        for i in range(1,11):
            print(i)
            sleep(1)
        slef.m1() # to call the outside functions inside run method
class demo(Thread):
    def run(self):
        for i in range(11,21):
            print(i)
            sleep(1)
obj=Sample()
obj1=demo()
obj.start()  # this method calls the run function 
obj1.start()
# all the logical statements are written inside this run method

# now, if we print anything after calling the run then it will get executed simulataneously in the for loop,
# if i want to print it at last, wait till the execution of threads are completed. To know that, we use join()

class Sample(Thread):
    def m1(self):
        print("m1")
    def run(self):
        for i in range(1,11):
            print(i)
            sleep(1)
        self.m1() # to call the outside functions inside run method
class demo(Thread):
    def run(self):
        for i in range(11,21):
            print(i)
            sleep(1)
obj=Sample()
obj1=demo()
obj.start()  # this method calls the run function 
obj1.start()
obj.join()
obj1.join()
print("executes at last")