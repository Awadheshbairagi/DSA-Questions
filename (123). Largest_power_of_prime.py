y=int(input())
for i in range(y):
 
    n=int(input())
    p=int(input())
        
    if(n<p):
        print(0)
        break
            
    else:
        x=0 
        while (n>=p):
            a=n//p 
            x=x+a
            n=a
    print(x)    
