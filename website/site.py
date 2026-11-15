from flask import Flask, render_template
import os

app = Flask(__name__)

# Твоя ссылка на игру (ZIP)
DOWNLOAD_URL = "https://github.com/lomar456/pixel-studio/releases/download/v1.6/Backrooms.Labyrinth.v1.6.beta.zip"

# Твоя ссылка на донат (CloudTips)
DONATE_URL = "https://pay.cloudtips.ru/p/f871c42e"

# Твоя ссылка на Telegram
TG_URL = "https://t.me/PixelStudioGames"

@app.route('/')
def index():
    return render_template('index.html', 
                           download_url=DOWNLOAD_URL,
                           donate_url=DONATE_URL,
                           tg_url=TG_URL)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
