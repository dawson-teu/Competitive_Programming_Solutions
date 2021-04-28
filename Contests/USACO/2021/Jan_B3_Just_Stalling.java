import java.util.*;
import java.io.*;

public class Jan_B3_Just_Stalling {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] cowHeights = new int[n];
        int[] maxHeights = new int[n];
        for (int i = 0; i < n; i++) {
            cowHeights[i] = readInt();
        }
        for (int i = 0; i < n; i++) {
            maxHeights[i] = readInt();
        }
        Arrays.sort(cowHeights);
        int[] newCowHeights = new int[n];
        for (int i = 0; i < n; i++) {
            newCowHeights[n - 1 - i] = cowHeights[i];
        }
        cowHeights = Arrays.copyOf(newCowHeights, n);
        long numPos = 1;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (maxHeights[j] >= cowHeights[i]) {
                    count += 1;
                }
            }
            numPos *= (count - i);
        }
        System.out.println(numPos);
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
