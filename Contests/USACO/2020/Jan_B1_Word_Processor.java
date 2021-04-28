import java.util.*;

public class Jan_B1_Word_Processor {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt(), k = input.nextInt();
        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = input.next();
        }
        input.close();

        List<List<String>> essay = new ArrayList<>();
        essay.add(new ArrayList<>());
        for (int i = 0; i < n; i++) {
            int lastIndex = essay.size() - 1;
            List<String> lastSentence = essay.get(lastIndex);
            if (strLength(lastSentence) + words[i].length() > k) {
                List<String> newSentence = new ArrayList<>();
                newSentence.add(words[i]);
                essay.add(newSentence);
            } else {
                essay.get(lastIndex).add(words[i]);
            }
        }

        for (List<String> sentence : essay) {
            System.out.println(String.join(" ", sentence));
        }
    }

    public static int strLength(List<String> strings) {
        int total = 0;
        for (String str : strings) {
            total += str.length();
        }
        return total;
    }
}
