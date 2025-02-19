# Filename: nested_for_loop_multiplication_table.py

# Step 1: Outer loop for rows (1 to 5)
for i in range(1, 6):
    
    # Step 2: Inner loop for columns (1 to 5)
    for j in range(1, 6):
        
        # Step 3: Calculate the product
        product = i * j
        
        # Step 4: Print the product with formatting
        print(f"{product:4}", end="")  # {product:4} ensures 4 spaces between numbers
    
    # Step 5: New line after each row
    print()  # Moves the cursor to the next line
