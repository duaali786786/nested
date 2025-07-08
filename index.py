medicalcause= input("Did you have any medical problem yes or no: ")
a=int( input("what is your attendance: "))

if medicalcause == "yes":
    print('you are allowed')
else:
    if a>=75:
        print("you are allowed")
    else:
        print("you are not allowed")
    
    

