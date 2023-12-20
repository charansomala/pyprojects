import two
print("top level in three")

if __name__=='__main__':
    print("three.py is being run directly")
else:
    print("three is being imported")