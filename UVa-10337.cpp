//
// Created by hessam on 4/15/18.
// https://github.com/hessam211/UVa-Solutions
//
#include <bits/stdc++.h>
#include <limits.h>
using namespace std;

#define MAX(X, Y) (X > Y) ? X : Y
#define MIN(X, Y) (X < Y) ? X : Y
#define POS(X) (X > 0) ? X : 0

int m[10][1001];
int fu[10][1001];
int n;

int fuel(int alt, int dis) {
    if (alt > 9 || alt < 0 || dis > n)
        return 1e9;

    if (dis == n) {
        if (alt == 0)
            return 0;
        else
            return 1e9;
    }

    if (fu[alt][dis] != -1)
        return fu[alt][dis];

    return fu[alt][dis] = min(
            60 - m[alt][dis] + fuel(alt + 1, dis + 1),
            min(30 - m[alt][dis] + fuel(alt, dis + 1),
                20 - m[alt][dis] + fuel(alt - 1, dis + 1)));
}

int main()
{
    cin >> n;
    n = n / 100;
    for(int i=9;i>=0;i--)
        for(int j=0;j<n;j++)
        {
            cin >> m[i][j];
        }
    memset(fu, -1, sizeof(fu));
    cout << fuel(0,0);
}