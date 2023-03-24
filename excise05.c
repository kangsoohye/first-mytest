#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
   FILE* fi;
   int number, middle, high, tot;
   char name[20], line[100];

   if ((fi = fopen("202068062.dat", "rt")) == NULL)
   {
      puts("202068062.dat - 파일이 없습니다.\n");
      return -1;
   }

   printf("석차  학번  중간성적  기말성적\t총점\t평균\n");
   printf("====  ====  =======   =======\t====\t====\n");

   while (fgets(line, 100, fi) != NULL)
    {
        sscanf(line, "%d %s %d %d", &number, name, &middle, &high);
        tot = middle + high;
        printf("%2d\t%-4s  %d\t%d\t%d\t%5.2f\n", number, name, middle, high, tot, (float)tot / 2);
    }
   fclose(fi);
   return 0;
}