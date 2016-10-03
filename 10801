#include <stdio.h>

int A[10];
int B[10];

int winA, winB = 0;

int main() {

	int i;

	for (i = 0; i < 10; i++) {
		scanf("%d",&A[i]);
	}
	for (i = 0; i < 10; i++) {
		scanf("%d", &B[i]);
	}
	
	for (i = 0; i < 10; i++) {
		if (A[i] > B[i]) {
			winA++;
		}
		else if(A[i] < B[i]) {
			winB++;
		}
	}

	if (winA > winB)printf("A");
	else if (winA < winB)printf("B");
	else printf("D");
}
