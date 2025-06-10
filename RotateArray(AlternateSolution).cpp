class Solution
{
public:
    void rotate(vector<int> &nums, int k)
    {
        vector<int> ans;
        int tmp;
        int n = nums.size();
        k = k % n;
        for (int j = 0; j < k; j++)
        {
            tmp = nums.back();
            ans.insert(ans.begin(), tmp);
            nums.pop_back();
        }
        int tmp2;
        while (!nums.empty())
        {
            tmp2 = nums.front();
            ans.push_back(tmp2);
            nums.erase(nums.begin());
        }
        nums = ans;
    }
};