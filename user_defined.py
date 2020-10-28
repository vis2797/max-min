def computepay(h,r):
    if h>40:
        pay=1.5*(h-40)*r+40*r
        
    else:
        pay=h*r
    return pay

h= float(input("Enter Hours:"))
r= float(input("Enter Rate:"))
p = computepay(h,r)
print("Pay",p)