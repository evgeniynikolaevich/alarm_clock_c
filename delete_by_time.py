import os
import datetime
requeried_space = 1
limit = 2
stock_size = 2000
from file_size import convert_name_to_datetime


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







def check_categories(file):
    date_creation = convert_name_to_datetime(file)
    today = datetime.datetime.today()
    #most old
    undef_delta = today - datetime.timedelta(days = 16)
    seven_day_delta = today-datetime.timedelta(days = 7)
    fifteen_day_delta = today -datetime.timedelta(days = 15)
    categories = dict()
    if date_creation < seven_day_delta:
        categories = {'seven_days' :[]}
        categories['seven_days'].append(date_creation)
        categories['seven_days'].append(file)
    if date_creation >= fifteen_day_delta:
        categories = {'fifteen_days' :[]}
        categories['fifteen_days'].append(date_creation)
        categories['fifteen_days'].append(file)
    if date_creation <= undef_delta:
        categories = {'indef' :[]}
        categories['indef'].append(date_creation)
        categories['indef'].append(file)

    return categories





def main():
    #space = find_free_space()
    #condition = delite_by_condition(stock_size,space)
    print(check_categories("cam42_09_06_2019___01_30_15.mp4"))


if __name__ == "__main__":
    main()



