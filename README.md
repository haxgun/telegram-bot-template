# ✨ Telegram Bot Template

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![GitHub License](https://img.shields.io/github/license/haxgun/telegram-bot-template?color=green)](https://github.com/haxgun/telegram-bot-template/blob/main/LICENSE)
[![Stars](https://img.shields.io/github/stars/haxgun/telegram-bot-template?style=flat&color=green)](https://github.com/haxgun/telegram-bot-template/stargazers)
[![Forks](https://img.shields.io/github/forks/haxgun/telegram-bot-template?style=flat&color=green)](https://github.com/haxgun/telegram-bot-template/forks)
[![Issues](https://img.shields.io/github/issues/haxgun/telegram-bot-template?style=flat)](https://github.com/haxgun/telegram-bot-template/issues)

## 🚀 Technology Stack and Features

- 🔧 [**Aiogram**](https://docs.aiogram.dev/) `(v3.17)` for building Telegram bots with ease.
- 🪴 [**Fluentogram**](https://github.com/Arustinal/fluentogram) a proper way to use an i18n mechanism with Aiogram3.
- 📊 [**SQLite**](https://www.sqlite.org/index.html) for lightweight database storage using **aiosqlite**.
- 🔌 [**Alembic**](https://alembic.sqlalchemy.org/) for database migrations.
- ⚡ [**Asyncio**](https://docs.python.org/3/library/asyncio.html) for asynchronous programming.
- 🛠️ [**Pydantic**](https://docs.pydantic.dev/) and [Pydantic Settings](https://docs.pydantic.dev/latest/usage/settings/) for robust data validation and settings management.
- 🔮 [**SQLAlchemy**](https://www.sqlalchemy.org/) for database ORM.
- 🎨 [**Loguru**](https://github.com/Delgan/loguru) for advanced logging capabilities.
- ⚛ [**UV**](https://github.com/astral-sh/uv) extremely fast Python package and project manager, written in Rust.

## 🛠️  Installation and Setup

### 📋 Prerequisites
- Recommended Python version: **3.12**
- Make sure to have [UV](https://github.com/your-package-manager/uv) installed

### 🔧 Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/haxgun/telegram-bot-template.git
   cd telegram-bot-template
   ```

2. Install dependencies:
   ```bash
   uv init
   ```
   
3. Set up the virtual environment:
   - Create a virtual environment: ```uv venv```
   - Activate the virtual environment: ```source ./venv/bin/activate```
   

4. Set up the environment variables:
   - Create a `.env` file in the project root.
   - Add the necessary configurations (e.g., `BOT_TOKEN`, `ADMIN_IDS`).

5. Run database migrations:
   ```bash
   alembic revision --autogenerate -m "Initial revision"
   alembic upgrade head
   ```

6. Start the bot:
   ```bash
   python3 -m bot.main
   ```

## 🗂️ Directory Structure

```
telegram-bot-template/
├── bot/
│   ├── __init__.py
│   ├── main.py             # Main entry point
│   ├── config.py           # Configuration settings
│   ├── handlers/           # Bot handlers ✋
│   ├── keyboards/          # Custom keyboards 🎹
│   ├── i18n/               # Internationalization 🌍
│   ├── middlewares/        # Custom middlewares 🔑
│   ├── services/           # Utility services 🔧
│   ├── migrations/         # Alembic migrations 🔄
│   │   ├── env.py          # Environment variables 🌱
│   │   ├── script.py.mako  # Alembic migration script 🔨
│   ├── database/           # Database files 📊
│   │   ├── database.py     # Database setup 🗄️
│   │   ├── models.py       # Database models 🧑‍💻
├── data/                   # Data files 📂
│   ├── __init__.py
├── .env.example            # Example environment variables 🌱
├── .gitignore              # Ignored files 🚫
├── alembic.ini             # Configuration file for Alembic ⚙️
├── LICENSE                 # License file 📜
├── pyproject.toml          # Dependencies 📋
├── requirements.txt        # Dependencies 🔌
└── README.md               # Project documentation 📚
```

## ✨ Key Features

- Modular architecture for scalability.
- Asynchronous database operations with SQLite.
- Easy-to-use logging via Loguru.
- Seamless environment variable management with Pydantic Settings.
- Effortless database migrations with Alembic.

## 🌱 Environment Variables

Ensure you have the following variables set in your `.env` file:

```env
BOT_TOKEN=your-telegram-bot-token
ADMIN_IDS=[AdminID1, AdminID2, AdminID3]
```

## 🧑‍💻 Contributing

1. Fork the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

🎉  Happy Coding! 🌟

