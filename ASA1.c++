#include <iostream>
#include <fstream>

int get_value_of_operation(int line, int collumn, int** table) {
    return table[line][collumn];
}

bool func_princ(int* sequence, int result, int lenght_op, int** matrix, int mat_size) { //change return to something
    int second_opp; 
    int cond;
    
    if (lenght_op == 2) {
        if (matrix[sequence[1]-1][sequence[0]-1] == result) return true;
        else return false;
    }

    for (int i = lenght_op - 1; i >= 0; i--) { 
        // this for is to try the place of this parentheses ex.: (A B C D ) E -> (A B C ) D E -> ...
        if (i == lenght_op - 1) second_opp = sequence[lenght_op-1]; 
        else second_opp = matrix[second_opp - 1][sequence[i]-1]; 
        // ^ opperations to decide witch value 'x' is the second opperator ex.: (A B C D ) 'X' -> (A B C ) 'X' -> ... 

        for (int j = 0; j < mat_size; j++) {
            if (matrix[second_opp-1][j] == result) {
                if ( ) // do recursion 
                    return true;
            }
        
        }
    }
}

int main() {
    ifstream inputFile("input.txt"); // Abrir o ficheiro

    int n,
        m,
        result;
    
    ifstream >> n >> m;
    
    int* sequence  = new int[m];
    int** table = new int*[n];

    for (int i = 0; i < n, i++) {
        table[i] = new int[n];
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

