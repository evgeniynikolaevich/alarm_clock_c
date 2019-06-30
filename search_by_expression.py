#search file with date and mp4 extension
import re
import os

def find_all_files(path):
  files = []
  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
      for file in f:
          if re.match(r'^\w\w\w\d\d_\d\d_\d\d_\d{4}___\d\d_\d\d_\d\d',file):
                files.append(os.path.join(r, file))
  return files


def search_by_template(dirname):
    d = list()
    for filename in dirname:
        root, ext = os.path.splitext(filename)
        if ext == '.mp4':
           d.append(filename)
    return d

def search_videos():
    files = find_all_files(os.getcwd())
    video = search_by_template(files)
    sort_videos = sorted(video)
    return sort_videos

if __name__ == "__main__":
    print(search_videos())


