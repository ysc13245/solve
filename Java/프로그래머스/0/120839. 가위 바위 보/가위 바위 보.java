class Solution {
    public String solution(String rsp) {
        StringBuilder sb = new StringBuilder();
        for (char c: rsp.toCharArray()) {
            if (c=='2') sb.append('0');
            else if (c=='5') sb.append('2');
            else if (c=='0') sb.append('5');
        }
        return sb.toString();
    }
}