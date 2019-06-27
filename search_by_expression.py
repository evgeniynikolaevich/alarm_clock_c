
import re
import os

def find_all_files(path):
  files = []
  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
      for file in f:
          files.append(os.path.join(r, file))
  return files


def search_by_template(dirname):
    for filename in dirname:
        root, ext = os.path.splitext(filename)
        if ext == '.mp4':
            print(filename)


def flow():
    files = find_all_files(os.getcwd())
    search_by_template(files)

if __name__ == "__main__":
    flow()


