import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> kda = Arrays.stream(br.readLine().split("/"))
                .map(Integer::parseInt)
                .collect(Collectors.toList());

        System.out.println(kda.get(0)+kda.get(2)<kda.get(1)||kda.get(1)==0?"hasu":"gosu");

    }
}
