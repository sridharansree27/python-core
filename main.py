from abc import ABC,abstractmethod
from threading import Thread
from time import sleep

def log_customer(func):
    def wrapper(cls, instance):
        print("[LOG] Calling:", func.__name__)
        print("[LOG] Class:", cls.__name__)
        print("[LOG] Customer Name:", instance.customer_name)
        return func(cls, instance)
    return wrapper

class Abstract(ABC,Thread):
    customer = []
    i=0
    @staticmethod
    def __iter__():
        return Abstract.customer

#___________________________________________________
     # ITERATOR
#    @staticmethod
#    def __next__():
#        if Abstract.i<len(Abstract.__iter__()):
#          item=Abstract.__iter__()[Abstract.i]
#          Abstract.i+=1
#          return item
#        else:
#            return None
# ___________________________________________________
    @staticmethod
    def generator():
        while Abstract.i<len(Abstract.__iter__()):
            yield Abstract.__iter__()[Abstract.i]
            Abstract.i+=1

    @staticmethod
    def input():
        n = int(input("Enter number of customers: "))

        for _ in range(n):
            name = input("Name: ")
            Abstract.customer.append(Driver(name))

       # for _ in Abstract.__iter__():
       #     Bank.main(_)
#___________________________________________________

        def iterator():
           # Iterator without Thread
           ## while True:
           ##     object = Abstract.__next__()
           ##     if object is None:
           ##         break
           ##     Bank.main(object)

           generator = Abstract.generator()

           class CustomerThread(Thread):
               def __init__(self, customer):
                   super().__init__()
                   self.customer = customer

               def run(self):
                   Bank.main(self.customer)

           threads = []

           while True:
               try:
                   customer = next(generator)
                   t = CustomerThread(customer)
                   t.start()
                   sleep(1/2)
                   threads.append(t)
               except StopIteration:
                   break

           for t in threads:
               t.join()

          # Generator without Thread
          # while True:
          #     try:
          #         object = next(generator)
          #         Bank.main(object)
          #     except StopIteration:
          #         break
        iterator()
# ___________________________________________________

    @classmethod
    @abstractmethod
    def main(cls,instance):
        pass

class Bank(Abstract):
    name={
        "State Bank of India":{0:"Sridharan",1:"Ram"},
        "Canara Bank":{2:"Jennifer",3:"Rakesh"},
        "Indian Overseas Bank":{4:"Krishna",5:"Jessica"},
        "Indian Bank":{6:"Ramya",7:"Vijay"},
        "Punjab National Bank":{8:"Pradeep",9:"Kavya"}
    }

    @classmethod
    @log_customer
    def main(cls,instance):
        cls.driver(instance)

    def __init__(self,name):
        self.customer_name=name
        self.search = False
        self.Customer(self)

    def __eq__(self, other):
      if self.search and other.search:
        if (self.id == other.id):
            return True
        else:
            return False
      return False

    @staticmethod
    def driver(customer):
       try:
            Bank.disp(customer)
       except Exception as e:
           print("EXCEPTION:"+str(e))
       finally:
           pass

    def disp(self):
        print("NAME:", self.customer_name)
        print("ID:", self.id)
        print("Bank:", self.bank)
        print("Namespace:", vars(self))
        print("______________________________________")

    class Customer:
        def __init__(self,other):
            self.search_name(other)
            #Bank.driver(other)

        @staticmethod
        def search_name(other):
            for bank, users in Bank.name.items():
                for id, name in users.items():
                    if name.lower() == other.customer_name.lower():
                        other.id = id
                        other.bank = bank
                        other.search = True
                        break

class Driver(Bank):
    def __init__(self,name):
        super().__init__(name)

Abstract.input()

#if Abstract.customer[0]==Abstract.customer[1]:
#    print("Both customers are same")
#else:
#    print("Both customers are different")

#for _ in Abstract.customer:
# Bank.main(_)