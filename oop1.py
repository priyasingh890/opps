class fraction:
    def __init__(self,n,d):
        self.num=n
        # print(self.num)
        # print(self.num)
        self.den=d
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self,other):
        tem_num=self.num*other.den+self.den*other.num
        tem=self.den*other.den
        return "{}/{}".format(tem_num,tem)

    def __sub__(self,other):
        tem_num=self.num*other.den-self.den*other.num
        tem=self.den*other.den
        return "{}/{}".format(tem_num,tem)

    def __mul__(self,other):
        tem_num=self.num*other.num
        tem=self.den*other.den
        return "{}/{}".format(tem_num,tem)

  

    def __truediv__(self,other):
        tem_num=self.num*other.den
        tem=self.den*other.num
        return "{}/{}".format(tem_num,tem)
    
        
x=fraction(4,5)
y=fraction(6,8)
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
