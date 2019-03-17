#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int w,h;
int map[52][52];
int visit[52][52];
int dx[8] = {-1,1,0,0,1,-1,1,-1};
int dy[8] = {0,0,-1,1,1,-1,-1,1};
int cnt = 0;

void dfs(int x, int y){
    
    visit[x][y] = 1;
    
    for( int k = 0; k < 8; k++ ){
        
       int nx = x+dx[k];
       int ny = y+dy[k];
       
       if( nx >= 0 && nx < h && ny >= 0 && ny < w ){
           
            if(!visit[nx][ny] && map[nx][ny] == 1) dfs(nx,ny);   
           
        }   
        
        
    }
    
}

int main() {
	// your code goes here
	while(1){
	    
	    cin >> w >> h;
	    
	    if( w == 0 && h == 0)return 0;
	    
	    // renew map
	    for( int i = 0; i < h; i++ ){
	        for( int j = 0; j < w; j++ )
	            cin >> map[i][j];
	    }
	    
	    // visit array clear
	    for( int i = 0; i < h; i++ ){
	        for( int j = 0; j < w; j++ )
	            visit[i][j] = 0;
	    }
	    
	    
	    for( int i = 0; i < h; i++ ){
	        for( int j = 0; j < w; j++ ){
	            
	            if( !visit[i][j] && map[i][j] == 1){ 
	                
	                dfs(i,j);
	                cnt++;
	            }
	            
	        }
	            
	    }
	    
	    cout << cnt << endl;
	    cnt = 0;
   
	    
	}
	
	
	
	return 0;
}
