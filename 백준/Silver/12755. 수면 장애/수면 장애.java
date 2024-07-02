import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 1; true; i++) {
            if (sb.length() >= N) {
                break;
            }
            sb.append(i);
        }
        System.out.println(sb.charAt(N-1));

    }
}