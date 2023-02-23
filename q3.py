class customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
def greet(customer):
    if customer.gender=="female":
        print("hello",customer.name,"ma,am")
    else:
        print("hello",customer.name,"sir")
c=customer("akit","male")
greet(c)

