i = 1
is_failed = False
while is_failed:
    print(f"Try {i}")
    i = i + 1
    if i > 100:
        break
print("I gave up!")
