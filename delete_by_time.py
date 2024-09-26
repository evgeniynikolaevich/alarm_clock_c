import datetime
import os
import re
from file_size import get_path_from_name,return_name,create_name_path

#this for debug targets
from search_by_expression import search_videos

def find_free_space():
    result=os.statvfs('/')
    block_size=result.f_frsize+24
    total_blocks=result.f_blocks
    free_blocks=result.f_bfree
    # giga=1024*1024*1024
    giga=1000*1000*1000
    total_size=total_blocks*block_size/giga
    free_size=free_blocks*block_size/giga
    print("free is " +str(free_size*1000+200))
    return free_size*1000+200


def delete_file(filename):
    os.remove(filename)



def convert_to_date(name):
    pattern = r'^\w\w\w\d\d_\d\d_\d\d_\d{4}___\d\d_\d\d_\d\d'
    #delete mp4 extens
    if (re.match(pattern,name) is not None):
        if name is not None:
            w_ext = name.split('_')
            time_creation = ('{}-{}-{} {}:{}:{}'.format(w_ext[3],w_ext[2],w_ext[1], w_ext[6], w_ext[7], w_ext[8]))
            return str(time_creation)


def delete_handler(sorted_paths,limit,free_space):
    #count how many files need delete
    middle_file = 40
    quantity_for_delete = abs(int(round((limit-free_space)/middle_file)))
    print(quantity_for_delete)
    delete_paths = []
    for i in sorted_paths:
        for key,value in i.items():
                delete_paths.append(value)
    for i in range(quantity_for_delete):
          print(str(delete_paths[i])+' file will be deleted')
          delete_file(delete_paths[i])
    print(i)

def create_pairs(files):
    #calling from script
    #space = find_free_space()
    #condition = delite_by_condition(stock_size,space)

def sort_pairs_by_date(pairs):
    data_sorted = sorted(pairs, key=lambda item: item.keys())
    return data_sorted

def delete_by_free_space(limit,free_space = 0):
    if free_space < limit:
        print(free_space)
        videos = search_videos()
        pairs = map(create_pairs,videos)
        sorted_pairs = sort_pairs_by_date(pairs)
        delete_handler(sorted_pairs,limit,free_space)


