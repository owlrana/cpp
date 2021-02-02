/*Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].*/

#include<iostream>

using namespace std;

int search(int a[], int n, int target) {
    int first = -1, last = -1;

    for (int i = 0; i < n; i++) {
        if (a[i] != target)
            continue;
        if (first == -1)
            first = i;
        last = i;

    }
    cout << first << " " << last;
    return 0;

}
int main() {
    int n;
    cin >> n;
    int a[n];

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int target;
    cin >> target;
    search(a, n, target);
    return 0;
}