def to_infinity():
    index = 0
    while True:
        yield index
        index += 1

for i in to_infinity():
    if i > 10:
        i1=1
