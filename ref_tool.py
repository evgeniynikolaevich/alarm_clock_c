
import re
import os
from collections import Counter,OrderedDict


def broke_lines(filename):
    allNums = []
    total = []
    with open(filename, "r+") as f:
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


def digit_finder(filename):
    name_with_digits =[]
    files = broke_lines(filename)
    clean = delete_garbage(files)
    digits = remove_words(clean)
    #count duplicates
    e = dict(Counter(digits))
    #sort counters
    d = OrderedDict(sorted(e.items()))
    name_with_digits.append(filename)
    name_with_digits.append(d)
    return name_with_digits

def find_all_files(path):
  files = []
  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
      for file in f:
           if re.match(r'^\w+.py',file):
                 files.append(os.path.join(r, file))
  return files


def search_by_template(dirname):
    d = list()
    for filename in dirname:
        root, ext = os.path.splitext(filename)
        if ext == '.py':
           d.append(filename)
    return d

def search_py_files():
    files = find_all_files(os.getcwd())
    pythons = search_by_template(files)
    return pythons


#input sys.arg after
if __name__=="__main__":
    pyfiles = search_py_files()
    results = map(digit_finder,pyfiles)
    print(list(results))

