#include <stdio.h>


void fun() {
  char str[50];
  syscall(3,0,str,10 );
  puts(str);
}

int main() {
    fun();
}
