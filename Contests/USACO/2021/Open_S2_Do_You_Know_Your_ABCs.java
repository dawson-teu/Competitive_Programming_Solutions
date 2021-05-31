import java.util.*;
import java.io.*;

public class Open_S2_Do_You_Know_Your_ABCs {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int t = readInt();
        for (int m = 0; m < t; m++) {
            int n = readInt();
            int[] nums = new int[n + 1];
            nums[0] = 0;
            for (int i = 0; i < n; i++) {
                nums[i + 1] = readInt();
            }

            Set<Integer> possibleABC = new HashSet<>();
            for (int x: nums) {
                for (int y: nums) {
                    if (x < y) {
                        possibleABC.add(y - x);
                    }
                }
            }

            int ans = 0;
            for (int a: possibleABC) {
                for (int b: possibleABC) {
                    for (int c: possibleABC) {
                        if (a <= b && b <= c) {
                            boolean solution = true;
                            for (int num: nums) {
                                if (!(num == 0 || num == a || num == b || num == c || num == a + b || num == b + c || num == a + c || num == a + b + c)) {
                                    solution = false;
                                    break;
                                }
                            }
                            if (solution) {
                                ans++;
                            }
                        }
                    }
                }
            }
            System.out.println(ans);
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
