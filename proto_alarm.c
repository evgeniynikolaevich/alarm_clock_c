#include<stdlib.h>
#include<unistd.h>
#include<stdio.h>

void play_music();
int fetch();
void tiner();
int range;
int count_time;


int main()
{
    
    fetch();
    count_time = range *60;
    tiner(count_time);
    
    return 1;


}

void play_music(){
    system("afplay 1.mp3");
}


int  fetch()
{
    printf("choose range in minutes/  not any more 60 \n");
    scanf("%d",&range);
    if (range >= 60){
        printf("try again\n");
        fetch(range);
    }
    return range;
  
}
void tiner(count_time)


{
      for(int coun = 0;coun<count_time;coun ++){
        sleep(1);
        printf("%d\n",coun);
      }   
    play_music();     
}
