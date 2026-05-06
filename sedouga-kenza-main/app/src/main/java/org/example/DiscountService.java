package org.example;

public class DiscountService {

    public double apply(double amount, String customerType, String code) {

        if (customerType.equals("VIP")) {
            amount *= 0.8;
        }

        if (code.equals("SAVE10")) {
            amount *= 0.9;
        }

        return amount;
    }
}