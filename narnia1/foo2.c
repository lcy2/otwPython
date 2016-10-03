#include <stdio.h>


void fun() {
  unsigned char str_len = 6;
  unsigned char fmt_len = 2;

  char str_chars[6] = {'h', 'e', 'l', 'l', 'o', '\n'};
  char fmt_chars[2] = {'%', 's'};
  
  char* str = (char*) calloc(str_len, sizeof(char));
  char* fmt = (char*) calloc(fmt_len, sizeof(char));

  strncpy(str, str_chars, str_len);
  strncpy(fmt, fmt_chars, fmt_len);
  
  printf(fmt, str);
}

int main() {
    fun();
}
