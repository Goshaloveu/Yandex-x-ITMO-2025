#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int n, A, B, C;

int bfs() {
    queue<int> q;
    q.push(1);

    vector<int> d(n + 1, -1);
    d[1] = 0;

    while (!q.empty()) {
        int v = q.front();
        q.pop();
        int n1 = v * A, n2 = v * B, n3 = v + 1, n4 = v + C;
        if ((n1 <= n) && (d[n1] == -1)) {
            q.push(n1);
            d[n1] = d[v] + 1;
        }
        if ((n2 <= n) && (d[n2] == -1)) {
            q.push(n2);
            d[n2] = d[v] + 1;
        }
        if ((n3 <= n) && (d[n3] == -1)) {
            q.push(n3);
            d[n3] = d[v] + 1;
        }
        if ((n4 <= n) && (d[n4] == -1)) {
            q.push(n4);
            d[n4] = d[v] + 1;
        }
    }

    return d[n];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // freopen("inp.txt", "r", stdin);
    // freopen("out.txt", "w", stdout);

    int k;
    cin >> k;

    for (int i = 0; i < k; i++) {
        cin >> n >> A >> B >> C;
        cout << bfs() << "\n";
    }

    return 0;
}
