/*Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.*/

#include<iostream>


struct ListNode {
    int val;
    ListNode * next;
    ListNode(): val(0), next(nullptr) {}
    ListNode(int x): val(x), next(nullptr) {}
    ListNode(int x, ListNode * next): val(x), next(next) {}
};

int getDecimalValue(ListNode * head) {

    int ans = head->val;
    while((head = head->next))
        ans = ans*2 + head->val;
    return ans;
}