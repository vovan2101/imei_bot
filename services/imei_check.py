import cloudscraper
import logging
from config import IMEI_CHECK_API_URL, IMEI_CHECK_API_TOKEN

logging.basicConfig(level=logging.INFO)

def check_imei_info(imei: str):
    url = f"{IMEI_CHECK_API_URL}?imei={imei}&token={IMEI_CHECK_API_TOKEN}"
    
    logging.info(f"📡 Отправка запроса через cloudscraper: {url}")

    scraper = cloudscraper.create_scraper()  # Эмуляция браузера
    response = scraper.get(url)

    logging.info(f"✅ Ответ от imeicheck.net: {response.status_code}")
    logging.info(f"📄 Тело ответа: {response.text}")

    if response.status_code == 200:
        return response.json()
    
    logging.error(f"❌ Ошибка: {response.status_code} - {response.text}")
    return None
