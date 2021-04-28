import java.util.*;

public class Jan_B2_Photoshoot {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] b_num = new int[n + 1];
        for (int i = 1; i < n; i++) {
            b_num[i] = input.nextInt();
        }

        int[] a_num = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            boolean[] visited = new boolean[1001];
            boolean numCorrect = true;
            a_num[i] = 1;
            visited[1] = true;
            for (int j = i - 1; j > 0; j--) {
                a_num[j] = b_num[j] - a_num[j + 1];
                if (a_num[j] < 1 || a_num[j] > n || visited[a_num[j]]) {
                    numCorrect = false;
                    break;
                }
                visited[a_num[j]] = true;
            }
            for (int j = i + 1; j < n + 1 && numCorrect; j++) {
                a_num[j] = b_num[j - 1] - a_num[j - 1];
                if (a_num[j] < 1 || a_num[j] > n || visited[a_num[j]]) {
                    numCorrect = false;
                    break;
                }
                visited[a_num[j]] = true;
            }
            if (numCorrect) {
                StringBuilder output = new StringBuilder();
                for (int j = 1; j < n + 1; j++) {
                    output.append(a_num[j]).append(" ");
                }
                System.out.println(output);
                break;
            }
        }
    }
}
