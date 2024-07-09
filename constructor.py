class sample:
    def m1(self):
        print("m1")
    def m2(self):
        print("m2")
    def __init__(self):            # this is the constructor
        print("constructor called")
ob=sample()
ob.m1()