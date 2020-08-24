#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n;
    cin >> n;
    
    int a = 0, t;
    t = n;
    while (t != 0) {
        a += t % 10;
        t /= 10;
    }
    
    cout << (n % a == 0 ? "Yes" : "No") << endl;
    
    return 0;
}
