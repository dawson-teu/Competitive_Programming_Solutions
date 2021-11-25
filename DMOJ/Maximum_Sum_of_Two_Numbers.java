import java.util.*;
import java.io.*;

public class Maximum_Sum_of_Two_Numbers {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = readInt();
        }
        Arrays.sort(nums);
        int left = 0;
        int right = n - 1;
        int ans = -1;
        while (left < right) {
            if (nums[left] + nums[right] > m) {
                right -= 1;
            } else {
                ans = Math.max(ans, nums[left] + nums[right]);
                left += 1;
            }
        }
        System.out.println(ans);
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
