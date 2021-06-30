import java.util.*;
import java.io.*;

public class Subarray_Search {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        long mod = (int) 1e9 + 7;
        int n = readInt(), f = readInt();
        long s = readLong();
        int[] nums = new int[n];
        int maxNum = -1;
        for (int i = 0; i < n; i++) {
            nums[i] = readInt();
            maxNum = Math.max(maxNum, nums[i]);
        }
        int left = 0;
        int right = 0;
        int total = nums[0];
        long greatCount = 0;
        while (right < n) {
            if (total <= s) {
                greatCount += right - left + 1;
                greatCount %= mod;
                right += 1;
                if (right < n) {
                    total += nums[right];
                }
            } else {
                total -= nums[left];
                left += 1;
            }
        }
        left = 0;
        right = 0;
        long goodCount = 0;
        int[] freq = new int[maxNum + 1];
        freq[nums[0]] += 1;
        int maxFreq = 1;
        int maxFreqCount = 1;
        while (right < n) {
            if (maxFreq <= f) {
                goodCount += right - left + 1;
                goodCount %= mod;
                right += 1;
                if (right < n) {
                    freq[nums[right]] += 1;
                    if (freq[nums[right]] > maxFreq) {
                        maxFreq = freq[nums[right]];
                        maxFreqCount = 1;
                    } else if (freq[nums[right]] == maxFreq) {
                        maxFreqCount += 1;
                    }
                }
            } else {
                if (freq[nums[left]] == maxFreq) {
                    maxFreqCount -= 1;
                }
                freq[nums[left]] -= 1;
                if (maxFreqCount == 0) {
                    maxFreq = freq[nums[left]];
                    maxFreqCount = 1;
                }
                left += 1;
            }
        }
        left = 0;
        right = 0;
        long greatGoodCount = 0;
        total = nums[0];
        freq = new int[maxNum + 1];
        freq[nums[0]] += 1;
        maxFreq = 1;
        maxFreqCount = 1;
        while (right < n) {
            if (total <= s && maxFreq <= f) {
                greatGoodCount += right - left + 1;
                greatGoodCount %= mod;
                right += 1;
                if (right < n) {
                    total += nums[right];
                    freq[nums[right]] += 1;
                    if (freq[nums[right]] > maxFreq) {
                        maxFreq = freq[nums[right]];
                        maxFreqCount = 1;
                    } else if (freq[nums[right]] == maxFreq) {
                        maxFreqCount += 1;
                    }
                }
            } else {
                if (freq[nums[left]] == maxFreq) {
                    maxFreqCount -= 1;
                }
                freq[nums[left]] -= 1;
                if (maxFreqCount == 0) {
                    maxFreq = freq[nums[left]];
                    maxFreqCount = 1;
                }
                total -= nums[left];
                left += 1;
            }
        }
        System.out.println((((goodCount * greatCount) % mod) * greatGoodCount) % mod);
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
