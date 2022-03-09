class Time:
    def __init__(self,h,m,s):
        self._h1=h
        self._m1=m
        self._s1=s
    def __add__(self, x):
        sum1 = self._h1 + x._h1
        sum2 = self._m1 + x._m1
        sum3 = self._s1 + x._s1
        if(sum3>=60):
            sum3=sum3-60
            sum2=sum2+1
        if(sum2>=60):
            sum2=sum2-60
            sum1=sum1+1
        print("After adding the two given times :")
        print(sum1,":",sum2,":",sum3)
h1=int(input("Enter the time 1 in hours: "))
m1=int(input("Enter the time 1 in minutes: "))
s1=int(input('Enter the time in seconds: '))
print(h1,":",m1,":",s1)
obj1=Time(h1,m1,s1)
h2=int(input("Enter the time 2 in hours: "))
m2=int(input("Enter the time 2 in minutes: "))
s2=int(input('Enter the time 2 in seconds: '))
print(h2,":",m2,":",s2)
obj2=Time(h2,m2,s2)
print(obj1+obj2)