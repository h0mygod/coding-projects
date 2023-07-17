#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long cc = get_long("Number: ");
    int sum = 0;
    int length = 0;
    int digits[16];
    while (cc != 0)
    {
        digits[length] = cc % 10;
        cc /= 10;
        length++;
    }
    for (int i = 0; i < length; i++)
    {
        if (i % 2 != 0)
        {
            if (2 * (digits[i]) >= 10)
            {
                int temp = 2 * (digits[i]);
                while (temp != 0)
                {
                    sum += temp % 10;
                    temp /= 10;
                }
            }
            else
            {
                sum += 2 * (digits[i]);
            }
        }
        else
        {
            sum += digits[i];
        }
    }

    if (sum % 10 == 0 && length > 12)
    {
        if (digits[length - 1] == 3 && (digits[length - 2] == 4 || digits[length - 2] == 7))
        {
            printf("AMEX\n");
        }
        else if (digits[length - 1] == 4)
        {
            printf("VISA\n");
        }
        else if (digits[length - 1] == 5 && (digits[length - 2] > 0 && digits[length - 2] < 6))
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
