import os
from googleapiclient.discovery import build


class Video:
    """Класс для видео"""

    api_key: str = os.getenv('YT_API_KEY')  # берет значение переменной окружения
    youtube: str = build('youtube', 'v3', developerKey=api_key)  # создает объект для работы с API

    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется по id видео """
        self.video_id: str = video_id  # id видео

        # Получаем данные видео по api
        self.video: dict = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=self.video_id).execute()

        # Создаём необходимые атрибуты
        self.title: str = self.video['items'][0]['snippet']['title']  # название видео
        self.url: str = f"https://www.youtube.com/watch?v={self.video['items'][0]['id']}"  # ссылка на видео
        self.viewCount: int = self.video['items'][0]['statistics']['viewCount']  # количество просмотров
        self.like_count: int = self.video['items'][0]['statistics']['likeCount']  # количество лайков

    def __str__(self) -> str:
        """Возвращает название видео """
        return self.title


class PLVideo(Video):
    """Класс для видео и плейлиста, является подклассом класса Video"""

    def __init__(self, video_id, pl_id):
        """Экземпляр инициализируется по id видео и id плейлиста"""
        super().__init__(video_id)
        self.pl_id = pl_id  # id плейлиста
