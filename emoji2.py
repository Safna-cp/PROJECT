emotions = {
    "happy": "😊", "sad": "😢", "angry": "😠", "love": "❤️", "surprised": "😲",
    "confused": "😕", "bored": "😐", "excited": "🤩", "tired": "😴", "nervous": "😬"
}
emoji_to_word = {v: k for k, v in emotions.items()}
emotion = input("Enter your message: ").strip().lower()
words = emotion.split()
converted = [emoji_to_word.get(word, word) for word in words]
new_message = " ".join(converted)
print(new_message)