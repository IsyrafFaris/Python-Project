def startup():
    print("Welcome to UNITEN Sports Facility Booking System")
    print("************************************************************")
    print("Please choose a station by entering the appropriate number")
    for stations in ["1. Futsal","2. Takraw","3. Basketball","4. Volleyball","5. Badminton"]:
        print(stations)
    validation()


def validation():
    #Loop repeats until condition is false
    while (True):
        try:
            court = input("Please enter appropriate number for the corresponding station: ")
            selectCourt = int(court)
            break
        except:
            print("Incorrect, please enter correct value")
    while True:
        try:
            while selectCourt > 5:
                REcourt = input("Station does not exist. Please re-enter appropriate number: ")
                selectCourt = int(REcourt)
            break
        except:
            print("Incorrect, please enter correct value")
    #Stations
    if selectCourt == 1:
        print("You have chosen Futsal")
    elif selectCourt == 2:
        print("You have chosen Takraw")
    elif selectCourt == 3:
        print("You have chosen Basketball")
    elif selectCourt == 4:
        print("You have chosen Voleyball")
    else:
        print("You have chosen Badminton")
    uniten()
    
    
def uniten():
       student = input("Are you a UNITEN student? (Type Yes or No)\n")
       yesChoice = ["Yes","yes","Y","y"]
       noChoice = ["No","no","N","n"]
       while student not in yesChoice and student not in noChoice:
           print("Incorrect value, please re-enter")
           student = input("Are you a UNITEN student? (Type Yes or No)\n")
       

  

startup()
input("Press ENTER to escape")
           



                
            


