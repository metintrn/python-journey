print("rollarkoster a hoşgeldin!")

height=int(input("what is your height?"))

bill=0



if height>= 120:
    print("you can use rollarcoaster")
    age=int(input("how old are you? "))
    if age <=12:
        print("you need to pay5$")
        bill=5
    elif age<=18:
        print("you need to pay7$")
        bill=7
    elif age >=45 or age<=55:
        print("have a free ride on us")
    else:
        print("you need to pay17$")
        bill=17



    want_photos=input(" do you want photograf? y/n :")  

    if want_photos=="y":
        print()  
        bill+=3


    print(f"you will pay ${bill}")

else:
    print("you are not old enough!")
#This Python program simulates a roller coaster ticket system.
#It checks the user's height and age to determine eligibility and ticket price, applies free rides for certain ages, and adds an optional photo fee.
