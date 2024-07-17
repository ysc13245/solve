class Solution {
    public String solution(String my_string) {
        StringBuilder sb= new StringBuilder();
        for (char c:my_string.toCharArray()){
            if(!sb.toString().contains(c+"")){
                sb.append(c);
            }
        }
        return sb.toString();
    }
}