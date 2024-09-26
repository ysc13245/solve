import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            Map<String, Integer> map = new HashMap<>();
            Arrays.stream(br.readLine().split(" "))
                    .forEach(n -> map.put(n, map.getOrDefault(n, 0) + 1));

            int sum = map.values().stream().mapToInt(Integer::intValue).sum();
            int max = map.values().stream().mapToInt(Integer::intValue).max().orElse(0);
            String maxKey = map.entrySet().stream()
                    .filter(e -> e.getValue() == max)
                    .map(Map.Entry::getKey)
                    .findFirst().get();

            System.out.println(max * 2 >= sum ? maxKey : "SYJKGW");
        }
    }
}
