package Lecture2;

import java.util.Scanner; // variables, packages start with small, classes with capitals

public class LeapYear {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in); // System.in means we take input from console
        // s is the object of Scanner class (Scanner can take input from a LOT of sources)
        int year = s.nextInt();
//            System.out.println(year);
        if (year % 4 == 0) {
            System.out.println("Leap Year!");
        } else {
            System.out.println("Not a Leap Year!");
        }
    }
}