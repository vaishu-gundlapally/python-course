from abc import *

class Account:
    def savings(Self):
        print("zero balance")
class cards(ABC):
    @abstractmethod
    def cashbacks(self):
        pass
    def easypay(self):
        pass
class cards1:
    def cashbacks(Self):
        print("cash back credit card")
obj1=cards()