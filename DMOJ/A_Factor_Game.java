import java.util.*;
import java.io.*;

public class A_Factor_Game {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] nums = new int[n];
        int maxNum = -1;
        for (int i = 0; i < n; i++) {
            nums[i] = readInt();
            maxNum = Math.max(maxNum, nums[i]);
        }
        int[] freq = new int[maxNum + 1];
        for (int i = 0; i < n; i++) {
            freq[nums[i]] += 1;
        }
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 1; j <= Math.floor(Math.sqrt(nums[i])); j++) {
                if (nums[i] % j == 0) {
                    if (j * j == nums[i] && j != 1) {
                        count += freq[j];
                    } else {
                        if (j != nums[i]) {
                            count += freq[j];
                        }
                        if (j == 1) {
                            count += freq[nums[i]] - 1;
                        } else {
                            count += freq[nums[i] / j];
                        }
                    }
                }
            }
            System.out.println(count);
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
