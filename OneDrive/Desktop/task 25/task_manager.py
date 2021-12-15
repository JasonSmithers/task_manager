# for current date to be stored
from datetime import date

# defining function created
def reg_user():
    with open("user.txt","r") as user_file:
        # inputs stored in variables
        new_username = input("please provide a new username ")
        new_password = input("Please provide a new password ")
        confirm_password = input("Please confirm your new password ")
        read_file = user_file.read()
        # if new username not in file
        if new_username not in read_file:
            # if password matches confirm password
            if new_password == confirm_password:
                user_file = open("user.txt","a")
                # file is written with new username and new password
                user_file.write("\n" + new_username + ", " + new_password)
                print("New user has been created!")
                user_file.close()
                # if passwords don't match
            else:
                print("Passwords do not match")
        if new_username in read_file:
            print("Username already exists")
            print(reg_user())

def view_mine():
     # file will be opened
     with open("tasks.txt","r") as task_file:
         user_task_number = input("Which task number would you like to see? \n" + "or type -1 to return to main menu \n")
         
         if user_task_number == "-1":
             print(main_menu())
         for line in task_file:
             # contents located in task_file
             task_number = line.split(",")[0]
             username_contents = line.split(",")[1]
             task_title_contents = line.split(",")[2]
             description_task_contents = line.split(",")[3]
             current_date_contents = line.split(",")[4]
             due_date_contents = line.split(",")[5]
             completion_contents = line.split(",")[6]
             # if input task number matches task number
             if user_task_number  == task_number:
                 # print out is then done with split content
                 print()
                 print("Task number:    ",task_number + "\n")
                 print("Task:           ",task_title_contents + "\n")
                 print("Assigned to:    ",username_contents + "\n")
                 print("Date Assigned:  ",current_date_contents + "\n")
                 print("Due Date:       ",due_date_contents + "\n")
                 print("Task Complete:  ",completion_contents + "\n")
                 print("Task Description:",description_task_contents)
                 print("___________________________________________________________")
                 user_edit_complete = input("Press 1: edit task \nPress 2: mark complete \n")
                 # if input is 1
                 if user_edit_complete == "1":
                     # asks for new input
                     user_edit = input("Press 1: to change the user the task is assigned to?\nPress 2: change the due date of task?\n")
                     # if input is 1
                     if user_edit == "1":
                         # asks new username to be assigned
                         assigned_name = input("Please provide a new username to assign ")
                         task_file = open("tasks.txt","r")
                         file = task_file.read()
                         # replacement of username into line
                         new_line = line.replace(username_contents," " + assigned_name)
                         # replacement of line with new line
                         new_content = file.replace(line,new_line)
                         output = open("tasks.txt","w")
                         output.write(new_content)
                         task_file.close()
                         
                     # if user input is 2    
                     if user_edit == "2":
                         # new due date is inputted
                         user_new_date = input("Please provide a new due date ")
                         task_file = open("tasks.txt","r")
                         file = task_file.read()
                         # replacement of date into line
                         new_line = line.replace(due_date_contents," " + user_new_date)
                         # replacement of line with new line
                         new_content = file.replace(line,new_line)
                         output = open("tasks.txt","w")
                         output.write(new_content)
                         task_file.close()
                 # if input is 2            
                 if user_edit_complete == "2":
                     task_file = open("tasks.txt","r")
                     file = task_file.read()
                     # Yes is replaced in line
                     new_line = line.replace(completion_contents," "+"Yes")
                     # line is replaced with new line
                     new_content = file.replace(line,new_line + "\n")
                     output = open("tasks.txt","w")
                     output.write(new_content)
                     task_file.close()
                     
                     
                 
                     
                        
                         

                             
def add_task():
    # variables created for input of all information needed
    assigned_user = input("Please provide the user this task is assigned to ")
    task_title = input("Please provide the title of the task ")
    description_task = input("Please provide a brief description of the task ")
    current_date = date.today()
    due_date = input("What date is the task due ")
    completion = "No"
    # task file opened with "a" to not overwrite
    # found this method on google
    # https://stackoverflow.com/questions/22441803/how-to-write-to-a-file-without-overwriting-current-contents
    task_file = open("tasks.txt","a")
    task_file.write("\n" + assigned_user + ", " + task_title + ", " + description_task + ", " + str(current_date)+ ", " + due_date + ", " + completion)
    # task file closed
    task_file.close()

    
