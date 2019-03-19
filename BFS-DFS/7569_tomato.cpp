#include <iostream>
#include <queue>
using namespace std;

int map[102][102][102];
bool visit[102][102][102];
int m,n,h;
int tomato = 0;
int temp_tom = 0;
int day = 0;
int dx[6] = {0,0,1,0,-1,0};
int dy[6] = {0,0,0,1,0,-1};
int dz[6] = {1,-1,0,0,0,0};

//pair<pair<int,int>,pair<int,int>>

void bfs(){
    
    queue< pair<pair<int,int>,pair<int,int>> >q;
    
    for( int k = 0; k < h; k++ ){
	    
	  for(int i = 0; i < n; i++ ){
	      
    	    for( int j = 0; j < m; j++ ){
    	        
    	        if(map[i][j][k] == 1 ){ 
    	            q.push({{0,i},{j,k}}); //익은 토마토 큐에 삽입.
    	            //visit[i][j][k] = true;
    	        }
    	    }
	    }
	  
    }
    
    
    
    while(!q.empty()){
        
      int tday = q.front().first.first;
      int x = q.front().first.second;
      int y = q.front().second.first;
      int z = q.front().second.second;
      
      
      q.pop();
      
      if(visit[x][y][z]) continue; //
      
      if(map[x][y][z] == 0 ) temp_tom++;
      map[x][y][z] = 1;
      visit[x][y][z] = true;
      
      day = max(tday,day);
      
      for( int k = 0; k < 6; k++ ){
	    
	    int nx = x + dx[k];
	    int ny = y + dy[k];
	    int nz = z + dz[k];
	    
	    
	    if( nx >= 0 && nx < n && ny >= 0 && ny < m && nz >= 0 && nz < h && !visit[nx][ny][nz] 
	    && map[nx][ny][nz] == 0){
	        
	        q.push({{tday+1,nx},{ny,nz}});
	        
	    }
	   
      }
      
      
        
    
    }

}
int main() {
	// your code goes here
	
	cin >> m >> n >> h;
	
	for( int k = 0; k < h; k++ ){
	    
	  for(int i = 0; i < n; i++ ){
	      
    	    for( int j = 0; j < m; j++ ){
    	      
    	        cin >> map[i][j][k];
    	        if(map[i][j][k] == 0 ) tomato++; // 익지않은 토마토 총 개수.
    	    }
	    }
	  
    }
	
	
	bfs();
	
// 	for( int k = 0; k < h; k++ ){
	    
// 	  for(int i = 0; i < n; i++ ){
	      
//     	    for( int j = 0; j < m; j++ ){
    	      
//     	        if(map[i][j][k] == 0 ){
//     	          cout << -1 << endl; 
//     	          return 0;
//     	        } 
//     	    }
// 	    }
	  
//     }
	
	
	
	if( tomato == temp_tom ) cout << day << endl;
	else cout << -1 << endl;
	
	
	return 0;
}
