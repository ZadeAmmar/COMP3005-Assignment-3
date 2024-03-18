# this is the loader file. it populates the db with data so that you do not have to.
import psycopg

# connect to the database
try:
    conn = psycopg.connect("dbname=3005Assignment3 user=postgres password=postgres")
except:
    print("Error connecting to database. Exiting...")
    exit(1)

# creating cursor
cur = conn.cursor()

# Creating student table
try:
    cmds = open("DB_Init.sql", "r") # open the DDL file
    cur.execute(str(cmds.read())) # execute the commands in the file
    conn.commit() # commit the changes
# error handling
except FileNotFoundError:
    print("Error: File not found. Exiting...") # file not found
    exit(1) # exit
except psycopg.Error:
    print("Error: Could not execute commands. Exiting...") # error executing commands
    exit(1) # exit

cur.execute("SELECT * FROM students") # select all from students
#checking if the table has been populated
if cur.rowcount == 0:
    # if the table is empty, print message accordingly
    print("Unable to populate database. Database is empty. Exiting...") 
else:
    # if the table is not empty, print message accordingly
    print(f"Database populated successfully: {cur.rowcount} rows inserted.") 
conn.commit() # commit the changes