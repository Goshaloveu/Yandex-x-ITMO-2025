#include <algorithm>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <time.h>

using namespace std;

struct Node {
    int value, pr, size = 1;
    Node *l = 0, *r = 0;

    Node(int x) {
        value = x, pr = rand();
    }
};

Node *root = 0;

int sz(Node *p) {
    return p ? p->size : 0;
}

void update_size(Node *p) {
    if (p) {
        p->size = 1 + sz(p->l) + sz(p->r);
    }
}

Node *merge(Node *l, Node *r) {
    if (!l)
        return r;
    if (!r)
        return l;
    if (l->pr > r->pr) {
        l->r = merge(l->r, r);
        update_size(l);
        return l;
    } else {
        r->l = merge(l, r->l);
        update_size(r);
        return r;
    }
}

pair<Node *, Node *> split(Node *p, int x) {
    if (!p)
        return {0, 0};
    if (p->value <= x) {
        auto res = split(p->r, x);
        p->r = res.first;
        update_size(p);
        return {p, res.second};
    } else {
        auto res = split(p->l, x);
        p->l = res.second;
        update_size(p);
        return {res.first, p};
    }
}

void insert(int x) {
    auto res = split(root, x);
    Node *t = new Node(x);
    root = merge(res.first, merge(t, res.second));
}

int find_k(Node *p, int k) {
    if (!p) {
        return -1;
    }

    int left_size = sz(p->l);

    if (k == left_size) {
        return p->value;
    }
    if (k < left_size) {
        return find_k(p->l, k);
    } else {
        return find_k(p->r, k - left_size - 1);
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
    srand(time(0));

    for (int i = 1; i <= k; i++) {
        cin >> some_v;
        insert(some_v);

        if (i % 2 == 1) {
            cout << find_k(root, i / 2) << "\n";
        } else {
            cout << (find_k(root, i / 2) + find_k(root, i / 2 - 1)) / 2 << "\n";
        }
    }
    return 0;
}
