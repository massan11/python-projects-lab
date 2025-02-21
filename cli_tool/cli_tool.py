import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="CLI Tool for various operations.")
    parser.add_argument("--task", required=True, choices=["file_organizer", "text_manipulation", "calculator", "todo_list", "password_generator"],
                        help="Select the task to perform.")
    
    parser.add_argument("--folder", type=str, help="Folder path to organization.")
    
    args = parser.parse_args()
    
    try:
        if args.task == "file_organizer":
            if not args.folder:
                print("Error: --folder argument is required for file_organizer")
                sys.exit(1)
            file_organizer.organize_files(args.folder)
            
        else:
            print("Invalid task. use --help for more information.")
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
        
if __name__ == "__main__":
    main()
    
            

                
    