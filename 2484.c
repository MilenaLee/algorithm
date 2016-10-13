//http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1527&sca=50
//https://www.acmicpc.net/problem/2484

#include <stdio.h>

int people = 0;
int input[1000][4] = { 0, };

int dice[7] = { 0, };
int count = 0;
int max = 0;

void clearVal() {
	for (int a = 0; a < 7; a++) {
		dice[a] = 0;
	}
	count = 0;
}

int main() {

	int i = 0,j=0;
	scanf("%d", &people);

	for (i = 0; i < people; i++)
	{
		for (j = 0; j < 4; j++) {
			scanf("%d", &input[i][j]);
		}
	}

	int temp = 0;

	for (i = 0; i < people; i++) {
		clearVal();
		for (j = 0; j < 4; j++) {
			dice[input[i][j]]++;
			if (dice[input[i][j]] == 1) {
				count++;
			}
		}
		switch (count) {
		case 1:
			for (j = 1; j < 7; j++) {
				if (dice[j] != 0) {
					temp = 50000 + (j * 5000);
					max = (max > temp) ? max : temp;
					break;
				}
			}
			break;
		case 2:
			for (j = 1; j < 7; j++) {
				switch (dice[j]) {
				case 3:
					temp = 10000 + (j * 1000);
					max = (max > temp) ? max : temp;
					break;
				case 2:
					temp = 2000 + (j * 500);
					for (int z = j+1; z < 7; z++) {
						if (dice[z] == 2) {
							temp += z * 500;
						}
					}
					max = (max > temp) ? max : temp;
					break;

					break;

				}
			}
			break;
		case 3:
			for (j = 1; j < 7; j++) {
				if (dice[j] == 2) {
					temp = 1000 + (j * 100);
					max = (max > temp) ? max : temp;
					break;
				}
			}
			break;
		case 4:
			for (j = 6; j > 0; j--) {
				if (dice[j] == 1) {
					temp = (j * 100);
					max = (max > temp) ? max : temp;
					break;
				}
			}
			break;
		}

	}


	printf("%d", max);

	return 0;
}
/*
#include <stdio.h>
 
int max (int a, int b) { return a > b ? a : b; }
 
int main (void)
{
    int N, a[7], x, i, m = 0;
 
    scanf ("%d", &N);
 
    while (N--)
    {
        for (i = 1; i < 7; i++) a[i] = 0;
 
        for (i = 0; i < 4; i++)
        {
            scanf ("%d", &x);
            a[x]++;
        }
 
        x = 0;
 
        for (i = 6; i > 0; i--)
        {
            switch (a[i])
            {
                case 4: m = max (m, i*5000 + 50000); break;
                case 3: m = max (m, i*1000 + 10000); break;
                case 2:
                    if (x > 0)
                        m = max (m, i*500 + x*500 + 2000);
                    else
                        m = max (m, i*100 + 1000);
                    x = i;
                    break;
                case 1: m = max (m, i*100); break;
            }
        }
    }
 
    printf ("%d\n", m);
}

https://www.acmicpc.net/source/2707485
*/
