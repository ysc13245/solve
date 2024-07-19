class Solution {
    public int solution(int[] array) {
        int sum = 0;
        for (int n:array) {
            for (char c: (n+"").toCharArray()) {
                if (c=='7') {
                    sum++;
                }
            }
        }
        return sum;
    }
}