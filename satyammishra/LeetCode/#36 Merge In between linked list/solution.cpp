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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode *tail, *first, *second;
        tail = first = list1;
        second  = list2;

        int ta = 0;
        int tb = 0;
        while(tb != b){
            tail = tail->next;
            tb++;
        }
        while(first != NULL && first->next != NULL)
        {
            if(ta == a-1){
                first->next = second;
            }
            first = first->next;     
            ta ++;      
            
        }
        first->next = tail->next;
        while(first && first->next){
                   
            first = first->next;
        }
       
        return first;
        
    }
};
return first;

first = first->next;
first = second->next;

second = second