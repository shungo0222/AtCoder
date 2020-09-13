#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(void) {
    ll a, b, c, d;
    cin >> a >> b >> c >> d;
    cout << max(b*d, max(b*c, max(a*c, a*d))) << endl;
    return 0;
}