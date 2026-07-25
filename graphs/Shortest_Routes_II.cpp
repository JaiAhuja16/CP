#include <bits/stdc++.h>
#define int long long int
using namespace std;

int INF = 1e18;

void solve(){
    int n, m, q;
	cin >> n >> m >> q;

	vector<vector<int>> dist(n + 1, vector<int> (n + 1, INF));

	for (int i = 0 ; i < n + 1 ; i++) dist[i][i] = 0;

	int src, dst, cost;
	
	while (m--){
		cin >> src >> dst >> cost;
		dist[src][dst] = min(dist[src][dst], cost);
		dist[dst][src] = min(dist[dst][src], cost);
	}

	for (int imm = 1 ; imm <= n ; imm++){
		for (int src = 1 ; src <= n ; src++){
			for (int dst = 1 ; dst <= n ; dst++){
				dist[src][dst] = min(dist[src][imm] + dist[imm][dst], dist[src][dst]);
			}
		}
	}

	while (q--){
		cin >> src >> dst;
		cout << ((dist[src][dst] < INF) ? dist[src][dst] : -1) << '\n';
	}

}

int32_t main() {
    solve();
    return 0;
}