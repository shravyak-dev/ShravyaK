# Reading a File ("r" mode)
file = open("C:\\Users\\User\\Documents\\Details.txt","r")
content=file.read()
print(content)
file.close()

#  write File ("w" mode)
file = open("C:\\Users\\User\\Documents\\Details.txt","w")
file.write("I am part of pythonlife session\n")
file.write("filehandling practice")
file.close

# Appending to a File ("a" mode)
file = open("C:\\Users\\User\\Documents\\Details.txt","a")
file.write("\npractice file")
file.close

# Read + Write ("r+" mode)
file = open("C:\\Users\\User\\Documents\\Details.txt","r+")
print(file.read())
file.write("\nadded using r+ mode")
file.close

# write + Read ("w+" mode)
file = open("C:\\Users\\User\\Documents\\Details.txt","w+")
file.write("Hello ,I am shravya\n")
file.write("this is w+ mode")
file.seek(0)
print(file.read())
file.close


# Append + Read ("a+" mode)
file = open("C:\\Users\\User\\Documents\\Details.txt","a+")
file.write("\nthis is a+mode")
file.seek(0)
print(file.read())
file.close
