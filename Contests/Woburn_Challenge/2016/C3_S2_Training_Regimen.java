import java.util.*;
import java.io.*;

public class C3_S2_Training_Regimen {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        int[] training = new int[n];
        for (int i = 0; i < n; i++) {
            training[i] = readInt();
        }

        List<List<Edge>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int a = readInt(), b = readInt(), c = readInt();
            adjList.get(a - 1).add(new Edge(b, 0, c));
            adjList.get(b - 1).add(new Edge(a, 0, c));
        }

        PriorityQueue<Edge> queue = new PriorityQueue<>();
        queue.add(new Edge(1, 0, training[0]));
        long[] dist = new long[n];
        Arrays.fill(dist, (long) 1e9);
        dist[0] = 0;
        int level = 1;
        int min_level = training[0];
        long ans = 0;

        while (!queue.isEmpty()) {
            Edge node = queue.poll();
            if (dist[node.v - 1] > level) {
                ans += min_level * (dist[node.v - 1] - level);
                level = (int) dist[node.v - 1];
            }
            if (node.v == n) {
                System.out.println(ans);
                ans = -1;
                break;
            }
            min_level = Math.min(min_level, training[node.v - 1]);
            for (Edge neighbour : adjList.get(node.v - 1)) {
                if (neighbour.t < dist[neighbour.v - 1]) {
                    dist[neighbour.v - 1] = neighbour.t;
                    queue.add(new Edge(neighbour.v, dist[neighbour.v - 1], training[neighbour.v - 1]));
                }
            }
        }
        if (ans != -1) {
            System.out.println(-1);
        }
    }

    static class Edge implements Comparable<Edge> {
        final int v;
        final long w;
        final int t;

        Edge(int v, long w, int t) {
            this.v = v;
            this.w = w;
            this.t = t;
        }

        public int compareTo(Edge o) {
            if (this.w == o.w) {
                return Integer.compare(this.t, o.t);
            } else {
                return Long.compare(this.w, o.w);
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
