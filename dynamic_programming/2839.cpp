#include <iostream>
#include <vector>

using namespace std;

int main(){
	int n;
	int ans = 0;
	cin>>n;
	
	while(n>=0){
		if(n%5 == 0){
			cout<<ans + n/5<<endl;
			return 0;
		}
		else{
			n = n-3;
			ans++;
		}
	}
	cout<<-1<<endl;

}
