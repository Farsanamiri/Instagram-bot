import itertools

letters = 'abcdefghijklmnopqrstuvwxyz'

combinations = itertools.product(letters, repeat=4)

with open("combinations.txt", "w") as file:
    for combo in combinations:
        file.write("".join(combo) + "\n")

print("تمام ترکیب‌ها در فایل 'combinations.txt' ذخیره شد.")
