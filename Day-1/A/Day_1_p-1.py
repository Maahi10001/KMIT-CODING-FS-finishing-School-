/*
Ramesh and Suresh are best friends. They decided to play a word game.
 The game rules are as follows:
 	- The game board shows a word W consist of two characters only A and B.
	- You are allowed to replace a pair of neighbour letters AA with BB in W.
 	- Finally, The one who failed to replace the letters will lose the game.
 Your task is to find all the possible ways of W, after one valid replacement. 
 You have to perform the replacement of the pair from left to right in the word.
 and print the result in the same order of replacement.
   
  
Input Format:
-------------
 A string W, word.

 Output Format:
 --------------
 Print the list of possible replacements of W.
  
Sample Input-1:
---------------
 AAABAA

Sample Output-1:
----------------
[BBABAA, ABBBAA, AAABBB]
  
Sample Input-2:
---------------
AAAAA

Sample Output-2:
----------------
[BBAAA, ABBAA, AABBA, AAABB] 

*/


#include<bits/stdc++.h>

using namespace std;

vector<string> res;
void get_ans(int i,int j,string str,int n){
    
    
    if(i==n) return;
    if(j==n) return;
    string s = "";
    if(str[i] == 'A' && str[j]== 'A'){
        s = str;
        s[i] = 'B';
        s[j] = 'B';
        res.push_back(s);
        get_ans(i+1,j+1,str,n);
    }
    else{
        get_ans(i+1,j+1,str,n);
    }
}

int main(){
    
    string w;
    cin>>w;
    int n = w.length();
    get_ans(0,1,w,n);
    cout<<"[";
    for(int i=0;i<res.size();i++){
        if(i==res.size()-1){
            cout<<res[i];
        }
        else{
        cout<<res[i]<<",";
        }
    }
    cout<<"]";
    
    
    
    
}
