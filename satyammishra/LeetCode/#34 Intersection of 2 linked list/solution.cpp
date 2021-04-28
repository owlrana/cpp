/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int ca = 0, cb = 0;
        ListNode *first , *second ;
        first = headA;
        second = headB;
        
        while(first){
            first = first->next;
            ca++;

        }
        while(second){
            second = second->next;
            cb++;
        }
        int diff;
        diff = abs(ca-cb);
        
        if(ca>cb){
        
            while(diff>0){
                headA = headA->next;
                diff--;
            }
        }
        else{
        
            while(diff>0){
                headB = headB ->next;
                diff--;
            }
        }
        while(headA && headB){
            if(headA == headB)
                return headA;
            headA = headA->next;
            headB = headB->next;
        }
        return headA;
    }
};