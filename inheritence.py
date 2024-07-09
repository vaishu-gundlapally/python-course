# multi-level inheritence:
class Iphone13:
    def camera(self):
        print("15MP")
    def charge(self):
        print("Iphone type")
class Iphone14(Iphone13):
    def camera(self):
        print("20MP")
    def display(self):
        print("Dynamic")
class Iphone15(Iphone14):
    def camera(slef):
        print("25MP")
        super().camera()
    def charge(self):
        print("cType")
Iphone=Iphone15()
Iphone.camera()
Iphone.charge()
Iphone.display()

# if we want to access the previous property present in the parent then we use "super" keyword

# hierarchial inheritence
class teacher:
    def eng(self):
        print("english language")
class student1(teacher):
    pass
class student2(teacher):
   pass
t=student2()
t.eng()
