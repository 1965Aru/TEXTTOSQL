import sqlite3
import random

# Connect to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_info)

# Insert sample records
students = [
    ('Krish', 'Data Science', 'A', 90),
    ('Sudhanshu', 'Data Science', 'B', 100),
    ('Darius', 'Data Science', 'A', 86),
    ('Vikash', 'DevOps', 'A', 50),
    ('Dipesh', 'DevOps', 'A', 35)
]

# Generate additional records to make 50 total records
classes = ['Data Science', 'DevOps', 'AI', 'ML']
sections = ['A', 'B', 'C']

for i in range(45):  # 45 more records to make it a total of 50
    students.append((
        f"Student{i+6}",  # Unique name
        random.choice(classes),
        random.choice(sections),
        random.randint(30, 100)  # Random marks between 30 and 100
    ))

# Insert data into the table
cursor.executemany("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)", students)

# Display all the records
print("The inserted records are:")

data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

# Commit changes and close the connection
connection.commit()
connection.close()
