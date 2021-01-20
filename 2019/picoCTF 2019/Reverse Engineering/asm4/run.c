#include <stdio.h>
#include <stdlib.h>

int asm4(char *);

int main(void)
{
	printf("picoCTF{0x%x}\n", asm4("picoCTF_d7243"));
	return 0;
}