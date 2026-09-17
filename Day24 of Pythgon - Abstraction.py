'''
Abstaction:
-----------
--> Abstraction means hiding the implemented data and showing only neeed data to user
ABC --> Abstract base class
--> The abstractmethod is used to hide that particular information of a base class 
example:
--------
from abc import ABC, abstractmethod

class gov_bank(ABC):
    @abstractmethod
    def interest(self):
        print('Government intrest is 3.5')

class SBI_bank(gov_bank):
    def interest(self):
        print("SBI bank intrest is 7.8")

class ICIC_bank(gov_bank):
    def interest(self):
        print("ICIC bank intrest is 8.9")

obj = SBI_bank()
obj.interest()

obje = ICIC_bank()
obje.interest()
-------------------------------------------------
from abc import ABC,abstractmethod
class cls_fee(ABC):
    @abstractmethod
    def fee_str(self):
        print('college fee 45000')
class manag(cls_fee):
    def fee_str(self):
        print('college fee 100000')
class Em_(cls_fee):
    def fee_str(self):
        print('college fee 150000')

obj = manag()
obj.fee_str ()

gov = Em_()
gov.fee_str()
----------------------------------------------------
'''

