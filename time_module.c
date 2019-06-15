#include<stdio.h>
#include<time.h>
/* this module represents time operation */
    

    int range;    
    int difference;


    int choose_range();
    int find_time_range(int range);
    int calculate_time_difference(int difference);
    int find_time();

int main() 
{ 
    return 0; 
}


int find_time_range()
{
    return 1;
}



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






