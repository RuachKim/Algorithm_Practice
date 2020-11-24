#include <iostream>
#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

int n;
int MAP[100][100];
int visit[100][100];
int cnt = 1;
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};
int block[100] = {0, };

void init(){
    
    for(int i= 0; i < 100; i++)
        block[i] = 1;
    
}
void process(int i, int j){
    
    queue<pair<int,int>> q;
    q.push(pair<int,int>(i,j));
    
    visit[i][j] = cnt;
    while(!q.empty()){
        
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for(int i=0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(nx>=0 && nx < n && ny >=0 && ny < n && MAP[nx][ny] == 1 && !visit[nx][ny]){
                
                q.push(pair<int,int>(nx,ny));
                visit[nx][ny] = cnt;
                block[cnt] += 1;
            }
        }
        
    }
    

}


int main(){
    
    init();
    
    cin>>n;
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            scanf("%1d", &MAP[i][j]);        
        }
    }
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            visit[i][j] = 0;        
        }
    }
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(MAP[i][j] == 1 && !visit[i][j]){
                process(i,j);
                cnt += 1;
            }
        }
    }
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            printf("%1d ", visit[i][j]);        
        }
        cout<<'\n';
    }

    for(int i = 1; i < cnt-1; i ++){
        for(int j = i+1; j < cnt; j++){
            if(block[i] > block[j]){
                int tmp = block[i];
                block[i] = block[j];
                block[j] = tmp;
            }
        }
        //cout<<block[i]<<' ';
    }
    if(cnt == 1) 
        cout<<'0';
    else{
        for(int i = 1; i < cnt; i++){
            cout<<block[i]<<' ';
        }
    }
    
    return 0;
}