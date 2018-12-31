#include <stdio.h>
#include <string.h>

int main(void)
{
  char *s = "MCMXCIV";
  int len = strlen(s);
  int i, answer =0 ;
  for(i=len-1; i>=0; i--)
  {
    if(s[i] == 'I') answer++;
    else if(s[i] == 'V')
    {
      if(s[i-1] == 'I'){
        answer += 4;
        i--;
      }
      else answer += 5;
    }
    else if(s[i] == 'X')
    {
      if(s[i-1] == 'I')
      {
        answer += 9;
        i--;
      }
      else answer += 10;
    }
    else if(s[i] == 'L')
    {
      if(s[i-1] == 'X')
      {
        answer += 40;
        i--;
      }
      else answer += 50;
    }
    else if(s[i] == 'C')
    {
      if(s[i-1] == 'X')
      {
        answer += 90;
        i--;
      }
      else answer += 100;
    }
    else if(s[i] == 'D')
    {
      if(s[i-1] == 'C')
      {
        answer += 400;
        i--;
      }
      else answer += 500;
    }
    else if(s[i] == 'M')
    {
      if(s[i-1] == 'C')
      {
        answer += 900;
        i--;
      }
      else answer += 1000;
    }
  }
  printf("%d\n", answer);
  return 0;
}
