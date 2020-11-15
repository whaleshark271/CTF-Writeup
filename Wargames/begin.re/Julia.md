# Julia

![1](Pictures/Julia_1.jpg)

The first block of the main function. It checks if there is an argument for the function.

![2](Pictures/Julia_2.jpg)

Not sure what `shl eax, 0` is doing. (Edit: The hint says this does nothing, the compiler might have some issues.)

Starting from the third line, ecx holds the address of the argv array. Then, edx is assigned the address of the second element of argv (argument of the function).

The value of edx is pushed to the stack as the argument for `strlen()`. The return value of `strlen()` is stored in eax once it is finished.

The program then malloc a size of eax + 1 and store the address at dest. It checks if the function fails. If it doesn't, then continue from 0x40109f.

![3](Pictures/Julia_3.jpg)

It pushes the address of the argument onto the stack and then pushes the address of dest. It then calls `strcpy()` to copy the input argument to the malloc space. 