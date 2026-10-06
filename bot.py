import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🎬 Catálogo", callback_data="catalogo"),
            InlineKeyboardButton("🔥 Populares", callback_data="populares"),
        ],
        [
            InlineKeyboardButton("🆕 Novidades", callback_data="novidades"),
            InlineKeyboardButton("🔎 Pesquisar", callback_data="pesquisar"),
        ],
        [
            InlineKeyboardButton("❤️ Minha Lista", callback_data="minha_lista"),
            InlineKeyboardButton("💎 Meu Acesso", callback_data="acesso"),
        ],
        [
            InlineKeyboardButton("💬 Suporte", callback_data="suporte")
        ],
    ]

    await update.message.reply_text(
        "🎬 *Bem-vindo ao DoramaPass!*\n\n"
        "Escolha uma opção abaixo:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown",
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    respostas = {
        "catalogo": "🎬 O catálogo será disponibilizado aqui.",
        "populares": "🔥 Aqui ficarão os títulos populares.",
        "novidades": "🆕 Aqui ficarão as novidades.",
        "pesquisar": "🔎 Digite o nome do título que deseja pesquisar.",
        "minha_lista": "❤️ Sua lista aparecerá aqui.",
        "acesso": "💎 Aqui você poderá consultar seu acesso.",
        "suporte": "💬 Entre em contato com o suporte.",
    }

    await query.message.reply_text(
        respostas.get(query.data, "Opção não encontrada.")
    )


def main():
    token = os.environ["BOT_TOKEN"]

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("DoramaPassBot iniciado!")

    app.run_polling()


if __name__ == "__main__":
    main()
