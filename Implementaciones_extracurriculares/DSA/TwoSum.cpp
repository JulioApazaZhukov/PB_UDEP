#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution 
{
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int l = nums.size();
        for (int i = 0; i < l; i++){
            for (int j = i+1; j < l; j++){
                if (nums[i] + nums[j] == target){
                    return {i, j};
                }
            }
        }
        return {};
    }
};

int main()
{
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    Solution solution;
    vector<int> result = solution.twoSum(nums, target);

    if (!result.empty()) {
        cout << "Indices: " << result[0] << ", " << result[1] << endl;
    } else {
        cout << "No solution found." << endl;
    }

    return 0;
}