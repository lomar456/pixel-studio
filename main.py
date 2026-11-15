from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Ссылки
    download_url = "https://github.com/lomar456/pixel-studio/releases/download/v1.6/Backrooms.Labyrinth.v1.6.beta.zip"
    donate_url = "https://pay.cloudtips.ru/p/f871c42e"
    tg_url = "https://t.me/PixelStudioGames"
    
    return render_template('index.html', 
                           download_url=download_url,
                           donate_url=donate_url,
                           tg_url=tg_url)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
