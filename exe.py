import re
from collections import Counter,OrderedDict

def broke_lines():
    allNums = []
    total = []
    with open("1.py", "r+") as f:
        data = f.readlines() # read the text file
        for line in data:
            allNums += line.strip().split() # get a list containing all the numbers in the file
        for num in allNums:
            s = re.split('\W',num)
            total.append(s)
        return total


def delete_garbage(files):
    f = []
    mylist_n = [j for i in files for j in i]
    for mylist in mylist_n:
        if mylist != '':
            f.append(mylist)
    return f


def remove_words(files):
    n =[]
    for file in files:
        if re.match(r'^([0-9]{1,10})',file):
            n.append(file)
    return n


def flow():

    files = broke_lines()
    clean = delete_garbage(files)
    digits = remove_words(clean)
    e = dict(Counter(digits))
    d = OrderedDict(sorted(e.items()))
    print(d)


if __name__ == "__main__":
    flow()