def view_all():
    #it will open tasks text file as task_file
    with open("tasks.txt","r") as task_file:

        #for loop used
        for line in task_file:
        # all content are split from commas and taken from positions
            task_number = line.split(",")[0]
            username_contents = line.split(",")[1]
            task_title_contents = line.split(",")[2]
            description_task_contents = line.split(",")[3]
            current_date_contents = line.split(",")[4]
            due_date_contents = line.split(",")[5]
            completion_contents = line.split(",")[6]
            # print out is then done with split content
            print()
            print("Task number:    ",task_number + "\n")
            print("Task:           ",task_title_contents + "\n")
            print("Assigned to:    ",username_contents + "\n")
            print("Date Assigned:  ",current_date_contents + "\n")
            print("Due Date:       ",due_date_contents + "\n")
            print("Task Complete:  ",completion_contents + "\n")
            print("Task Description:",description_task_contents)
            print("___________________________________________________________")
    
def total_users():
    # open user text file as user_file
    with open("user.txt","r") as user_file:

        # for loop used, counts number of lines
        # enumerate code found on google
        # https://pynative.com/python-count-number-of-lines-in-file/
        for count_two,line in enumerate(user_file):
            pass
        total_users = count_two + 1
    return total_users


        
def total_tasks():
    #opening of tasks text file as task_file
    with open("tasks.txt","r") as task_file:

    # for loop used, counts number of lines
    # enumerate code found on google
    # https://pynative.com/python-count-number-of-lines-in-file/
        for count,line in enumerate(task_file):
            pass
        total_tasks = count + 1
    return total_tasks

def report_overview():
    # imort of datetime
    from datetime import datetime
    # file opened
    task_file = open("tasks.txt","r")
    # counters created 
    over_due_counter = 0
    completed_counter = 0
    incomplete_counter = 0
    # for loop used to loop through text file
    for line in task_file:
        line = line.strip("\n")
        # task_number located
        task_number = line.split(",")[0]
        # username located
        username_contents = line.split(",")[1]
        # task title located
        task_title_contents = line.split(",")[2]
        # task_number located
        description_task_contents = line.split(",")[3]
        # current located
        current_date_contents = line.split(",")[4]
        # due date located
        due_date_contents = line.split(",")[5]
        # completion status located
        completion_contents = line.split(",")[6]
        completion_contents = completion_contents.replace(" ","")
        completion_contents = completion_contents.strip("\n")
        current_date_contents = current_date_contents.replace("-","")
        due_date_contents = due_date_contents.replace("-","")
        # if completion is "No"
        if completion_contents == "No":
            # add to counter
            incomplete_counter +=1
            # if completion is "Yes"
        if completion_contents == "Yes":
            # add to counter
            completed_counter +=1
        # if current date is larger than due date
        if current_date_contents > due_date_contents:
            # add to counter
            over_due_counter +=1
        #calculation of percentages
        percentage_overdue = (over_due_counter/total_tasks())*100
        percentage_incompleted = (incomplete_counter/total_tasks())*100
    
    # output stored in new variable
    new_string =("\nThe total of tasks: {}\n".format(total_tasks())
                +"The total of completed tasks: {}\n".format(completed_counter)
                +"The total of uncomplete tasks: {}".format(incomplete_counter)
                +"The total of uncompleted tasks overdue: {}\n".format(over_due_counter)
                +"The percentage of tasks overdue: {}%\n".format(round(percentage_overdue,2))
                +"The percentage of incompleted tasks: {}%\n".format(round(percentage_incompleted,2))
                )
    task_overview = open("task_overview.txt","w")
    task_overview.write(new_string)
    print(new_string)
    
    # open task file and user file
    task_file = open("tasks.txt","r")
    user_file = open("user.txt","r")
    # read task file
    read_task_file = task_file.read()
    # for loop used 
    for line in user_file:
        # to find username in user file
        user_name = line.split(",")[0]
        if user_name in read_task_file:
            # count usernames
            count = read_task_file.count(user_name)
            # calculate percentsga of user to total tasks
            percentage = (count/total_tasks())*100
            # variable created for output
            string =("Username: {}\n".format(user_name)
                  +"Number of tasks: {}\n".format(count)
                  +"Percentage of tasks to user: {}\n".format(round(percentage,2))
                  + "_____________________________________________________________________\n"
                  )
            # variable written to file
            user_overview = open("user_overview.txt","a")
            user_overview.write(string)
            print(string)
            # if possible i would please like help with the remainder of this task, i was unable to complete the last info for user_overview
            # as I was not sure how to do it
            # i have tried emailing but i havent recieved a reply

    
        
            
            
    
                        
   
            
    
    
    

 
            


    
