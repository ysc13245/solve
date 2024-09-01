import java.io.*;
import java.util.*;


class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .sorted()
                .toArray()[1]);
    }
}
