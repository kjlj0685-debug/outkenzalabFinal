package org.example;

public class App {

    public static double calculate(double[] prices, int[] qty, String type, String code) {

        double subtotal = 0;

        for (int i = 0; i < prices.length; i++) {
            subtotal += prices[i] * qty[i];
        }

        // 1. VIP discount
        if (type.equals("VIP")) {
            subtotal = subtotal * 0.8;
        }

        // 2. SAVE10 discount (بعد VIP)
        if (code.equals("SAVE10")) {
            subtotal = subtotal * 0.9;
        }

        // tax
        double tax = subtotal * 0.15;

        return subtotal + tax;
    }
}