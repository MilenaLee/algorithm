#include <stdio.h>

int M, N;
int input[101][101] = { 0, };
int mem[101][101] = {0,};
int point[3][4] = { 0, };

int dirX[4] = {0,0,1,-1 };
int dirY[4] = {1,-1,0,0 };

int res=1e9;


void dfs(int si, int sj, int sd, int go, int total) {
	if (total > res || total > mem[si][sj]) return;

	if (point[2][1] == si && point[2][2] == sj) {
		if (sd != point[2][3]) {
			if (sd*(point[2][3]) == 12 || (sd*(point[2][3]) == 2)) {
				total += 2;
			}
			else { total++; }
		}

		if (go >0 && go<4) {
			total++;
		}

		if (res > total) res = total;
		return;
	}

	mem[si][sj] = total;
	if (go > 0 && go < 4) {
		mem[si][sj]++;
	}

	for (int i = 0; i < 4; i++) {
		if (si + dirX[i]<1 || si + dirX[i] > M || sj + dirY[i]<1 || sj + dirY[i] >N) continue;
		if (input[si + dirX[i]][sj + dirY[i]] == 0) {
			int tempdir = sd;
			int tempgo = go;
			int tempTotal = total;
			//방향확인
			if (tempdir != i + 1) {
				if (tempdir*(i + 1) == 12 || (tempdir*(i + 1) == 2)) {
					tempTotal+=2;
				}
				else { tempTotal++; }

				tempdir = i + 1;
				//방향맞춰줌
				if (tempgo ==1 || tempgo==2) {
					tempTotal++;
				}
				tempgo=1;

			}
			else {//가려는 방향과 로봇이 보고있는 방향이 같으면
				tempgo++;
				if (tempgo==3) {
					tempTotal++;
					tempgo = 0;
				}
			}		  

			input[si + dirX[i]][sj + dirY[i]] = -1;
			dfs(si + dirX[i], sj + dirY[i], tempdir, tempgo, tempTotal);
			input[si + dirX[i]][sj + dirY[i]] = 0;
			//방향 원위치
		}
	}

}

int main() {
	int i, j;

	scanf("%d %d", &M, &N);
	for (i = 1; i <= M; i++) {
		for (j = 1; j <= N; j++) {
			scanf("%d", &input[i][j]);
			mem[i][j] = 1e9;
		}
	}

	for (i = 1; i <= 2;i++) {
		for (j = 1; j <= 3; j++) {
			scanf("%d", &point[i][j]);
		}
	}

	input[point[1][1]][point[1][2]]=-1;

	dfs(point[1][1], point[1][2], point[1][3],0, 0);

	printf("%d",res);


	return 0;
}

//https://www.acmicpc.net/problem/1726
//http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=285&sca=3040

//백준은 맞고 정올은 틀리다
