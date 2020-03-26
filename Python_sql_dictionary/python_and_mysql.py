import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word=input("Enter the word: ")
count = 0
while True:
    query = cursor.execute(f"SELECT Definition FROM Dictionary WHERE Expression = '{word}'")
    results = cursor.fetchall()
    if results or count == 3:
        break
    elif count == 0:
        word = word.lower()
    elif count == 1:
        word = word.title()
    elif count == 2:
        word = word.upper()
    count += 1

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")