#include <iostream>
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::string;

int hmmDistance(string string_a, string string_b){
	if (string_a.length() != string_b.length())
		return -1;

	int distance = 0;
	for (int i = 0; i < string_a.length(); i++){
		if (string_a[i] != string_b[i])
			distance +=1;
	}
	return distance;
};

int main(){

	string str_a, str_b;

	cin >> str_a;
	cin >> str_b;

	cout << hmmDistance(str_a, str_b) << endl;	
}
