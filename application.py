# This function is used to display the product details nicely
# It takes in a list called data
def display(data: list) -> None:
    print("Product details:")
    print(f"\tID: {data[0]}")   # printing the product ID
    print(f"\tName: {data[1]}")  # printing the product name
    
    # If the length is 7, that means it is a Book (because books have extra info)
    if len(data) == 7:
        print(f"\tAuthor: {data[5]}")  # printing the author of the book
    
    print(f"\tCost price: {data[2]}")  # printing cost price
    print(f"\tRetail price: {data[3]}")  # printing retail price
    print(f"\tQuantity in stock: {data[4]}")  # printing quantity available
    
    # If it is a book, print genres also
    if len(data) == 7:
        print(f"\tGenre(s): {data[6]}")


# I am using this variable to count how many times the user enters wrong filename
attempts = 0

# This loop allows the user to try 5 times
while attempts < 5:
    try:
        # Asking the user to enter the file name
        filename = input("Please enter the inventory filename: ")

        # Trying to open the file
        with open(filename, "r") as file_handle:

            # Looping through each line in the file
            for line in file_handle:
                try:
                    # Removing any extra spaces or new line characters
                    line = line.strip()
                    
                    # Splitting the line using %% because that is the format in the file
                    components = line.split("%%")

                    # Creating a list to store the product details
                    data = []
                    
                    # Adding the correct values from the file into the list
                    data.append(components[1])  # ID
                    data.append(components[2])  # Name
                    data.append(float(components[3]))  # Cost price (converted to float)
                    data.append(float(components[4]))  # Retail price (converted to float)
                    data.append(int(components[5]))  # Quantity (converted to int)

                    # If the product type is Book, add author and genres
                    if components[0] == "Book":
                        data.append(components[6])  # Author
                        genres = components[7].split("&&")  # Splitting genres
                        data.append(genres)

                    # Displaying the product details
                    display(data)

                # If there is a problem converting numbers (like text instead of number)
                except ValueError:
                    print("Warning: Number error in this line. Skipping.")

                # If the line does not have enough values
                except IndexError:
                    print("Warning: Incorrect format in this line. Skipping.")

        # If file opens successfully, break out of the loop
        break

    # If the filename entered does not exist
    except FileNotFoundError:
        attempts += 1  # Increase attempt count
        print("File not found. Try again.")

# If user fails 5 times, close program
if attempts == 5:
    print("Too many wrong attempts. Program closing.")