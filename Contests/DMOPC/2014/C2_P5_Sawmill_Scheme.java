import java.util.*;
import java.io.*;

public class C2_P5_Sawmill_Scheme {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int a = readInt(), b = readInt();
            adjList.get(a - 1).add(b);
        }
        double[] dp = new double[n];
        dp[0] = 1;
        for (int i = 0; i < n; i++) {
            for (int child: adjList.get(i)) {
                dp[child - 1] += dp[i] / adjList.get(i).size();
            }
        }
        for (int i = 0; i < n; i++) {
            if (adjList.get(i).size() == 0) {
                System.out.println(dp[i]);
            }
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
