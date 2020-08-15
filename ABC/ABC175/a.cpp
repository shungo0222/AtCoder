#include <bits/stdc++.h>
using namespace std;

int main(void){
    string str;
    cin >> str;
    int r = 0;
    for (int i=0; i<3; i++){
        if (str[i] == 'R') r++;
    }
    if (r == 2) cout << (str[1]=='R' ? 2 : 1) << endl;
    else cout << r << endl;
    return 0;
}
