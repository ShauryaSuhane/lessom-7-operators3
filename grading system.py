marks1=int(input("enter the number:"))
marks2=int(input("enter the number:"))
marks3=int(input("enter the number:"))
sum=marks1 + marks2 + marks3
average=sum/3
if average>=91 and average<=100:
    print("the grade is A1")
elif average>=81 and average<91:
    print("the grade is A2")
elif average>=71 and average<81:
    print("the grade is B1")   
elif average>=61 and average<71:
    print("the grade is B2") 
elif average>=51 and average<61:
    print("the grade is C1")
elif average>=41 and average<51:
    print("the grade is C2")
elif average>=33 and average<41:
    print("the grade is D")
elif average>=21 and average<33:
    print("the grade is E1")
elif average>=0 and average<21:
    print("the grade is E2")