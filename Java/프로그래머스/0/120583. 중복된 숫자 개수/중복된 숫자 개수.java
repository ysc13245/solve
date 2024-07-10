class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        for (int m : array) {
            answer += n == m ? 1 : 0;
        }
        return answer;
    }
}