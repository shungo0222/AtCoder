#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n;
    cin >> n;
    vector<int> p(n);
    for (int i=0; i<n; i++) cin >> p[i];

    int match = 0;
    for (int i=0; i<n; i++) {
        if (i+1 == p[i]) match++;
    }

    int sub = 0;
    for (int i=0; i<n-1; i++) {
        if (i+1 == p[i] and i+2 == p[i+1]) {
            sub++;
            i++;
        }
    }

    cout << match - sub << endl;

    return 0;
}