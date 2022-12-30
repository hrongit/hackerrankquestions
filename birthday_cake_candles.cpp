//https://www.hackerrank.com/challenges/birthday-cake-candles

#include <iostream>

using namespace std;

int main() {
    
    int n, maks = 0, kolko, m;
    
    cin >> n;
    
    for( int i=0; i<n; i++ ) {
        cin >> m;
        
        if( m > maks ) {
            maks = m; 
            kolko = 1;
        }
        else if( m == maks )
            kolko++;
    }
    
    cout << kolko;
    
    
    return 0;
}