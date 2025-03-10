#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long countOfSubstrings(string word, int k) {  // Use long long
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        unordered_map<char, int> vow_map, tvow;
        long long cons = 0, tcons = 0, temp = 0, left = 0, result = 0;  // Use long long
        int n = word.size();

        for (int right = 0; right < n; right++) {
            if (vowels.count(word[right])) {
                vow_map[word[right]]++;
                tvow[word[right]]++;

                if (tvow.size() == 5 && tcons == k) {
                    while (temp < right && tvow.size() == 5 && tcons == k) {
                        if (vowels.count(word[temp])) {
                            if (--tvow[word[temp]] == 0)
                                tvow.erase(word[temp]);
                        } else {
                            tcons--;
                        }
                        temp++;
                    }
                }
            } else {
                cons++;
                tcons++;
            }

            while (cons > k) {
                if (temp == left) {
                    if (vowels.count(word[left])) {
                        if (--vow_map[word[left]] == 0)
                            vow_map.erase(word[left]);
                        if (--tvow[word[temp]] == 0)
                            tvow.erase(word[temp]);
                    } else {
                        cons--;
                        tcons--;
                    }
                    temp++;
                } else if (vowels.count(word[left])) {
                    if (--vow_map[word[left]] == 0)
                        vow_map.erase(word[left]);
                } else {
                    cons--;
                }
                left++;
            }

            if (temp <= left) {
                while (temp < right && tvow.size() == 5 && tcons == k) {
                    if (vowels.count(word[temp])) {
                        if (--tvow[word[temp]] == 0)
                            tvow.erase(word[temp]);
                    } else {
                        tcons--;
                    }
                    temp++;
                }
            }

            if (temp > left) {
                result += (temp - left);  // Ensure no overflow
            }
        }
        return result;
    }
};
