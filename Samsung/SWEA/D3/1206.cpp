#include <iostream>

using namespace std;
int floor[1001];

int max_struct(int i){
	int max_floor = floor[i-2];
	if(max_floor < floor[i-1])
		max_floor = floor[i-1];
	if(max_floor < floor[i+1])
		max_floor = floor[i+1];
	if(max_floor < floor[i+2])
		max_floor = floor[i+2];

	return max_floor;
}


int main(int argc, char const *argv[])
{
	
	int num;
	for(int tc = 1; tc <= 10; tc++){

		cin >> num;
		for(int i = 0; i < num; i++)
			cin >> floor[i];

		int st, result = 0;
		for(int i = 2; i < num -2; i++){
			st = max_struct(i);
			if( st < floor[i])
				result += floor[i] - st;

		}

		cout << '#' << tc <<' '<< result << endl;
	}





	return 0;
}