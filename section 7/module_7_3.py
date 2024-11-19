class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = []
        self.all_words = {}
        for file in file_names:
            self.file_names.append(file)

    def get_all_words(self):
        punktuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        words = []
        for file in self.file_names:
            with open(file, encoding='utf-8') as f:
                for line in f:
                    line = line.lower()
                    for p in punktuation:
                        if line.__contains__(p):
                            line = line.replace(p, '')
                    for word in line.split():
                        words.append(word)
            self.all_words[file] = words
            return self.all_words


    def find(self, word):
        find_dict = {}
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word.lower() == words[i]:
                    find_dict[name] = i + 1
                    return find_dict

    def count(self, word):
        count_dict = {}
        count = 0
        for name, words in self.get_all_words().items():
            for w in words:
                if word.lower() == w:
                    count += 1
            count_dict[name] = count
            return count_dict


if __name__ == '__main__':

    finder1 = WordsFinder('Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('AnD'))
    print(finder1.count('ANd'))

    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())
    print(finder2.find('TEXT'))
    print(finder2.count('teXT'))

    finder3 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
    print(finder3.get_all_words())
    print(finder3.find('cAPTaiN'))
    print(finder3.count('captAIN'))