#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void){
    int n;
    cin >> n;
    vector<ll> l(n);
    for (int i=0; i<n; i++) cin >> l[i];
    int cnt = 0;
    for (int i=0; i<n-2; i++){
        for (int j=i+1; j<n-1; j++){
            for (int k=j+1; k<n; k++){
                if (l[i]!=l[j] && l[j]!=l[k] && l[i]!=l[k] && l[i]+l[j]>l[k] && l[j]+l[k]>l[i] && l[k]+l[i]>l[j]){
                    cnt++;
                }
            }
        }
    }
    cout << cnt << endl;
    return 0;
}
