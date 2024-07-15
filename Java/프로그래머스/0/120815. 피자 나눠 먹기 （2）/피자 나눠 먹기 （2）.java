class Solution {
    public int solution(int n) {
        for (int i = 1;true;i++) {
            if (i * 6 % n == 0) return i;
        }
    }
}