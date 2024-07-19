import java.util.Arrays;

class Solution {
    public String solution(String s) {

        int[] cnt = new int[26];
        
        for (char c : s.toCharArray()) {
            cnt[c - 'a']++;
        }
        
        char[] carr = new char[26];
        int idx=0;
        for (int i = 0; i < 26; i++) {
            if (cnt[i] == 1) {
                carr[idx++] = (char) (i + 'a');
            }
        }
        carr = Arrays.copyOf(carr, idx);
        Arrays.sort(carr);
        
        StringBuilder sb = new StringBuilder();
        for (char c : carr) {
            sb.append(c);
        }

        return sb.toString();
    }
}