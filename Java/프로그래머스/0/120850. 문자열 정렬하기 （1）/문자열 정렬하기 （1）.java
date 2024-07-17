import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
        int []answer=new int[my_string.length()];
        int idx=0;
        for (char c: my_string.toCharArray()){
            if (Character.isDigit(c)) {
                answer[idx++] = c-'0';
            }
        }
        answer = Arrays.copyOf(answer,idx);
        Arrays.sort(answer);
        return answer;
    }
}