# this is the CRUD application for the database

# import the required modules
import psycopg

# connect to the database
try:
    conn = psycopg.connect("dbname=3005Assignment3 user=postgres password=postgres")
except:
    print("Error connecting to database. Exiting...")
    exit(1)

# creating cursor
cur = conn.cursor()

# function to get all students
# this function will fetch all the students from the database and print them in a neat way
def getAllStudents():
    cur.execute("SELECT * FROM students") # getting all students from table
    conn.commit() # commit the changes
    results = [] # list to store the results
    # fetching the results and adding them to the list
    for x in cur.fetchall():
        results.append((x[0], x[1], x[2], x[3], str(x[4]))) # adding the student to the list

    print("ID | fName | lName | Email Address | Enrollment Date") # adding the header to the list
    print("-----------------------------------------------------------")
    # printing the results by iterating through the list
    for x in results:
        print(x)

# function to add a student
# this function will add a student to the database based off the parameters, and print the student's id if successful
def addStudent(firstName, lastName, email, enrollmentDate):
    email = email.lower() # making the email lowercase

    #check if student exists
    cur.execute("SELECT * FROM students WHERE LOWER(email) = %s", (email,))
    rows = cur.fetchall()
    # if the student does exist, print an error and return
    if len(rows) > 0:
        print("Error: Student already exists")
        return
    
    # add the student using SQL - this try and except will catch any errors
    try:
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (firstName, lastName, email, enrollmentDate))
        conn.commit() # commit the changes
    except:
        print("Error adding student. Please check your input and try again.")
        return
    
    # get the student's id
    cur.execute("SELECT student_id FROM students WHERE LOWER(email) = %s", (email,))
    conn.commit() # commit the changes
    rows = cur.fetchall() # get the results
    id = rows[0][0] # get the id from the results

    print(f"Student added successfully. ID: {id}") # print the id of the student

# function to update a student's email
# this function will update a student's email based off the parameters, and print the student's id if successful
def updateStudentEmail(student_id: int, email):
    email = email.lower() # making the email lowercase

    # check if student exists
    cur.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    rows = cur.fetchall()
    # if the student does not exist, print an error and return
    if len(rows) == 0:
        print("Error: Student does not exist")
        return
    
    # update the student using SQL- this try and except will catch any errors
    try:
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (email, student_id))
        conn.commit() # commit the changes
    except:
        print("Error updating student. Please check your input and try again.")
        return
    
    print(f"Student updated successfully. ID: {student_id}") # print the id of the student

# function to delete a student
# this function will delete a student based off the parameters, and print the student's id if successful
def deleteStudent(student_id: int):
    # check if student exists
    cur.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    rows = cur.fetchall()
    # if the student does not exist, print an error and return
    if len(rows) == 0:
        print("Error: Student does not exist")
        return
    
    # delete the student using SQL
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit() # commit the changes

    print(f"Student deleted successfully. ID: {student_id}") # print the id of the student
    
# main function
# this function will call the other functions and test them
def main():
    # loop to keep the program running
    while True:
        # print the main menu
        print("\n----- Main Menu -----")
        print("1. Get all students")
        print("2. Add a student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("0. Exit")
        # try and except to handle invalid input
        try:
            # get the user's choice
            choice = int(input("Enter your choice: "))
        except:
            # print an error and continue the loop
            print("Invalid input. Please enter a number.")
            continue
        
        # If user chooses 1, get all students
        if choice == 1:
            # get all students
            print()
            getAllStudents()
        
        # If user chooses 2, add a student - get the required information from the user
        elif choice == 2:
            # add a student
            print()
            # get the required information from the user
            firstName = input("Enter the first name: ")
            lastName = input("Enter the last name: ")
            email = input("Enter the email: ")
            enrollmentDate = input("Enter the enrollment date (YYYY-MM-DD): ")
            # call the function to add the student
            addStudent(firstName, lastName, email, enrollmentDate)
        
        # If user chooses 3, update a student's email - get the required information from the user
        elif choice == 3:
            # update a student's email
            print()
            # loop if the user enters an invalid input
            while True:
                try:
                    # getting the student's id
                    student_id = int(input("Enter the student's ID: "))
                    break
                except:
                    # print error and continue the loop
                    print("Invalid input. Please enter a number.")
                    continue
            
            # get the new email from the user
            email = input("Enter the new email: ")
            # call the function to update the student's email
            updateStudentEmail(student_id, email)
        
        # If user chooses 4, delete a student - get the required information from the user
        elif choice == 4:
            # delete a student
            print()
            # loop if the user enters an invalid input
            while True:
                try:
                    # getting the student's id
                    student_id = int(input("Enter the student's ID: "))
                    break
                except:
                    # print error and continue the loop
                    print("Invalid input. Please enter a number.")
                    continue

            # call the function to delete the student
            deleteStudent(student_id)

        # If user chooses 0, exit the program
        elif choice == 0:
            # exit the program
            print("Exiting...")
            break

# calling the main function
main()
