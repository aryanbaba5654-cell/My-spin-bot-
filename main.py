from telegram.ext import Application, MessageHandler, filters

# Apna Token yahan daalein
TOKEN = "8939290954:AAE0CxTaamrt8GvJ1zmQwjLDw_g1e7wDv-4"

async def get_id(update, context):
    # Check karein ki message mein GIF (animation) hai ya nahi
    if update.message.animation:
        file_id = update.message.animation.file_id
        print(f"GIF File ID: {file_id}")
        await update.message.reply_text(f"Ye rahi tumhari GIF ID: `{file_id}`")

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ANIMATION, get_id))
    print("Bot chal gaya! Ab Telegram par GIFs bhejein.")
    app.run_polling()
