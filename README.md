# 🔐 Password Manager (Day 29 - Python Bootcamp)

This project is my **Day 29 Python Bootcamp project** 🚀  
It is a **Password Manager** built with **Tkinter**, **Random**, and **Pyperclip**.  

I used the **password generator code from Day 5** as the foundation, but I improved it with **list comprehension** and added a **Graphical User Interface (GUI)** for a real-world application.

---

## 📌 Features
- 🔑 **Generate secure random passwords** (letters, numbers, and symbols).  
- 📋 **Automatically copy passwords** to your clipboard.  
- 📝 **Save website, email/username, and password** into a local text file (`data.txt`).  
- ⚠️ **Validation**: Warns you if required fields are empty.  
- 🖥️ **User-friendly Tkinter GUI** with labels, entry fields, and buttons.  

---

## 🛠️ Code Overview

### 1. **Imports**
```python
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
```
- `tkinter`: For GUI.  
- `messagebox`: To show alerts and confirmation dialogs.  
- `random`: To generate random letters, numbers, and symbols.  
- `pyperclip`: To copy the generated password to the clipboard.  

---

### 2. **Password Generator**
- Creates a random password using:
  - 8–10 random letters  
  - 2–4 random symbols  
  - 2–4 random numbers  
- Uses **list comprehension** with `random.choice()`.  
- Shuffles the characters for stronger randomness.  
- Inserts the generated password into the entry field and copies it to clipboard.

```python
letters_list = [random.choice(letters) for _ in range(nr_letters)]
numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]

password_list.extend(letters_list)
password_list.extend(numbers_list)
password_list.extend(symbols_list)

random.shuffle(password_list)

password = "".join(password_list)
password_entry.insert(0, password)
pyperclip.copy(password)
```

---

### 3. **Saving Passwords**
- Fetches values from input fields:
  - Website  
  - Email/Username  
  - Password  
- If website or password fields are empty → shows alert.  
- Otherwise, asks for confirmation before saving.  
- Appends the data into `data.txt`.

```python
with open("data.txt", "a") as f:
    f.write(f" {website_input}  | {email_input}  | {password_input}\n")
```

---

### 4. **User Interface (Tkinter)**
- **Window setup**:
  ```python
  window = Tk()
  window.title("Password Manager")
  window.config(pady=50, padx=50)
  ```
- **Canvas**: Displays a logo image (`logo.png`).  
- **Labels**: Website, Email/Username, Password.  
- **Entries**: Input fields for website, email, and password.  
- **Buttons**:
  - *Generate Password* → calls `generate_password()`  
  - *Add* → calls `save()`  

---

## 📂 Files
- `main.py` → The main code.  
- `data.txt` → Stores saved credentials.  
- `logo.png` → Logo displayed in the GUI.  

---

## 🧠 Learning Reflection
- **Day 5**: Created a password generator using loops.  
- **Day 29**: Improved it with **list comprehensions** and built a **Password Manager GUI** with Tkinter.  
- Learned:
  - File handling in Python.  
  - Tkinter layouts (`grid`, `Canvas`, `Label`, `Entry`, `Button`).  
  - Clipboard operations with `pyperclip`.  
  - Validation and confirmation dialogs with `messagebox`.  

---
