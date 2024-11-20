class Solution {
public:
    int takeCharacters(string s, int k) {
    unordered_map<char, int> hashMap;

    // Populate the hashMap with character frequencies
    for (char c : s) {
        hashMap[c]++;
    }

    // Edge case: If k is 0, no time is needed
    if (k == 0) return 0;

    // Check if any character has less than 'k' occurrences
    if (hashMap['a'] < k || hashMap['b'] < k || hashMap['c'] < k) return -1;

    int n = s.length();
    int minMinutes = n, i = 0, j = 0;

    while (i <= j && j < n) {
        char c = s[j];
        hashMap[c]--;

        // Adjust the window to maintain the condition
        while (i <= j && (hashMap['a'] < k || hashMap['b'] < k || hashMap['c'] < k)) {
            char leftChar = s[i];
            hashMap[leftChar]++;
            i++;
        }

        minMinutes = min(minMinutes, n - (j - i + 1));
        j++;
    }

    return minMinutes;
}

};
