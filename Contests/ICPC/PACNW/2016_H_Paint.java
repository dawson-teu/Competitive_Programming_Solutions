import java.util.*;
import java.io.*;

public class H_Paint {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        long n = readLong();
        int k = readInt();
        Interval[] paint = new Interval[k];
        for (int i = 0; i < k; i++) {
            long r = readLong(), l = readLong();
            paint[i] = new Interval(r, l, l - r + 1);
        }
        Arrays.sort(paint);
        long[] dp = new long[k + 1];
        for (int i = 1; i <= k; i++) {
            int index = binarySearch(paint[i - 1].l, paint);
            dp[i] = Math.max(dp[i - 1], paint[i - 1].v + dp[index + 1]);
        }
        System.out.println(n - dp[k]);
    }

    static int binarySearch(long start, Interval[] arr) {
        int low = 0;
        int high = arr.length - 1;
        int ans = -1;
        while (low <= high) {
            int middle = (low + high) / 2;
            if (arr[middle].r <= start) {
                ans = middle;
                low = middle + 1;
            } else {
                high = middle - 1;
            }
        }
        return ans;
    }

    static class Interval implements Comparable<Interval> {
        final long l;
        final long r;
        final long v;

        public Interval(long l, long r, long v) {
            this.l = l;
            this.r = r;
            this.v = v;
        }

        public int compareTo(Interval other) {
            return Long.compare(this.r, other.r);
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
