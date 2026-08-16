import requests
import re
import base64

# URL репозитория terik21, откуда берем свежие ключи
SUBS_URL = "https://githubusercontent.com"

# Ваша разметка текстового профиля с вашими обычными серверами
PROFILE_TEMPLATE = """# profile-title: Tisonan VPN
# profile-update-interval: 1
#announce: Если не работает, то пробуйте другие варианты!
{auto_server}
vless://f01801ca-4264-453e-bca1-2d9abe45b6b5@82.26.91.166:26362?type=grpc&security=none&encryption=none#🇵🇱Польша #1
vless://f01801ca-4264-453e-bca1-2d9abe45b6b5@82.26.91.166:26363?type=xhttp&security=none&path=%2F&mode=auto&encryption=none#🇵🇱Польша #2
vless://670decfe-68cc-499e-8cb1-22b39c20acbb@://helper-internet.com🇪🇸Испания
vless://2a650f3b-d95b-4bd6-aadf-16ccc0717155@134.0.116.208:9878?encryption=none&fp=qq&mode=gun&pbk=bnRIb3Er1i-K6NGGByCO9UbGfOvu43ZoiK7ulPd1SzU&security=reality&serviceName=grpc-tunnel&sid=aa&sni=://google.com&type=grpc#🇫🇷Франция
hysteria2://owefv0_92Z540k2F_nx83245_J9130oS_tY@5.180.27.221:8443?sni=://bumbleshrimp.com#🇰🇿Казахстан
hysteria2://e8c93f75-4ed5-41b1-a32e-a846e54582e8@89.106.85.19:8444?sni=premium-de-hy2.geodema.network#🇩🇪Для BrawlStars #1
hysteria2://08794874-93d0-4cf2-b9d6-1f2774cdffeb@144.31.5.9:2101?sni=panel.vlessbotkey.ru#🇵🇱Для BrawlStars #2
vless://081f4a5d-f8ed-07d0-b824-49d1d563730f@139.100.197.28:52006?type=raw&security=tls&flow=xtls-rprx-vision&fp=qq&sni=search.setlisting.ru#🇷🇺YouTube без рекламы
vless://2a650f3b-d95b-4bd6-aadf-16ccc0717155@45.151.30.127:9882?encryption=none&mode=gun&pbk=bnRIb3Er1i-K6NGGByCO9UbGfOvu43ZoiK7ulPd1SzU&security=reality&serviceName=grpc-tunnel&sni=://google.com&type=grpc&fp=firefox#🇰🇿Мобильный интернет #1
vless://2a650f3b-d95b-4bd6-aadf-16ccc0717155@194.58.95.183:9871?security=reality&encryption=none&pbk=bnRIb3Er1i-K6NGGByCO9UbGfOvu43ZoiK7ulPd1SzU&type=grpc&serviceName=grpc-tunnel&sni=://google.com&sid=aa&fp=chrome#🇸🇪Мобильный интернет #2
vless://ca599ed4-f7a0-4ddf-a45d-3cb6276d6cd7@85.193.84.49:443?alpn=http/1.1&encryption=none&fp=firefox&path=/api/v1/connect&security=tls&sni=files-x.bosx.net&type=ws#🇵🇱Мобильный интернет #3
vless://2a650f3b-d95b-4bd6-aadf-16ccc0717155@62.233.43.86:9898?type=grpc&security=reality&pbk=bnRIb3Er1i-K6NGGByCO9UbGfOvu43ZoiK7ulPd1SzU&sid=aabbccdd&sni=://google.com&serviceName=grpc-tunnel&fp=chrome#🇫🇮Мобильный интернет #4
vless://2a650f3b-d95b-4bd6-aadf-16ccc0717155@45.151.30.127:9873?type=grpc&headerType=none&security=reality&encryption=none&sni=://google.com&fp=qq&pbk=bnRIb3Er1i-K6NGGByCO9UbGfOvu43ZoiK7ulPd1SzU&serviceName=grpc-tunnel#🇺🇸Мобильный интернет #5"""

def get_first_vless():
    try:
        response = requests.get(SUBS_URL, timeout=10)
        if response.status_code != 200:
            return None
        text = response.text
        
        # Если данные в Base64, декодируем их в обычный текст
        if not text.strip().startswith("vless://") and not text.strip().startswith("#"):
            try:
                text = base64.b64decode(text.strip()).decode('utf-8')
            except Exception:
                pass
                
        # Находим первую строчку, начинающуюся с vless://
        vless_keys = re.findall(r'(vless://[^\s]+)', text)
        if vless_keys:
            first_key = vless_keys[0]
            # Заменяем оригинальный комментарий сервера на ваш красивый тег
            if '#' in first_key:
                first_key = first_key.split('#')[0]
            return first_key + "#🇷🇺Авто-обход"
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
    return None

def main():
    auto_server = get_first_vless()
    if not auto_server:
        # Резервный ключ, если чужой репозиторий упал или недоступен
        auto_server = "vless://633c112c-11dd-48d3-8595-e151dd589ef4@85.234.86.105:2053?security=reality&type=grpc&mode=gun&serviceName=grpc&packetEncoding=xudp&sni=://google.com&fp=chrome&sid=dd70b6a4e3e9e7ce&pbk=XrNOGI1TNjL2rcq65LBsjw8ouZ9PQMOZt466XeJt8XE#🇷🇺Авто-обход"
    
    # Подставляем спарсенный ключ на первое место шаблона
    final_profile = PROFILE_TEMPLATE.format(auto_server=auto_server)
    
    # Сохраняем результат в index.html для работы GitHub Pages
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(final_profile)

if __name__ == "__main__":
    main()
