#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width; x++)
        {
            if (!image[y][x].rgbtRed && !image[y][x].rgbtBlue && !image[y][x].rgbtGreen)
            {
                image[y][x].rgbtRed = 255;
                image[y][x].rgbtGreen = 255;
                image[y][x].rgbtBlue = 0;
            }
        }
    }
}
