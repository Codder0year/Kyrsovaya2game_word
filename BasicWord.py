class BasicWord:
    def __init__(self, original_word, under_the_word):
        self.original_word = original_word
        self.under_the_word = under_the_word
        self.user_input = None

    def check(self):
        '''
        проверка введенного слова в списке допустимых подслов.
        :param :
        :return: (вернет bool)
        '''
        return self.user_input in self.under_the_word

    def count_word(self):
        '''
        ведет подсчет  количества подслов
        :return:int
        '''
        return len(self.under_the_word)

    def __repr__(self):
        return f"""
{self.original_word}-это исходное слово,
{self.under_the_word}-это подслова
{self.user_input}-ввод пользователя"""
