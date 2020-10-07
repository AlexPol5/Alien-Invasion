class GameStats():
    """Отслеживание статистики для игры Инопланетное вторжение."""

    def __init__(self, ai_settings):
        """Инициализирует статистику."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Игра Инопланетное вторжение запускается в неактивном состоянии.
        self.game_active = False

        # Рекорд не должен сбрасываться.
        # Открывает файл с рекордом очков игры, читает значение
        # рекорда.
        with open('high_record.txt') as file_object:
            record = file_object.read()
            self.high_score = int(record)

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


