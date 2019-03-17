#include <iostream>
#include <string.h>
#include <vector>

using namespace std;

int arr[102][102];
//int cpy_arr[22][22];

int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};
int m,n;
bool visited[102][102];

vector<pair<int,int>>v;

int check(){ // Count block which has cheese.
    
    int cnt = 0;
	for(int i = 0; i < m; i++ ){
	    for( int j = 0; j < n; j++ ){
	        
	        if( arr[i][j] == 1) cnt++;

	    }
	}
	return cnt;
}


void drawair(int x, int y){
    
    
    arr[x][y] = 2;
    visited[x][y] = true;
    for( int k = 0; k < 4; k++ ){
        
        int nx = x + dx[k];
        int ny = y + dy[k];
        
        if( nx >= 0 && nx < m && ny >= 0 && ny < n && arr[nx][ny] != 1 && !visited[nx][ny] ){
            
            drawair(nx,ny);

        }
 
    }

}

void initVisited(){
    
    for(int i = 0; i < m; i++ ){
	    for( int j = 0; j < n; j++ ){
	       
	       visited[i][j] = false; 
 
	    }
    }
}

void contactAir(int x, int y){
    
    int cnt = 0;
    for( int k = 0; k < 4; k++ ){
        
        int nx = x + dx[k];
        int ny = y + dy[k];
        
        if( arr[nx][ny] == 2 ){
            
            cnt++;

        }

    }
    
    if( cnt > 1) v.push_back({x,y});
    
}

int main() {
	// your code goes here
	
	cin >> m >> n;
	
	for(int i = 0; i < m; i++ ){
	    for( int j = 0; j < n; j++ )
	        cin >> arr[i][j];
	}
	
	int T = 0;
	int cnt = 0;
	//printf("%d\n",check());
	while((cnt=check()) != 0) // till cheese no remains on the map
	{
	   
	   T++;
	   // Draw air on the map to tell which block is air or not.
	   // Air fill out function
	   drawair(0,0);
	   //Init visited array
	   initVisited();
	   
       for(int i = 0; i < m; i++ ){
	    for( int j = 0; j < n; j++ ){
	        
	        contactAir(i,j);
  
	    }
       }
       
       for( int i = 0; i < v.size(); i++ ){
           arr[v[i].first][v[i].second] = 2;
       }
       
       v.clear();
	    
	}
	
	cout << T << endl;
	
	return 0;
}
