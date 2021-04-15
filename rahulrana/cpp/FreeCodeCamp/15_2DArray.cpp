// to see how to create and use a 2Dimensional array
# include <iostream>
# include <conio.h>


using namespace std;

int main()
{
    // create two [] to tell compiler we want 2 dimensional array
    // each element in an array can be visualised as another array
    // in first [] specify how many array elements are inside the outer array
    // in secodn [] specify how many elements each array in outer array has
    int row = 3, col = 2, numberGrid[row][col] = {
                            {1,2},
                            {3,4},
                            {5,6}

                        };

    // outputs 2
    cout << numberGrid[0][1] << endl;
    // outputs 4
    cout << numberGrid[1][1] << endl;

    // Nested for loop to iterate all the elements in the array
    for (int i = 0; i < row; i ++) { // first for loop to go through each arr inside the outer arr (ROWS)
        for (int j = 0; j < col; j ++) { // elements inside each array (COLUMNS)
            cout << numberGrid[i][j] << ", ";
        }
        cout << "\b\b \n";
    }

    return 0;
}