import java.io.*;
import java.util.*;
import java.util.stream.*;


class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            System.out.println(Arrays.stream(br.readLine().split(" "))
                    .map(x -> new StringBuilder(x).reverse().toString())
                    .collect(Collectors.joining(" ")));
        }
    }

}
