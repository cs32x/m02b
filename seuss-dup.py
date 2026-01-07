# Open the book
my_open_book = open('CatInTheHat.txt')

# Open the book again, which creates a duplicate object
the_same_book = open('CatInTheHat.txt')

# Read the first line
the_line = my_open_book.readline()
print(the_line, end='')

# Reads which line?
the_line = the_same_book.readline()
print(the_line, end='')