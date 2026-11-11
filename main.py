import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_CODE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pixel Studio - Games</title>
    <style>
        body {
            background-color: #0d0d0d;
            color: #ffffff;
            font-family: 'Courier New', Courier, monospace;
            margin: 0;
            padding: 0;
            text-align: center;
            overflow-x: hidden;
        }
        @keyframes flicker {
            0% { opacity: 1; }
            50% { opacity: 0.8; text-shadow: 0 0 20px #ff0000; }
            100% { opacity: 1; }
        }
        header {
            background-color: #1a1a1a;
            padding: 30px 20px;
            border-bottom: 3px solid #ff0000;
            box-shadow: 0 0 30px rgba(255, 0, 0, 0.4);
        }
        h1 {
            color: #ff0000;
            text-shadow: 0 0 10px #ff0000;
            letter-spacing: 8px;
            margin: 0;
            font-size: 3em;
            animation: flicker 4s infinite;
        }
        .subtitle {
            color: #888;
            margin-top: 10px;
            letter-spacing: 2px;
        }
        .container {
            max-width: 800px;
            margin: 60px auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 30px;
        }
        .game-card, .links-card {
            background-color: #1a1a1a;
            border: 1px solid #333;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(255, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .game-card:hover, .links-card:hover {
            box-shadow: 0 0 40px rgba(255, 0, 0, 0.5);
            transform: translateY(-5px);
            border-color: #ff0000;
        }
        .game-title, .links-title {
            color: #ffcccc;
            font-size: 32px;
            margin-bottom: 15px;
            font-weight: bold;
            text-shadow: 0 0 5px rgba(255, 0, 0, 0.5);
        }
        .game-desc {
            color: #aaaaaa;
            margin-bottom: 25px;
            line-height: 1.6;
            font-size: 16px;
        }
        .btn-download {
            display: inline-block;
            background-color: #8b0000;
            color: white;
            padding: 15px 40px;
            text-decoration: none;
            font-weight: bold;
            font-size: 18px;
            border-radius: 5px;
            text-transform: uppercase;
            transition: all 0.3s ease;
            border: 2px solid #ff0000;
            cursor: pointer;
        }
        .btn-download:hover {
            background-color: #ff0000;
            box-shadow: 0 0 30px #ff0000;
            transform: scale(1.05);
        }
        .links-list {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .link-item {
            display: inline-block;
            background-color: #2a2a2a;
            color: #ffcccc;
            padding: 12px 25px;
            text-decoration: none;
            border-radius: 8px;
            border: 1px solid #444;
            transition: 0.3s;
            font-size: 16px;
        }
        .link-item:hover {
            background-color: #ff0000;
            color: white;
            border-color: #ff0000;
            box-shadow: 0 0 15px #ff0000;
        }
        footer {
            margin-top: 80px;
            color: #555;
            font-size: 14px;
            padding-bottom: 30px;
        }
    </style>
</head>
<body>
    <header>
        <h1>PIXEL STUDIO</h1>
        <div class="subtitle">Независимая разработка игр</div>
    </header>

    <div class="container">
        <!-- Карточка игры -->
        <div class="game-card">
            <div class="game-title">BACKROOMS LABYRINTH</div>
            <div class="game-desc">
                Психологический хоррор от первого лица. Исследуйте бесконечные желтые коридоры, 
                собирайте ключи, прячьтесь от Объекта-1 и постарайтесь выбраться живым...
            </div>
            <!-- Твоя ссылка на скачивание -->
            <a href="https://github.com/lomar456/pixel-studio/releases/download/v1.0/Backrooms.Labyrinth.beta.1.5.rar" class="btn-download">Скачать (Beta)</a>
        </div>

        <!-- Карточка ссылок -->
        <div class="links-card">
            <div class="links-title">Наши соцсети</div>
            <div class="links-list">
                <a href="https://www.youtube.com/@pixel.studioo.fficial" target="_blank" class="link-item">YouTube</a>
                <a href="https://t.me/PixelStudioGames" target="_blank" class="link-item">Telegram</a>
                <a href="https://pixel-studio-1.onrender.com/" target="_blank" class="link-item">Сайт</a>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2026 Pixel Studio. Все права защищены.</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
