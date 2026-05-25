#  Security Vault Password Checker

A sleek, lightweight desktop security tool built using Python and Tkinter. This application provides real-time cryptographic strength assessment of user-entered passwords, wrapped in a high-contrast dark charcoal UI with custom electric orange accents.

## ✨ Key Features
* **Real-Time Assessment**: Dynamically evaluates your password security layer as you type.
* **Green Match Indicators**: Individual security parameters turn vivid green with a solid bullet point (`●`) the exact moment they are successfully satisfied.
* **Dynamic Metric Bar**: An animated horizontal progress bar that changes size and shifts colors depending on your overall password threat assessment level.
* **Privacy Controls**: Features a built-in eye symbol toggle button (`👁` / `⚡` / `👁‍🗨`) to instantly obscure or reveal sensitive text inputs.
* **Zero External Dependencies**: Developed entirely inside Python's native core standard libraries (`tkinter` and `re`). No heavy external downloads required.

## 📊 Evaluation Metrics & Tiers

The app checks for 5 essential parameters:
1. **Length Check**: Verifies if the password contains 12+ total characters.
2. **Case Verification**: Checks for uppercase characters (`A-Z`).
3. **Case Verification**: Checks for lowercase characters (`a-z`).
4. **Numeric Indexing**: Checks for numeric integer digits (`0-9`).
5. **Special Characters**: Searches for secure symbols (`!@#$%^&*` etc.).

### System Status Classifications
* **CRITICAL SECURITY RISK** (🔴 Red) — Less than 3 rules met.
* **STANDARD SECURITY** (🟠 Orange) — 3 or 4 rules met.
* **ULTRA ADVANCE PASSWORD STRENGTH** (🟢 Green) — All 5 rules successfully achieved.

## 🚀 How to Run the App

### 1. Prerequisites
Ensure you have Python 3 installed on your Mac or system environment. You can check your version in your terminal using:
```bash
python3 --version
```

### 2. Execution Steps
1. Save your code into a file named `Password_checker.py`.
2. Open your desktop terminal, change directories into your project folder, and run:
```bash
python3 Password_checker.py
```
