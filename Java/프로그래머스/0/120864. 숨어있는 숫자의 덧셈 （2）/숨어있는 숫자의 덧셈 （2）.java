class Solution {
    public int solution(String my_string) {
        int sum = 0;
        for (char c = 'A';c<='z';c++) {
            my_string = my_string.replace(c+"", "/");
        }
        String[]sarr = my_string.split("/");
        for (String s:sarr) {
            if (s.equals("")) continue;
            sum += Integer.parseInt(s);
        }
        return sum;
    }
}