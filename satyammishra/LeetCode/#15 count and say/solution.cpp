/*The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which 
is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups 
so that each group is a contiguous section all of the same character. Then for each group,
say the number of characters, then say the character. To convert the saying into a digit 
string, replace the counts with a number and concatenate every saying.

Given a positive integer n, return the nth term of the count-and-say sequence.*/



class Solution {
public:
    string countAndSay(int n) {
       string s="1";//initialising
        if(n==1)//directly return 
            return s;
        s+='1';//storing result for n=2 
        if(n==2)
            return s;
        n-=2;
        while(n--)//looping for n>2,(n-2 times looping)
        {   int i=0;
            string res="";//initialising temperoary result
           while(i<s.size())
           {   
               int c=1;
               while(s[i]==s[i+1])//finding frequency of the present chracter
               {   c++;
                   i++;
               }
               string d=to_string(c);//convertinhg the frequency c into string
               res+=d;//apending frequency first &then the present charcter
               res+=s[i];
               i++;
           }
        s=res;//restoring s for the next loop to work
        }
        return s;
    }
};