print("which vehicle do you want? ")
print("1.bike")
print("2.car")
choice=int(input("choose the type"))
if choice==2:
    print("1.sedan")
    print("2.SUV")
    choice1=int(input("SUV OR SEDAN"))
    if choice1==1:
        print("you have choosen sedan")
    else:
        print("you have choosen SUV")
elif choice==1:
    print("1.heavy bike")
    print("2.scooter")
    choice1=int(input("Scooter or Heavy bike"))
    if choice1==1:
        print("you have choosen scooter")
    else:
        print("you have choosen heavy bike")
else:
    print("choice not avalible")