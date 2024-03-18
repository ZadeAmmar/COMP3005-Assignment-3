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

def getAllStudents():
    # get all students
    cur.execute("SELECT * FROM students")
    conn.commit()
    results = []
    for x in cur.fetchall():
        results.append((x[0], x[1], x[2], x[3], str(x[4])))
    for x in results:
        print(x)

def addStudent(firstName, lastName, email, enrollmentDate):
    email = email.lower()
    #check if student exists
    cur.execute("SELECT * FROM students WHERE LOWER(email) = %s", (email,))
    rows = cur.fetchall()
    if len(rows) > 0:
        print("Error: Student already exists")
        return
    # add the student
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (firstName, lastName, email, enrollmentDate))
    cur.execute("SELECT student_id FROM students WHERE LOWER(email) = %s", (email,))
    conn.commit()
    rows = cur.fetchall()
    id = rows[0][0]

    print(f"Student added successfully. ID: {id}")

def updateStudentEmail(student_id: int, email):
    email = email.lower()
    # check if student exists
    cur.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    rows = cur.fetchall()
    if len(rows) == 0:
        print("Error: Student does not exist")
        return
    # update the student
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (email, student_id))
    conn.commit()

    print(f"Student updated successfully. ID: {student_id}")

def deleteStudent(student_id: int):
    # check if student exists
    cur.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    rows = cur.fetchall()
    if len(rows) == 0:
        print("Error: Student does not exist")
        return
    # delete the student
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()

    print(f"Student deleted successfully. ID: {student_id}")
    


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
    
main()