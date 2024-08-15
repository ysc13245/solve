import java.io.*;
import java.util.*;


public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        br.lines().forEach(s -> sb.append(s.trim()));

        int sum = Arrays.stream(sb.toString().split(","))
                .mapToInt(Integer::parseInt).sum();
        System.out.println(sum);
    }
}