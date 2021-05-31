import java.util.*;
import java.io.*;

public class C2_P4_Koala_Gambling {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int t = readInt();
        for (int m = 0; m < t; m++) {
            int n = readInt();
            int[] nums = new int[n];
            for (int i = 0; i < n; i++) {
                nums[i] = readInt();
            }
            Arrays.sort(nums);
            if (n % 2 == 1) {
                System.out.println(toString(nums));
            } else if (nums[0] != nums[n - 1]) {
                if (n != 2) {
                    int tmp = nums[1];
                    nums[1] = nums[n - 2];
                    nums[n - 2] = tmp;
                }
                System.out.println(toString(nums));
            } else {
                System.out.println(-1);
            }
        }
    }

    static String toString(int[] arr) {
        StringBuilder output = new StringBuilder();
        for (int elem: arr) {
            output.append(elem).append(" ");
        }
        return output.substring(0, output.length() - 1);
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
