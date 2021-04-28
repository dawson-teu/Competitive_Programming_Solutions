import java.util.*;
import java.io.*;

public class P2_King_Gruff {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt(), a = readInt(), b = readInt();
        List<List<Edge>> adjList = new ArrayList<>();
        List<List<Edge>> revList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
            revList.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int x = readInt(), y = readInt(), l = readInt(), c = readInt();
            adjList.get(x - 1).add(new Edge(y, l, c));
            revList.get(y - 1).add(new Edge(x, l, c));
        }

        int[] forDist = dijkstra(a, n, adjList);
        int[] revDist = dijkstra(b, n, revList);
        List<Edge> paths = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (Edge neighbour : adjList.get(i)) {
                paths.add(new Edge(0,forDist[i] + neighbour.w + revDist[neighbour.v - 1], neighbour.cost));
            }
        }
        Collections.sort(paths);
        for (int i = 1; i < paths.size(); i++) {
            paths.get(i).cost += paths.get(i - 1).cost;
        }

        int q = readInt();
        Edge[] queries = new Edge[q];
        for (int i = 0; i < q; i++) {
            int d = readInt();
            queries[i] = new Edge(0, d, i);
        }
        Arrays.sort(queries);

        int[] ans = new int[q];
        int index = 0;
        for (int i = 0; i < q; i++) {
            while (index < paths.size() && queries[i].w >= paths.get(index).w) {
                index += 1;
            }
            if (index > 0) {
                ans[queries[i].cost] = paths.get(index - 1).cost;
            }
        }

        for (int i = 0; i < q; i++) {
            System.out.println(ans[i]);
        }
    }

    public static int[] dijkstra(int start, int n, List<List<Edge>> graph) {
        PriorityQueue<Edge> queue = new PriorityQueue<>();
        boolean[] visited = new boolean[n];
        int[] dist = new int[n];
        Arrays.fill(dist, (int) 1e9);
        queue.add(new Edge(start, 0, 0));
        dist[start - 1] = 0;

        while (!queue.isEmpty()) {
            Edge vertex = queue.poll();
            visited[vertex.v - 1] = true;
            for (Edge neighbour : graph.get(vertex.v - 1)) {
                if (!visited[neighbour.v - 1]) {
                    int newDist = dist[vertex.v - 1] + neighbour.w;
                    if (newDist < dist[neighbour.v - 1]) {
                        dist[neighbour.v - 1] = newDist;
                        queue.add(new Edge(neighbour.v, dist[neighbour.v - 1], 0));
                    }
                }
            }
        }
        return dist;
    }

    static class Edge implements Comparable<Edge> {
        final int v;
        final int w;
        int cost;

        Edge(int v, int w, int cost) {
            this.v = v;
            this.w = w;
            this.cost = cost;
        }

        public int compareTo(Edge o) {
            if (this.w == o.w) {
                return Integer.compare(this.cost, o.cost);
            } else {
                return Integer.compare(this.w, o.w);
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
