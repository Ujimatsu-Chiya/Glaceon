# include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N=100004;
bool is_sqrt(ll x){
    ll y=sqrt(x)+1e-7;
    return y*y==x;
}
vector<int>g[N];
ll a[N];
int n;
int f1[N],f2[N];
void dfs(int u,int fa){
    for(int v:g[u]){
        if(v==fa) continue;
        dfs(v,u);
    }
    int sum=0;
    for(int v:g[u]){
        if(v==fa) continue;
        sum+=max(f1[v],f2[v]);
    }
    f2[u]=sum;
    for(int v:g[u]){
        if(v==fa) continue;
        if(is_sqrt(a[u]*a[v])){
            f1[u]=max(f1[u],sum-max(f1[v],f2[v])+f2[v]+1);
        }
    }

}
int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%lld",&a[i]);
    int u,v;
    for(int i=1;i<n;i++){
        scanf("%d %d",&u,&v);
        g[u].push_back(v);
        g[v].push_back(u);
    }
    dfs(1,0);
    printf("%d\n",max(f1[1],f2[1])*2);
}
