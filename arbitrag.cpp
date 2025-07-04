#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
using namespace std;

const double INF = 1e100;
const double EPS = 1e-12;

int n, m;
unordered_map<string, int> id;
vector<vector<double>> dist;

void readCurrencies() {
    id.clear();
    string name;
    for (int i = 0; i < n; ++i) {
        cin >> name;
        id[name] = i;
    }
}

void readGraph() {
    dist.clear();
    dist.resize(n, vector<double>(n, INF));
    for (int i = 0; i < n; ++i) dist[i][i] = 0.0;

    string u, v; double rate;
    for (int i = 0; i < m; ++i) {
        cin >> u >> rate >> v;
        int a = id[u], b = id[v];
        dist[a][b] = min(dist[a][b], -log(rate));
    }
}

void floydWarshall() {
    for (int k = 0; k < n; ++k)
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (dist[i][k] + dist[k][j] < dist[i][j] - EPS)
                    dist[i][j] = dist[i][k] + dist[k][j];
}

bool hasArbitrage() {
    for (int i = 0; i < n; ++i)
        if (dist[i][i] < -EPS)
            return true;
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int caseNo = 1;
    while (cin >> n && n) {
        readCurrencies();
        cin >> m;
        readGraph();
        floydWarshall();
        cout << "Case " << caseNo++ << ": " 
             << (hasArbitrage() ? "Yes" : "No") << '\n';
    }
    return 0;
}