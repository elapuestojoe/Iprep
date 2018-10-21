#include <iostream>
#include <vector>

using namespace std;

void displayVector(std::vector<int> &vector);

int main() {
    std::vector<int> intVector;

    intVector.push_back(4);
    intVector.push_back(4);
    displayVector(intVector);
    return 0;
}

void displayVector(std::vector<int> &intVector) {
    for(std::vector<int>::const_iterator i = intVector.begin(); i < intVector.end(); i++) {
        std::cout << *i << "\t";
    }
    std::cout << std::endl;
}