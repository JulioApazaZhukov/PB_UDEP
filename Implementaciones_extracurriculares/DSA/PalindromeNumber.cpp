#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0) && x != 0){return false;}
        else{
            long long int auxx = x;
            long long int revx = 0;
            int digit;
            while (x > 0){
                digit = x % 10;
                revx = revx * 10 +digit;
                x = x / 10;
            }
            if (revx == auxx) {return true;}
            else {return false;}
        }
    }
};

int main() 
{
    int x = 12021;
    Solution solution;
    int result = solution.isPalindrome(x);
    if (!result == false){
        cout << "True";
    } else {cout << "False";}

    return 0;
}