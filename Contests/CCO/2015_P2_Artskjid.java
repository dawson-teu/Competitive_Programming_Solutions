import java.util.*;
import java.io.*;

public class P2_Artskjid {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        List<List<Edge>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int s = readInt(), d = readInt(), l = readInt();
            adjList.get(s).add(new Edge(d, l));
        }
        int[][] dp = new int[n][1 << n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], -1);
        }
        Deque<Edge> stack = new ArrayDeque<>();
        dp[0][1] = 0;
        stack.add(new Edge(0, 1));
        while (!stack.isEmpty()) {
            Edge vertex = stack.pop();
            for (Edge neighbour: adjList.get(vertex.v)) {
                int newDist = neighbour.w + dp[vertex.v][vertex.w];
                int curDist = dp[neighbour.v][vertex.w | (1 << neighbour.v)];
                if ((vertex.w & (1 << neighbour.v)) == 0 && newDist > curDist) {
                    dp[neighbour.v][vertex.w | (1 << neighbour.v)] = newDist;
                    stack.add(new Edge(neighbour.v, vertex.w | (1 << neighbour.v)));
                }
            }
        }
        int ans = -1;
        for (int i = 0; i < 1 << n; i++) {
            ans = Math.max(ans, dp[n - 1][i]);
        }
        System.out.println(ans);
    }

    static class Edge {
        final int v;
        final int w;

        Edge(int v, int w) {
            this.v = v;
            this.w = w;
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
