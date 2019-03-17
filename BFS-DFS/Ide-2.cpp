#include <iostream>
#include <string.h>

using namespace std;

char arr[22][22];
//int cpy_arr[22][22];
int cnt,ans;
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};
int m,n;
bool visited[22];

void search( int x, int y, int cnt){
    
    ans = max(ans, cnt);
    
    for( int k = 0; k < 4; k++ ){
        
        int nx = x + dx[k];
        int ny = y + dy[k];
        
        if( nx >= 0 && nx < m && ny >= 0 && ny < n ){
            
            if( visited[arr[nx][ny]-'A'] == false){
                
                visited[arr[nx][ny]-'A'] = true;
                search(nx,ny,cnt+1);
                visited[arr[nx][ny]-'A'] = false;
                
            }
    
        }
        
       
    }
    
  
}

int main() {
	// your code goes here
	
	cin >> m >> n;
	
	for(int i = 0; i < m; i++ ){
	    for( int j = 0; j < n; j++ )
	        cin >> arr[i][j];
	}
	
	visited[arr[0][0]-'A'] = true;
	search(0,0,1);
	
	printf("%d",ans);
	
	return 0;
}
