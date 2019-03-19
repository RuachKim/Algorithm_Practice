#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int n,m,v;
int a[1001][1001]; // 해당 정점이 존재 하는지 check 배열, 1: exist 0: empty
bool visit[1001];


void dfs(int s){
    
    cout<<s<<"";
    visit[s] = true;
    
    for(int i = 1; i <= n; i++ ){
        
        if( a[s][i] == 1 && !visit[i] ) dfs(i);
    }
    
}

void bfs(int s){
    
    queue<int>q;
    q.push(s);
    visit[s] = true;
    
    while(!q.empty()){
        
       int next = q.front();
       cout << next <<"";
       q.pop();
        
       for(int i = 1; i <= n; i++ ){
            if( a[next][i] == 1 && !visit[i] ){
                
                visit[i] = true;
                q.push(i);
            }
        } 
        
    }
      
}


int main() {
	// your code goes here
	cin >> n >> m >> v;
	int t, u;
	for( int i = 0; i < m; i++ ){
	    
	    cin >> t >> u;
        
        a[t][u] = 1;
        a[u][t] = 1;
        	    
	}
	
	dfs(v);
	cout << endl;
	for(int i = 1; i <= n; i++ ) visit[i] = false;
	bfs(v);
	
	
	
	
	
	return 0;
}
