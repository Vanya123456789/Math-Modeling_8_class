def vysokosniygod(x):
    if x%4==0 and (x%4==0 and x%100==0 and x%400==0):
        print("высокосный")
    elif x%4==1 and x%100==1:
         print("невысокосный")    
    else:
         print("невысокосный")

vysokosniygod(2000)