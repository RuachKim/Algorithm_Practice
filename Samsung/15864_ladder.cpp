#include<cstdio>
int N, M, H, ret = 1e5, map[31][11];
// Check if the ladder is designed as it planned.
bool chk(){
    for (int i = 1, pos; i <= N; i++){
        pos = i;
        for (int j = 1; j <= H; j++){
            if (map[j][pos] == 1)    pos++;
            else if (map[j][pos - 1] == 1) pos--;
        }
        if (i != pos) return false;
    }
    return true;
}
// Backtracking with trial and error - Full Search
void func(int cnt, int x, int y){
    if (cnt >= ret) return; // Find minimum
    if (chk()){
        ret = cnt;
        return;
    }
    if (cnt == 3) return;
    for (int i = y; i <= H; i++, x = 1) for (int j = x; j < N; j++) {
        if (map[i][j]) {
            j++;
            continue;
        }
	// else if no road to cross to the other pole.
        map[i][j] = 1;
        func(cnt + 1, j + 2, i);
        map[i][j] = 0;
    }
}
int main(){
    scanf("%d%d%d", &N, &M, &H);
    for (int i = 0, a, b; i < M; i++){
        scanf("%d%d", &a, &b);
        map[a][b] = 1;
    }
    func(0, 1, 1);
    if (ret>3) printf("-1");
    else printf("%d", ret);
    return 0;
}
