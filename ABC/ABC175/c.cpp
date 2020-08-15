#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void){
    ll x, k, d;
    cin >> x >> k >> d;
    x = abs(x);
    if (x / d < k){
        if ((k - x / d) % 2 == 0){
            cout << x % d << endl;
        } else {
            cout << abs(x % d - d) << endl;
        }
    } else if (x / d > k){
        cout << x - d * k << endl;
    } else{
        cout << x % d << endl;
    }
    return 0;
}
