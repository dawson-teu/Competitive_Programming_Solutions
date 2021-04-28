import java.util.*;

public class Cherry_Tree {
    static int n, c, k;
    static List<List<Edge>> adjList;
    static int[] numCherry;
    static int[] weight;
    static int[] size;
    static int result;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        n = input.nextInt();
        c = input.nextInt();
        k = input.nextInt();
        numCherry = new int[n];
        weight = new int[n];
        size = new int[n];
        result = 0;
        for (int i = 0; i < n; i++) {
            numCherry[i] = input.nextInt();
        }
        adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int i = 0; i < n - 1; i++) {
            int a = input.nextInt(), b = input.nextInt(), weight = input.nextInt();
            adjList.get(a - 1).add(new Edge(b, weight));
            adjList.get(b - 1).add(new Edge(a, weight));
        }
        dfs(1, 1000000001, 0);
        System.out.println(result);
        input.close();
    }

    public static void dfs(int v, int w, int parent) {
        weight[v - 1] = w;
        size[v - 1] = numCherry[v - 1];
        for (Edge e : adjList.get(v - 1)) {
            if (e.v != parent) {
                dfs(e.v, e.w, v);
                size[v - 1] += size[e.v - 1];
                weight[v - 1] += weight[e.v - 1];
            }
        }
        if (size[v - 1] >= c && weight[v - 1] <= k) {
            result += 1;
        }
    }

    static class Edge {
        final int v;
        final int w;

        Edge(int v, int w) {
            this.v = v;
            this.w = w;
        }
    }
}
