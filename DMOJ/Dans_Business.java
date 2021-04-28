import java.util.*;
import java.io.*;

public class Dans_Business {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        int[] numServersAvailable = new int[n];
        for (int i = 0; i < n; i++) {
            numServersAvailable[i] = readInt();
        }
        int[][] orderRequests = new int[m][3];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < 3; j++) {
                orderRequests[i][j] = readInt();
            }
        }
        int left = 0, right = m;
        while (left < right) {
            int middle = (left + right) / 2;
            int[] diffArr = new int[n + 1];
            for (int i = 0; i < middle; i++) {
                diffArr[orderRequests[i][1] - 1] += orderRequests[i][0];
                diffArr[orderRequests[i][2]] -= orderRequests[i][0];
            }
            int[] prefSumArr = new int[n + 1];
            boolean canServe = true;
            for (int i = 1; i < n + 1; i++) {
                prefSumArr[i] = prefSumArr[i - 1] + diffArr[i - 1];
                if (prefSumArr[i] > numServersAvailable[i - 1]) {
                    canServe = false;
                    break;
                }
            }
            if (canServe) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        if (left == m) {
            System.out.println(0);
        } else {
            System.out.println(-1);
            System.out.println(left);
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
