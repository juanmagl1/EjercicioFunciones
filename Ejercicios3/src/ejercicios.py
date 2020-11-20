def factorial(num):
    resultado=1
    if num==0:
        resultado=1
    elif num==1:
        resultado=1
    elif num==-0:
        resultado=1
    elif num<0:
        resultado=-1
    else:
        for i in range(1,num+1):  
            resultado=resultado*i
    return resultado
   
def leapYear(num):
    if num%4 ==0 and num%100!=0 and num%400!=0:
        return 1
    elif num <0:
        return -1
    else:
        return -1

def daysInMonth(num1,num2):
    if num1<0 or num2<0:
        return-1
    elif leapYear(num2)==1 and num1 ==2:
        return(29)
    elif leapYear(num2)!=1 and num1==2:
        return(28)
    elif num1 >12:
        return -1
    elif num1 == 1 or num1==3 or num1==5 or num1==7 or num1==8 or num1==10 or num1==12:
        return(31)
    elif num1==4 or num1==6 or num1==9 or num1==11:
        return(30)
    
def dayOfWeek(num1,num2,num3):
    a = (14 - num2) / 12 
    y = num3 - a 
    m = num2 + 12 * a - 2 
    d = (num1 + y + y/4 - y/100 + y/400 + (31*m)/12)%7
    if d ==0:
        return (0)
    elif d==1:
        return (1)
    elif d==2:
        return (2)
    elif d==3:
        return (3)
    elif d==4:
        return (4)
    elif d==5:
        return (5)
    elif d==6:
        return (6)
    
def myPower(numero,numero1):
    if numero==0:
        return (1)
    elif numero <0 and numero1==0:
        return (numero**numero1)
    elif numero<0 and numero1%2==0:
        return(numero**numero1)
    elif numero>0 and numero1<0:
        return (-1)
    elif numero>0 and numero1>0:
        return (numero**numero1)
    
def numberOfNumbers(num):
    
     
    
    
    
            
        
        
        