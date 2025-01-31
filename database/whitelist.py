WHITELIST = {5655223856}  # Здесь Telegram ID разрешенных пользователей

def is_user_allowed(user_id: int) -> bool:
    """ Проверяет, есть ли пользователь в белом списке """
    return user_id in WHITELIST
