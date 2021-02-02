package com.competitive.Lecture3;

import java.util.Scanner;

public class SimpleInterestMethod {

    public static double interest() {

        Scanner myObj = new Scanner(System.in); // creating an object that helps receive the input

        System.out.println("Enter Principal Amount: ");
        int p = myObj.nextInt(); // uses the object created earlier and then stores the input in ref
        System.out.println("Enter Rate: ");
        int r = myObj.nextInt();
        System.out.println("Enter Time in years: ");
        int t = myObj.nextInt();

        double si = (p * r * t) / 100.0;
        return si;
    }

    public static void main(String[] args) {

    }
}
