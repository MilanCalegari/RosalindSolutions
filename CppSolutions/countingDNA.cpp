#include <iostream>
#include <string>

using namespace std;

int main() {
	string inp;
	cin >> inp;

	int size = inp.size();
	int A = 0;
	int T = 0;
	int C = 0;
	int G = 0;

	for (int i = 0; i < size; ++i){

		if (inp[i] == 'A'){
			++A;
		}
		if (inp[i] == 'T'){
			++T;
		}
		if (inp[i] == 'C'){
			++C;
		}
		if (inp[i] == 'G'){
			++G;
		}
	}
	cout << A << " " << C << " " << G << " " << T << endl; 
	return 0;
}
