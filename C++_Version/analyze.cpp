#include <iostream>
#include <string>
#include <fstream>
#include <unordered_map>
#include <sstream>
#include <vector>
using namespace std;

auto varsInt = unordered_map<string,int>();
auto varsStr = unordered_map<string,string>();

string line;
vector<string> code = {};

void analyze(string cmd, string cmd2, string cmd3) {
    if (cmd3[cmd3.length() - 1] == ';') {
        if (cmd == "int") {
            cmd3 = cmd3.substr(0, cmd3.length() - 1);
            int value = stoi(cmd3);
            varsInt[cmd2] = value;
            
        } else if (cmd == "print") {
            cout << varsInt[cmd2];
        }
    } else {
        cout << "Error! Need the ; in end line. Fix this, please";
    }
}

int main() {
    ifstream MyReadFile("test.pk");

    while (getline(MyReadFile, line)) {
        stringstream ss(line);

        string cmd;
        string cmd2;
        string cmd3;

        ss >> cmd >> cmd2 >> cmd3;
        code.push_back(cmd);
        code.push_back(cmd2);
        code.push_back(cmd3);
    }

    MyReadFile.close();
    analyze(code[0], code[1], code[2]);
    
    cout << varsInt["P"];
    //cout << code.size();
    //cout << vars["T"] << endl;
    return 0;
}