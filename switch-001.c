#include<stdio.h>
int main()
{
    int day;//1-mon;2-tues;3-wed
    printf("enter day(1-7):");
    scanf("%d",&day);

switch (day)
{
case'm': printf("monday\n");
    break;
case't': printf("tuesday\n");
    break;
case'w': printf("wednesday\n");
    break;
case'T': printf("thusday\n");
    break;
case'f': printf("friday\n");
    break;
case's': printf("saturday\n");
    break;
case'S': printf("sunday\n");
    break;
default:printf(" not a valid day!\n");
}

return 0;

}