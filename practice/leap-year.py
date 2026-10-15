def  leapyear(self,year:int)->boolen:
    if year%400==0:
        return True
    elif year%100==0:
        return false:
    elif year%4==0:
        return True
    else:
        return false            
