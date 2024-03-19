## COMP3005 Assignment 3 Part 1

### Name:
* Zade Ammar

___

### Installing packages

If you have not already installed psycopg, install it as shown below:
```bash
pip install "psycopg[binary]"
```
This will only work if your pip is up to date. You can update pip as follows:
```bash
pip install --upgrade pip
```

___

### Project Files

* `README.md`: This file contains the program description and instructions for use.
* `App/CRUD_App.py`: This file contains the 4 CRUD functions and a tester, and is used to view, update, delete, and add to the contents of the database.
* `DB_init.sql`: This file contains SQL code to create and populate the table within the database. It can be used directly within PGAdmin, but the `loader.py` file uses it and can do all the populating for you.
* `loader.py`: This file uses the code within the `DB_init.sql` file to create a table in the database and populate it with sample data.

___

### Creating and populating the database

To create a table, you must already have a database created. Navigate into PGAdmin and create a database called `3005Assignment3`. Once you have done this, ensure your **postgres** login has a password of **postgres**. You can do this by clicking on `login/user roles` in PGAdmin, right clicking on `postgres`, clicking on `properties`, then `definition`, and then setting the password to be **postgres**. 

There is a `loader.py` script to create and populate the table for you. To use it, simply navigate into the `dbScripts` directory and run the python script like so:
```bash
cd dbScripts
python loader.py
```
Note that if you do not want to populate the database, you may navigate into the `DB_init.sql` file and delete lines 13 to 17, or comment them out by surrounding them with comment markers like so:
```SQL
/* 
[lines 13 to 17 here]
*/
```
___

### Testing the CRUD App

To test the CRUD application on the student database, navigate into the `App` directory and run the `CRUD_App.py` file as shown below:

```bash
cd App
python CRUD_App.py
```

Follow the given instructions on the menu to add, delete, update, or read the data from the database table.


___

### Youtube Video:
[![COMP3005 A3 Part 1](https://i9.ytimg.com/vi_webp/twMDnXjLC5U/mq2.webp?sqp=COTE468G-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGYgZihmMA8=&rs=AOn4CLAUSW3Z8zPJSP8VZawqV_wp3khGSA)](https://youtu.be/twMDnXjLC5U)

___

### Link:
https://youtu.be/twMDnXjLC5U
