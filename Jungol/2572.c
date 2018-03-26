#include <stdio.h>
#define MAX 30000

int N, d, k, c;
int belt[MAX] = { 0, };

int max = 0;

int main() {

	int i = 0,j=0;

	scanf("%d %d %d %d",&N, &d, &k, &c);

	for (i = 0; i < N; i++) {
		scanf("%d", &belt[i]);
	}

	for (i = 0; i < N; i++) {
		int tempi = i;
		int count = 0;
		int coupon = 0;
		int index[MAX] = { 0, };

		for (j = 0; j < k; j++) {
			if (index[belt[tempi%N]] == 0) {
				index[belt[tempi%N]]++;
				count++;
				if (belt[tempi%N] == c) coupon = 1;
			}
			tempi++;
		}

		if (coupon == 0) count++;
		if (count > max) max = count;
		
	
	}
	printf("%d",max);
	return 0;
}
