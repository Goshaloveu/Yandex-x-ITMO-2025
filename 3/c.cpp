#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m, some_v;
    vector<int> x, y;

    cin >> n;

    int n_sum = 0, m_sum = 0;
    for (int i = 0; i < n; i++) {
        cin >> some_v;
        x.push_back(some_v);
        n_sum += some_v;
    }

    cin >> m;

    for (int i = 0; i < m; i++) {
        cin >> some_v;
        y.push_back(some_v);
        m_sum += some_v;
    }

    int i = 0, j = 0;
    for (; n_sum > 0 && m_sum > 0;) {
        if (n_sum > m_sum) {
            n_sum -= x[i];
            cout << 1 << " ";
            i++;
        } else if (m_sum > n_sum) {
            m_sum -= y[j];
            cout << 2 << " ";
            j++;
        } else {
            n_sum -= x[i];
            cout << 1 << " ";
            i++;
        }
    }

    for (; n_sum > 0; i++) {
        n_sum -= x[i];
        cout << 1 << " ";
    }

    for (; m_sum > 0; j++) {
        m_sum -= y[j];
        cout << 2 << " ";
    }

    return 0;
}
