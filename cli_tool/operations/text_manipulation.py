import os
import sys

def count_words(file_path: str) -> int:
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return len(text.split())
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def remove_duplicates(file_path: str) -> None:
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            
        unique_lines = list(set(lines))
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(unique_lines)
            
        print(f"Duplicates removed from {file_path}")
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
        
def to_uppercase(file_path: str) -> None:
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text.upper())
        
        print(f"Converted text to uppercase in {file_path}")
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
        
def process_text(file_path: str, action: str) -> None:
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
        
    if action == "count_words":
        print(f"Word count: {count_words(file_path)}")
    elif action == "remove_duplicates":
        remove_duplicates(file_path)
    elif action == "to_uppercase":
        to_uppercase(file_path)
    else:
        print(f"Error: Invalid operation {action}")
        sys.exit(1)