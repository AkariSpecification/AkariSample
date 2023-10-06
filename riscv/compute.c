#include <stdio.h>
#include <stdint.h>

typedef int16_t __m64[4];
typedef float __m128[4];

void cvtpi16_ps(__m128 *dst, __m64 a)
{
    for (int j = 0; j < 4; j++)
    {
        (*dst)[3 - j] = (float)a[j];
    }
}

int main()
{
    short a, b, c, d;

    scanf("%hu %hu %hu %hu", &a, &b, &c, &d);
    __m64 input = {a, b, c, d};
    __m128 output;
    cvtpi16_ps(&output, input);

    printf("%f %f %f %f\n", output[0], output[1], output[2], output[3]);
    return 0;
}
