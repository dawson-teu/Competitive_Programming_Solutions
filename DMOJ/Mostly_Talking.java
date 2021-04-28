import java.io.*;
import java.util.*;

public class Mostly_Talking {
    static int n;
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        n = readInt();
        int m = readInt();
        List<List<Edge>> adjList = new ArrayList<>();
        List<List<Edge>> revList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
            revList.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int a = readInt();
            int b = readInt();
            int k = readInt();
            adjList.get(a - 1).add(new Edge(b, k));
            revList.get(b - 1).add(new Edge(a, k));
        }
        long[] forDist = dij(1, adjList);
        long[] revDist = dij(n, revList);

        int d = readInt();
        long min = forDist[n - 1];
        for (int i = 0; i < d; i++) {
            int a = readInt();
            int b = readInt();
            int g = readInt();
            if (forDist[a - 1] + g + revDist[b - 1] < min) {
                min = forDist[a - 1] + g + revDist[b - 1];
            }
        }
        if (min >= (long) 1e12) {
            System.out.println(-1);
        } else {
            System.out.println(min);
        }
    }

    public static long[] dij(int start, List<List<Edge>> graph) {
        PriorityQueue<Edge> queue = new PriorityQueue<>();
        boolean[] visited = new boolean[n];
        long[] dist = new long[n];
        for (int i = 0; i < n; i++) {
            dist[i] = (long) 1e12;
        }
        queue.add(new Edge(start, 0));
        dist[start - 1] = 0;

        while (!queue.isEmpty()) {
            Edge vertex = queue.poll();
            visited[vertex.v - 1] = true;
            for (Edge neighbour : graph.get(vertex.v - 1)) {
                if (!visited[neighbour.v - 1]) {
                    long newDist = dist[vertex.v - 1] + neighbour.w;
                    if (newDist < dist[neighbour.v - 1]) {
                        dist[neighbour.v - 1] = newDist;
                        queue.add(new Edge(neighbour.v, dist[neighbour.v - 1]));
                    }
                }
            }
        }
        return dist;
    }

    static class Edge implements Comparable<Edge> {
        final int v;
        final long w;

        Edge(int v, long w) {
            this.v = v;
            this.w = w;
        }

        public int compareTo(Edge o) {
            return Long.compare(w, o.w);
        }
    }

    static int readInt() throws IOException {
        return Integer.parseInt(next());
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }
}
