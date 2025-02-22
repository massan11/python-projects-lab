import argparse
import sys
from operations import file_organizer
from operations import text_manipulation
from operations import calculator
from operations import todo_list

def main():
    '''
    Main function to parse the command line arguments and call the respective functions.'''
    parser = argparse.ArgumentParser(description="CLI Tool for various operations.")
    parser.add_argument("--task", required=True, choices=["file_organizer", "text_manipulation", "calculator", "todo_list"],
                        help="Select the task to perform.")
    
    parser.add_argument("--folder", type=str, help="Folder path to organization.")
    parser.add_argument("--file", type=str, help="File path for text manipulation.")
    parser.add_argument("--action", type=str, help="Action for text manipulation or to-do list.")
    parser.add_argument("--operation", type=str, help="Operation for calculator (add, subtract, multiply, divide).")
    parser.add_argument("--num1", type=float, help="First number for calculator.")
    parser.add_argument("--num2", type=float, help="Second number for calculator.")
    parser.add_argument("--task_text", type=str, help="Task text for to-do list.")
    
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
            
        elif args.task == "calculator":
            if not args.operation or args.num1 is None or args.num2 is None:
                print("Error: --operation, --num1, and --num2 arguments are required for calculator")
                sys.exit(1)
            result = calculator.calculate(args.operation, args.num1, args.num2)
            print(f"Result: {result}")
            
        elif args.task == "todo_list":
            if not args.action or not args.task_text:
                print("Error: --action and --task_text arguments are required for to_do")
                sys.exit(1)
            todo_list.manage_tasks(args.action, args.task_text)
            
        else:
            print("Invalid task. use --help for more information.")
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
        
if __name__ == "__main__":
    main()
    
            

                
    