
# We will read content from the file and then we will print it
with open('test_files/file_for_reading.txt') as fr:
    file_contents = fr.read()

print("File contents are", file_contents)

# Now we will write some random number

import random

with open('test_files/file_for_writing.txt', 'w') as fw:
    fw.write(random.randint(1,10))