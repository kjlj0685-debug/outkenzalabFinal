# 💰 Pricing & Discount Engine

## 📌 Overview
This project is a **Java-based Pricing Engine** built using **Gradle** and tested with **JUnit 5**.

It simulates a real-world e-commerce pricing system that calculates the final order price by applying:
- Item pricing
- Quantity handling
- Customer-based discounts (VIP)
- Coupon discounts (SAVE10)
- Tax calculation

The project focuses on:
- Clean Code principles
- Refactoring techniques
- Unit testing
- Design patterns (Strategy Pattern)
- Git workflow best practices

---

## ⚙️ Features

- 🧾 Calculate subtotal from multiple items
- 👤 Apply customer-based discount (VIP)
- 🎟️ Apply coupon discount (SAVE10)
- 🧮 Apply tax calculation (15%)
- 🧩 Strategy Pattern for flexible discount system
- 🧪 Unit testing with JUnit 5

---

## 🏗️ Architecture

The system is structured into modular components:

### Core Components:
- `App.java` → Main pricing engine
- `DiscountStrategy` → Interface for discount rules
- `VIPDiscount` → VIP discount implementation
- `SAVE10Discount` → Coupon discount implementation
- `TaxService` → Handles tax calculation

### Design Pattern Used:
✔ Strategy Pattern  
Used to separate discount logic into independent classes, making the system:
- Flexible
- Extensible
- Easy to maintain

---

## 🧪 Testing Strategy

Unit tests are implemented using **JUnit 5**.

### Covered scenarios:
- Regular customer without discounts
- VIP discount only
- Coupon discount only
- Combined discounts (VIP + SAVE10)
- Multiple items calculation

# 🚀 Discount Calculation System (Java + Gradle)

A clean and modular Java project demonstrating **Design Patterns**, **Refactoring**, and **Unit Testing**.

---

## 🔧 Build & Run

### Run tests

```bash
./gradlew test
```

### Build project

```bash
./gradlew build
```

---

## 🧠 Refactoring Highlights

This project was improved through iterative refactoring:

* Separated business logic into services
* Implemented **Strategy Pattern** for discounts
* Improved code readability and maintainability
* Fixed combined discount calculation logic
* Reduced code duplication

---

## 📊 Example Calculation

**Input:**

* Items: 100 + 50
* Quantities: 1 + 2
* Customer Type: VIP
* Coupon: SAVE10

**Process:**

* Subtotal = 200
* VIP discount (20%) → 160
* SAVE10 discount (10%) → 144
* Tax (15%) → 165.6

**Output:**

```
165.6
```

---

## 📁 Project Structure

```
app/
 └── src/
     ├── main/java/org/example/
     │   ├── App.java
     │   ├── DiscountStrategy.java
     │   ├── VIPDiscount.java
     │   ├── SAVE10Discount.java
     │   ├── TaxService.java
     │   └── DiscountService.java
     └── test/java/org/example/
         └── AppTest.java
```

---

## 🔄 Git Workflow

* `feat:` Add initial test cases
* `refactor:` Apply Strategy Pattern
* `test:` Add comprehensive unit tests
* `refactor:` Improve structure and separation of concerns

---

## 🎯 Key Learning Outcomes

* Gradle build system
* Unit testing with JUnit 5
* Clean Code principles
* Design Patterns (Strategy Pattern)
* Refactoring techniques
* Git workflow best practices

---

## 📌 Author

**Kenza Sedouga**
Master IoT Student

---

## 🏁 Project Status

✔ Completed
✔ Tests Passing
✔ Refactored Architecture
✔ Ready for Submission
