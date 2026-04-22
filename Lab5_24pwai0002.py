# AI PASSWORD CHECKER
max_attempts = 5
attempt = 0

while attempt < max_attempts:
    attempt += 1
#Step 1: User Input 
    password = input("Enter your password: ")
    
# ste2 --> # password strength
    score = 0 
    
    if len(password) >= 8: # 1. length of 8 character
        score+=1
        
    #2. must contain at least one digit(0-9)
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        score += 1
        
    #3. must contain at least one capital letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if has_upper:
        score += 1
        
#Step 3: Give Feedback
#Step 4: Attempts Rule 
    if score == 0:
        strength = "very weak"
    
    elif score == 1:
        strength = "weak"
        
    elif score == 2:
        strength = "moderate"
        
    else: 
        strength = "strong"
        
    remaining = max_attempts  - attempt
    print(f"password strength : {strength}")
    print(f"Attempts remaining: {remaining}")
    
    
# Step 5: Winning Condition
    
    if score == 3:
        print(f"You created a strong password! ")
        break
#Step 6: Losing Condition 
    else:
        print(f"Final Result: Password is not strong enough.")
