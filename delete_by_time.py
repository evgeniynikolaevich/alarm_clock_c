import os
requeried_space = 1
limit = 2
stock_size = 2000
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


def find_list():
#change import from show video for import specific files

    path_ = os.getcwd()
    files = os.listdir(path_)
    return files(path_)


def date_analizator(date):
    #date today
    #seven_day_delay
    #fiteen_day_delay
    #unlimited_delay
    if date < delay:



def unpack_date(file):
    pass


def pack_date(file):
    pass



def find_categories(date_creation):
    today = datetime.datetime.today()
    #most old
    undef_delta = today - datetime.timedelta(days = 16)
    seven_day_delta = todaydatetime.timedelta(days = 7)
    fifteen_day_delta = datetime.timedelta(day = 15)

    categories = {'indef':[],'seven_days':[],'fifteen_days':[]}
    date = find_date_creation(date_creation)
    if date_creation > sevenday_delta:
        categories['seven_day'].append(date_creation)
    if date_creation <= fifteen_day_delta
        categories['fifteen_day'].append(date_creation)
    if date_creation >= undef_delta:
        categories['indef'].append(date_creation)

    return categories

def del_by_category(categories):
    if len(categories["indef"]) != 0:
        delite_file(categories['indef'])
        del categories['indef'][]
    if len(categories['fifteen_day']) !=0:
        delite_file(categories['seven_day'])
        del categories['seven_day'][]
    if len(categories['seven_day']) !=0:
        delite_file(categories['seven_day'])
        del categories['seven_day'][]



def main()




def delete_file(filename):
    os.remove(filename)

def delite_by_condition(stock_size,space):
    if space > stock_size:
        print("You have enough space")
    else:
        enough = False
        counter()


def counter():




def main():
    space = find_free_space()
    condition = delite_by_condition(stock_size,space)



if __name__ == "__main__":
        print(main())

def separate_by_category(files):
    files = find_older_files()


def delete_by_category():
    files = find_older_files()
    category = separate_by_category()
    pass


def delete_by_category():
    pass

