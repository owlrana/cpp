#include<iostream>
#include<vector>
using namespace std;
vector<bool> checkOperations(vector<int> a, vector<char> signs, vector<int> b, vector<int> c) {
    
    int n = a.size();
    vector<bool> answer;
    for(int i = 0; i < n ; i++)
    {
            if(signs[i] == '+')
            {
                if(c[i] == a[i] + b[i])
                    answer[i] = true;
                else
                    answer[i] = false;
            }
            else
            {
                if(c[i] == a[i] - b[i])
                    answer[i] = true;
                else
                    answer[i] = false;                
            }
            cout<<answer[i];
    }
    
     return answer;

}
int main()
{
        int a[4] = [3, 2, -1, 4];
        int b[4] = [2, 7, -5, 2];
        int c[4] = [5, 5, 4, 2];
        char signs[4] = {'+', '-', '-', '+'};
        
        checkOperations( a, signs, b, c);,



}