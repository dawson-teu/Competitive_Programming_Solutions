import java.util.*;

public class Frog1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] h = new int[n];
        for (int i = 0; i < n; i++) {
            h[i] = input.nextInt();
        }

        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = Integer.MAX_VALUE;
        }
        dp[0] = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 1; j < 3; j++) {
                if (j + i < n) {
                    dp[j + i] = Math.min(dp[j + i], dp[i] + Math.abs(h[j + i] - h[i]));
                }
            }
        }
        System.out.println(dp[n - 1]);
    }
}

