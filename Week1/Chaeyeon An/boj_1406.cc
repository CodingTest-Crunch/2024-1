// https://www.acmicpc.net/problem/1406

#include <iostream>
#include <string>
#include <list>

using namespace std;

int main() {

	ios::sync_with_stdio(0);
	cin.tie(0);

	string s;
	list<char> L;

	cin >> s;
	for (auto c : s) L.push_back(c);
	auto cursor = L.end();

	char cmd; int n;
	cin >> n;

	while (n--) {
		cin >> cmd;

		if (cmd == 'L') {
			if (cursor != L.begin()) {
				cursor--;
			}
		}
		else if (cmd == 'D') {
			if (cursor != L.end()) {
				cursor++;
			}
		}
		else if (cmd == 'B') {
			if (cursor != L.begin()) {
				cursor--;
				cursor = L.erase(cursor);
			}
		}
		else if (cmd == 'P') {
			char k;
			cin >> k;
			L.insert(cursor, k);
		}
	}

	for (auto c : L) cout << c;

	return 0;

}