import sqlite3

# Establishing a connection to the SQLite database
db = sqlite3.connect('ebookstore.db')
c = db.cursor()

# Creating the books table with the required fields
c.execute("""
CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    qty INTEGER
)
""")

# Inserting the sample data into the books table
books_data = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
]

c.executemany('INSERT INTO book(id, title, author, qty) VALUES(?,?,?,?)', books_data)

# Committing the changes to the database
db.commit()

def enter_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter book quantity: "))
    
    c.execute("INSERT INTO book (title, author, qty) VALUES (?, ?, ?)", (title, author, qty))
    db.commit()
    print("Book added successfully!")

# Function to update book information
def update_book():
    book_id = int(input("Enter the book ID to update: "))
    new_quantity = int(input("Enter the new quantity: "))
    
    c.execute("UPDATE book SET qty = ? WHERE id = ?", (new_quantity, book_id))
    db.commit()
    print("Book information updated!")

# Function to delete a book from the database
def delete_book():
    book_id = int(input("Enter the book ID to delete: "))
    
    c.execute("DELETE FROM book WHERE id = ?", (book_id,))
    db.commit()
    print("Book deleted from the database!")

# Function to search for a specific book
def search_book():
    search_title = input("Enter book title to search: ")
    
    c.execute("SELECT * FROM book WHERE title LIKE ?", ('%' + search_title + '%',))
    books = c.fetchall()
    
    if not books:
        print("No matching books found.")
    else:
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Qty: {book[3]}")
while True:
    print("\nMenu:")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search book")
    print("0. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        enter_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        search_book()
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")

# Closing the database connection and the cursor
db.close()
c.close()

