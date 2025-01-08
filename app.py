from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as geneai
import pandas as pd

# Configure the API key
geneai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to Load Gemini Model and provide SQL query as response
def get_gemini_response(question, prompt):
    model = geneai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the SQL database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    columns = [description[0] for description in cur.description]  # Get column names
    conn.commit()
    conn.close()
    return columns, rows

# Define prompt for generating SQL query
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION, and MARKS \n\nFor example,\nExample 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \nExample 2 - Tell me all the students studying in the Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT
    WHERE CLASS="Data Science";
    \nExample 3 - How many students are in the database?
    SQL query: SELECT COUNT(*) FROM STUDENT;
    \nExample 4 - What are the names of all the students in the 'Data Science' class?
    SQL query: SELECT NAME FROM STUDENT WHERE CLASS="Data Science";
    \nExample 5 - Which students have more than 80 marks?
    SQL query: SELECT NAME FROM STUDENT WHERE MARKS > 80;
    \nExample 6 - Show all students in the 'A' section of 'Data Science'.
    SQL query: SELECT * FROM STUDENT WHERE CLASS="Data Science" AND SECTION="A";
    \nExample 7 - How many students are in the 'DEVOPS' class?
    SQL query: SELECT COUNT(*) FROM STUDENT WHERE CLASS="DEVOPS";
    \nExample 8 - What are the names and marks of students with marks less than 40?
    SQL query: SELECT NAME, MARKS FROM STUDENT WHERE MARKS < 40;
    
    Your task is to convert the following English question into a corresponding SQL query. The SQL query should not contain any extra characters or explanations, and should be as simple as possible.

    The SQL code should not have ''' in the beginning or end and the word 'sql' in the output.
    """
]

# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# If submit is clicked
if submit:
    # Get response from Gemini model for SQL query
    response = get_gemini_response(question, prompt)
    
    # Retrieve data from the database using the generated SQL query
    columns, data = read_sql_query(response, "student.db")
    
    # Display the query result in a table
    if data:
        df = pd.DataFrame(data, columns=columns)
        st.subheader("The Response Data")
        st.dataframe(df)
