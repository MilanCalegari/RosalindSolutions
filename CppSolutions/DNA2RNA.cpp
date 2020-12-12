#include <iostream>
#include <string>

using std::string;
using std::cout;
using std::cin;

string conversion(string dna) {
	int size = dna.size();

	for (int i = 0; i < size; ++i) {
		if (dna[i] == 'T')
			dna[i] = 'U';
	}
	return dna;
}

int main() {
	string dna;
	cin >> dna;

	cout << '\n' << conversion(dna) << '\n';
	return 0;
}
