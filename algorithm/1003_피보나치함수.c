#include <stdio.h>

int arr[41][2];
int fibonacci(int n) {

    arr[0][0] = 1;
    arr[0][1] = 0;
    arr[1][0] = 0;
    arr[1][1] = 1;
    for (int i = 2; i <= n; i++)
    {
        arr[i][0] = arr[i - 1][0] + arr[i - 2][0];
        arr[i][1] = arr[i - 1][1] + arr[i - 2][1];
    }
    return 0;
}

int main()
{
    const int T;
    int n;
    scanf("%d", &T);
    fibonacci(40);
    for (int i = 0; i < T; i++)
    {
        scanf("%d", &n);
        printf("%d %d\n", arr[n][0], arr[n][1]);
    }

    return 0;
}
