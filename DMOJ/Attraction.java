import java.util.*;
import java.io.*;

public class P5_Attraction {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int t = readInt();
        for (int z = 0; z < t; z++) {
            int n = readInt(), a = readInt(), b = readInt();
            int[] fixedAttractors = new int[a];
            for (int i = 0; i < a; i++) {
                fixedAttractors[i] = readInt();
            }
            Arrays.sort(fixedAttractors);
            PriorityQueue<Pair> queue = new PriorityQueue<>();
            if (fixedAttractors[0] > 1) {
                queue.add(new Pair(fixedAttractors[0] - 1, 0));
            }
            if (fixedAttractors[a - 1] < n) {
                queue.add(new Pair(n - fixedAttractors[a - 1], 0));
            }
            for (int i = 1; i < a; i++) {
                if (fixedAttractors[i - 1] + 1 != fixedAttractors[i]) {
                    int gap = fixedAttractors[i] - fixedAttractors[i - 1] - 1;
                    if (gap % 2 == 0) {
                        queue.add(new Pair(gap / 2, 2));
                    } else {
                        queue.add(new Pair((gap + 1) / 2, 3));
                    }
                }
            }
            int total = 0;
            while (!queue.isEmpty() && b > 0) {
                Pair pair = queue.poll();
                if (pair.b == 3 && pair.a >= 2) {
                    queue.add(new Pair(pair.a - 2, 1));
                } else if (pair.b == 2) {
                    queue.add(new Pair(pair.a, 0));
                } else if (pair.b == 1) {
                    queue.add(new Pair(1, 0));
                }
                total += pair.a;
                b -= 1;
            }
            System.out.println(total);
        }
    }

    static class Pair implements Comparable<Pair> {
        final int a;
        final int b;

        Pair(int a, int b) {
            this.a = a;
            this.b = b;
        }

        public int compareTo(Pair other) {
            return Integer.compare(other.a, this.a);
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
