#include <stdio.h>
#include <stdlib.h>

int main(){
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
	char input[10];
	int a = 0x0;
	puts("just change variable");
	puts("Input:");
	gets(input);
	if(a == 0xdeadbeef) {
		system("/bin/sh");
	}
	puts(input);
}
