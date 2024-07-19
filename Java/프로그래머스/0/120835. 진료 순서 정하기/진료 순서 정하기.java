import java.util.Arrays;

class Solution {
    public int[] solution(int[] emergency) {
        int l = emergency.length;
        int [] sorted = Arrays.copyOf(emergency, l);
        Arrays.sort(sorted);
        int [] answer = new int [l];
        for (int i =0;i<l;i++) {
            for (int j=0;j<l;j++) {
                if (sorted[i] == emergency[j]) {
                    answer[i] = l-j;
                }
            }
        }
        return answer;
    }
}