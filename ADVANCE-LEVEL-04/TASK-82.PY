'''
Question 82
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

Hints: Use zlib.compress() and zlib.decompress() to compress and decompress a string.
'''


#zlib is a software library used for data compression and decompression. It provides a way to compress data 
# into a smaller size and decompress it back into its original form. It's widely used in various programming languages, 
# including Python, due to its efficiency and reliability.


import zlib as z

#it only takes data in bytes 
# i added b before the string that converts it into bytes 
string =  b"hello world!hello world!hello world!hello world!"



compressed_data = z.compress(string)


print(compressed_data)

decompressed_data = z.decompress(compressed_data)


print(decompressed_data)