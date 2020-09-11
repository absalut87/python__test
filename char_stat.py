# Скрипт подсчитывает статистику по буквам в романе Война и Мир.
# И выводит результат
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Скрипт написан по шаблону проектирование "Шаблонный метод",
# работает с любым зипованым txt файлом

import zipfile


class LetterCounter:

    def __init__(self, file_name):
        self.file_name_zip = file_name
        self.file_name = None
        self.stat = {}

    def run(self):
        self.unzip()
        self.collect()
        print(f'+{"":-^9}+{"":-^10}+')
        print(f"|{'Буква':^9}|{'Частота':^10}|")
        print(f'+{"":-^9}+{"":-^10}+')
        self.sort_stat()
        self.output_on_display()

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name_zip, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        name_list = zfile.namelist()
        self.file_name = name_list[-1]

    def collect(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1

    def sort_stat(self):  # Сортировка по возрастанию алфавита
        list_keys = list(self.stat.keys())
        list_keys.sort()

        for i in list_keys:
            print(f'|{i:^9}|{self.stat[i]:^10}|')

    def output_on_display(self):
        self.total_chars = 0
        for v in self.stat.items():
            ch, val = v
            self.total_chars = self.total_chars + val
        print(f'+{"":-^9}+{"":-^10}+')
        print(f"|{'Итого':^9}|{self.total_chars:^10}|")
        print(f'+{"":-^9}+{"":-^10}+')


class SortCounter(LetterCounter):  # сортировка по убыванию

    def sort_stat(self):
        list_keys = list(reversed(sorted(self.stat.keys())))

        for i in list_keys:
            print(f'|{i:^9}|{self.stat[i]:^10}|')


class SortValues(LetterCounter): # сортировка по частоте по возрастанию

    def sort_stat(self):

        for k, v in sorted(self.stat.items(), key=lambda x: x[1]):
            print(f'|{k:^9}|{v:^10}|')


if __name__ == '__main__':
    sorting_type = int(
        input('Выбереите вид сортировки:\n1 - По частоте по возрастанию,\n2 - По алфавиту по возрастанию\n'
              '3 - По алфавиту по убыванию\n---->   '))
    if sorting_type == 1:
        sort_counter = SortValues(file_name='voyna-i-mir.txt.zip')
    elif sorting_type == 2:
        sort_counter = LetterCounter(file_name='voyna-i-mir.txt.zip')
    elif sorting_type == 3:
        sort_counter = SortCounter(file_name='voyna-i-mir.txt.zip')
    sort_counter.run()