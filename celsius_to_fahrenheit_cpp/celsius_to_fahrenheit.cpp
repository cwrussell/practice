// from C++ for dummies

#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
    // get temperature in C from user
    int celsius;
    cout << "Enter the temperature in Celsius: ";
    cin >> celsius;

    // conversion factor from C -> F
    int factor;
    factor = 212 - 32;

    // convert from C -> F
    int fahrenheit;
    fahrenheit = factor * celsius/100 + 32;

    // output the reusults
    cout << "Fahrenheit value is: ";
    cout << fahrenheit << endl;
}