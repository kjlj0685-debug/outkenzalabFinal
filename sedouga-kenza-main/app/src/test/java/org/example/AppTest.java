
package org.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class AppTest {

    // 1. حالة عادية (بدون خصم)
    @Test
    void regularCustomerNoDiscount() {
        double result = App.calculate(
                new double[]{100, 50},
                new int[]{1, 1},
                "REGULAR",
                "NONE"
        );

        // 150 + 15% tax = 172.5
        assertEquals(172.5, result, 0.01);
    }

    // 2. VIP discount فقط
    @Test
    void vipCustomerDiscountOnly() {
        double result = App.calculate(
                new double[]{100, 100},
                new int[]{1, 1},
                "VIP",
                "NONE"
        );

        // 200 → 20% discount = 160 → tax = 184
        assertEquals(184.0, result, 0.01);
    }

    // 3. كود خصم فقط SAVE10
    @Test
    void save10Only() {
        double result = App.calculate(
                new double[]{200},
                new int[]{1},
                "REGULAR",
                "SAVE10"
        );

        // 200 → 10% = 180 → tax = 207
        assertEquals(207.0, result, 0.01);
    }

    // 4. VIP + SAVE10 معًا (أقوى test مهم جدًا)
    @Test
    void vipAndSave10Combined() {
        double result = App.calculate(
                new double[]{100},
                new int[]{1},
                "VIP",
                "SAVE10"
        );

        // 100 → VIP 80 → SAVE10 72 → tax = 82.8
        assertEquals(82.8, result, 0.01);
    }

    // 5. حالة متعددة المنتجات
    @Test
    void multipleItemsTest() {
        double result = App.calculate(
                new double[]{50, 50, 100},
                new int[]{1, 2, 1},
                "REGULAR",
                "NONE"
        );

        // subtotal = 50 + 100 + 100 = 250
        // tax = 287.5
        assertEquals(287.5, result, 0.01);
    }
}