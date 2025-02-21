import os
import shutil

file_categories = {
    "Dacuments": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Images": [".jpg", ".ipeg", ".png", ".gif", ".bmp"],
    "Music": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

def organize_files(folder_path: str) -> None:
    ''' Organize files in a folder based on their categories.'''
    
    if not os.path.exists(folder_path):
        print(f"Folder path {folder_path} does not exist.")
        return
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Skip if it is a folder
        if os.path.isdir(file_path):
            continue
        
        file_extension = os.path.splitext(file_path)[1].lower()
        destination_folder = "Others" #Default folder
        
        # Find the category for the file
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                destination_folder = category
                break
        
        # Create the category folder if it does not exist    
        category_folder_path = os.path.join(folder_path, destination_folder)
        os.makedirs(category_folder_path, exist_ok=True)
        
        # Move the file to the category folder
        try:
            shutil.move(file_path, os.path.join(category_folder_path, filename))
            print(f"Moved {filename} to {destination_folder}")
        except Exception as e:
            print(f"Error moving {filename}: {e}")
            
if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ")
    organize_files(folder)