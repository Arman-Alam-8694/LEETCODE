#include <vector>
using namespace std;

class Solution {
public:
    bool recur(int idx, long long prev, long long maxx, const vector<int>& differences, int n, int lower, int upper, long long &answer) {
        if (idx == n) {
            answer = maxx;
            return true;
        }

        long long ahead = differences[idx] + prev;
        if (ahead >= lower && ahead <= upper) {
            long long temp = max(maxx, ahead);
            bool correct = recur(idx + 1, ahead, temp, differences, n, lower, upper, answer);
            if (correct) return true;
        }

        return false;
    }

    int numberOfArrays(vector<int>& differences, int lower, int upper) {
        int n = differences.size();

        for (int i = lower; i <= upper; ++i) {
            long long ahead = (long long)differences[0] + i;
            if (ahead >= lower && ahead <= upper) {
                long long maxx = max((long long)i, ahead);
                long long ans = 0;
                if (recur(1, ahead, maxx, differences, n, lower, upper, ans)) {
                    return 1 + (upper - ans);
                }
            }
        }

        return 0;
    }
};
