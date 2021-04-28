import java.util.*;
import java.io.*;

public class Mynerva {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        List<List<Edge>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int x = readInt(), y = readInt(), z = readInt();
            adjList.get(x - 1).add(new Edge(y, z));
            adjList.get(y - 1).add(new Edge(x, z));
        }
        Pair[] white_dist = dijkstra(false, n, adjList);
        Pair[] black_dist = dijkstra(true, n, adjList);
        int q = readInt();
        for (int i = 0; i < q; i++) {
            String line = readLine();
            int dest = Integer.parseInt(line.split(" ")[0]);
            String color = line.split(" ")[1];
            if (color.equals("White")) {
                System.out.println(white_dist[dest - 1].b + " " + -white_dist[dest - 1].c);
            } else {
                System.out.println(black_dist[dest - 1].b + " " + black_dist[dest - 1].c);
            }
        }
    }

    public static Pair[] dijkstra(boolean black, int n, List<List<Edge>> adjList) {
        Pair[] dist = new Pair[n];
        Arrays.fill(dist, new Pair(0, (int) 1e9, (int) 1e9));
        dist[0] = new Pair(1, 0, 0);
        boolean[] visited = new boolean[n];
        PriorityQueue<Pair> queue = new PriorityQueue<>();
        queue.add(new Pair(1, 0, 0));

        while (!queue.isEmpty()) {
            Pair vertex = queue.poll();
            visited[vertex.a - 1] = true;
            for (Edge neighbour : adjList.get(vertex.a - 1)) {
                if (!visited[neighbour.v - 1]) {
                    Pair newDist;
                    if (black) {
                        newDist = new Pair(neighbour.v, vertex.b + 1, vertex.c + neighbour.w);
                    } else {
                        newDist = new Pair(neighbour.v, vertex.b + 1, vertex.c - neighbour.w);
                    }
                    if (newDist.compareTo(dist[neighbour.v - 1]) < 0) {
                        dist[neighbour.v - 1] = newDist;
                        queue.add(newDist);
                    }
                }
            }
        }
        return dist;
    }

    public static class Pair implements Comparable<Pair>{
        final int a;
        final int b;
        final int c;
        public Pair(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }

        public int compareTo(Pair other) {
            if (this.b != other.b) {
                return Integer.compare(this.b, other.b);
            } else {
                return Integer.compare(this.c, other.c);
            }
        }
    }

    static class Edge {
        final int v;
        final int w;
        public Edge(int v, int w) {
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

    static String readLine() throws IOException {
        return br.readLine().trim();
    }
}
