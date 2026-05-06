package org.example;

public class SAVE10Discount implements DiscountStrategy {

    public double apply(double amount) {
        return amount * 0.9;
    }
}