# one_thru_nine = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# for i in one_thru_nine:
#     print(i)
# print("ten \neleven \ntweleve \nthirteen \nfourteen \nfifteen \nsixteen \nseventeen \neighteen \nnineteen \ntwenty")
# for i in one_thru_nine:
#     print(f'twenty {i}')
# print("thirty")
# for i in one_thru_nine:
#     print(f'thirty {i}')
# print("forty")
# for i in one_thru_nine:
#     print(f'forty {i}')
# print("fifty")
# for i in one_thru_nine:
#     print(f'fifty {i}')
# print("sixty")
# for i in one_thru_nine:
#     print(f'sixty {i}')
# print("seventy")
# for i in one_thru_nine:
#     print(f'seventy {i}')
# print("eighty")
# for i in one_thru_nine:
#     print(f'eighty {i}')
# print("ninety")
# for i in one_thru_nine:
#     print(f'ninety {i}')
# print("one hundred")
x = 50
try:
    if x > 10:
        raise ValueError("x is too large!")
except ValueError as e:
    print(f"Caught a {e.__class__.__name__} exception!")