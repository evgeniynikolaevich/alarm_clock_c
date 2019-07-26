import datetime
import os
import re
from collections import OrderedDict
# from file_size import get_path_from_name,return_name,create_name_path

#TODO remember wrong regexp pattern return # WARNING: NONE
#_PATH = '/home/_VideoArchive'
_PATH = os.getcwd()


def convert_name_to_datetime(name):
      pattern = r'\w{1,3}\d{1,3}_\d\d_\d\d_\d{4}___\d\d_\d\d_\d\d'
      # delete mp4 extens
      print('name for convert')
      print(name)
      if re.match(pattern, name) is not None:
          if name is not None:
              w_ext = name.split('_')
              # CONVERT!!!!
              # time_creation = datetime.time(year =int(w_ext[3]),month=int(w_ext[2]),day =int(w_ext[1]),
              #                              hour = int(w_ext[6]),min = int(w_ext[7]),sec = int(month[8])
              # fix datetime
              dt = datetime.datetime(int(w_ext[3]), int(w_ext[2]), int(w_ext[1]))
              tm = datetime.time(int(w_ext[6]), int(w_ext[7]), int(w_ext[8]))
              time_creation = dt.combine(dt, tm)
              # datetime_object = datetime.strptime('{}/{}/{} {}:{}:{}'.format(int(w_ext[1]),int(w_ext[2]),int(w_ext[3]), int(w_ext[6]), int(w_ext[7]), int(w_ext[8])), '%m/%d/%Y %I:%M%p')
              print('&'*50)
              print('time creation from name')
              print(time_creation)
              return time_creation


def find_weight(path_to_file):
  if path_to_file is not None:
      statinfo = os.stat(path_to_file)
      size = statinfo.st_size
      return size


def find_older_one_hour_files(name_path,time_limit):
      # fix compare staff
      for name, path in name_path.items():
          time_creation = convert_name_to_datetime(name)
          print(time_creation)
          if time_creation <= time_limit:
              return path


def create_limit():
  today = datetime.datetime.now()
  hour = datetime.timedelta(hours=1)
  limit = today - hour
  delay = limit.replace(second = 0,microsecond=0)
  return delay

#time for shitcode!!!!!
def day_limit():
    today = datetime.datetime.now()
    hour = datetime.timedelta(days=1)
    limit = today - hour
    delay = limit.replace(second = 0,microsecond=0)
    return delay


def find_size(filename):
  time_limit = create_limit()
  path = get_path_from_name(filename)
  name = return_name(path)
  name_path = create_name_path(name, path)
  file_older_one_hour = find_older_one_hour_files(name_path,time_limit)
  weight = find_weight(file_older_one_hour)
  return weight

def find_all_files(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if re.match(r'\w{1,3}\d{1,3}_\d\d_\d\d_\d{4}___\d\d_\d\d_\d\d.mp4', file):
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
    files = find_all_files(_PATH)
    video = search_by_template(files)
    return video

def find_free_space():
    result = os.statvfs('/')
    block_size = result.f_frsize + 24
    total_blocks = result.f_blocks
    free_blocks = result.f_bfree
    # giga=1024*1024*1024
    giga = 1000 * 1000 * 1000
    total_size = total_blocks * block_size / giga
    free_size = free_blocks * block_size / giga
    return (free_size * 1000 + 200)*100000


def delete_file(filename):
    os.remove(filename)

def convert_to_date(name):
    pattern = r'\w{1,3}\d{1,3}_\d\d_\d\d_\d{4}___\d\d_\d\d_\d\d'
    # delete mp4 extens
    if re.match(pattern, name) is not None:
        if name is not None:
            w_ext = name.split('_')
            time_creation = ('{}-{}-{} {}:{}:{}'.format(w_ext[3], w_ext[2], w_ext[1], w_ext[6], w_ext[7], w_ext[8]))
            return str(time_creation)


def delete_handler(sorted_paths, limit, free_space = 0):
    # count how many files need deleted
    middle_file = 40
    quantity_for_delete = abs(int(round((limit - free_space) / middle_file)))
    print('files need deleted '+str(quantity_for_delete))
    delete_paths = []
    for i in sorted_paths:
        for key, value in i.items():
            delete_paths.append(value)
    try:
        for i in range(quantity_for_delete):
            print(str(delete_paths[i]) + ' file will be deleted')
            #delete_file(delete_paths[i])
        print(str(len(quantity_for_delete))+'will deleted')
    except:
        pass


def create_pairs(files):
    path = get_path_from_name(files)
    name = return_name(path)
    date_create = convert_to_date(name)
    name_path = create_name_path(date_create, path)
    return name_path


def sort_pairs_by_date(pairs):
    pairs_for_sort = OrderedDict(pairs)
    data_sorted = sorted(pairs, key=lambda item: item.keys()[-1])
    return data_sorted


def delete_by_free_space(limit, free_space=0):
    if free_space < limit:
        videos = search_videos()
        #add something here compare with today delay
        pairs = map(create_pairs, videos)
        #here create delay for files and seacrh older 1 day # WARNING:i use older func find older one hour he was be usefull for this target
        #TODO after need refactor change names for find_older_one_hour and create_limit
        older_one_day_delay =day_limit()
        files_older_one_day = find_older_one_hour_files(pairs,older_one_day_delay)
        sorted_pairs = sort_pairs_by_date(files_older_one_day)
        print('this sorted parts')
        print(sorted_pairs)
        delete_handler(sorted_pairs,limit,free_space)


def get_path_from_name(name):
  path = os.path.abspath(name)
  return path

def return_name(path):
  filename = os.path.splitext(path)[0]
  name = filename.split('/')[-1]
  return name


def create_name_path(name, path):
  # name-key is time of creation
  name_path = {name: path}
  return name_path
