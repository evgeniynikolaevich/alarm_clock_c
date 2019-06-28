from file_size import find_size
from search_by_expression import search_videos

def main():
    files = search_videos()
    files_by_hour = map(find_size,files)
    total_by_hour = sum(filter(None,files_by_hour))
    print(str(total_by_hour/1000000)+'mb')
if __name__ == "__main__":
    main()

