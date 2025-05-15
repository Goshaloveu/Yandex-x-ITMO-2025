#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

priority_queue<int, vector<int>, greater<int>> upp;
priority_queue<int> low;

void balance() {
    if (low.size() > (upp.size() + 1)) {
        upp.push(low.top());
        low.pop();
    } else if (upp.size() > low.size()) {
        low.push(upp.top());
        upp.pop();
    }
}

void push(int x) {
    if (low.empty() || x <= low.top()) {
        low.push(x);
    } else {
        upp.push(x);
    }
    balance();
}

int find() {
    if (low.size() == upp.size()) {
        return (low.top() + upp.top()) / 2;
    } else {
        return low.top();
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // freopen("input.txt", "r", stdin);
    // freopen("out.txt", "w", stdout);

    int k, some_v;
    cin >> k;

    for (int i = 0; i < k; ++i) {
        cin >> some_v;

        push(some_v);
        cout << find() << "\n";
    }
    return 0;
}
