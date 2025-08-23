emotions={"happy": "😊", "sad": "😢", "angry": "😠", "love": "❤️", "surprised": "😲", "confused": "😕", "bored": "😐",
         "excited": "🤩", "tired": "😴", "nervous": "😬"}
print(emotions)

# emotion = input("Enter an emotion: ").strip().lower()
# if emotion in emotions:
#     print(f"The emoji for {emotion} is {emotions[emotion]}")
# else:
#     print("Emotion not found.")


emotion = input("Enter your message: ").strip().lower()
words = emotion.split()
converted = [emotions.get(word, word) for word in words]
new_message = " ".join(converted)

print(new_message)