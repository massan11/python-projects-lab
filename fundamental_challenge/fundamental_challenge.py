
def get_numbers() -> list[int]:
    
    while True:
        try:
            input_lst = input("Enter numbers sparated by spase: ")
            numbers = list(map(int, input_lst.split()))
            return numbers
        except ValueError:
            print("numbers only!")
    
    
def duplicate_remover(input_num):
    duplicated_num = []
    for i in input_num:
        if i not in duplicated_num:
            duplicated_num.append(i)
    return duplicated_num
    

def sorted_num(duplicated_num):
    sorte_num = sorted(duplicated_num, reverse=True)
    return sorte_num
    

input_num = get_numbers()  
duplicated_num = duplicate_remover(input_num)  
    
numbers = sorted_num(duplicated_num)



with open("output.txt", "w") as f:
    for i in numbers:
        f.write(str(i) + " ")
    f.close()




