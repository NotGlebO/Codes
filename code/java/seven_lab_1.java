import java.util.Scanner;

class seven_lab_1 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("x=");
    double x = sc.nextDouble();
    sc.close();
    if (x < 0.1 || x > 1.5) {
      System.out.println("error");
      return;
    }

    double s = 0;  // TODO: piešķirt mainīgam s sākumvērtību
    double a = 4 * x * x;  // TODO: piešķirt mainīgam a sākumvērtību
    int i = 0;     // TODO: piešķirt mainīgam i sākumvērtību
    double factorial = 1;

    while (Math.abs(a) > 0.001) {
      factorial *= ((i+1)*(i+2));
      a = -1 * a*x*x*4/factorial;  // TODO: aprēķināt nākošo rindas elementu un piešķirt mainīgam a
      s += a;  // TODO: pieskaitīt a pie rindas summas s
      i += 2;  // TODO: izmainīt cikla parametru i
    }
    System.out.printf("function=%.4f%n", 2*(Math.cos(x)*Math.cos(x)-1));
    System.out.printf("summa=%.4f", s);
  }
}