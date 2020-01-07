// Testing different types of looping
// Compare with loops.py
// g++ --std=c++11 -o loops.exe loops.cpp

#include <array>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {

    // for loop over states vector, C-style loop
    vector<string> states = {"California", "Utah", "New Mexico"};
    cout << "for loop - vector - C-style loop" << endl;
    for (size_t i = 0; i < states.size(); i++) {
        cout << "\t" << states[i] << endl;
    }

    // for loop over states vector, c++11 loop
    cout << "for loop - vector - c++11 loop" << endl;
    for (string state : states) {
        cout << "\t" << state << endl;
    }

    // for loop over states C-style array, C-style loop
    // note: no simple member function to get size of array (?), so keep track of yourself
    cout << "for loop - C-style array - C-style loop" << endl;
    string states_carr[] = {"Texas", "Arizona", "Wyoming"};
    for (size_t i = 0; i < 3; i++) {
        cout << "\t" << states_carr[i] << endl;
    }

    // for loop over states C-style array, c++11 loop
    cout << "for loop - C-style array - c++11 loop" << endl;
    for (string state: states_carr) {
        cout << "\t" << state << endl;
    }

    // for loop over c++11 array
    array<string, 3> states_arr = {"New York", "New Jersey", "Florida"};
    cout << "for loop - c++11 array - c++11 loop" << endl;
    for (string state : states_arr) {
        cout << "\t" << state << endl;
    }

    // while loop over c++11 array
    size_t i = 0;
    cout << "while loop - c++11 array" << endl;
    while (i < states_arr.size()) {
        cout << "\t" << states_arr[i] << endl;
        i++;
    }

    // break in for loop
    cout << "for loop - break" << endl;
    for (int j = 0; j < 10; j++) {
        if (j == 5) {
            break;
        }
        cout << "\t" << j << endl;
    }

    // continue in for loop
    cout << "for loop - continue" << endl;
    for (int j = 0; j < 10; j++) {
        if (j == 5) {
            continue;
        }
        cout << "\t" << j << endl;
    }

    // for-else loop
    // have to use the "found" boolean
    cout << "for else loop" << endl;
    bool found_100 = false;
    for (int j = 0; j < 10; j++) {
        if (j == 100) {
            found_100 = true;
        }
    }
    if (!found_100) {
        cout << "Never found 100" << endl;
    }

}