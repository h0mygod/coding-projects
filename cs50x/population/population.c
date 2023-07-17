#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start;
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);

    // TODO: Prompt for end size
    int end;
    do
    {
        end = get_int("End size: ");
    }
    while (end < start);

    // TODO: Calculate number of years until we reach threshold
    int pop = start;
    int years = 0;
    while (pop < end)
    {
        pop = pop + (pop / 3 - pop / 4);
        years++;
    };
    // TODO: Print number of years
    printf("Years: %i\n", years);
}
