def is_valid_imei(imei: str) -> bool:
    if not imei.isdigit() or len(imei) != 15:
        return False

    # Исправленный алгоритм Луна
    digits = [int(d) for d in imei]
    checksum = 0

    for i in range(0, 15):
        num = digits[i]
        if i % 2 == len(imei) % 2:  # Корректная проверка
            num *= 2
            if num > 9:
                num -= 9
        checksum += num

    return checksum % 10 == 0
