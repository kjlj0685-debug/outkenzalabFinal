package org.example;

public class VIPDiscount implements DiscountStrategy {

    public double apply(double amount) {
        return amount * 0.8;
    }
}