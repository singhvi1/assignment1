# assignment1


#soln 1
a=int(input("please enter the first number:"))
b=int(input("please enter the second number:"))
c=int(input("please enter the third number:"))
s=(a+b+c)/3
print("the average of the above given three numbers is",s)
     

#soln 2
a=int(input("please enter your gross income to nearest penny:"))
b=int(input("please enter number of dependents(if nil write 0):"))
c=((b*3000)+10000)
d=(a-c)
e=(d*0.2)
print("the total tax to be paid by you is",e)
     

#soln 3
a=int(input("please enter number of seconds:"))
min=a//60
sec=a%60
print("these are",min,"minutes and",sec,"seconds")
     

#soln 4
a=int(25)
b=int('25')
c=float(25.0)
s=str(a+b+c)
print("the sum of three numbers is",s)
     

#soln 5
from math import * 
#create a for loop
for i in range(0,360,15):
  print(i,'',round(sin(i),4),round(cos(i),4))
     
