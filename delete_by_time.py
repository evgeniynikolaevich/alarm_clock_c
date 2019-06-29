import os
import datetime
from file_size import convert_name_to_datetime
#this for debug targets
from search_by_expression import search_videos

def find_free_space():
    result=os.statvfs('/')
    block_size=result.f_frsize
    total_blocks=result.f_blocks
    free_blocks=result.f_bfree
    # giga=1024*1024*1024
    giga=1000*1000*1000
    total_size=total_blocks*block_size/giga
    free_size=free_blocks*block_size/giga
    print('total_size = %s' % total_size)
    return free_size*1000


def delete_file(filename):
    os.remove(filename)





def check_categories(file):
    date_creation = convert_name_to_datetime(file)
    today = datetime.datetime.now()
    #most old
    undef_delta = today - datetime.timedelta(days = 17)
    seven_day_delta = today-datetime.timedelta(days = 7)
    fifteen_day_delta = today -datetime.timedelta(days = 15)
    categories = dict()
    if seven_day_delta <= date_creation:
        categories = {'seven_days' :[]}
        categories['seven_days'].append(date_creation)
        categories['seven_days'].append(file)
    elif fifteen_day_delta < date_creation:
        categories = {'fifteen_days' :[]}
        categories['fifteen_days'].append(date_creation)
        categories['fifteen_days'].append(file)
    else:
        print(undef_delta < date_creation)
        categories = {'indef' :[]}
        categories['indef'].append(date_creation)
        categories['indef'].append(file)

    return categories

#target unpack dict
#and files have infinied
#sorting date by date time
# and return list with path for delete


def sort_list_by_categories(list_categories):
    #put to end new and put to begin older
    sorted_list = []
    for key,value in list_categories:
        if key == '7days':
            sorted_list.append(value)
            if key == '15days':
                sorted_list.append(value)
                if key == 'indef':
                    sorted_list.append(value)

    return sorted_list

def sort_by_date_time(sorted_list):
    now = datetime.datetime.now()
    sorted_paths = []
    for i in sorted_list:
        if now > i[1]:
            sorted_paths.append(i[2])
    return sorted_paths


def delete_handler(sorted_paths):
    #count how many files need delete
    quantity_for_delete = round((free_space - limit)/middle_file)
    for i in range(quantity_for_delete):
        delete_file(sorted_path[i])
        del sorted_path[i]
        print('file will be deleted')


def delete_by_free_space(files,freespace = 10000):
    #calling from script
    #space = find_free_space()
    #condition = delite_by_condition(stock_size,space)
    categories = map(check_categories,files)
    #sorted_list = sort_list_by_categories(categories)
    #list_with_datetime = sort_by_date_time(sorted_list)
    #delete_handler(sorted_paths)


if __name__ == "__main__":
    videos = search_videos()
    delete_by_free_space(videos)



