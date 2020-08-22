#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n, x, t, ans;
    cin >> n >> x >> t;
    ans = n / x * t;
    if (n % x > 0) ans += t;
    cout << ans << endl;
    return 0;
}
