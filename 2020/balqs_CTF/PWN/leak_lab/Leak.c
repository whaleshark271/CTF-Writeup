#include "stdio.h"
#include "stdlib.h"
#include "time.h"
#include "stdbool.h"
#include "string.h"
struct Message{
    char* Type;
    char Data[0x20];
};
char secret[8]; 
char *ListType[3] = {"Critical","Warning","Info"};
struct Message ListMessage[8];
char Tempbuffer2[0x300];


void Init(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    int iRandomFD = open("/dev/urandom", 0);
    if(iRandomFD < 0){
        printf("Error!!\n");
        exit(-1);
    }
    read(iRandomFD,secret,8);
    close(iRandomFD);
}
void Menu(){
    printf("#######################\n");
    printf("1. AskSecret\n");
    printf("2. Grill\n");
    printf("3. LeaveMessage\n");
    printf("4. ShowMessage\n");
    printf("5. CheckAns\n");
    printf("#######################\n");
}
void AskSecret(){
    char GuessSecret[8] = {0};
    char TempSecret[8] = {0};
    memcpy(TempSecret,secret,8);
    printf("H:I won't tell you, but maybe you can guess\n");

    printf("Try: ");
    int iReadLength = read(0,GuessSecret,0x10);

    if(iReadLength < 0){
        exit(-1);
    }
    if(memcmp(TempSecret,secret,8)){
        puts("H:Somthing went wrong!");
    }
    else{
        if(!memcmp(TempSecret,GuessSecret,8)){
            puts("H:OK........Maybe you are right");
        }
        else{
            puts("H:NoNoNo");
        }
    }
    memset(TempSecret,0,8);
}
void Grill(){
    int iCounter = 0;
    char buff[2] = {0};
    char TempBuffer[0x208] = {0};
    
    while(1){
        puts("Y:Do you want to surrender?");
        puts("H:Never!!");

        puts("Take some note?[y/n]");
        read(0,buff,2);
        buff[1] = 0;
        if(strcmp(buff,"y") == 0){
            puts("Note: ");
            read(0,TempBuffer,0x210);
            time_t timep;
            time(&timep);
            printf("%d: %s%s\n",iCounter,asctime(gmtime(&timep)),TempBuffer);
        }
        puts("Continue?[y/n]");
        read(0,buff,2);
        buff[1] = 0;
        if(strcmp(buff,"n") == 0){
            break;
        }
        ++iCounter;
    }
    
}
void LeaveMessage(){
    char padding[0x1e0];
    char buffer[0x20] = {0};
    int iMessageIndex = -1;
    printf("Message Index: ");
    scanf("%d",&iMessageIndex);
    if(iMessageIndex >= 0 && iMessageIndex < 8){
        puts("Message Level");
        puts("--------------------------");
        puts("1. Critical");
        puts("2. Warning");
        puts("3. Info");
        puts("--------------------------");
        printf(">");
        int iIndex = -1;
        read(0,padding+0x1e0-2,2);
        padding[0x1e0-1]=0;
        iIndex = atoi(padding+0x1e0-2);
        if(iIndex < 1 || iIndex > 3){
            exit(-1);
        }
        else{
            ListMessage[iMessageIndex].Type = ListType[iIndex-1];
            printf("Message: ");
            int iReadLength = read(0,buffer,0x20);
            int iLength = strlen(buffer);
            memcpy(ListMessage[iMessageIndex].Data,buffer,iLength);
            ListMessage[iMessageIndex].Data[0x20-1] = 0;
        }
    }
}
void ShowMessage(){
    int iMessageIndex = -1;
    printf("Message Index: ");
    scanf("%d",&iMessageIndex);
    if(iMessageIndex >= 0 && iMessageIndex < 8){
        printf("Message Level: %s\n",ListMessage[iMessageIndex].Type);
        printf("Message: %s\n",ListMessage[iMessageIndex].Data);
    }
}
int CheckAnswer(){

    int iType = -1;
    char *StackAns = &StackAns;
    char SecretAns[8] = {0};
    char *PIEAns = &ListMessage;
    char *LibcAns = &system;

    char Input[0x20];
    int ReturnValue = 0;
    memset(Input,0,0x30);
    memcpy(SecretAns,secret,8);
    puts("Type");
    puts("--------------------------");
    puts("1. Partial(Stack,Secret,Canary)");
    puts("2. All(Stack,Secret,PIE,Libc,Canary)");
    puts("--------------------------");
    printf(">");
    scanf("%d",&iType);
    if(iType == 1){
        printf("Stack: ");
        read(0,Input,8);
        printf("Secret: ");
        read(0,Input+8,8);
        printf("Canary: ");
        read(0,Input+0x28,8);

        if(memcmp(Input,&StackAns,8) == 0 && memcmp(Input+8,SecretAns,8) == 0){
            ReturnValue = 2;
        }
    }
    else if(iType == 2){
        
        printf("Input your answer: ");
        read(0,Input+8,0x28);
        
        
        if(memcmp(&StackAns,Input+8,0x20) == 0){
            ReturnValue = 1;
        }
        
    }
    memset(&StackAns,0,0x20);
    
    return ReturnValue;
}



int main(){
    int iResult = 0;
    Init();
    while(1){
        Menu();
        int iIndex = 0;
        printf(">");
        scanf("%d",&iIndex);
        switch(iIndex){
            case 1:
                AskSecret();
                break;
            case 2:
                Grill();
                break;
            case 3:
                LeaveMessage();
                break;
            case 4:
                ShowMessage();
                break;
            case 5:
                iResult = CheckAnswer();
                if(iResult == 1){
                    printf("Good Job!!!\n");
                    system("/bin/sh");
                }
                else if(iResult == 2){
                    puts("Here you go!");
                    system("cat /home/leak/flag1");
                }
                else{
                    printf("It's wrong!!!\n");
                }
                break;
            default:
                exit(0);
                break;
        }
        
    }
    return 0;
}
