class Solution {
    public int solution(int[] array, int n) {
        if (array.length == 0 || array.length > 100) throw new IllegalArgumentException();
        if (n<0 || n>1000) throw new IllegalArgumentException();
        for (int e:array){
            if (e<0 || e > 1000) throw new IllegalArgumentException();
        }
        int answer = 0;
        for (int m : array) {
            answer += n == m ? 1 : 0;
        }
        return answer;
    }
}