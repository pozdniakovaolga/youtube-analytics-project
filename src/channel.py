import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')  # берет значение переменной окружения
    youtube: str = build('youtube', 'v3', developerKey=api_key)  # создает объект для работы с API

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется по id канала """
        self.__channel_id: str = channel_id  # id канала

        # Получаем данные канала по api
        self.channel: dict = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

        # Создаём необходимые атрибуты
        self.title: str = self.channel['items'][0]['snippet']['title']  # название канала
        self.description: str = self.channel['items'][0]['snippet']['description']  # описание канала
        self.url: str = f"https://www.youtube.com/channel/{self.channel['items'][0]['id']}"  # ссылка на канал
        self.subscriberCount: int = int(self.channel['items'][0]['statistics']['subscriberCount'])  # число подписчиков
        self.video_count: int = int(self.channel['items'][0]['statistics']['videoCount'])  # количество видео на канале
        self.viewCount: int = int(self.channel['items'][0]['statistics']['viewCount'])  # количество просмотров

    def __str__(self) -> str:
        """Возвращает информацию о канале: название(ссылка) """
        return f"{self.title} ({self.url})"

    def __add__(self, other) -> int:
        """Возвращает общее количество подписчиков двух каналов """
        return self.subscriberCount + other.subscriberCount

    def __sub__(self, other) -> int:
        """Возвращает разницу в количестве подписчиков двух каналов """
        return self.subscriberCount - other.subscriberCount

    def __gt__(self, other) -> bool:
        """Возвращает результат сравнения(>) количества подписчиков двух каналов """
        return self.subscriberCount > other.subscriberCount

    def __ge__(self, other) -> bool:
        """Возвращает результат сравнения(>=) количества подписчиков двух каналов """
        return self.subscriberCount >= other.subscriberCount

    def __lt__(self, other) -> bool:
        """Возвращает результат сравнения(<) количества подписчиков двух каналов """
        return self.subscriberCount < other.subscriberCount

    def __le__(self, other) -> bool:
        """Возвращает результат сравнения(<=) количества подписчиков двух каналов """
        return self.subscriberCount <= other.subscriberCount

    def __eq__(self, other) -> bool:
        """Проверяет равны ли количества подписчиков двух каналов """
        return self.subscriberCount == other.subscriberCount

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале """
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self) -> str:
        """Возвращает id канала """
        return self.__channel_id

    @classmethod
    def get_service(cls) -> object:
        """Возвращает объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, file_name) -> None:
        """Сохраняет в файл значения атрибутов экземпляра Channel"""
        # Создаем словарь на основе атрибутов
        dict = {"channel_id": self.channel_id,
                "title": self.title,
                "description": self.description,
                "url": self.url,
                "subscriberCount": self.subscriberCount,
                "videoCount": self.video_count,
                "viewCount": self.viewCount,
                }
        # Сохраняем словарь в файл
        with open(file_name, "w") as outfile:
            json.dump(dict, outfile, ensure_ascii=False)
