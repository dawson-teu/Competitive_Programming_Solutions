import java.util.*;
import java.io.*;

public class C2_P2_Koala_Party {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] nums = new int[n];
        Set<Integer> num_set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            nums[i] = readInt();
            num_set.add(nums[i]);
        }
        if (n == 2 && (nums[0] + nums[1]) % 2 == 0) {
            System.out.println(2);
        } else if (n == 2) {
            System.out.println(1);
        } else {
            boolean is_three = false;
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    if ((nums[i] + nums[j]) % 2 == 0 && num_set.contains((nums[i] + nums[j]) / 2)) {
                        is_three = true;
                        break;
                    }
                }
            }
            if (is_three) {
                System.out.println(3);
            } else {
                System.out.println(2);
            }
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
