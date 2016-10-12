#include <stdio.h>
#define MAXINC 21
#define MAXMONEY 301

int money=0, inc = 0;

int invest[MAXMONEY][MAXINC] = { 0, };
int res[MAXMONEY][MAXINC] = { 0, };

int incInvest[MAXMONEY][MAXINC] = { 0, };

void print_result(int m, int c) {
	if (c == 1)
		printf("%d ", m);
	else {
		print_result(m - incInvest[m][c], c - 1);
		printf("%d ", incInvest[m][c]);
	}
}

int main() {

	int i = 0, j = 0, z = 0;

	scanf("%d %d", &money, &inc);
	for (i = 1; i <= money; i++) {
		for (j = 0; j <= inc; j++) {
			scanf("%d", &invest[i][j]);
		}
		invest[i][0] = 0;
	}


	for (i = 1; i <= inc; i++) {//회사개수 i
		for (j = 1; j <= money; j++) {//돈 j
				for (z = 0; z <= j; z++) {//각각의 투자마다 모든 경우 계산
					if(res[j][i] < res[z][i - 1] + invest[j - z][i]){

					res[j][i] =res[z][i - 1] + invest[j - z][i];
					incInvest[j][i] = j - z;//i번째 기업에 투자한 돈 저장
				}
			}
		}
	}

	printf("%d\n", res[money][inc]);

	print_result(money, inc);
	return 0;
}
