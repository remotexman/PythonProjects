import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    users = {}
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users:
            if hash(password) == hash(self.users[password]):
                self.current_user = nickname

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users[nickname] = [hash(password), age]
            self.current_user = nickname
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, search_word):
        list_of_search_videos = []
        for i in self.videos:
            if search_word.lower() in i.title.lower():
                list_of_search_videos.append(i.title)
        return list_of_search_videos

    def watch_video(self, title):
        for i in self.videos:
            if title in i.title:
                if self.current_user is None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                else:
                    if i.adult_mode == True and self.users[self.current_user][1] >= 18:
                        for j in range(1, i.duration+1):
                            time.sleep(0.3)
                            print(j, end=' ')
                        print('Конец видео')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')


if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    ur.add(v1, v2)

    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    ur.watch_video('Лучший язык программирования 2024 года!')