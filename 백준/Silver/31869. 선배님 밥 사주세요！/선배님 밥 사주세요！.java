import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        List<Boolean> calendar = new ArrayList<>(Collections.nCopies(71, false));
        HashMap<String, List<Integer>> schedule = new HashMap<>();

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            schedule.put(name, new ArrayList<>());

            schedule.get(name).add(Integer.parseInt(st.nextToken()));
            schedule.get(name).add(Integer.parseInt(st.nextToken()));
            schedule.get(name).add(Integer.parseInt(st.nextToken()));

        }

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            String name = st.nextToken();
            int balance = Integer.parseInt(st.nextToken());

            if (schedule.get(name).get(2) <= balance) {
                calendar.set((schedule.get(name).get(0) - 1) * 7 + schedule.get(name).get(1), true);
            }
        }

        int max_cnt = 0;
        int cnt = 0;

        for (Boolean b : calendar) {
            if (b) {
                cnt++;
            } else {
                max_cnt = Math.max(cnt, max_cnt);
                cnt = 0;
            }
        }
        System.out.println(max_cnt);
    }
}