class Solution {
    public int solution(int n) {
        int answer = 0;
        int i = 0;
        while (true) {
            if (n < Math.pow(10,i++)) break;
            answer += n % Math.pow(10,i--) / Math.pow(10, i++);
        }
        return answer;
    }
}