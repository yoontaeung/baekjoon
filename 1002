#include <iostream>
using namespace std;
int main()
{
    int testcase;
    int x1, y1, r1, x2, y2, r2;
    cin >> testcase;
    int length_sq;
    int a, b, r, result;
    int temp, temp2;
    for (int i = 0; i < testcase; i++)
    {
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        a = x1 - x2;
        a = a * a;
        b = y1 - y2;
        b = b * b;
        r = r1 + r2;
        length_sq = a + b;
        //temp is longer than temp2
        if(r1 == r2){
            if(length_sq == 0){
                result = -1;
            }else{
                if(length_sq > r*r){
                    result = 0;
                }else if(length_sq == r*r){
                    result = 1;
                }else{
                    result = 2;
                }
            }
        }else{
            if(r1 < r2){
                temp = r2;
                temp2 = r1;
            }else{
                temp = r1;
                temp2 = r2;
            }
            if((length_sq > r*r)&&(length_sq>temp*temp)){
                result = 0;
            }
            if((length_sq == r*r)&&(temp*temp<length_sq)){
                result = 1;
            }
            if(length_sq < r*r){
                result = 2;
            }
            if((length_sq == (temp-temp2)*(temp-temp2))&&(length_sq<temp*temp)){
                result = 1;
            }
            if(length_sq < (temp-temp2)*(temp-temp2)){
                result = 0;
            }
            


        }     
        
        cout << result << endl;
    }
}
