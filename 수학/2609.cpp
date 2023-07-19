#include <iostream>
using namespace std;

int gcd(int a, int b){
    int r = a%b;
    while(r != 0){
        a = b;
        b = r;
        r = a%b;
    }
    return b;
}

int main(){
    int N, M;
    cin >> N >> M;
    cout << gcd(N, M) << endl;
    cout << (N*M) / gcd(N, M) << endl;
}