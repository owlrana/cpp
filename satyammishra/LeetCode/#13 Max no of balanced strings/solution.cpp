#include<iostream>
#include<stack>
#include<string.h>

int balancedStringSplit(string s) {

    stack < char > st;
    int flag = 0, count = 0, balance = 0;
    for (char ch: s) {
        st.push(ch);

        if (ch == 'R') count++;
        else
            flag++;
        if (count == flag) {
            balance++;
            while (st.empty())
                st.pop();
            flag = 0;
            count = 0;
        }
    }
    return balance;
}