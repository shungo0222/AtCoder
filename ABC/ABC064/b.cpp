#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i=0; i<n; i++) cin >> a[i];
    sort(a.begin(), a.end());
    cout << a.back() - a.front() << endl;
    return 0;
}