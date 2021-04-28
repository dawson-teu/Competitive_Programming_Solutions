import java.util.Scanner;

class S2_Poetry {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        input.nextLine();
        String[] lines = new String[n * 4];
        for (int i = 0; i < n * 4; i++) {
            lines[i] = input.nextLine();
        }
        input.close();

        String[][] verses = new String[n][4];
        for (int i = 0; i < n; i++) {
            System.arraycopy(lines, i * 4, verses[i], 0, 4);
        }

        for (String[] verse : verses) {
            if (isPerfect(verse)) {
                System.out.println("perfect");
            } else if (isEven(verse)) {
                System.out.println("even");
            } else if (isCross(verse)) {
                System.out.println("cross");
            } else if (isShell(verse)) {
                System.out.println("shell");
            } else {
                System.out.println("free");
            }
        }
    }

    private static boolean isPerfect(String[] verse) {
        String[] lastWords = lastWords(verse);
        boolean first = isRhyme(lastWords[0], lastWords[1]) && isRhyme(lastWords[0], lastWords[2])
                && isRhyme(lastWords[0], lastWords[3]);
        boolean second = isRhyme(lastWords[1], lastWords[2]) && isRhyme(lastWords[1], lastWords[3]);
        boolean third = isRhyme(lastWords[2], lastWords[3]);
        return first && second && third;
    }

    private static boolean isEven(String[] verse) {
        String[] lastWords = lastWords(verse);
        return isRhyme(lastWords[0], lastWords[1]) && isRhyme(lastWords[2], lastWords[3]);
    }

    private static boolean isCross(String[] verse) {
        String[] lastWords = lastWords(verse);
        return isRhyme(lastWords[0], lastWords[2]) && isRhyme(lastWords[1], lastWords[3]);
    }

    private static boolean isShell(String[] verse) {
        String[] lastWords = lastWords(verse);
        return isRhyme(lastWords[0], lastWords[3]) && isRhyme(lastWords[1], lastWords[2]);
    }

    private static String[] lastWords(String[] verse) {
        String[] lastWords = new String[verse.length];
        for (int i = 0; i < verse.length; i++) {
            String[] words = verse[i].split(" ");
            lastWords[i] = words[words.length - 1];
        }
        return lastWords;
    }

    private static boolean isRhyme(String word1, String word2) {
        return lastSyllable(word1).equals(lastSyllable(word2));
    }

    private static String lastSyllable(String word) {
        String[] vowels = { "a", "e", "i", "o", "u" };
        int lastVowel = -1;
        for (int i = 0; i < word.length(); i++) {
            if (contains(vowels, String.valueOf(word.charAt(i)).toLowerCase())) {
                lastVowel = i;
            }
        }
        if (lastVowel == -1) {
            return word.toLowerCase();
        } else {
            return word.substring(lastVowel).toLowerCase();
        }
    }

    private static boolean contains(String[] array, String element) {
        for (String elem : array) {
            if (elem.equals((element))) {
                return true;
            }
        }
        return false;
    }
}
