import telebot
from datetime import datetime

API = '7551864776:AAHPKGAv2MesW4ahOl5Yp7QFl1lexA24MZk'  # Replace with your actual bot token
bot = telebot.TeleBot(API, parse_mode='HTML')

user_data = {}

def format_sum(summa: str) -> str:
    try:
        val = int(summa)
        return f"{val:,.2f}".replace(",", ".").replace(".", ",", 1) + " UZS"
    except:
        return summa

@bot.message_handler(commands=['start'])
def start_message(msg):
    ID = msg.chat.id
    user_data[ID] = {'step': 0, 'inputs': []}
    
    matn = (
        "Assalomu alaykum botimizga xush kelibsiz\n\n"
        "Ushbu shaklda maʼlumot yuboring:\n"
        "<code>2500000\n6506\n2611931</code>"
    )
    bot.send_message(ID, matn)

@bot.message_handler(func=lambda msg: True)
def handle_input(msg):
    ID = msg.chat.id
    txt = msg.text.strip()

    if ID not in user_data:
        bot.send_message(ID, "Iltimos, avval /start buyrug‘ini yuboring.")
        return

    # Foydalanuvchi 3 ta qatorda ma'lumot yuborishi kerak
    lines = txt.split('\n')
    if len(lines) != 3 or not all(line.strip().isdigit() for line in lines):
        bot.send_message(ID, "❗️Noto‘g‘ri format. Quyidagicha yuboring:\n<code>2500000\n6506\n2611931</code>", parse_mode='HTML')
        return

    # Malumotlar
    amount = lines[0].strip()
    card = lines[1].strip()
    balance = lines[2].strip()
    now = datetime.now().strftime("%H:%M %d.%m.%Y")

    javob = (
        "🎉 <b>To'ldirish</b>\n"
        f"➕ <b>{format_sum(amount)}</b>\n"
        f"📍 <b>KAPPA 5 ECOM POPOL N</b>\n"
        f"💳 <b>HUMOCARD *{card}</b>\n"
        f"🕓 <b>{now}</b>\n"
        f"💰 <b>{format_sum(balance)}</b>"
    )

    bot.send_message(ID, javob)
    user_data.pop(ID, None)  # foydalanuvchini tozalab qo‘yamiz
bot.polling()