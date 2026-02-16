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

void analyze();

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
    
    
    //cout << vars["T"] << endl;
    return 0;
}

void analyze(string cmd, string cmd2, string cmd3) {
    
}
