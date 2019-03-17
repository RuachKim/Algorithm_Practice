 #include <iostream>
 #include <vector>
 #include <queue>
 #include <algorithm>
 #include <string>
 
 using namespace std;
 
 int n,m;
 int cnt;
 
 int dx[4] = {-1,1,0,0};
 int dy[4] = {0,0,-1,1};
 
 bool visit[100][100];
 int map[100][100] = {0,};
 int dist[100][100];
 
 void bfs(){
     
    queue<pair<int,int>>q;
    
    int x = 0;
    int y = 0;
    
    q.push({x,y});
    cnt = 0;
    dist[0][0] = 1;
    
    while(!q.empty()){
        
        x = q.front().first;
        y = q.front().second;
        
        visit[x][y] = true;
        q.pop();
        
        for( int k = 0; k < 4; k++ ){
            
                
            int p_x = x+dx[k];
            int p_y = y+dy[k];
            
            if( p_x >= 0 && p_x < n && p_y >= 0 && p_y < m )
            {
               if( visit[p_x][p_y] == false && map[p_x][p_y] == 1 ){
                   visit[p_x][p_y] = true;
                    q.push({p_x,p_y});
                    dist[p_x][p_y] = dist[x][y] + 1;
      
               }
               
               
            }
            
        }
        
        
    }
    
 }
 
 
 int main(){
    
    cin >> n >> m;
    
    int d;
    
    for( int i = 0; i < n; i++ ){
        for( int j = 0; j < m; j++ ){
            scanf("%1d", &d);
            map[i][j] = d;
        }
    }
  
    
    bfs();
    
    printf("%d\n", dist[n-1][m-1]);
    
    
     return 0;
 }