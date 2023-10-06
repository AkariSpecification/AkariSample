#include <stdio.h>
#include <xmmintrin.h>
int main()
{
    short d1, d2, d3, d4;

    scanf("%hu %hu %hu %hu", &d1, &d2, &d3, &d4);
    __m64 a = _mm_set_pi16(d1, d2, d3, d4);
    __m128 b = _mm_cvtpi16_ps(a);

    float *f = (float *)&b;
    printf("%f %f %f %f\n", f[0], f[1], f[2], f[3]);

    return 0;
}
