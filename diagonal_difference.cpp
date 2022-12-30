//Question - https://www.hackerrank.com/challenges/diagonal-difference/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
      
    int squareMatrix[100][100];
    int i;
    cin>>i;
    for(int m=0;m<i;m++){
        for(int y=0;y<i;y++){
            cin>>squareMatrix[m][y];
        }
    }
   int diag1,diag2;
diag1=0;diag2=0;
    for(int m=0;m<i;m++)
        {
        diag1=diag1+squareMatrix[m][m];
    }
    for(int m=i-1;m>-1;m--)
        {
       
        diag2=(diag2+squareMatrix[i-m-1][m]);   
    }
    int diff = diag1-diag2;
    if(diff<0){
        cout<<-(diff);
    }
    else
        cout<<diff;
    
    return 0;
}
