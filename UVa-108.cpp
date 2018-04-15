//
// Created by hessam on 4/15/18.
// https://github.com/hessam211/UVa-Solutions
//
#include <bits/stdc++.h>
#include <limits.h>
using namespace std;

#define MAX(X, Y) (X > Y) ? X : Y
#define POS(X) (X > 0) ? X : 0

int N[101][101];
int M[101];

int kadane(int r)
{
    int x, sum, maxSum = INT_MIN;
    bool flag = false;
    int min = M[0];
    for (sum = POS(M[0]), x = 0; x < r; ++x, sum = POS(sum + M[x]))
        maxSum = MAX(sum, maxSum);

    if (maxSum <= 0)
    {

        for (int i = 0; i < r ; i++)
        {
            if (M[i] > 0)
            {
                flag = true;
            }
            min = MAX(min , M[i]);
        }

    } else
    {
        return maxSum;
    }
    if (flag != true)
    {
        return min;
    }



}


int main() {
    int p, maxSum = INT_MIN;
    cin >> p;
    for (int l = 0; l < p; l++) {
        for (int r = 0;  r < p; r++)
            cin >> N[l][r];
    }
    for (int l = 0; l < p; l++) {
        memset(M, 0, sizeof(M));
        for (int r = l; r < p ; r++)
        {
            for(int k = 0; k<p ; k++)
                M[k] += N[k][r];
            maxSum = MAX(maxSum, kadane(p));
        }
    }
    cout << maxSum;
}



