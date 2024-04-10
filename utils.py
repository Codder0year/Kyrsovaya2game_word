import random
import requests
import urllib3
from BasicWord import BasicWord
from players import Player


def load_random_word():
    '''
    загрузка списка с Json
    :return: экземпляр класса с веденными полями
    '''
    urllib3.disable_warnings()
    response = requests.get("https://www.jsonkeeper.com/b/WIX6", verify=False)
    load_json = response.json()
    list_word = random.choice(load_json)
    basic_word = BasicWord(list_word['word'], list_word['subwords'])
    return basic_word


def hello():
    '''
    приветствие игрока и информация по игре
    :return: 2 экземпляра класса: Player, BasicWord
    '''
    basic_word = load_random_word()
    gamer = Player(input("Ввведите имя игрока"))
    print(f"""Привет, {gamer.name}!
    Составьте {basic_word.count_word()} слов из слова {basic_word.original_word.upper()}
    Слова должны быть не короче 3 букв
    Чтобы закончить игру, угадайте все слова или напишите "stop"
    Поехали, ваше первое слово?
    """)
    return [gamer, basic_word]


def main():
    """
    Основной цикл игры, в котором игроку предлагается вводить слова,
     соответствующие допустимым подсловам,
    и проверяется их правильность. Игра продолжается до тех пор,
     пока игрок не введет команду "стоп" или не
    угадает все допустимые подслова.
     В конце выводится общее количество угаданных слов.
    """
    gamer, basic_word = hello()
    # i = 100000000000000000000000000000000000
    # for small_word in basic_word.under_the_word:
    #     """сравниваем элемент списка с последующим по длине
    #     получаем самое короткое
    #     """
    #     if len(small_word) < i:
    #         i = len(small_word)
    # Это 1 вариант


    small_word = min(basic_word.under_the_word, key=len)
    print(small_word)
    print(basic_word.user_input)
    while gamer.count_user_answer() < len(basic_word.under_the_word):
        basic_word.user_input = gamer.user_input = input()
        if len(basic_word.user_input) < len(small_word):
            print("слишком короткое слово")
        elif gamer.is_word_used():
            print("уже использовано")
        elif basic_word.user_input.lower() == 'стоп' or basic_word.user_input.lower() == 'stop':
            print(f"Игра завершена, вы угадали {gamer.count_user_answer()} слов!")
            quit()
        elif not basic_word.check():
            print("неверно")
        else:
            gamer.add_words()
            print("верно!!!!!!!!!!!!!!!!!!!!!")
    print(f"Игра завершена, вы угадали {gamer.count_user_answer()} слов!")


main()
