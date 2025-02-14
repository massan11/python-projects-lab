
def get_numbers() -> list[int]:
    
    while True:
        try:
            input_lst = input("Enter numbers sparated by spase: ")
            numbers = list(map(int, input_lst.split()))
            return numbers
        except ValueError:
            print("numbers only!")
    
    
def duplicate_remover(numbers):
    duplicated_num = []
    for i in numbers:
        if i not in duplicated_num:
            duplicated_num.append(i)
    return duplicated_num
    

def sorted_num(duplicated_num):
    sorte_num = sorted(duplicated_num, reverse=True)
    return sorte_num

def save_to_file(numbers: list[int], filename: str = "output.txt") -> None:
    try:
        with open(filename, "w") as f:
            f.write(" ".join(map(str, numbers)))
        print(f"Results saved in {filename}")
    except Exception as e:
        print(f"Error: {e}")



input_num = get_numbers()  
duplicated_num = duplicate_remover(input_num)  
    
numbers = sorted_num(duplicated_num)

save_to_file(numbers)






