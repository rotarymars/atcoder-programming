#include <iostream>
#include <vector>
using namespace std;
signed main()
{
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);
    int n;
    cin>>n;
    vector<int>a(n);
    for(int&i:a)cin>>i;
    int q;
    cin>>q;
    bool first=true;
    for(;q;q--){
        int t;
        cin>>t;
        if(t==1){
            int k,x;
            cin>>k>>x;
            a[--k]=x;
        }else {
            int k;
            cin>>k;
            cout<<a[--k]<<'\n';
        }
    }
    return 0;
}
