import java.util.*;
import java.io.*;

public class Fun_in_Forag {
    static int a, b, n;
    static long c;
    static List<List<Edge>> adjList;

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        n = readInt();
        int m = readInt();

        adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int a = readInt();
            int b = readInt();
            int c = readInt();
            adjList.get(a - 1).add(new Edge(b, c, i));
            adjList.get(b - 1).add(new Edge(a, c, i));
        }

        a = readInt();
        b = readInt();
        c = readLong();
        int left = 1;
        int right = m;
        int ans = -1;
        while (left <= right) {
            int middle = (left + right) / 2;
            if (dij(middle)) {
                ans = middle;
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        System.out.println(ans);
    }

    public static boolean dij(int level) {
        long[] dist = new long[n];
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            dist[i] = Long.MAX_VALUE;
            visited[i] = false;
        }
        PriorityQueue<Edge> queue = new PriorityQueue<>();

        queue.add(new Edge(a, 0, 0));
        dist[a - 1] = 0;
        while (!queue.isEmpty()) {
            Edge vertex = queue.poll();
            visited[vertex.v - 1] = false;
            for (Edge neighbour : adjList.get(vertex.v - 1)) {
                long newDist = dist[vertex.v - 1] + neighbour.w;
                if (neighbour.id < level && newDist < dist[neighbour.v - 1]) {
                    dist[neighbour.v - 1] = newDist;
                    if (!visited[neighbour.v - 1]) {
                        queue.add(new Edge(neighbour.v, (int) dist[neighbour.v - 1], 0));
                        visited[neighbour.v - 1] = true;
                    }
                }
            }
        }
        return dist[b - 1] < c;
    }

    static class Edge implements Comparable<Edge> {
        final int v;
        final int w;
        final int id;

        Edge(int v, int w, int id) {
            this.v = v;
            this.w = w;
            this.id = id;
        }

        public int compareTo(Edge o) {
            return Integer.compare(this.w, o.w);
        }
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }

    static long readLong() throws IOException {
        return Long.parseLong(next());
    }

    static int readInt() throws IOException {
        return Integer.parseInt(next());
    }
}
