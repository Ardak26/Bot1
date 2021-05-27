import telebot

bot = telebot.TeleBot("1899779814:AAGF2PXvkegd_CILeSlrcn1PIVuTFIGGZsY")

questions = []
questions.append({
    "question":"What is a capital of UK?",
    "var1": "Madrid", "var2": "London", "var3": "Astana", "var4": "Almaty", "ans": "London"
})
questions.append({
    "question": "What is a capital of Spain?",
    "var1": "Madrid", "var2": "London", "var3": "Astana", "var4": "Almaty", "ans": "Madrid"
})
questions.append({
    "question": "What is a capital of Kazakhstan?",
    "var1": "Madrid", "var2": "London", "var3": "Astana", "var4": "Almaty", "ans": "Astana"
})

index = 0
score = 0

@bot.message_handler(content_types=["text"])
def handle_text(message):

    global index
    global score

    if message.text.lower() == "/start":

        bot.send_message(message.chat.id, "#########################\n")
        bot.send_message(message.chat.id, "Welcome to test questions\n")
        bot.send_message(message.chat.id, "We will ask you for 3 questions about capitals\n")
        bot.send_message(message.chat.id, "#########################\n")
        index = 0

    else:

        if message.text.lower() == questions[index]["ans"].lower():
            bot.send_message(message.chat.id, "Yes!!! You are right!!! + 1 point\n")
            index = index + 1
            score = score + 1
        else:
            bot.send_message(message.chat.id, "No!!! Incorrect!!!\n")
            index = index+1

    if index == 3:
        index = 0
        bot.send_message(message.chat.id, "Game Over!!! You got " + str(score) + " points\n")
    else :
        bot.send_message(message.chat.id, questions[index]['question'] + "?")
        bot.send_message(message.chat.id, "A) "+questions[index]['var1'] + "\n")
        bot.send_message(message.chat.id, "B) " + questions[index]['var2'] + "\n")
        bot.send_message(message.chat.id, "C) " + questions[index]['var3'] + "\n")
        bot.send_message(message.chat.id, "D) " + questions[index]['var4'] + "\n")

bot.polling(none_stop=True, interval=0)