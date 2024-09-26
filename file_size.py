import re
import os
import datetime
#files = [f for f in os.listdir('.') if re.match(r'^\w\w\w\d\d_\d\d_\d\d_\d{4}___\d\d_\d\d_\d\d.mp4', f)]
#


def get_path_from_name(name):
    path = os.path.abspath(name)
    return path


def return_name(path):
    filename = os.path.splitext(path)[0]
    name = filename.split('/')[-1]
    return name




def create_name_path(name,path):
    #name-key is time of creation
    name_path ={}
    name_path[name] = path
    return name_path


def convert_name_to_datetime(name):
    pattern = r'^\w\w\w\d\d_\d\d_\d\d_\d{4}___\d\d_\d\d_\d\d'
    #delete mp4 extens
    if (re.match(pattern,name) is not None):
            if name is not None:
                w_ext = name.split('_')
                #CONVERT!!!!
                #time_creation = datetime.time(year =int(w_ext[3]),month=int(w_ext[2]),day =int(w_ext[1]),
                #                              hour = int(w_ext[6]),min = int(w_ext[7]),sec = int(month[8])
                #fix datetime
                dt = datetime.datetime(int(w_ext[3]),int(w_ext[2]),int(w_ext[1]))
                tm = datetime.time(int(w_ext[6]),int(w_ext[7]),int(w_ext[8]))
                time_creation = dt.combine(dt, tm)
                #datetime_object = datetime.strptime('{}/{}/{} {}:{}:{}'.format(int(w_ext[1]),int(w_ext[2]),int(w_ext[3]), int(w_ext[6]), int(w_ext[7]), int(w_ext[8])), '%m/%d/%Y %I:%M%p')
                print(time_creation)
                return time_creation

def create_limit():
    today = datetime.datetime.now()
    hour = datetime.timedelta(hours =1)
    limit = today - hour
    return limit


def find_older_one_hour_files(name_path):
    #fix compare staff
    limit = create_limit()
    limit = today - hour
    return limit


def find_older_one_hour_files(name_path):
    #fix compare staff
    limit = create_limit()
    for name,path in name_path.items():
        time_creation = convert_name_to_datetime(name)
        if time_creation >= limit:
           return path


def find_weight(path_to_file):
    if path_to_file is not None:
         statinfo = os.stat(path_to_file)
         size = statinfo.st_size
         return size

def find_size(filename):
    path = get_path_from_name(filename)
    name = return_name(path)
    name_path = create_name_path(name,path)
    file_older_one_hour = find_older_one_hour_files(name_path)
    weight = find_weight(file_older_one_hour)
    return weight


