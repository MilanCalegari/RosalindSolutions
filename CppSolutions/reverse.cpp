#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

string complement(string dna) {
	int size = dna.size();

	for (int i = 0; i < size; ++i){
		if (dna[i] == 'A')
			dna[i] = 't';
		if (dna[i] == 'T')
			dna[i] = 'a';
		if (dna[i] == 'C')
			dna[i] = 'g';
		if (dna[i] == 'G')
			dna[i] = 'c';
	}
	transform(dna.begin(), dna.end(), dna.begin(), ::toupper);
	return dna;
}

string reverse (string dna) {
	reverse(dna.begin(), dna.end());
	return dna;
}

int main() { 
	string dna;

	cin >> dna;
	cout << '\n' << reverse(complement(dna)) << '\n';
	return 0;
}
