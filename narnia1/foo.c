#include <stdio.h>


void fun() {
  char str[7] = {'h', 'e', 'l', 'l', 'o', '\n', '\0'};
  char fmt[3] = {'%', 's', '\0'};
  //printf(fmt, str);
}

int main() {
    fun();
}
