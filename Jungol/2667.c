#include <stdio.h>
#include <stdlib.h>

char map[25][25];
int complex[315] = { 0, };

int mapsize = 0;
int numcplx = 0;

int findcomplex(int x, int y) {
	if (x<0 || x >= mapsize || y<0 || y >= mapsize) return 0;

	if (map[x][y] == '1'){
		map[x][y] = '0';
		complex[numcplx]++;
		findcomplex(x - 1, y);
		findcomplex(x + 1, y);
		findcomplex(x, y - 1);
		findcomplex(x, y + 1);
	}
}

int main()
{
	int i, j, k = 0;

	scanf("%d", &mapsize);
	for (i = 0; i<mapsize; i++) {
		scanf("%s", map[i]);

	}

	for (i = 0; i<mapsize; i++) {
		for (j = 0; j<mapsize; j++) {
			if (map[i][j] == '1') {
				numcplx++;
				findcomplex(i, j);
			}
		}
	}

	int min, temp;
	for (i = 1; i<numcplx; i++) {
		min = i;
		for (j = i + 1; j <= numcplx; j++) {
			if (complex[j]<complex[min])
				min = j;
		}
		temp = complex[i];
		complex[i] = complex[min];
		complex[min] = temp;
	}

	printf("%d", numcplx);
	for (i = 1; i <= numcplx; i++) {
		printf("\n%d", complex[i]);
	}


}
