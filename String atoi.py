def myAtoi(self, str: str) -> int:
    str=str.strip()
    neg= False
    out=''
    if not str:
        return 0
    
    if str[0]=='-':
        neg = True
    elif str[0] == '+':
        neg = False
    elif str[0].isnumeric()== False:
        return 0
    else:
        out+=str[0]
    
    for i in range(1, len(str)):
        if str[i].isnumeric():
            out+=str[i]
        else:
            break
     
    if len(str)<=1 and str.isnumeric()==False:
        return 0
    elif str[0] in '+-' and str[1] not in ('0123456789'):
        return 0
    else:
        out = int(out)
        
    print(out)
    
    if neg == True and out >= 2147483648: 
        return -2147483648 
    elif neg == False and out >2147483647: 
        return 2147483647
    elif neg == True:
        return out  * -1          
    else: 
        return out