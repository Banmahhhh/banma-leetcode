#include <stdio.h>

/*
the volume is determined by the shorter line
go through from the first one, and find the farthest line which is longer than it
*/

int main(void)
{
  int height[11] = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1};
  int heightSize = 10;
  int maxCon = 0;
  int i, j;
  int start = 0, end = heightSize-1;
  while((end - start) != 0)
  {
    printf("start is %d, end is %d\n", start, end);
    if(height[start] > height[end])
    {
      if(height[end]*(end-start) > maxCon)
        maxCon = height[end]*(end-start);
      end--;
    }
    else if(height[start] < height[end])
    {
      if(height[start]*(end-start) > maxCon)
        maxCon = height[start]*(end-start);
      start++;
    }
    else
    {
      if(height[start]*(end-start) > maxCon)
        maxCon = height[start]*(end-start);
      for(i=0; height[start+i] == height[end-i] && i<=(end-start-1)/2; i++)
        printf("i is %d\n", i);
      if(height[start+i] > height[end-i]) start++;
      else end--;
    }
    printf("container is %d\n", maxCon);
  }
  printf("%d\n", maxCon);
  return 0;
}
