#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

bool visit[1002][1002];
int map[1002][1002];
int m,n;
int tomato = 0;
int tmp_tom = 0;
int day = 0, tday = 0;

int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};

struct p{
    int d;
    int r;
    int c;
};

int main() {
	// your code goes here
	cin >> m >> n;
	
	for(int i = 0; i < n; i++ ){
	    for( int j = 0; j < m; j++ ){
	        cin >> map[i][j];
	        if(map[i][j] == 0) tomato++;
	    }
	}
	
	queue<p>q;
	
	for(int i = 0; i < n; i++ ){
	    for( int j = 0; j < m; j++ ){
	        
	        if(map[i][j] == 1) q.push({0,i,j});
	    }
	}
	
	while(!q.empty()){
	    
	  int x = q.front().r;
	  int y = q.front().c;
	  tday = q.front().d;
	  q.pop();
	  
	  if(visit[x][y]) continue;
	  
	  visit[x][y] = true;
	  
	  if(map[x][y] == 0) tmp_tom++;
	  map[x][y] = 1;
	  
	  day = max(tday,day);
	  
	  for( int k = 0; k < 4; k++ ){
	      int nx = x+dx[k];
	      int ny = y+dy[k];
	      
	      if( nx >= 0 && nx < n && ny >= 0 && ny < m && !visit[nx][ny] && map[nx][ny] == 0){
	          
	          q.push({tday+1,nx,ny});
	          
	      }
	  }
	    
	    
	}
	
	if( tomato == tmp_tom ) cout << day << endl;
	else cout << -1 << endl;
	
	
	return 0;
}
