import morse

phrase = "1234567890 The quick red fox jumped over the lazy dog."
encoded = morse.encode(phrase)
print (encoded)
decoded = morse.decode(encoded)
print (decoded)