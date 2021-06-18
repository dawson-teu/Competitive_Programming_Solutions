import java.util.*;
import java.io.*;

public class Bobs_Portal_Travel {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        long k = readLong();
        int[] portals = new int[n];
        for (int i = 0; i < n; i++) {
            portals[i] = readInt() - 1;
        }
        HashMap<Integer, Integer> portal_index = new HashMap<>();
        int cur_node = 0;
        int index = 0;
        int[] path = new int[n];
        while (!portal_index.containsKey(cur_node)) {
            portal_index.put(cur_node, index);
            path[index] = cur_node;
            cur_node = portals[cur_node];
            index += 1;
        }
        int cycle_length = index - portal_index.get(cur_node);
        int offset = index - cycle_length;
        if (k < offset) {
            System.out.println(path[(int) k] + 1);
        } else {
            System.out.println(path[(int) ((k - offset) % cycle_length) + offset] + 1);
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

    static long readLong() throws IOException {
        return Long.parseLong(next());
    }
}
