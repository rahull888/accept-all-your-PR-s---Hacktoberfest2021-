#include<bits/stdc++.h>
using namespace std;

void reversestring(string &s,int st,int e){
    while(st < e){
        swap(s[st],s[e]);
        st++;
        e--;
    }
}

void reversealternatewords(string &s){
    int count = 0;
    int len = s.size();
    int st,e;
    st = e = 0;
    for (int i = 0; i < len; i++)
    {   
        if(s[i] == '.'){
            count++;
            if(count % 2 == 0){
                reversestring(s,st,e);
            }
            st = i+1;
        } else {
            e = i;
        }
    }
    count++;
    if(count % 2 == 0){
        reversestring(s,st,e);
    } 
}

int main() {
	string s;
	cin >> s;
	
	reversealternatewords(s);
	
	cout << s << endl;
	
	return 0;
}
