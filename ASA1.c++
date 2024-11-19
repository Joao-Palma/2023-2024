#include <iostream>
#include <fstream>

int get_value_of_operation(int line, int collumn) {
    return 1;
}

int main() {
    ifstream inputFile("input.txt"); // Abrir o ficheiro

    int n, m, result;
    
    ifstream >> n >> m;
    
    int* sequence  = new int[m];
    int** table = new int*[n]

    for (int i = 0; i < n, i++) {
        table[i] = new int[n]
    }

     // Fill the table with values from the file
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            inputFile >> table[i][j];
        }
    }

    for (int i = 0; 1 < n; i++) {
        inputFile >> sequence[i];
        }

    inputFile >> result

    // Print the table to verify
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            std::cout << table[i][j] << " ";
        }
        std::cout << std::endl;
    }

    // Deallocate memory
    delete[] sequence;
    for (int i = 0; i < n; i++) {
        delete[] table[i];
    }
    delete[] table;

    std::cout << "1 ou 0" << std::endl;
    std::cout << "expressão" << std::endl;
    return 0;
}