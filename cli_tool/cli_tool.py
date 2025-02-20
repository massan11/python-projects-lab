import argparse


def main():
    parser = argparse.ArgumentParser(description="CLI Tool for various operations.")
    parser.add_argument("--task", required=True, choices=["file_organizer", "text_manipulation", "calculator", "todo_list", "password_generator"],
                        help="Select the task to perform.")
    