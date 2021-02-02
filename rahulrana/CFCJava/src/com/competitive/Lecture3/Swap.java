package com.competitive.Lecture3;

public class Swap {

    public static void swap(int x, int y) {
        int temp = x;
        x = y;
        y = temp;
    }
    public static void main(String[] args) {

        int x = 10;
        int y = 20;
        swap(x, y);
        System.out.println(x + "" +  y);
        // there is NO pass be address in Java
        // there are NO pointers in Java
        // Thus, if you want to have a change from the function show up in the code,
        // you need to have something to receive it outside of the function called
        // i.e, to store the value in another/or same variable
    }
}
