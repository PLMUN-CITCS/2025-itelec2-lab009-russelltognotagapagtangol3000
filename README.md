# 2025-ITELEC2-LAB009
Week 04 - Conditional Statements

Laboratory # 09 - Guided Coding Exercise: if...else Statement in Python

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 09 - Guided Coding Exercise: if...else Statement in Python**

   **Objective:**
   - Learn how to handle binary decisions using if...else.
   - Understand how the else block executes when the if condition is false.
   - Practice using the modulus operator (%) for determining even and odd numbers.
   - Reinforce input handling and type conversion.

   **Desired Output (Example 1):**
   ```bash
   Enter a number: 10
   The number 10 is Even.
   
   ```

   **Desired Output (Example 1):**
   ```bash
   Enter a number: 7
   The number 7 is Odd.
   
   ```
      
   **Notable Observations (to be discussed after completing the exercise):**
   - The if block executes only when the condition is True.
   - The else block executes only when the condition is False.
   - The modulus operator (%) returns the remainder of a division. If a number is divisible by 2 (remainder is 0), it's even; otherwise, it's odd.
   - if...else provides a way to handle two mutually exclusive cases.

   **Python Best Practices**
   - Input Validation (Recommended): While not explicitly in the original prompt, it's good practice to validate user input. You could use a try-except block to handle cases where the user enters something that's not an integer. This prevents your program from crashing.
   - Descriptive Messages: Use clear and descriptive messages in your print() statements to guide the user and explain the output.
   - Clear Variable Names: Use meaningful variable names (e.g., number instead of n).
   - Comments: Add comments to explain your logic, especially for more complex conditions.
   - Consistent Indentation: Maintain consistent indentation (4 spaces per level is standard).
   - Test Thoroughly: Test your code with different inputs (even and odd numbers, positive and negative numbers, and potentially non-integer inputs if you include validation) to ensure it works correctly in all cases.

   **Step-by-Step Instructions:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `if_else_statement.py`
      
   2.  Get input from the user:
      - Use the input() function to prompt the user to enter a number. Store the returned string in a variable.
```python
user_input = input("Enter a number: ")
```
      
   3.  Convert input to an integer:
      - Convert the input string to an integer using the int() function. Store the result in a variable named number.
```python
number = int(user_input)
```

   4. Check if the number is even or odd (using if...else):
      - Use an if statement to check if the number is even. The condition should use the modulus operator (%) to check if the remainder when dividing by 2 is 0.
      - If the condition is true (even), print a message indicating that the number is even.
      - Use an else block to handle the case where the condition is false (odd). Print a message indicating that the number is odd.
```python
if number % 2 == 0:
    print("The number", number, "is Even.")
else:
    print("The number", number, "is Odd.")
```

   5. Complete Code: Combine the steps above to form the complete program.
   6. Run the code: Execute your Python code.
   7. Observe the output: Enter different numbers (even and odd) and observe the output.
   8. (Optional) Input Validation:  Add a try-except block to handle potential ValueError if the user enters non-integer input.
```python
try:
    #code here
except ValueError:
    print("Invalid input. Please enter an integer.")
```

   **Conclusion**
   This exercise demonstrated the use of the if...else statement to handle binary decisions. You learned how the else block provides an alternative execution path when the if condition is false. You also practiced using the modulus operator for determining even and odd numbers and (optionally) improved the program's robustness by adding input validation. The if...else statement is a fundamental control flow structure that allows your programs to make choices and handle different scenarios.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
```bash
git status
```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
```bash
git add .
```
   
3. Commit your changes:
   Write a meaningful commit message:
   
```bash
git commit -m "Submitting Python Week 04 - Laboratory # 09"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
