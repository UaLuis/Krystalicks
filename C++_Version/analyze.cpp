#include <iostream>
#include <string>
#include <fstream>
#include <unordered_map>
#include <variant>
#include <sstream>
#include <vector>
using namespace std;

auto vars = unordered_map<string,variant<int,string>>();

void analyze(string cmd1, string cmd2, string cmd3);

int main() {
    ifstream MyReadFile("test.pk");
    string line;
    vector<string> code = {};

    while (getline(MyReadFile, line)) {
        stringstream ss(line);

        string cmd1;
        string cmd2;
        string cmd3;

        ss >> cmd1 >> cmd2 >> cmd3;
        analyze(cmd1, cmd2, cmd3);
            
        code.push_back(cmd1);
        code.push_back(cmd2);
        code.push_back(cmd3);
    }

    MyReadFile.close();
    return 0;
}

void analyze(string cmd1, string cmd2, string cmd3) {
        if (cmd1 == "int") {
            int value = stoi(cmd3);
            vars[cmd2] = value;
            
        } else if (cmd1 == "str") {
            string value = cmd3;
            vars[cmd2] = value;
            
        } else if (cmd1 == "print") {
            if (cmd2 == "int") {
                cout << get<int>(vars[cmd3]) << endl;
            } else if (cmd2 == "str") {
                cout << get<string>(vars[cmd3]) << endl;
            }
        }

}