# VITyarthi
# Contact Book

A simple command-line Contact Book application written in Python. It allows users to add, view, search, update, and delete contacts.

The contacts are stored permanently in a `contacts.json` file using Python's built-in JSON and file-handling modules.

---

## Features

* Add a new contact
* View all saved contacts
* Search for a contact by name
* Update an existing contact's phone number or email
* Delete a contact
* Automatically save contacts to a JSON file
* Load previously saved contacts when the program starts
* Simple menu-driven command-line interface

---

## Project Structure

The project should have the following structure:

```text
contact-book/
│
├── main.py
├── contacts.json
└── README.md
```

### Files

* **`main.py`** — Contains the complete Python program.
* **`contacts.json`** — Stores contact information. This file is created automatically when the first contact is saved.
* **`README.md`** — Project documentation and setup instructions.

> If `contacts.json` does not exist when the program is started, the application automatically creates the required data structure and creates the file when a contact is added.

---

## Requirements

Before running the project, make sure you have:

* Python 3.8 or newer
* A terminal/command prompt
* A text editor or IDE such as VS Code, PyCharm, or IDLE

The project uses only Python's **standard library**, so no external packages are required.

---

## Step 1: Install Python

Download and install Python from the official Python website:

https://www.python.org/downloads/

During installation on Windows, make sure to select:

```text
Add Python to PATH
```

To verify that Python is installed, open a terminal and run:

```bash
python --version
```

You should see a version similar to:

```text
Python 3.12.0
```

On some systems, you may need to use:

```bash
python3 --version
```

---

## Step 2: Create the Project Directory

Create a folder for the project:

```text
contact-book
```

Open the folder in your preferred code editor.

For example, using VS Code:

```bash
code contact-book
```

---

## Step 3: Add the Python File

Create a file named:

```text
main.py
```

Copy the provided Contact Book Python code into `main.py`.

The program uses:

```python
import json
import os
```

Both modules are included with Python, so they do not need to be installed separately.

---

## Step 4: Set Up a Virtual Environment

A virtual environment is recommended even though this project does not require third-party packages.

### Windows

Open Command Prompt or PowerShell inside the project folder and run:

```bash
python -m venv venv
```

Activate it using:

```bash
venv\Scripts\activate
```

### macOS/Linux

Run:

```bash
python3 -m venv venv
```

Then activate it:

```bash
source venv/bin/activate
```

After activation, the terminal will usually show something similar to:

```text
(venv)
```

---

## Step 5: Install Dependencies

This project has **no external dependencies**.

The required modules are part of Python's standard library:

* `json`
* `os`

Therefore, there is nothing to install with `pip`.

You can verify that the required modules are available by running:

```bash
python -c "import json, os; print('Dependencies are available')"
```

Expected output:

```text
Dependencies are available
```

---

## Step 6: Configuration

No additional configuration is required.

The application uses:

```python
FILE_NAME = "contacts.json"
```

This means the contact data is stored in a file named:

```text
contacts.json
```

in the same directory from which the program is run.

The file is automatically created when contact information is saved.

### Important

Do not manually modify `contacts.json` while the application is running unless you understand the JSON format.

---

## Step 7: Run the Application

Make sure you are inside the project directory.

Run:

```bash
python main.py
```

On macOS/Linux, you may need:

```bash
python3 main.py
```

The program will display:

```text
--- Contact Book ---

1. Add Contact
2. View All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Choose an option (1-6):
```

Enter the number corresponding to the operation you want to perform.

---

## How to Use

### 1. Add Contact

Choose:

```text
1
```

The program will ask for:

```text
Enter name:
Enter phone number:
Enter email:
```

The contact will then be saved to `contacts.json`.

---

### 2. View All Contacts

Choose:

```text
2
```

The program displays all saved contacts.

Example:

```text
--- All Contacts ---

Name: Rahul | Phone: 9876543210 | Email: rahul@gmail.com
Name: Priya | Phone: 9123456780 | Email: priya@gmail.com
```

---

### 3. Search Contact

Choose:

```text
3
```

Enter the name of the contact you want to find.

Example:

```text
Enter name to search: Rahul

Name: Rahul | Phone: 9876543210 | Email: rahul@gmail.com
```

If the contact does not exist:

```text
Contact not found.
```

---

### 4. Update Contact

Choose:

```text
4
```

Enter the name of the contact you want to update.

The program allows you to change the phone number and/or email.

If you leave a field blank, its existing value is retained.

Example:

```text
New phone (leave blank to keep '9876543210'):
New email (leave blank to keep 'rahul@gmail.com'):
```

---

### 5. Delete Contact

Choose:

```text
5
```

Enter the name of the contact you want to delete.

Example:

```text
Enter name to delete: Rahul

Contact 'Rahul' deleted.
```

The change is automatically saved to `contacts.json`.

---

### 6. Exit

Choose:

```text
6
```

The program displays:

```text
Goodbye!
```

and exits.

---

## Data Storage

Contacts are stored in JSON format.

For example:

```json
{
    "Rahul": {
        "phone": "9876543210",
        "email": "rahul@gmail.com"
    },
    "Priya": {
        "phone": "9123456780",
        "email": "priya@gmail.com"
    }
}
```

Each contact contains:

* `name`
* `phone`
* `email`

The contact name is used as the key in the main dictionary.

---

## Error Handling

The application handles several common situations:

### Existing Contact

If you try to add a contact with a name that already exists:

```text
Contact already exists! Use update instead.
```

### Contact Not Found

If you search, update, or delete a contact that does not exist:

```text
Contact not found.
```

### Invalid Menu Option

If an option other than `1`–`6` is entered:

```text
Invalid choice, try again.
```

### Empty Contact List

If no contacts have been saved:

```text
No contacts saved yet.
```

---

## Technologies Used

* **Python 3**
* **JSON**
* **File Handling**
* **Dictionaries**
* **Functions**
* **Conditional Statements**
* **Loops**

### Python Standard Library

```python
import json
import os
```

No third-party libraries are required.

---

## Running the Project from a Fresh Clone

If the project is downloaded or cloned onto a new computer, follow these steps:

```bash
cd contact-book
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Or on macOS/Linux:

```bash
source venv/bin/activate
```

No dependency installation is required.

Finally, run:

```bash
python main.py
```

---

## Troubleshooting

### `python` is not recognized

If the terminal reports that Python is not recognized, install Python and ensure that Python is added to your system PATH.

You can also try:

```bash
python3 main.py
```

### `contacts.json` is missing

This is normal when running the project for the first time.

The program starts with an empty contact dictionary and creates `contacts.json` when a contact is saved.

### JSON File Error

If `contacts.json` has been manually edited and contains invalid JSON, the program may fail to load it.

Restore the file to valid JSON format or remove the corrupted file and restart the application.

---

## Future Improvements

Possible improvements include:

* Validate phone numbers and email addresses
* Search contacts without case sensitivity
* Search by phone number or email
* Sort contacts alphabetically
* Add contact groups/categories
* Add a graphical user interface
* Add password protection
* Add confirmation before deleting a contact
* Export contacts to CSV
* Add unit tests

---

## License

This project is intended for educational and personal use.