def main_menu():

    # I adapted this code from google
    # google source : https://stackoverflow.com/questions/4940032/how-to-search-for-a-string-in-text-files
    with open("user.txt","r+") as task_file:
        found = False
        # file read and "\n" has been replaced with a blank space
        info = task_file.read().replace('\n',' ')
        # comma replaced with no space
        info = info.replace(',','')


        #for loop used
        for line in info:
            # variables created for user input
            input_username = input("Please provide your username: ")
            input_password = input("Please provide your password: ")

            # if input in txt file
            if input_username in info:

                #if  input is also in txt file
                if input_password in info:
                    found = True

                    # if input is admin
                    if input_username == "admin":
                        print("You have successfully logged in")
                        print()
                        print("Please select one of the following options:\nr - register user\na - add task\nva - view all tasks\nvm - view my tasks\ngr - generate reports\nds - display statistics\ne - ")
                        admin_selection = input("Your option ")

                        # if input is "r"
                        if admin_selection == "r":
                            print(reg_user())
                                        

                        # if input is st for statistics
                        if admin_selection == "ds":

                            #opening of tasks text file as task_file
                            with open("tasks.txt","r") as task_file:

                                # for loop used, counts number of lines
                                # enumerate code found on google
                                # https://pynative.com/python-count-number-of-lines-in-file/
                                for count,line in enumerate(task_file):
                                    pass
                                print("Number of Tasks:",count + 1)

                                    # open user text file as user_file
                                with open("user.txt","r") as user_file:

                                    # for loop used, counts number of lines
                                    # enumerate code found on google
                                    # https://pynative.com/python-count-number-of-lines-in-file/
                                    for count_two,line in enumerate(user_file):
                                        pass
                                    print("Number of Users:",count_two + 1)

                        # if selection is "a"
                        if admin_selection.lower() == "a":
                            print(add_task())

                        # if selection is "va"
                        if admin_selection.lower() == "va":
                            print(view_all())

                        # if input is "vm"                  
                        if admin_selection.lower() == "vm":
                            task_file.close()
                            print(view_mine())

                        if admin_selection.lower() == "gr":
                            task_file.close()
                            report_overview()
                            
                                    
                                                    
                        # if input is "e"                
                        if admin_selection.lower() == "e":
                             print("program exited")
                             break
                                                                
                    # if statement used, if input is not admin, it will execute the following                                
                    if  input_username != "admin":
                        print("You have successfully logged in!")
                        print()
                        print("Please select one of the following options:\nr - register user\na - add task\nva - view all tasks\nvm - view my tasks\ne - ")
                        user_selection = input("Your option: ")
                                
                        # if input is "r" it will print out the following
                        if user_selection.lower() == "r":
                            print("only admin can register a user")

                        # if input is "a" it will execute the following    
                        if user_selection.lower() == "a":
                            print(add_task())

                        # if selection is "va"
                        if user_selection.lower() == "va":
                            print(view_all())
                   
                        # if input is "vm"                  
                        if user_selection.lower() == "vm":
                            print(view_mine())

                                
                        # if input is "e"                
                        if user_selection.lower() == "e":
                            # print out will be executed
                            print("program exited")
                            break

            # if found is false, print out will execute
            if found == False:
                print("Username and password incorrect, please try again")            




    

print(main_menu())                  
    
user_file.close()  
