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

    # printing the results by iterating through the list
    for x in results:
        print(x) # printing the student

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
    
    # add the student using SQL
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (firstName, lastName, email, enrollmentDate))

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
    
    # update the student using SQL
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (email, student_id))
    conn.commit() # commit the changes

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
    #getting all students
    getAllStudents()

    #adding a student named Jack Johnson
    addStudent("Jack", "Johnson", "jack.johnson@gmail.com", "2024-03-18")

    #updating John Doe's email (id 1)
    updateStudentEmail(1, "jdoe@gmail.com")

    #deleting Jane Smith (id 2)
    deleteStudent(2)

    #getting all students
    getAllStudents()
    
# calling the main function
main()