#include <bits/stdc++.h>
using namespace std;

int main(void){
    int n, x = 0, ans = 0;
    string s;
    cin >> n >> s;
    for (int i=0; i<n; i++){
        if (s[i] == 'I') x++;
        else x--;
        ans = max(ans, x);
    }
    cout << ans << endl;
    return 0;
}