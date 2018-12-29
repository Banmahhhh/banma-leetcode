#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(void)
{
  char s[] = "aa";
  if(s[0] == 0)
    return 0;
  int len = strlen(s);
  int i;
  int middle_temp = 0;
  int maxlen = 1;
  int middle = 0;
  for(i=0; i<len-1; i++)
  {
    printf("i is %d\n", i);
    int start;
    int templen;
    if(s[i-1] == s[i+1])
    {
      middle_temp = i;
      for(start=2; start<=i && start <= (len-i); start++)
        if(s[i-start] != s[i+start])
          break;
      if((start*2-1) > maxlen)
      {
        middle = middle_temp;
        printf("first, start is %d\n", start);
        maxlen = start*2-1;
      }
    }
    if(s[i] == s[i+1])
    {
      middle_temp = i;
      for(start=1; start<=i && start < (len-i); start++)
        if(s[i-start] != s[i+start+1])
          break;
      printf("end at %d\n", start);
      if((start*2) > maxlen)
      {
        middle = middle_temp;
        maxlen = start*2;
      }
    }
  }

  printf("middle is %d\n", middle);
  printf("maxlen is %d\n", maxlen);
  char* answer = (char*)malloc(sizeof(char)*(maxlen+1));
  int qutayade;
  if(maxlen%2 == 1)
    qutayade = middle-(maxlen-1)/2;
  else qutayade = middle-(maxlen-2)/2;
  int j;
  for(j=0; j < maxlen; j++)
    answer[j] = s[qutayade+j];
    //strncpy(answer, s+(middle-(maxlen-1)/2), maxlen);
    //strncpy(answer, s+(middle-(maxlen-2)/2), maxlen);
  puts(answer);
  return 0;
}
