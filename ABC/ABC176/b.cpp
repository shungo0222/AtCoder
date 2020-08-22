#include <bits/stdc++.h>
using namespace std;

int main(void) {
    string n;
    cin >> n;
    int num = 0;
    for (auto x : n) {
        num += x - '0';
    }
    cout << (num % 9 == 0 ? "Yes" : "No") << endl;
    return 0;
}
