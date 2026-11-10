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
        .game-card {
            background-color: #1a1a1a;
            border: 1px solid #333;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(255, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .game-card:hover {
            box-shadow: 0 0 40px rgba(255, 0, 0, 0.5);
            transform: translateY(-5px);
            border-color: #ff0000;
        }
        .game-title {
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
        <div class="game-card">
            <div class="game-title">BACKROOMS LABYRINTH</div>
            <div class="game-desc">
                Психологический хоррор от первого лица. Исследуйте бесконечные желтые коридоры, 
                собирайте ключи, прячьтесь от Объекта-1 и постарайтесь выбраться живым...
            </div>
            <!-- Сюда потом вставишь ссылку на скачивание игры -->
            <a href="#" class="btn-download">Скачать (Beta)</a>
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
    # Этот блок нужен, чтобы сайт работал и на домашнем ПК, и на Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
