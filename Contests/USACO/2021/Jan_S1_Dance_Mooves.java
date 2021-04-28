import java.util.*;
import java.io.*;

public class Jan_S1_Dance_Mooves {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), k = readInt();
        int[] cowPos = new int[n];
        List<List<Integer>> cowVisited = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            cowVisited.add(new ArrayList<>());
            cowVisited.get(i).add(i + 1);
            cowPos[i] = i + 1;
        }

        for (int i = 0; i < k; i++) {
            int a = readInt(), b = readInt();
            int cowsA = cowPos[a - 1], cowsB = cowPos[b - 1];
            cowVisited.get(cowsA - 1).add(b);
            cowVisited.get(cowsB - 1).add(a);
            cowPos[a - 1] = cowsB;
            cowPos[b - 1] = cowsA;
        }

        int[] cowNumPos = new int[n];
        for (int i = 0; i < n; i++) {
            if (cowPos[i] != 0) {
                int cur = i + 1;
                List<Integer> curCycle = new ArrayList<>();
                while (cowPos[cur - 1] != 0) {
                    int prev = cur;
                    curCycle.add(cur);
                    cur = cowPos[cur - 1];
                    cowPos[prev - 1] = 0;
                }
                Set<Integer> cowsInCycle = new HashSet<>();
                for (int cow : curCycle) {
                    cowsInCycle.addAll(cowVisited.get(cow - 1));
                }
                for (int cow : curCycle) {
                    cowNumPos[cow - 1] = cowsInCycle.size();
                }
            }
        }
        for (int i = 0; i < n; i++) {
            System.out.println(cowNumPos[i]);
        }
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }

    static int readInt() throws IOException {
        return Integer.parseInt(next());
    }
}
