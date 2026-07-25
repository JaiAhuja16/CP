#include <bits/stdc++.h>
#define int long long int
using namespace std;

int dfs(int u, vector<vector<int>> &adj, vector<int> &subtree){
	int st = 1;
	for (auto v: adj[u]){
		st += dfs(v, adj, subtree);
	}
	subtree[u] = st - 1 ;
	return st;
}

void solve(){
    int n, par;
	cin >> n;
	vector<vector<int>> adj(n + 1);
	vector<int> subord(n + 1);

	for (int child = 2 ; child <= n ; child++){
		cin >> par;
		adj[par].push_back(child);
	}

	dfs(1, adj, subord);

	for (int i = 1 ; i < n + 1 ; i++){
		cout << subord[i] << ' ';
	}
	cout << '\n';
}

int32_t main() {
	solve();
    return 0;
}