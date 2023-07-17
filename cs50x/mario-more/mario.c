#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    int space;
    int count = 1;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    space = height - 1;
    for (int j = height; j > 0; j--)
    {
        for (int i = 0; i < space; i++)
        {
            printf(" ");
        }
        space--;
        for (int i = 0; i < count; i++)
        {
            printf("#");
        }
        printf("  ");
        for (int i = 0; i < count; i++)
        {
            printf("#");
        }
        printf("\n");
        count++;
        height--;
    }
}