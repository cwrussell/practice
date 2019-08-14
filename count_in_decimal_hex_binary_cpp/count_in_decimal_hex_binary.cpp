#include <iostream>

using namespace std;

int main()
{
    unsigned short int start_point, stop_point;
    cout << "Enter a starting point and stopping point (in decimal) for counting." << endl << "Enter a starting point, between 0 and 65534: ";
    cin >> start_point;
    cout << "Enter a stopping point that is greater than the starting point, between 1 and 65535: ";
    cin >> stop_point;

    if (start_point < 0)
    {
        cout << "Starting point must be 0 or greater." << endl;
        return 1;
    }

    if (start_point >= stop_point)
    {
        cout << "Starting point must be less than the stopping point." << endl;
        return 1;
    }

    for (int i = start_point; i <= stop_point; i++)
    {
        // print decimal
        cout << dec << i << "\t";

        // print hexadecimal
        cout << hex << uppercase << i << "\t";

        // print binary
        cout << bitset<16>(i) << endl;
    }

}