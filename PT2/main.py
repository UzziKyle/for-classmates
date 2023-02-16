userID = input("Enter User ID: ")
userName = input("Enter Username: ")

print("\n||Customer - 1|\t|Merchandiser - 0||")
modNum = int(input("Enter module number: "))

if modNum == 0:
    import module2

elif modNum == 1:
    import module1