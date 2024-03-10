#include <stdio.h>
#include <math.h>

int main() {
    int N = 3;                                   // The number of vectors, can be increased for different inputs
    int x_components[] = {104,105,106};        // Array containing the x components of the vectors
    int y_components[] = {30,31,32};        // Array containing the y components of the vectors
    int resx = 0;                                // Sum of all x components
    int resy = 0;                                // Sum of all y components
    int j = N - 1;                               // Loop controller
    double result = 0;                           // To store the value returned by square root
    int resx_sq, resy_sq;                        // To store the square of the x and y components of the resultant
    int int_part_of_res, dec_part_of_res;        // Integer and decimal parts of the resultant magnitude

    // Calculate the sum of x and y components
    while (j >= 0) {
        resx += x_components[j];
        resy += y_components[j];
        j--;
    }

    // Calculate the square of x and y components and find the magnitude
    resx_sq = pow(resx, 2);
    resy_sq = pow(resy, 2);
    result = sqrt(resx_sq + resy_sq);

    // Extract integer and decimal parts of the magnitude
    int_part_of_res = (int)result;
    dec_part_of_res = (int)((result - (int)result) * 100);

    // Display the results
    printf("Integer part of result = %d\n", int_part_of_res);
    printf("Decimal part of result = .%d\n", dec_part_of_res);
    printf("Final Magnitude: %d.%d\n", int_part_of_res, dec_part_of_res);

    return 0;
}
