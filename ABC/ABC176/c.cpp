#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(void) {
    int n;
    cin >> n;
    vector<ll> a(n);
    for (int i=0; i<n; i++) cin >> a[i];
    
    ll ans = 0;
    for (int i=1; i<a.size(); i++) {
        if (a[i] < a[i-1]) {
            ans += a[i-1] - a[i];
            a[i] = a[i-1];
        }
    }
    cout << ans << endl;
    return 0;
}
