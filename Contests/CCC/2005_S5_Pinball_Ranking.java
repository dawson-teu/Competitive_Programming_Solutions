import java.util.Collections;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Question1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();
        int[] scores = new int[t];
        for (int i = 0; i < t; i++) {
            scores[i] = input.nextInt();
        }
        input.close();

        List<Integer> ranking = new ArrayList<>();
        float total = 0;
        for (int i = 0; i < t; i++) {
            ranking.add(scores[i]);
            Collections.sort(ranking);
            Collections.reverse(ranking);
            total += ranking.indexOf(scores[i]) + 1;
        }
        System.out.format("%.2f", total / t);
    }
}
