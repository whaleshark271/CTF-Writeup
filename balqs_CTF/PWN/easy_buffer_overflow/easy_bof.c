#include <stdio.h>
#include <stdlib.h>

void evil(){
	system("/bin/sh");
}

int main(){
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
	char input[10];
	puts("just easy buffer overflow");
	puts("Input:");
	gets(input);
	puts(input);
}
