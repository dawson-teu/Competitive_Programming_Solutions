import java.util.*;
import java.io.*;

public class P2_World_of_StarCraft {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int[] disjointSet;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt(), k = readInt();
        String planetRaces = readLine();
        disjointSet = new int[n];
        for (int i = 0; i < n; i++) {
            disjointSet[i] = i + 1;
        }
        for (int i = 0; i < m; i++) {
            int a = readInt(), b = readInt();
            if (planetRaces.charAt(a - 1) == planetRaces.charAt(b - 1)) {
                disjointSet[find(a) - 1] = find(b);
            }
        }
        int count = 0;
        for (int i = 0; i < k; i++) {
            int x = readInt(), y = readInt();
            if (find(x) == find(y)) {
                count += 1;
            }
        }
        System.out.println(count);
    }

    static int find(int elem) {
        if (elem != disjointSet[elem - 1]) {
            disjointSet[elem - 1] = find(disjointSet[elem - 1]);
        }
        return disjointSet[elem - 1];
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
