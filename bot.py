from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# دالة البداية
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("أهلاً بيك يا نجم! أنا بوت حوده، قولي عاوز أساعدك في إيه؟ 😎")

# دالة الرد على الرسائل
def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    update.message.reply_text(f"انت كتبت: {user_message} 🙌. لسه بطور نفسي عشان أخدمك أكتر!")

# إعداد البوت
def main():
    # حط التوكن بتاعك هنا
    TOKEN = "7464643507:AAFr1x3pfZ-XU5FbOHGSiIV0rQPAmlXn-pU"

    # إنشاء البوت
    updater = Updater(TOKEN)

    # تحديد الأحداث (handlers)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dispatcher.add_handler(CommandHandler("help", help_user))
    dispatcher.add_handler(CommandHandler("song", write_song))
    dispatcher.add_handler(CommandHandler("code", solve_code))


    # تشغيل البوت
    updater.start_polling()
    updater.idle()

def help_user(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("أنا هنا عشان أساعدك! ممكن أسئلة، نصايح، أو أي حاجة تانية؟")

def write_song(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("دي شوية كلمات أغاني حب ليك: ❤️\nيا حبيبي قرب مني، ده انت حياتي وسنيني 🎵")

def solve_code(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("ابعتلي الكود اللي فيه مشكلة، وأنا هحاول أحلهولك. 🛠️")


if __name__ == "__main__":
    main()
