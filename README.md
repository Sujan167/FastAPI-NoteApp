# FastAPI NoteApp 
A simple note-taking application built with FastAPI and MySQL, demonstrating CRUD operations.

## Features
- Create, Read, Update, and Delete (CRUD) operations for notes.
- Uses SQLAlchemy for database interaction.
- Uses Pydantic for request and response validation.
- Securely stores database credentials using environment variables.
- Proper code destructure

### Prerequisites
- Python 3.7+
- pip (Python package installer)
- MySQL
  

## Installation
Clone the repository:
```
git clone https://github.com/your-username/fastapi-noteapp.git
```

Go Inside the folder:
```
cd fastapi-noteapp
```

## Setup
  1. Create a new virtual environment:
```
   python3 -m venv myenv
```

2. Activate the virtual environment:
- On Windows:
```
myenv\Scripts\activate
```

- On macOS and Linux:
```
source myenv/bin/activate
```



## Install dependencies:

```
pip install -r requirements.txt
```

## Set up environment variables:

Create a .env file in the root directory.
Add the following lines to .env, replacing placeholders with your MySQL database credentials:

```
DB_USER=username
DB_PASSWORD=password
DB_HOST=localhost
DB_NAME=dbname
```

## Run the FastAPI application:
- For Dev Environment

```
fastapi dev 
```

- For Prod Environment

```
fastapi run 
```

## API Endpoints
1. POST /note/: Create a new note.
2. GET /note/{note_id}: Retrieve a note by ID.
3. GET /notes/: Retrieve all notes.
4. PUT /note/{note_id}: Update a note by ID.
5. DELETE /note/{note_id}: Delete a note by ID.

## Example Usage
### Create a new note
```
curl -X POST "http://localhost:8000/note/" \
     -H "Content-Type: application/json" \
     -d '{"title": "New Note", "content": "This is a new note."}'
```

### Retrieve a note
```
curl -X GET "http://localhost:8000/note/1"
```

### Retrieve all notes
```
curl -X GET "http://localhost:8000/notes"
```

### Update a note
```
curl -X PUT "http://localhost:8000/note/1" \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Note", "content": "This note has been updated."}'
```

### Delete a note
```
curl -X DELETE "http://localhost:8000/note/1"
```

# License
This project is licensed under the MIT License - see the LICENSE file for details.
