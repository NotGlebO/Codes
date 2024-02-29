public class Main {
    public static void print(int[] a, int i) {
        if (i < a.length) {
            System.out.print(a[i] + " ");
            print(a, i+ 1);
        }
    }
    public static void main(String[] args) {
        int[] a = {1,2,3,4,5,6,7};
        print(a, 0);
    }
}
