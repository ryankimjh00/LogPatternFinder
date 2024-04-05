import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    private static final String PATTERN = "\\[.*?\\] \\[.*?\\]  \\[(\\w*-+.*?)\\]";

    public static void main(String[] args) {
        String inputFilePath = "./test.log";
        String outputFilePath = "./extracted_data11.txt";
        processFile(inputFilePath, outputFilePath);
        String longestPattern = findLongestRepeatingPattern(outputFilePath);
        System.out.println(longestPattern);
    }

    private static void processFile(String inputFilePath, String outputFilePath) {
        try (BufferedReader reader = new BufferedReader(new FileReader(inputFilePath));
             BufferedWriter writer = new BufferedWriter(new FileWriter(outputFilePath))) {
            while (true) {
                ArrayList<String> extractedData = new ArrayList<>();
                for (int i = 0; i < 1000; i++) {
                    String line = reader.readLine();
                    if (line == null) {
                        break;
                    }
                    ArrayList<String> extractedLines = processLines(line);
                    extractedData.addAll(extractedLines);
                }
                if (extractedData.isEmpty()) {
                    break;
                }
                for (String data : extractedData) {
                    writer.write(data + " \n");
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static ArrayList<String> processLines(String line) {
        ArrayList<String> extractedData = new ArrayList<>();
        Pattern pattern = Pattern.compile(PATTERN);
        Matcher matcher = pattern.matcher(line);
        while (matcher.find()) {
            extractedData.add(matcher.group(1));
        }
        return extractedData;
    }
    private static int[] suffixArray(String string) {
        int n = string.length();
        int[] suffixArr = new int[n];
        for (int i = 0; i < n; i++) {
            suffixArr[i] = i;
        }
        Arrays.sort(suffixArr, (a, b) -> string.substring(a).compareTo(string.substring(b)));
        return suffixArr;
    }

    private static int[] lcpArray(String string, int[] suffixArr) {
        int n = string.length();
        int[] lcpArr = new int[n];
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) {
            rank[suffixArr[i]] = i;
        }
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (rank[i] == n - 1) {
                k = 0;
                continue;
            }
            int j = suffixArr[rank[i] + 1];
            while (i + k < n && j + k < n && string.charAt(i + k) == string.charAt(j + k)) {
                k++;
            }
            lcpArr[rank[i]] = k;
            if (k > 0) {
                k--;
            }
        }
        return lcpArr;
    }

    private static String findLongestRepeatingPattern(String string) {
        int[] suffixArr = suffixArray(string);
        int[] lcpArr = lcpArray(string, suffixArr);
        int maxLength = Arrays.stream(lcpArr).max().getAsInt();
        if (maxLength == 0) {
            return "";
        } else {
            int idx = 0;
            for (int i = 0; i < lcpArr.length; i++) {
                if (lcpArr[i] == maxLength) {
                    idx = i;
                    break;
                }
            }
            return string.substring(suffixArr[idx], suffixArr[idx] + maxLength);
        }
    }
}
