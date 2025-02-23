# **CLI Tool - Python Job Simulation 🚀**

## **📌 Overview**
This **CLI (Command-Line Interface) Tool** is part of my **Python Job Simulation** project.  
It provides multiple functionalities, including:

✅ **File Organizer** - Automatically sorts files into folders based on their type.  
✅ **Text Manipulation** - Processes text files (count words, remove duplicates, convert to uppercase).  
✅ **Simple Calculator** - Performs basic arithmetic operations (add, subtract, multiply, divide).  
✅ **To-Do List Manager** - Adds, removes, and lists tasks via the command line.  
✅ **Password Generator** - Generates secure passwords of customizable length.  

---

## **📌 How to Install & Run**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/massan11/Python-Job-Simulation.git
cd Python-Job-Simulation/cli_tool

### **2️⃣ Run the CLI Tool**
```sh
To see available options, run:
python cli_tool.py --help
**Output:**
usage: cli_tool.py --task {file_organizer,text_manipulation,calculator,todo_list,password_generator} [options]
📌 Available Tasks & Usage
1️⃣ File Organizer
Automatically organizes files in a specified folder.


python cli_tool.py --task file_organizer --folder "C:/Users/Downloads"
✅ Moves images, PDFs, music, etc., into categorized folders.

2️⃣ Text Manipulation
Perform operations on text files.

Count Words

python cli_tool.py --task text_manipulation --file sample.txt --action count_words
Remove Duplicate Lines

python cli_tool.py --task text_manipulation --file sample.txt --action remove_duplicates
Convert to Uppercase

python cli_tool.py --task text_manipulation --file sample.txt --action to_uppercase
3️⃣ Simple Calculator
Perform arithmetic calculations.


python cli_tool.py --task calculator --operation add --num1 10 --num2 5
✅ Supported operations: add, subtract, multiply, divide

4️⃣ To-Do List Manager
Manage tasks via the command line.

Add a Task

python cli_tool.py --task todo_list --action add --task_text "Buy groceries"
Remove a Task

python cli_tool.py --task todo_list --action remove --task_text "Buy groceries"
List All Tasks

python cli_tool.py --task todo_list --action list
Clear All Tasks

python cli_tool.py --task todo_list --action clear
5️⃣ Password Generator
Generate a secure password of a given length.


python cli_tool.py --task password_generator --length 12
✅ The generated password includes uppercase, lowercase, numbers, and special characters.

📌 Project Structure

📦 cli_tool
┣ 📜 cli_tool.py  # Main script to handle CLI commands
┣ 📂 operations/   # Contains all feature modules
┃ ┣ 📜 file_organizer.py
┃ ┣ 📜 text_manipulation.py
┃ ┣ 📜 calculator.py
┃ ┣ 📜 todo_list.py
┃ ┣ 📜 password_generator.py
┣ 📜 README.md  # Project documentation
📌 Technologies Used
✅ Python 3
✅ argparse - Handles command-line arguments
✅ os, shutil - File system operations
✅ random, string - Password generation

📌 Future Improvements
🔹 Add more text manipulation features (e.g., find & replace).
🔹 Improve the file organizer (custom user-defined rules).
🔹 Encrypt saved passwords.

📌 Contributing
If you have suggestions or want to contribute, feel free to submit a pull request! 🚀

🔗 Related Links
📄 Main Project Repository: Python Job Simulation
📄 Progress Tracker: Google Doc
