class sample:
    def m1(self,a,b):
        try:
            c=a/b
            print(a1)
        except ZeroDivisionError as e:
            print(e)
        except NameError as e:
            print(e)
        except Exception as e1:
            print(e1)
obj=sample()
obj.m1(40,0)
print("excecution is completed")

# user defined errors

# 1. declare an error
# 2. raise an error
# 3. handling error
class EligibleError(Exception):
    def __init__(Self,value):
        pass
class sample1:
    def eligible(self,age,percentage):
        if age<18 or percentage<60:
            raise EligibleError("not eligible")
        else:
            print("eligible")
obw=sample1()
try:
    obw.eligible(17,60)
except EligibleError as e:
    print(e)
print("end of the program")
            