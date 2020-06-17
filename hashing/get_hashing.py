def get_hash(key):
    h=0
    for i in key:
        h += ord(i)
    print(h%100)

get_hash('march 28')