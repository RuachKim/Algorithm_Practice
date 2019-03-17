#include <iostream>
#include <string.h>
#include <vector>
#include <queue>

using namespace std;

char arr[52][52];
//int cpy_arr[22][22];

int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};
int m,n;
bool visited[52][52];
int dist[52][52];


queue<pair<int,int>>q;

void bfs(int x, int y){
    
    dist[x][y] = 0;
    
    q.push({x,y});
    visited[x][y] = true;
    
    while(!q.empty()){
      
      int a = q.front().first;
      int b = q.front().second;
      q.pop();
      
      for( int k = 0; k < 4; k++ ){
          
        int nx = a + dx[k];
        int ny = b + dy[k];
          
        if( nx >= 0 && nx < m && ny >= 0 && ny < n){
         
         if(!visited[nx][ny] && arr[nx][ny] == 'L' ){
             q.push({nx,ny});
             dist[nx][ny] = dist[a][b]+1;
             visited[nx][ny] = true;
         }   
            
        }  
          
      }  
      
    }
 
}

void clear_visit(){
    
    for(int i = 0; i < m; i++ ){
        for( int j = 0; j < n; j++ ){
            visited[i][j] = false;
            
        }
            
    }
    
}

void clear_dist(){
    
    for(int i = 0; i < m; i++ ){
        for( int j = 0; j < n; j++ ){
            dist[i][j] = 0;
            
        }
            
    }
    
}
int main() {
	// your code goes here
	
	cin >> m >> n;
	
	int ans = 0;
	
	for(int i = 0; i < m; i++ ){
	    for( int j = 0; j < n; j++ )
	        cin >> arr[i][j];
	}
	
	queue<pair<int,int>>lq;
	for(int i = 0; i < m; i++ ){
	    for( int j = 0; j < n; j++ ){
	    
	        if(arr[i][j] == 'L') lq.push({i,j});
	    }
	}
	
	while(!lq.empty()){
	    int x = lq.front().first;
	    int y = lq.front().second;
	    lq.pop();
	    bfs(x,y);
	    
        for(int i = 0; i < m; i++ ){
    	    for( int j = 0; j < n; j++ )
    	        ans = max(ans, dist[i][j]);
    	} 
    	
    	clear_visit();
    	clear_dist();

	}
	
   

    cout<<ans<<endl;
	
	return 0;
}
