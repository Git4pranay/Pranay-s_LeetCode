class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(), strs.end());
        string first = strs[0];
        string last = strs[strs.size() - 1];
        int len = min(first.length(), last.length());
        string acc = "";
        for (int i = 0; i < len; i++){
            if (first[i] == last[i]){
                acc = acc + first[i];
            } else {
                return acc;
            }
        }
        return acc;
    }
};