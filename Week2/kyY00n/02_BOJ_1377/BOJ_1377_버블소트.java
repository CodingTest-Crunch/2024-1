import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_1377_버블소트 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        Element[] array = new Element[N];
        for (int i = 0; i < N; i++) {
            array[i] = new Element(i, Integer.parseInt(br.readLine()));
        }

        Element[] copyOf = Arrays.copyOf(array, N);
        Arrays.sort(copyOf);

        int max = 0;
        for(int i = 0; i < N; i++) {
            int originalIndex = copyOf[i].getIndex();
            max = Math.max(max, originalIndex - i);
        }

        System.out.println(max + 1);
    }

}

class Element implements Comparable {
    private int index;
    private int value;

    public Element(final int index, final int value) {
        this.index = index;
        this.value = value;
    }

    @Override
    public int compareTo(final Object o) {
        Element other = (Element) o;
        return this.value - other.value;
    }

    public int getIndex() {
        return index;
    }

    public int getValue() {
        return value;
    }

}
