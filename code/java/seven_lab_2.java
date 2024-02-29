// import java.util.Scanner;

// class seven_lab_2 {
//   public static void main(String[] args) {
//     Scanner sc = new Scanner(System.in);
//     System.out.print("x=");
//     double x = sc.nextDouble();
//     sc.close();
//     if (x < -0.7 || x > 0.7) {
//       System.out.println("error");
//       return;
//     }

//     double log_result = Math.log((1+x)/(1-x));
//     double result = 0; 

//     for(double c = 1; c != 17.0; c+=2){
        
//         result += ((2*Math.pow((x), c))/c);

        
//     }
//     String formattedResult = String.format("summa=%.4f", result); 
//     String formattedCos = String.format("x=function=%.4f%n", log_result); 

//     System.out.print(formattedCos);
//     System.out.print(formattedResult);

//   }
// }


import java.util.Scanner;

class seven_lab_2 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("x=");
    double x = sc.nextDouble();
    sc.close();
    if (x < -0.7 || x > 0.7) {
      System.out.println("error");
      return;
    }

    double a = 2;  // TODO: piešķirt mainīgam a sākumvērtību
    int i = 1;     // TODO: piešķirt mainīgam i sākumvērtību
    double s = 0;  // TODO: piešķirt mainīgam s sākumvērtību

    while (Math.abs(a) > 0.001) {
      s += a*x/i;  // TODO: pieskaitīt a pie rindas summas s

      a *= x*x;  // TODO: aprēķināt nākošo rindas elementu un piešķirt mainīgam a

      i += 2;  // TODO: izmainīt cikla parametru i

    }
    System.out.printf("function=%.4f%n", Math.log((1+x)/(1-x)));
    System.out.printf("summa=%.4f", s);
  }
}