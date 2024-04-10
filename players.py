class Player:
    def __init__(self, name):
        self.name = name
        self.used_user_answer = []
        self.user_input = None

    def add_words(self):
        '''
        добавление слова в использованные слова (ничего не возвращает);
        '''
        self.used_user_answer.append(self.user_input)

    def is_word_used(self):
        '''
        проверка использования данного слова до этого.
        :return: (возвращает bool).
        '''
        return self.user_input in self.used_user_answer

    def count_user_answer(self):
        '''
        получение количества использованных слов.
        :return: (возвращает int);
        '''
        return len(self.used_user_answer)

    def __repr__(self):
        return f"""
        Player(name={self.name},
        used_words={self.used_user_answer}
        user_input={self.user_input})
        """
