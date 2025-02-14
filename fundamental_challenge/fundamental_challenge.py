
def get_numbers() -> list[int]:
    
    while True:
        try:
            input_lst = input("Enter numbers sparated by spase: ")
            numbers = list(map(int, input_lst.split()))
            return numbers
        except ValueError:
            print("numbers only!")
            
def process_numbers(numbers: list[int]) -> list[int]:
    return sorted(list(set(numbers)), reverse = True)

def save_to_file(numbers: list[int], filename: str = "output.txt") -> None:
    try:
        with open(filename, "w") as f:
            f.write(" ".join(map(str, numbers)))
        print(f"Results saved in {filename}")
    except Exception as e:
        print(f"Error: {e}")



input_num = get_numbers()  
    
numbers = process_numbers(input_num)

save_to_file(numbers)






