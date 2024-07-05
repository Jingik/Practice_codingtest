import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] words = new String[5];

        // 다섯 줄의 입력 받기
        for (int i = 0; i < 5; i++) {
            words[i] = scanner.nextLine().trim();
        }

        // 결과를 저장할 StringBuilder
        StringBuilder result = new StringBuilder();

        // 가장 긴 단어의 길이 찾기
        int maxLength = 0;
        for (String word : words) {
            if (word.length() > maxLength) {
                maxLength = word.length();
            }
        }

        // 세로로 읽기
        for (int i = 0; i < maxLength; i++) {
            for (String word : words) {
                if (i < word.length()) {
                    result.append(word.charAt(i));
                }
            }
        }

        // 결과 출력
        System.out.println(result.toString());

        scanner.close();
    }
}
