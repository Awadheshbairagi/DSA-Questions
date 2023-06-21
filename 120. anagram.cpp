#include <iostream>
#include<bits/stdc++.h>
using namespace std;

    void sortString(string &str)
    {
        sort(str.begin(), str.end());
        
    }
   

int main()
{
    string str1;
    string str2;
    cout<<"enter first string: ";
    cin>>str1;
    cout<<"enter second string: ";
    cin>>str2;
    sortString(str1);
    sortString(str2);
    
    if(str1.length()!=str2.length()){
        cout<<"Not the anagram";
    }
    else{
        if(str1==str2){
            cout<<"Anagram";
        }
        else{
            cout<<"Not the anagram";
        }
    }
    

    return 0;
}
