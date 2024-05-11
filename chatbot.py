from threading import Thread, Event
from time import sleep


class ChatBot:
    def __init__(self, callback, first_message="Welcome to ChatBotAI", terminate="quit"):
        self.callback = callback
        self.terminate = terminate
        if first_message:
            print(first_message)

    def process_message(self, message):
        bot_message = self.callback(message)
        print("Bot:", bot_message)

    def user_input_handler(self):
        while True:
            message = input("You: ")
            if message.lower() == self.terminate:
                break
            self.process_message(message)

    def start(self):
        user_thread = Thread(target=self.user_input_handler)
        user_thread.start()
        user_thread.join()


def bot_response(message):
    if message.lower() == "hello":
        return "Hi there!"
    elif message.lower() == "how are you?":
        return "I'm just a bot, but thanks for asking!"
    else:
        return "I'm sorry, I don't understand that."


def main():
    chat_bot = ChatBot(bot_response)
    chat_bot.start()


if __name__ == "__main__":
    main()
