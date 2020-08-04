#include <bits/stdc++.h>
using namespace std;

int main(void){
    long long int n, d, x, y, cnt=0;
    cin >> n >> d;
    for (int i=0; i<n; i++){
        cin >> x >> y;
        if (sqrt(x*x + y*y) <= d) cnt++;
    }
    cout << cnt << endl;
    return 0;
}