#include <iostream>

using std::cin;
using std::cout;
using std::endl;

long long RecursionNaive(int n, int k) {
	if (n <= 1)
		return n;
	return (long long) RecursionNaive(n-1, k) + (RecursionNaive(n-2, k));
}

long long FastMeth(long long n, int k) {
	long long f[n + 2];
	f[0] = 0;
	f[1] = 1;
	f[2] = 1;

	for (int i=3; i <=n; ++i){
		f[i] = f[i-1] + (f[i-2]*k);
	}
	return f[n];
}

int main() {
	int n;
	int k;

	cin >> n;
	cin >> k;

	//cout << '\n' << RecursionNaive(n,k) << endl;
	cout << FastMeth(n, k) << endl;

	return 0;
}
