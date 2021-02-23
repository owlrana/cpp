#include<iostream>
using namespace std;

class Solution {
public:
    string defangIPaddr(string address) {
        
        vector<char> v;
        for(auto i : address)
        {
            if(i == '.')
                v.push_back('[');
            v.push_back(i);
            
            if(i == '.')
                v.push_back(']');
        }
        string s = {v.begin(), v.end()};

        return s;
    }
        
};