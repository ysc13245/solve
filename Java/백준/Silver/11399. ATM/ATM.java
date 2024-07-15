import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<Integer> input = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            input.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(input);

        List<Integer> summed = new ArrayList<>();
        summed.add(input.get(0));
        for (int i = 1; i < n; i++) {
            summed.add(summed.get(i - 1) + input.get(i));
        }
        int result = 0;
        for (Integer i : summed) {
            result += i;
        }
        System.out.println(result);
    }
}