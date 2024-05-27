#include <iostream>
using namespace std;
signed main()
{
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);
    int d,n;
    cin>>d>>n;
    if(n==100)n++;
    cout<<n;
    for(int i=0;i<d;i++)cout<<"00";
    cout<<endl;
    return 0;
}
