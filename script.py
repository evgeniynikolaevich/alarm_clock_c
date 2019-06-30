from file_size import find_size
from search_by_expression import search_videos
from delete_by_time import find_free_space,delete_by_free_space




def main():
    files = search_videos()
    #define how many size videos by hour
    files_by_hour = map(find_size,files)
    total_by_hour = sum(filter(None,files_by_hour))
    stock_size = (total_by_hour*4)/1000000
    space = find_free_space()
    print(stock_size)
    print(space)
    #delete_by_free_space(space,)
if __name__ == "__main__":
    main()

