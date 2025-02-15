from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the Dice Game! 🎲\nType /roll to roll the dice and guess the outcome.")

def roll_dice(update: Update, context: CallbackContext) -> None:
    dice_roll = random.randint(1, 6)
    update.message.reply_text(f"Guess the outcome of the dice roll! 🎲\nEnter a number between 1 and 6:")
    context.user_data['dice_roll'] = dice_roll

def guess_dice(update: Update, context: CallbackContext) -> None:
    try:
        user_guess = int(update.message.text)

        if user_guess < 1 or user_guess > 6:
            update.message.reply_text("Please enter a number between 1 and 6.")
            return

        dice_roll = context.user_data.get('dice_roll')

        if user_guess == dice_roll:
            update.message.reply_text(f"Congratulations! You guessed correctly! The dice rolled a {dice_roll}. 🎉")
        else:
            update.message.reply_text(f"Sorry, wrong guess. The dice rolled a {dice_roll}. Try again! 🎲")
    except ValueError:
        update.message.reply_text("Please enter a valid number between 1 and 6.")

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("roll", roll_dice))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, guess_dice))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
