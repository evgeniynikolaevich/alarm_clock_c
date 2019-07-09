import re
def one():
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


def two(files):
    f = []
    mylist_n = [j for i in files for j in i]
    for mylist in mylist_n:
        if mylist != '':
            f.append(mylist)
    return f






def flow():

    files = one()
    clean = two(files)
    print(clean)




if __name__ == "__main__":
    flow()
