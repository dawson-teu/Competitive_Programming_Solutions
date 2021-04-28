import java.util.*;

public class P2_The_Hungary_Games {
    static int n;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        n = input.nextInt();
        int m = input.nextInt();
        List<List<Edge>> adjList = new ArrayList<>();
        List<List<Edge>> revList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
            revList.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int a = input.nextInt();
            int b = input.nextInt();
            int l = input.nextInt();
            adjList.get(a - 1).add(new Edge(b, l));
            revList.get(b - 1).add(new Edge(a, l));
        }

        int[] forDist = dij(1, adjList);
        int[] revDist = dij(n, revList);

        if (forDist[n - 1] == Integer.MAX_VALUE) {
            System.out.println("-1");
            return;
        }

        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            for (Edge e : adjList.get(i)) {
                if (forDist[i] != Integer.MAX_VALUE && revDist[e.v - 1] != Integer.MAX_VALUE) {
                    if (forDist[i] + e.w + revDist[e.v - 1] > forDist[n - 1]) {
                        ans = Math.min(ans, forDist[i] + e.w + revDist[e.v - 1]);
                    }
                }
            }
        }
        if (ans == Integer.MAX_VALUE) {
            System.out.println("-1");
        } else {
            System.out.println(ans);
        }
    }

    public static int[] dij(int start, List<List<Edge>> graph) {
        PriorityQueue<Edge> queue = new PriorityQueue<>();
        boolean[] visited = new boolean[n];
        int[] dist = new int[n];
        for (int i = 0; i < n; i++) {
            dist[i] = Integer.MAX_VALUE;
        }
        queue.add(new Edge(start, 0));
        dist[start - 1] = 0;

        while (!queue.isEmpty()) {
            Edge vertex = queue.poll();
            visited[vertex.v - 1] = true;
            for (Edge neighbour : graph.get(vertex.v - 1)) {
                if (!visited[neighbour.v - 1]) {
                    int newDist = dist[vertex.v - 1] + neighbour.w;
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
        final int w;

        Edge(int v, int w) {
            this.v = v;
            this.w = w;
        }

        public int compareTo(Edge o) {
            return Integer.compare(w, o.w);
        }
    }
}
