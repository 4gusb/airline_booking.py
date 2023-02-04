import time
import os
import getpass
from passlib.hash import sha256_crypt


class User():
    def __init__(self):
        User.ID = validId()
        User.password = validPassword()
        User.hashedPass =  sha256_crypt.hash(User.password)
        
    def __userExistence__(self, usersData):
        if User.ID in usersData:
            if not sha256_crypt.verify(User.password, usersData[User.ID]): 
                return 1 
        else:
            usersData[User.ID] = User.hashedPass
        return 0

    def __reserve__(self, usersReserves):
        flight = input("\nFlight alphanumeric code you want to reserve: ")
        while flight.isalpha() or flight.isnumeric() or len(flight)!= 6:
            print("Indicate a valid code.")
            flight = input("\nFlight code you want to reserve: ")
        if (User.ID, flight) in usersReserves.items(): 
            print("\nYou already reserve this flight.")
        else:
            if User.ID not in usersReserves:
                usersReserves[User.ID] = flight
            else:
                usersReserves[User.ID] = usersReserves[User.ID], flight
            print("Saving your reservation...")
            

def validId():
    id = input("Input your ID: ")
    while not id.isnumeric() or len(id) != 8:
        print("Invalid input.")
        id = input("\nInput your ID: ")
    return id

def validPassword():
    print("Input your password (longer than 7 chars, include numbers): ")
    password = getpass.getpass()
    while password.isalpha() or len(password) < 7:
        print("Invalid input.")
        print("Input your password (longer than 7 chars, include numbers): ")
        password = getpass.getpass()
    return password

def validMenu():
    try:
        choice = int(input("Choose an option: "))
        if choice not in (1, 2, 3):
            print("Choose a valid option.")  
        else:
            return choice
    except ValueError:
        print("Choose a valid option.")

def userFeedback(usersData, usersReserves):
    actualUser = User()
    userExistence = actualUser.__userExistence__(usersData)
    ##while the password doesnt verify, go back to main menu
    if userExistence == 1:
        print("\nInvalid password")
    ## users menu
    else:
        time.sleep(2)
        os.system('cls')
        print("\nWhat do you want to do?:\n1) My reservations\n2) Make a reserve\n3) Log out")
        userOption = validMenu()
        while userOption!= 3:
            if userOption == 1:
                if actualUser.ID not in usersReserves:
                    print("\nYou do not have any reservations yet.")
                else:
                    print(f"\nYour reservations:\n{usersReserves[actualUser.ID]}")
                    
            elif userOption == 2:
                actualUser.__reserve__(usersReserves)
            time.sleep(3)    
            os.system('pause')
            os.system('cls')
            print("\nWhat do you want to do?:\n1) My reservations\n2) Make a reserve\n3) Log out")
            userOption = validMenu()
        print("Logging out...")

def main():
    usersData = {}
    usersReserves = {}
    print("\n---------Welcome to Cheetos Airlines---------")
    print("\n--------MENU---------")
    print("\n1) Log In\n2) Terms and Conditions\n3) Exit")
    appOption = validMenu()
    time.sleep(2)
    os.system('cls')
    while appOption != 3:
        if appOption == 1:
            userFeedback(usersData, usersReserves)              
        elif appOption == 2:
            print("\n---------TERMS AND CONDITIONS---------")
            print("\nThe purchase of Cheeto's tickets implies the total aceptance, by the client of Cheeto's general conditions of transport (passenger and baggage) and the acceptance without reservations of all the provisions contained therein. The general conditions of transport regulate the contractual relationship between Cheetos and the person named on the ticket and refer to, amongst others, the following matters: ---Reservations, tickets, fares, charges, taxes.---Changes, cancellations and refunds.---Obligations and rights---Cheetos reserves the right to update then at a ny given moment.\n")
        
        time.sleep(3)    
        os.system('pause')
        os.system('cls')
        print("\n--------MENU---------")
        print("\n1) Log In\n2) Terms and Conditions\n3) Exit")
        appOption = validMenu() 
    print("\nGoodbye..")       

main()