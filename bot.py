#!/usr/bin/env python3
"""
AdVerse CRM — Telegram bot that opens the Mini App.

Requirements:
  pip install -r requirements.txt

Environment:
  BOT_TOKEN      — from @BotFather
  MINI_APP_URL   — HTTPS URL of the hosted frontend
  BOT_USERNAME   — optional, without @ (for deep links)

Run:
  export BOT_TOKEN="123456:ABC..."
  export MINI_APP_URL="https://your-domain.com"
  export BOT_USERNAME="AdVerseCRM_bot"
  python3 bot.py
"""

from __future__ import annotations

import os
import logging

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
    MenuButtonWebApp,
)
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    level=logging.INFO,
)
log = logging.getLogger("adverse-bot")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
MINI_APP_URL = os.environ.get("MINI_APP_URL", "").strip().rstrip("/")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "").strip().lstrip("@")


def open_crm_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🚀 Открыть AdVerse CRM",
                    web_app=WebAppInfo(url=MINI_APP_URL),
                )
            ],
        ]
    )


def role_links_text() -> str:
    if not BOT_USERNAME:
        return ""
    return (
        "\n\nБыстрые роли (deep link):\n"
        f"• Buyer: https://t.me/{BOT_USERNAME}?startapp=role_buyer\n"
        f"• Agent: https://t.me/{BOT_USERNAME}?startapp=role_agent\n"
        f"• Admin: https://t.me/{BOT_USERNAME}?startapp=role_admin"
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    name = user.first_name if user else "друг"
    text = (
        f"Привет, *{name}*!\n\n"
        "Это *AdVerse* — CRM для медиабайеров и агентов Facebook Ads.\n\n"
        "• Заказы аккаунтов\n"
        "• Пополнения (напрямую агенту)\n"
        "• Аналитика и поддержка\n\n"
        "_Платформа не хранит и не переводит деньги — только подписка CRM._"
        f"{role_links_text()}"
    )
    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=open_crm_keyboard(),
        disable_web_page_preview=True,
    )


async def app_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Откройте CRM внутри Telegram:",
        reply_markup=open_crm_keyboard(),
    )


async def post_init(app: Application) -> None:
    """Menu button (left of message input) → Mini App."""
    await app.bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="AdVerse",
            web_app=WebAppInfo(url=MINI_APP_URL),
        )
    )
    me = await app.bot.get_me()
    log.info("Bot @%s ready | Mini App: %s", me.username, MINI_APP_URL)


def main() -> None:
    if not BOT_TOKEN:
        raise SystemExit("Set BOT_TOKEN (from @BotFather)")
    if not MINI_APP_URL:
        raise SystemExit("Set MINI_APP_URL (HTTPS URL of Mini App)")
    if not MINI_APP_URL.startswith("https://"):
        raise SystemExit("MINI_APP_URL must start with https://")

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("app", app_cmd))
    application.add_handler(CommandHandler("crm", app_cmd))

    log.info("Starting AdVerse bot…")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
