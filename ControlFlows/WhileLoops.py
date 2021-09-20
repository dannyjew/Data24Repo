# x = 0
#
# while x < 10:
#     print(f"it's working -> {x}")
#     if x == 4:
#         break
#     x += 1
#
user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("Please provide your answer in digits and less than 117")

