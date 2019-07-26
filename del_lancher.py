from delvideo_addition import find_size
from delvideo_addition import search_videos
from delvideo_addition import find_free_space,delete_by_free_space,create_limit
import datetime

def delvideo_addition_main():
    #timedelta hour
    rounding = 1000000
    time_limit = create_limit()
    files = search_videos()
    videos_none = filter(None,files)
    files_by_hour = map(find_size,videos_none)
    total_by_hour = sum(filter(None,files_by_hour))
    print('from hour')
    print(total_by_hour)
    limit = (total_by_hour*4)
    print('limiting')
    print(limit/rounding)
    free_space = find_free_space()
    print(free_space/rounding)
    delete_by_free_space(limit)

if __name__ == "__main__":
    delvideo_addition_main()
