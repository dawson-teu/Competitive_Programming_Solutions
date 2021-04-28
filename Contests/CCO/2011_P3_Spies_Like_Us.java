import java.util.*;

public class P3_Spies_Like_Us {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();
        int k = input.nextInt();
        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            adjList.add(new ArrayList<>());
        }
        boolean[][] commonContact = new boolean[n][n];
        for (int i = 0; i < k; i++) {
            int a = input.nextInt();
            int b = input.nextInt();
            for (int j : adjList.get(b - 1)) {
                if (!commonContact[a - 1][j - 1]) {
                    commonContact[a - 1][j - 1] = true;
                    commonContact[j - 1][a - 1] = true;
                } else {
                    System.out.println("NO");
                    return;
                }
            }
            adjList.get(b - 1).add(a);
        }
        System.out.println("YES");
    }
}
