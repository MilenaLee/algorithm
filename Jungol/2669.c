//https://www.acmicpc.net/problem/2669
#include <stdio.h>
#define SIZE 4
#define MAX 100

int square[SIZE][4] = { 0, };
int space[MAX][MAX] = { 0, };
int area = 0;

int main() {
	int i = 0, x = 0, y = 0;

	for (i = 0; i < SIZE; i++) {
		scanf("%d %d %d %d",&square[i][0], &square[i][1], &square[i][2], &square[i][3]);
	}

	for (i = 0; i < SIZE; i++) {
		for (x = square[i][0]; x < square[i][2]; x++) {
			for (y = square[i][1]; y < square[i][3]; y++) {
				if (space[x][y] == 0) {
					space[x][y] = 1;
					area++;
				}
			}
		}
	}

	printf("%d", area);

	return 0;
}
