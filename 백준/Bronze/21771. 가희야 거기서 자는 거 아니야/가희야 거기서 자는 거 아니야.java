import java.io.*;
import java.util.*;


public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().split(" ")[0]);
        int size = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .skip(2)
                .limit(2)
                .reduce(1, (a, b) -> a * b);

        int sum = br.lines()
                .mapToInt(x -> (int) x.chars().filter(c -> c == 'P').count())
                .sum();
        System.out.println(size != sum ? 1 : 0);
    }
}