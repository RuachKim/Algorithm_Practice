 #include <iostream>
 #include <vector>
 #include <queue>
 #include <algorithm>
 #include <string>
 
 using namespace std;
 
 int l,c;
 char inp;
 vector<char>a;
 vector<char>ans;
 
 bool visit[15];
 
 void PRINT(){
     
     for( int i = 0; i < l; i++ )
        printf("%c", ans[i]);
    
    printf("\n");
 
 }
 
 void dfs( int index, string str, int ja, int mo ){
     
    if( str.size() == l ){ 
        
        if( ja < 2 || mo < 1) return;
        
        cout << str << endl;
        
    }
    for( int i = index; i < c; i++ ){
        
        if( a[i] == 'a' || a[i] == 'e' || a[i] == 'i' || a[i] == 'o' || a[i] == 'u' )
            dfs(i+1, str+a[i], ja, mo+1);
        else
            dfs(i+1, str+a[i], ja+1, mo);
        
        
    }
     
     
 }
 
 int main(){
    
    // l: the number of alphabet to consist of password
    cin >> l >> c;
    
    // store input data
    for( int i = 0; i < c; i++ ){
        cin >> inp;
        a.push_back(inp);
    }
    
    sort(a.begin(), a.end());
    
    
    dfs(0, "", 0, 0);
    
    
     return 0;
 }