file_name = 'recipes.txt'

def made_cook_book(file_name:str):
    cook_book = {}

    with open(file_name,encoding='utf-8') as file:
        for line in file:
            dish = line.strip()
            # print(dish)
            number_ing = int(file.readline())
            # print(number_ing)
            ingridients = []
            # print(ingridients)



            for amount_ingridient in range(number_ing):
                ingridients.append(file.readline().strip().split('|'))

            # print(ingridients)


            first_recipes_book = []
            for ingridient in ingridients:
                second_book = {'ingridient_name':ingridient[0],'quantity':ingridient[1],'measure':ingridient[2]}


                first_recipes_book.append(second_book)
                cook_book.update({dish:first_recipes_book})

            empty = file.readline()

    # print(cook_book)
made_cook_book(file_name)


def get_shop_list_by_dishes(dishes,persone_count = 1):
    shop_book = {}

    with open(file_name, encoding='utf-8') as file:
        for line in file:
            if line.strip() in dishes:
                dish = line.strip()
                # print(dish)
                number_ing = int(file.readline())
                # print(number_ing)

                ingridients = []


                for amount_ingridient in range(number_ing):
                    ingridients.append(file.readline().strip().split('|'))



                for ingridient in ingridients:
                    if ingridient[0] not in shop_book:
                        book = {'measure': ingridient[2],'quantity': int(ingridient[1])*persone_count}
                        shop_book[ingridient[0]] = book


                    else:
                        book['quantity'] += int(ingridient[1])*persone_count
                        shop_book.update({ingridient[0]: book})

                file.readline()

    print(shop_book)

get_shop_list_by_dishes(['Омлет','Фахитос'],2)
#изменила список блюд в вызове функции для проверки кода: по повторяющемуся помидору все работает, сплюсовала
#но после этого одновременно предыдущий ингридиент (винный уксус) вместо 1, стал в количестве 3,
# хотя он уже обработан по логике, почему он снова попал в цикл и увеличился
#не могу найти ошибку







    # with open(file_name,encoding='utf-8') as file:
    #     for line in file:
    #         dish = line.strip()
    #         # print(dish)
    #         number_ing = int(file.readline())
    #         # print(number_ing)
    #         ingridients = []
    #         # print(ingridients)
    #
    #
    #         for amount_ingridient in range(number_ing):
    #             ingridients.append(file.readline().strip().split('|'))
    #
    #         # print(ingridients)
    #
    #
    #         first_recipes_book = []
    #         for ingridient in ingridients:
    #             second_book = {'ingridient_name':ingridient[0],'quantity':ingridient[1],'measure':ingridient[2]}
    #
    #
    #             first_recipes_book.append(second_book)
    #             cook_book.update({dish:first_recipes_book})
    #
    #         empty = file.readline()










