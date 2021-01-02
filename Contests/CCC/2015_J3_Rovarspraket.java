import java.util.Scanner;

class Question2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String s = input.nextLine();
        s = s.toLowerCase();
        input.close();

        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String vowels = "aeiou";
        StringBuilder consonants = new StringBuilder();
        for (char character : alphabet.toCharArray()) {
            if (vowels.indexOf(character) == -1) {
                consonants.append(character);
            }
        }

        StringBuilder output = new StringBuilder();
        for (char character : s.toCharArray()) {
            if (consonants.toString().indexOf(character) > -1) {
                output.append(character);

                int[] distance = new int[5];
                for (int i = 0; i < 5; i++) {
                    distance[i] = Math.abs(alphabet.indexOf(vowels.charAt(i)) - alphabet.indexOf(character));
                }
                int[] min = {0, 27};
                for (int i = 0; i < 5; i++) {
                    if (distance[i] < min[1]) {
                        min[1] = distance[i];
                        min[0] = i;
                    }
                }
                output.append(vowels.charAt(min[0]));

                if (character == 'z') {
                    output.append(character);
                } else {
                    output.append(consonants.charAt(consonants.toString().indexOf(character) + 1));
                }
            } else {
                output.append(character);
            }
        }
        System.out.println(output);
    }
}
