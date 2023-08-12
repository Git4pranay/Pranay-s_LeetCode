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
    int Addition(int val1, int val2,int carry){
            int s = (val1+val2)+carry;
            return s;
        }
   
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head1 = l1;
        ListNode* head2 = l2;
        ListNode* prev;
        int carry=0;
        int s;
        while(l2!=NULL && l1!=NULL){
            s = Addition(l1->val,l2->val,carry);
            carry = (s)/10;
            s = s%10;
            prev = l1;
            l1->val = s;
            l1 = l1->next;
            l2 = l2->next;
        }
        
        if (l1==NULL && l2==NULL){
            if (carry){
                l1=prev;
                l1->next = new ListNode(carry);
            }
        }
        else if (l1!=NULL){
            while(l1!=NULL){
                s = Addition(l1->val,0,carry);
                carry = (s)/10;
                s = s%10;
                prev = l1;
                l1->val = s;
                l1 = l1->next;
            }
            if (carry){
                l1=prev;
                l1->next = new ListNode(carry);
            }
        }
        else if (l2!=NULL){
            l1 = prev;
            while(l2!=NULL){
                s = Addition(0,l2->val,carry);
                carry = (s)/10;
                s = s%10;
                l1->next = new ListNode(s);
                l1 = l1->next;
                l2 = l2->next;
            }
            if (carry){
                l1->next = new ListNode(carry);
            }
        }
        return head1;
    }
};