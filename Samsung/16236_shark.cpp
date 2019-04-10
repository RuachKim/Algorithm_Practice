#include < iostream >
#include < vector >
#include < queue >
#include < cstring >
#include < algorithm >
 
using namespace std;
 
// 상어 구조체
struct fish {
    int r;
    int c;
    int size;
    int eat; // 몇 마리를 먹었는지
    int time; // 이동한 시간
};
 
int N;
int dr[4] = {-1,0,1,0};  // 북,동,남,서
int dc[4] = {0,1,0,-1};
int map[21][21];
int visited[21][21];
 
queue< fish > q;  // 방문 가능한 위치 - 사이즈가 같거나 0인 곳
vector< fish > v; // 먹을 수 있는 물고기 - 사이즈가 작은 곳
 
// 문제 조건에 맞는 비교연산
bool cmp(fish a, fish b) {
    // 가장 짧은 시간
    if (a.time <= b.time) {
         // 시간이 같을 경우
        if (a.time == b.time) {
            // y값이 더 작은 순서 ( 위(북쪽)에 잇는 물고기 우선)
            if (a.r <= b.r) {
                // y값잉 같다면
                if (a.r == b.r) {
                    // x값이 작은 순서로 정렬
                    if (a.c < b.c) {
                        return true;
                    }
                    return false;
                }
                return true;
            }
            return false;
        }
        return true;
    }
    return false;
}
 
void showmap() {
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            cout << map[r][c] << " ";
        }
        cout << endl;
    }
}
 
int main() {
 
    cin >> N;
     
    fish ex; // 이전 상어의 상태 저장
 
    // 입력
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            cin >> map[r][c];
            if (map[r][c] == 9) {  // 아기상어 -시작위치
                map[r][c] = 0;
                // 초기화
                ex = { r,c,2,0,0 };
            }
        }
    }
    cout << "시작::::아기 상어 위치 : (" << ex.r << "," << ex.c << ") , 사이즈 : " << ex.size << ", 이동 시간 : 0" << endl;
    cout << "-----------------------------------------------" << endl;
    int ans = 0; // 시간정보
    while (1) {
        // 물고기를 한번 먹을때마다 다시 초기화
        v.clear(); // 먹을 수 있는 물고기 update, 우선 순위가 다를 수도 있고,,,, 그러므로 지우기
        memset(visited, 0, sizeof(visited));  // 방문했던 곳도 다시 시작하기!
                                              // 잡아먹은 물고기는 map[][]=0으로 바꿔줬으니 신경쓰지 않아도 된다.
        visited[ex.r][ex.c] = 1;
        q.push(ex);
         
        while (!q.empty()) {  // map의 방문가능 한 모두 방문하기!!
                              // 크기가 작거나, 0인 곳 (길 혹은 이미 먹은 곳)
            int r = q.front().r;
            int c = q.front().c;
            int size = q.front().size;
            int eat = q.front().eat;
            int time = q.front().time;
            q.pop();
 
            // 북동남서 검사
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                if (nr >= 0 && nr < N && nc >= 0 && nc < N) {  // boundary check
                    if (!visited[nr][nc]) {
                        // 사이즈가 같은 상어이거나 길(0)인 경우
                        if (map[nr][nc]==0 || map[nr][nc]== size) {
                             
                            visited[nr][nc] = 1; // 방문 표시
                            q.push({nr, nc, size, eat, time+1}); // 시간만 +1 증가시킴
                                                                  // front에서 한 칸 이동한거니까
                        }
                        // 작은 상어 - 먹을 수 잇음
                        else if ( map[nr][nc] < size) {
                             
                            visited[nr][nc] = 1; // 방문 표시
                            v.push_back({nr,nc,size,eat+1,time+1});  // 잡아 먹은 물고기의 수 +1 증가
                                                                     // 시간 +1 증가
                        }
                    }
                }
            }
        }
 
        // 만약 벡터가 비어있다면 잡아 먹을 수 있는 상어가 없음
        // (map의 모든 곳을 다 확인했으니까!)
        if (v.size()==0) {
            break;
        }
 
        // vetor v = 먹을 수 있는 물고기들의 리스트
        // 이걸 문제의 조건(cmp)에 따라 정렬한다.
        sort(v.begin(), v.end(), cmp);
 
        // 먹은 상어의 숫자가 현재 사이즈와 같다면 사이즈 증가
        if (v[0].size == v[0].eat) {
            v[0].size++;
            v[0].eat = 0;
        }
 
        // 잡아먹은 상어는 map에서 지움
        map[v[0].r][v[0].c] = 0;
        // 이동 시간 저장
        ans += v[0].time;
        // 시간을 초기화하고 다시 큐에 넣어 이전 과정을 반복
        ex = { v[0].r, v[0].c, v[0].size, v[0].eat, 0 };
         
         
        showmap();
        cout << "아기 상어 위치 : (" << ex.r << "," << ex.c << ") , 사이즈 : " << ex.size << ", 이동 시간 : " << ans << endl;
    }
 
    //cout << ans;
 
    return 0;
}


