import argparse
import sys
from operations import file_organizer
from operations import text_manipulation


def main():
    parser = argparse.ArgumentParser(description="CLI Tool for various operations.")
    parser.add_argument("--task", required=True, choices=["file_organizer", "text_manipulation"],
                        help="Select the task to perform.")
    
    parser.add_argument("--folder", type=str, help="Folder path to organization.")
    parser.add_argument("--file", type=str, help="File path for text manipulation.")
    parser.add_argument("--action", type=str, help="Action for text manipulation or to-do list.")
    
    
    args = parser.parse_args()
    
    try:
        if args.task == "file_organizer":
            if not args.folder:
                print("Error: --folder argument is required for file_organizer")
                sys.exit(1)
            file_organizer.organize_files(args.folder)
            
        elif args.task == "text_manipulation":
            if not args.file or not args.action:
                print("Error: --file and --action arguments are required for text_manipulation")
                sys.exit(1)
            text_manipulation.process_text(args.file, args.action)
            
        else:
            print("Invalid task. use --help for more information.")
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
        
if __name__ == "__main__":
    main()
    
            

                
    