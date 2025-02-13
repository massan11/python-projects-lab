
def get_numbers() -> list[int]:
    
    input_lst = input().split()
    input_num = list(map(lambda x: int(x), input_lst))
    return input_num
    
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




