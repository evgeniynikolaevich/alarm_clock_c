#include<stdio.h>
#include<time.h>
/* this module represents time operation */
    

    int range = 1;    
    int difference;


    int choose_range(int range);
    int fetch();
    int calculate_time_difference(int difference);
    int find_time();

int main() 
{
   /*choose_range(range);*/
    fetch();
    return 1; 
}

int choose_range(int range)
{
    printf("choose range in minutes/  not any more 60 \n");
    scanf("%d",&range);
    if (range >= 60){
        printf("try again\n");
        choose_range(range);
    }
    return range;
}

int fetch()
{
    time_t s, val = 1; 
    struct tm* current_time; 
    //and put this on global variable 
    // time in seconds 
    s = time(NULL); 
  
    // to get current time 
    current_time = localtime(&s); 
  
    // print time in minutes, 
    // hours and seconds 
    printf("%02d:%02d", 
           current_time->tm_hour, 
           current_time->tm_min);
    return 1;
}








//TODO write sequence where at first check how many minutes user fetched after ,need calcultes minutes and hours

/*
int calculate_time_difference(difference)
{
    int time_wanted;
    int loc_time;
    time_wanted = time(NULL) + 10;
    loc_time=localtime(&time_wanted);
    return loc_time;
}








int find_time()
{
    time_t s, val = 1; 
    struct tm* current_time; 
  
    // time in seconds 
    s = time(NULL); 
  
    // to get current time 
    current_time = localtime(&s); 
  
    // print time in minutes, 
    // hours and seconds 
    printf("%02d:%02d:%02d", 
           current_time->tm_hour, 
           current_time->tm_min, 
           current_time->tm_sec); 
}





*/
