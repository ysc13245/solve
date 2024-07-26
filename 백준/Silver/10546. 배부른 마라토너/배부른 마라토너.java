import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<String, Boolean> players = new HashMap<>();
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N * 2 - 1; i++) {
            String player = br.readLine();
            if (players.remove(player) == null) {
                players.put(player, true);
            }
        }
        for (String s : players.keySet()) {
            System.out.println(s);
        }
    }
}