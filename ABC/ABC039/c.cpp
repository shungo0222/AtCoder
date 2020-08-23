#include <bits/stdc++.h>
using namespace std;

int main(void) {
    string str;
    cin >> str;
    int w;
    for (int i=0; i<=18; i++) {
        if (str[i] == 'W' && str[i+1] == 'W') {
            w = i;
            break;
        }
    }
    if (w == 4 && str[11] == 'W') cout << "Do" << endl;
    else if (w == 2 && str[8] == 'W') cout << "La" << endl;
    else if (w == 0 && str[6] == 'W') cout << "Si" << endl;
    else if (w == 6) cout << "Fa" << endl;
    else if (w == 4) cout << "So" << endl;
    else if (w == 2) cout << "Re" << endl;
    else if (w == 0) cout << "Mi" << endl;
    return 0;
}
