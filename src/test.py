test_list = ["Hallo", "wie", "gehts?", "wie", "test"]

for count, values in enumerate(test_list):
    if values == "wie":
        print(count)
        next_item = [x+1 for x in test_list]