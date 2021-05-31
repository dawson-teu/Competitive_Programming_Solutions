import java.util.*;
import java.io.*;

public class P2_Weird_Numeral_System {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int k = readInt(), q = readInt(), d = readInt();
        readInt();
        int[] digits = new int[d];
        boolean is_zero = false;
        for (int i = 0; i < d; i++) {
            digits[i] = readInt();
            if (digits[i] == 0) {
                is_zero = true;
            }
        }
        for (int t = 0; t < q; t++) {
            long num = readLong();
            if (num == 0 && is_zero) {
                System.out.println(0);
                continue;
            }
            Stack<Long> stack = new Stack<>();
            Set<Long> visited = new HashSet<>();
            Map<Long, Long> prev = new HashMap<>();
            Map<Long, Integer> digitUsed = new HashMap<>();
            stack.add(num);
            visited.add(num);
            while (!stack.isEmpty()) {
                long cur_num = stack.pop();
                if (cur_num == 0 && num != 0) {
                    break;
                }
                for (int digit: digits) {
                   if ((!visited.contains((cur_num - digit) / k) || (cur_num - digit) / k == 0) && (cur_num - digit) % k == 0) {
                       stack.add((cur_num - digit) / k);
                       visited.add((cur_num - digit) / k);
                       prev.put((cur_num - digit) / k, cur_num);
                       digitUsed.put((cur_num - digit) / k, digit);
                   }
                }
            }
            long cur = 0;
            StringBuilder output = new StringBuilder();
            while (prev.containsKey(cur) && !(output.length() > 0 && cur == 0)) {
                output.append(digitUsed.get(cur)).append(" ");
                cur = prev.get(cur);
            }
            if (output.length() == 0) {
                System.out.println("IMPOSSIBLE");
            } else {
                System.out.println(output.substring(0, output.length() - 1));
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

    static long readLong() throws IOException {
        return Long.parseLong(next());
    }
}
