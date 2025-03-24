# I declare that my work contains no examples of my misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID : w2053224

# Date : 2023.12.04

# Importing graphics.py to create histogram 
from graphics import *

# Define the Outcomes
def progression_outcomes(Pass_Mark,Defer_Mark,Fail_Mark):
    if Pass_Mark == 120:
        Outcomes = "Progress"
    elif Pass_Mark == 100:
        Outcomes = "Progress (module trailer)"
    elif Pass_Mark in [0,20,40] and Defer_Mark in [0,20,40] and Fail_Mark in [80,100,120]:
        Outcomes = "Exclude"
    else:
        Outcomes = "Do not Progress - module retriever"
    return Outcomes


# Using functions to define the list
def listed_output():
    print("\n\nPart 2 : \n")
    for inputed_data in Progression_List:
        print(f"{inputed_data[3]} - {inputed_data[0]} , {inputed_data[1]} , {inputed_data[2]}")

# Using functions to create the structure of create a text file
def create_file():
    with open(file_name , 'w') as file:
        file.write("\nPart 3: \n")
        for data in Progression_List:
            file.write(f"{data[3]} - {data[0]} , {data[1]}, {data[2]}\n")
    print(f"\nData written to : {file_name}\n")

# Function to read and print data from the written text file
def read_text():
    with open(file_name, 'r') as file:
        read_lines = file.readlines()
        for lines in read_lines:
            print(lines)

# Using functions to create the histogram from the students progression
def create_histogram():
    Win = GraphWin("Histogram", 500, 400)


    head_title = Text(Point(70,18), 'Histogram Results')
    head_title.draw(Win)

    line = Line(Point(50,340) , Point(430,340))
    line.draw(Win)

    bar1 = (340 - (Progress_Count * 10) )
    term_count = Text(Point(105,(bar1 - 10)),f"{Progress_Count}")
    label = Text(Point(105,350) , "Progress")
    rect = Rectangle(Point(70,340) , Point(140,bar1))
    rect.setFill("#39A7FF")
    rect.draw(Win)
    label.draw(Win)
    term_count.draw(Win)

    bar2 = (340 - (Trailer_Count * 10) )
    term_count = Text(Point(195,(bar2 - 10)),f"{Trailer_Count}")
    label = Text(Point(195,350) , "Trailer")
    rect = Rectangle(Point(160,340) , Point(230,bar2))
    rect.setFill("#C70039")
    rect.draw(Win)
    label.draw(Win)
    term_count.draw(Win)

    bar3 = (340 - (Module_Retriever_Count * 10) )
    term_count = Text(Point(285,(bar3 - 10)),f"{Module_Retriever_Count}")
    label = Text(Point(285,360) , "Module\nRetriever")
    rect = Rectangle(Point(250,340) , Point(320,bar3))
    rect.setFill("#9ADE7B")
    rect.draw(Win)
    label.draw(Win)
    term_count.draw(Win)

    bar4 = (340 - (Exclude_Count * 10) )
    term_count = Text(Point(375,(bar4 - 10)),f"{Exclude_Count}")
    label = Text(Point(375,350) , "Exclude")
    rect = Rectangle(Point(340,340) , Point(410,bar4))
    rect.setFill("#FBD85D")
    rect.draw(Win)
    label.draw(Win)
    term_count.draw(Win)

    Total_Count = Progress_Count + Trailer_Count + Module_Retriever_Count + Exclude_Count
    
    foot_title = Text(Point(70,387),f"{Total_Count} Outcomes in total")
    foot_title.draw(Win)

    Win.getMouse()
    Win.close()

# Checking the user inputs which Pass Marks, Defer Marks, Fail Marks are valid integer and which are in the valid range
def valid_int(Value):
    try:
        int(Value)
        return True
    except:
        return False

