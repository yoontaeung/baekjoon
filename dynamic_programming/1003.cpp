#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int testcase;
    cin >> testcase;
    int num;
    for(int i=0; i<testcase; i++){
        //solve fibonacci probelm by array
        //# of zero and one is fib(num-1) and fib(num-2) respectively
        cin >> num;
        int array[num];
        array[0] = 1;
        array[1] = 1;
        int zero = 0;    
        int one = 0;
        if(num == 0){
            zero = 1;
            
        }else if(num == 1){
            one = 1;
        }else{
            for(int i=2; i<num; i++){
                array[i] = array[i-1] + array[i-2];
            }
            zero = array[num-2];
            one = array[num-1];
        }
        cout<<zero<<" "<<one<<endl;
        
    }
    
}
