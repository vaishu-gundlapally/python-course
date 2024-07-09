
class sample:
    name="python"
    def m1(self):
        print("welcome to")
        print(self.name)
    def m2(self):
        print("hello")
        self.m1()
obj1=sample()
obj1.m2()

# inheritence
# when we create 2 classes which are not dependent, but have the different objects to be called
# here we use inheritence
class demo:
    def n1():
        print("n1")
class Sample1:
    def n2():
        print("n2")
# we can use inheritence
class demo:
    def n1(self):
        print("n1")
class Sample1(demo):
    def n2(self):
        print("n2")
obj2=Sample1()
obj2.n1()
obj2.n2()

