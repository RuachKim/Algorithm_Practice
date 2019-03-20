#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

#define INF 2123456789

int map[52][52];
int visit[52][52];
int n;
int block; // the number of crashed room
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};


int main() {
	// your code goes here
	
	fill_n(&map[0][0],50*50,-1);
	
	cin >> n;
	for( int i = 0; i < n; i++ ){
	    for( int j = 0; j < n; j++ ){
	        
	        cin >> map[i][j];
	        
	        
	    }
	}
	
    
    fill_n(&visit[0][0],50*50,INF);

	
	queue<pair<int,pair<int,int> > >q;
	q.push({0,{0,0}});
	
	while(!q.empty()){
	    
	    int x = q.front().second.first;
	    int y = q.front().second.second;
	    int block = q.front().first;
	    
	    q.pop();
	    
	    for( int k = 0; k < 4; k++ ){
	        
	        int nx = x + dx[k];
	        int ny = y + dy[k];
	        
	        if( nx < 0 && nx >= n && ny < 0 && ny >= n) continue;
	        
	        //if(map[nx][ny] == -1)continue;
	        
	        if( map[nx][ny] == 1 && visit[nx][ny] > block ){
	            visit[nx][ny] = block;
	            q.push({block,{nx,ny}});
	        }
	        
	        if( map[nx][ny] == 0 && visit[nx][ny] > block+1 ){
	            visit[nx][ny] = block+1;
	            q.push({block+1,{nx,ny}});
	        }
	        
	    }
	    
	   
	}
	
	cout<<visit[n-1][n-1]<<endl;
	
	
	
	
	
	return 0;
}
