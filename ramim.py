print('A Python coding of a physics student ')
print('Physics.Ramim.py ')
i=input('Press 1 for speed :')
i=int(i)
if i==(1):
    i=input('Press 1 for Distance ______×______Press 2 for Velocity ________×______ Press 3 for Accelaration :')
    i=int(i)
    if i==(1):
        print ('If you have the value of variable  Enter the value else Enter 0')
        
        a=input('Enter the value of a :')
        a=int(a)
        v=input('Enter the value of v :')
        v=int(v)
        t=input('Enter the value of t :')
        t=int(t)
        
        if a>0 and t>0 and v==0 :
            
            u=input('Enter the value of u :')
            u=int(u)
            ans =(u*t+.5*a*t*t)
            print('The distance is =',ans,'m')
        elif a==0  :
            ans=(v*t)
            print('The Distance is =',ans,'m')
        elif v>0 and t==0 and a>0:
            u=input('Enter the value of u :')
            u=int(u)
            
            ans=((v*v)-(u*u))/(2*a)
            print('The Distance is =',ans,'m')
        else :
            print('Sorry we could not calcluate') 
   
    elif i==(2):
        print ('If you have the value of variable  Enter the value else Enter 0')
        s=input('Enter the value of s :')
        s=int(s)
        a=input('Enter the value of a :')
        a=int(a)
        if s ==0 and a> 0 :
            u=input('Enter the value of u :')
            u=int(u)
            t=input('Enter the value of t :')
            t=int(t)
            ans=(u+a*t)
            print('The velocity is =',ans,'m/s')
        elif s>0 and a >0  :
                
            u=input('Enter the value of u :')
            u=int(u)
            ans=(u**2+2*a*s)**.5
            print('The velocity is =',ans,'m/s')
        elif a==0 and s>0 :
            
            t=input('Enter the value of t :')
            t=int(t)
            ans=s/t
            print('The velocity is =',ans,'m/s')
    elif i ==(3):
        print ('If you have the value of variable  Enter the value else Enter 0')
        v=input('Enter the value of v :')
        v=int(v)
        if v==0:
            s=input('Enter the value of s :')
            s=int(s)
            u=input('Enter the value of u :')
            u=int(u)
            t=input('Enter the value of t :')
            t=int(t)
            if s>0 and u>0 and t>0:
                ans=(s-u*t)/(.5*t*t)
                print('The accelaration  is =',ans,'m/s^2')
            else :
                print('Sorry we could not calcluate')
        elif v> 0:
            s=input('Enter the value of s :')
            s=int(s)
            u=input('Enter the value of u :')
            u=int(u)
            t=input('Enter the value of t :')
            t=int(t)
            if s==0 and (u>0 or u==0) and t>0:
                ans = (v-u)/t
                print('The accelaration  is =',ans,'m/s^2')
            elif s>0 and u>0:
                ans = ((v*v)-(u*u))/(2*s)
                print('The accelaration  is =',ans,'m/s^2')
                
            else :
                print('Sorry we could not calcluate')
          
     
        else :
            print('Sorry we could not calcluate') 
    else :
        print('Sorry we could not calcluate') 
else :
    print('Sorry we could not calcluate') 
     
