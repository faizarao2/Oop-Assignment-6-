# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.


class A:
    def show(self):
        print(f"hello from class A")

class B(A):
    def show(self):
        print(f"hello from class B")


class C(A):
    def show(self):
        print(f"hello from class C")


class D(B,C):  # Inherits from B and C
  
    pass


d = D()
d.show()   #output: hello from class B
print(D.mro())
# output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]