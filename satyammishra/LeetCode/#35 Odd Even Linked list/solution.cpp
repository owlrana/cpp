/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        queue<int> odd_1;
        queue<int> even_1;
        ListNode *odd, *even;
        odd = head;
        even = head->next;

        while(odd){
            odd_1.push(odd->val);
            odd = odd->next->next;
        }
        while(even){
            even_1.push(even->val);
            even = even->next->next;
        }

        while(!odd_1.empty()){
            head->val = odd_1.pop();
            head = head->next;
        }
        while(!even_1.empty()){
            head->val = even_1.pop();
            head = head->next;
        }
        return head;
        
    }
};