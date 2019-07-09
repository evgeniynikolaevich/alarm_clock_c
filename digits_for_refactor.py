from digit_finder import digit_finder

import re
import os

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






if __name__=="__main__":
    pyfiles = search_py_files()
    results = map(digit_finder,pyfiles)
    print(list(results))

