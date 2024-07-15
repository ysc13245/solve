class Solution {
    public int[] solution(int[] numbers, String direction) {
        int l = numbers.length;
        int[] answer = new int[l];
        int t= direction.equals("right")?-1:1;
        for (int i= 0;i<l;i++) {
            answer[i] = numbers[(i+t+l)%l];
        }
        return answer;
    }
}