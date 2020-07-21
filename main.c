#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int main()
{
    int tinggi_segitiga;
    int e;
    e=1;
    printf("Masukan Tinggi Segitiga : \n\n");
    scanf("%d",&tinggi_segitiga);
    for(int i=1;i<=tinggi_segitiga;i++)
        {
            for(int j=tinggi_segitiga;j>=i;j--)
                {
                    printf(" ");
                }
            for(int k=1;k<=e;k++)
                {
                    printf(" X");
                }
            e=e+1;
            printf("\n");
        }
    getch();
}
