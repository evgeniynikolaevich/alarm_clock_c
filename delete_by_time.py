import datetime
import os
import re
from file_size import get_path_from_name,return_name,create_name_path
from collections import OrderedDict

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
    print('total_size = %s' % total_size)
    print("free is " +str(free_size*1000))
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


def delete_handler(sorted_paths,limit):
    #count how many files need delete
    middle_file = 40
    quantity_for_delete = round((free_space - limit)/middle_file)
    for i in range(quantity_for_delete):
        for key,value in i:
            delete_file(sorted_path[i])
            del sorted_path[i]
            print(str(i)+' file will be deleted')


def create_pairs(files):
    #calling from script
    #space = find_free_space()
    #condition = delite_by_condition(stock_size,space)
    #sorted_list = sort_list_by_categories(categories)
    #list_with_datetime = sort_by_date_time(sorted_list)
    #delete_handler(sorted_paths)
    path = get_path_from_name(files)
    name = return_name(path)
    date_create = convert_to_date(name)
    name_path = create_name_path(date_create,path)
    return name_path

def sort_pairs_by_date(pairs):
    data_sorted = sorted(pairs, key=lambda item: item.keys())

def delete_by_free_space(free_space,limit):
    videos = search_videos()
    pairs = map(create_pairs,videos)
    sorted_pairs = sort_pairs_by_date(pairs)
    #delete_handler(freespace,limit)


