import java.util.*;
import java.io.*;

public class P1_Daisy_Chains {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] flowers = new int[n];
        int[] prefixSumArr = new int[n + 1];
        prefixSumArr[0] = 0;
        for (int i = 0; i < n; i++) {
            int flower = readInt();
            flowers[i] = flower;
            prefixSumArr[i + 1] = prefixSumArr[i] + flower;
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int sum = prefixSumArr[j + 1] - prefixSumArr[i];
                if (sum % (j - i + 1) != 0) {
                    continue;
                }
                int average = sum / (j - i + 1);
                for (int k = i; k < j + 1; k++) {
                    if (flowers[k] == average) {
                        count += 1;
                        break;
                    }
                }
            }
        }
        System.out.println(count);
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
