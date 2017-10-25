#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <sstream>
#include <algorithm>
#include <deque>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <list>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <climits>
#include <bitset>
#include <functional>
#include <numeric>
#include <ctime>
#include <cassert>
#include <cstring>
#include <fstream>

using namespace std;
const int INF = 1000000000;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    vector<int> l(n+1 , INF);
    l[0] = -INF;

    for (int i = 1; i <= n; i++) {
        auto pos = lower_bound(l.begin(), l.end(), a[i - 1]);
        cout<<*pos<<endl;
        *pos = a[i-1];

    }
    for (int i = n; i >= 0; i--)
        if (l[i] != INF) {
            cout << i << endl;
            break;
        }
    return 0;
}
