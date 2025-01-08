# TEXTTOSQL

## Project Overview
**TEXTTOSQL** is an innovative project designed to convert natural language queries into SQL commands. This tool simplifies database interactions by allowing users to generate SQL queries without requiring in-depth knowledge of SQL syntax. It leverages advanced natural language processing (NLP) techniques to bridge the gap between user intent and database operations.

## Features
- Converts natural language queries into SQL commands.
- Supports multiple database operations like SELECT, INSERT, UPDATE, DELETE, and more.
- User-friendly interface for ease of interaction.
- Robust error handling and query optimization.
- Easily extendable to support additional SQL dialects and complex queries.

## Technology Stack
- **Backend**: Streamlit framework
- **API**: Gemini API key integration
- **Database**: SQLite
- **Frontend**: Streamlit components

## Installation
### Prerequisites
1. Python 3.8 or higher installed.
2. SQLite installed on your system.
3. Git installed on your system.

## Usage
1. Enter a natural language query in the input box (e.g., "Show all employees who joined after 2020").
2. The application will generate the corresponding SQL query.
3. Review the query and execute it on the connected SQLite database.

## Example Queries
- **Input**: "List all products priced above $100."
  **Output**: `SELECT * FROM products WHERE price > 100;`
- **Input**: "Add a new user named John Doe."
  **Output**: `INSERT INTO users (name) VALUES ('John Doe');`

## Contribution
Contributions are welcome! If you have suggestions, ideas, or bug fixes, feel free to fork the repository and submit a pull request.
## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

Thank you for using TEXTTOSQL!