def valid_input(Input, valid_range):
    while True:
        User_Input = input(Input)           # Get the inputs from the user and check it
        if valid_int(User_Input):
            Value = int(User_Input)
            if Value in valid_range:
                return Value
            else:
                print("Out of Range\n")
        else:
            print("Integer Required\n")
# Declaring Varibles
Pass_Mark = 0
Defer_Mark = 0
Fail_Mark = 0
Progress_Count = 0
Trailer_Count = 0
Module_Retriever_Count = 0
Exclude_Count = 0
Total_Count = 0
Progression_List = []
bar1 = 0
bar2 = 0
bar3 = 0
bar4 = 0
user_choice = "y"
file_name = (f"Progression Data.txt")
category = ""

# Declaring the valid range of marks
valid_range = [0, 20, 40, 60, 80, 100, 120]

# Checking user is a student or a staff member

while category not in ["s","m"]:
    category = input("Please enter you are a student for 's' or a staff member for 'm' : ")
    if category not in ["s", "m"]:
        print("\nInvalid input \nPlease enter correct input using 's' or 'm' for student or the staff member : ")

if category == 's':
        Pass_Mark = valid_input("Please enter your credits at pass: ",valid_range)            # Checking the Pass Mark is valid or not
        Defer_Mark = valid_input("Please enter your credits at defer: ",valid_range)          # Checking the Defer Mark is valid or not
        Fail_Mark = valid_input("Please enter your credits at fail: ",valid_range)            # Checking the Fail Mark is valid or not
        
        if (Pass_Mark + Defer_Mark + Fail_Mark) != 120 :                                      # Checking the total marks are equal to 120
            print("Total incorrect")                                                                      
        else:
            Outcomes = progression_outcomes(Pass_Mark,Defer_Mark,Fail_Mark)                   # Printing the student outcome
            print(Outcomes)
else:
    # Looping
    while True:
        if user_choice == "y":
            Pass_Mark = valid_input("Please enter your total PASS credits: ",valid_range)            # Checking the Pass Mark is valid or not
            Defer_Mark = valid_input("Please enter your total DEFER credits: ",valid_range)          # Checking the Defer Mark is valid or not
            Fail_Mark = valid_input("Please enter your total FAIL credits: ",valid_range)            # Checking the Fail Mark is valid or not
        
            if (Pass_Mark + Defer_Mark + Fail_Mark) != 120 :                                      # Checking the total marks are equal to 120
                print("Total incorrect")                                                                      
            else:
                Outcomes = progression_outcomes(Pass_Mark,Defer_Mark,Fail_Mark)                   # Printing the student outcome
                print(Outcomes)                                                                  
                if Pass_Mark == 120:                                                                           # If the Pass Mark is 120 count 1 to proress count
                    Progress_Count += 1
                elif Pass_Mark == 100:                                                                         # If the Pass Mark is 100 count 1 to trailer count
                    Trailer_Count += 1
                elif Pass_Mark in [0, 20, 40] and Defer_Mark in [0, 20, 40] and Fail_Mark in [80, 100,120]:    # If the Pass Mark,Defer Mark,Fail Mark is in the given count 1 to exclude count
                    Exclude_Count += 1
                else:                                                                                          # If not in any above condition cont 1 to module retriever counr 
                    Module_Retriever_Count += 1 
                    
                Progression_List.append([Pass_Mark, Defer_Mark, Fail_Mark, Outcomes])                          # Appending data to list  

                # Asking from the user's choice to continue or not
                user_choice = input("\n\nWould you like to enter another set of data\nEnter 'y' for yes or 'q' to quit view results: ").capitalize().lower()
                print()

        else:
            while user_choice not in ["y" , "q"]:                                                      # If the user input invalid choice beside 'y' or 'q'
                user_choice = input("Invalid input choice \nPlease enter 'y' to continue or 'q' to quit the program : ")
    
        if user_choice == "q":                                                                         # # If the user want to quit from the program
            listed_output()
            create_file()
            create_histogram()
            read_text()
            break
