class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i = 1 ; i <= Math.pow(n, 0.5); i++) {
            if (n % i == 0) {
                answer += 2;
                if (i * i == n) answer--;
            }
        }
        return answer;
    }
}