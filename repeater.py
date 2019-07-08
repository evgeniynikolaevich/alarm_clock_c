import re
import os



def break_by_word():
   with open(os.getcwd()+'/freeze_15_percent.py') as f:
    for line in f:
        for word in line.split():
             for i in re.findall(r'^\d+', word):
                 print(word)




def find_number_in_file():
    l = []
    with open(os.getcwd()+'/freeze_15_percent.py') as file:
        for line in file:
            for i in re.findall(r'\d', line):
                l.append(i)

    return l


def unpack_unique_values(list_):
    result = list(set(list_))
    return result


def flow():
    #numbers = find_number_in_file()
    #unique = unpack_unique_values(numbers)
    break_by_word()




if __name__ == "__main__":
    flow()
