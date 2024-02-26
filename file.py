import tkinter as tk
from PIL import Image, ImageTk
import pygame
from threading import Thread
from nltk.chat.util import Chat, reflections

class ChatbotUI:
    def __init__(self, master):
        self.master = master
        master.title("Modern Cartoon Chatbot")
        master.geometry("400x500")
        master.configure(bg='black')  # Set background color to a shade of red

        # Initialize pygame for animation
        pygame.init()

        # Load dancing character images
        self.frames = []
        for i in range(1, 6):
            frame_path = f"D:\\chatbot-nltk\\images\\{i}.jpg"
            frame = Image.open(frame_path)
            frame = frame.resize((100, 100), Image.ANTIALIAS)
            self.frames.append(ImageTk.PhotoImage(frame))

        # Create label for displaying dancing character
        self.character_label = tk.Label(master)
        self.character_label.pack(pady=10)

        # Listbox to display messages
        self.message_text = tk.Text(master, width=40, height=10, font=("Comic Sans MS", 12), wrap=tk.WORD, bg='#ECF0F1')  # Set background color to a shade of gray
        self.message_text.pack(padx=10, pady=10)

        # Entry widget for user input
        self.user_input_entry = tk.Entry(master, font=("Comic Sans MS", 12))
        self.user_input_entry.pack(fill=tk.X, padx=10, pady=5)

        # Stylish send button
        self.send_button = tk.Button(
            master, text="Send", command=self.send_message, font=("Comic Sans MS", 12), bg="#3498DB", fg="white"
        )
        self.send_button.pack(pady=5)

        # Stylish quit button
        self.quit_button = tk.Button(
            master, text="Quit", command=self.quit_application, font=("Comic Sans MS", 12), bg="#E74C3C", fg="white"
        )
        self.quit_button.pack(pady=5)

        # Define custom responses for the chatbot
        self.responses = [
            (r"hi", ["Hello, how can I help you?"]),
            (r"Please tell me about virtual delights?", ["Virtual delights is QR based Cafe for online order and delivery."]),
            (r"how are you\??", ["I'm good, thank you for asking."]),
            (r"what is your name\??", ["My name is Chatbot. How about you?"]),
            (r"quit", ["Goodbye!"]),
            (r".*", ["I'm not sure I understand. Can you please rephrase?"])
        ]

        # Initialize the chatbot
        self.chatbot = Chat(self.responses)

        # Start the animation thread
        self.animation_thread = Thread(target=self.animate_character)
        self.animation_thread.start()

    def animate_character(self):
        while True:
            for frame in self.frames:
                self.character_label.configure(image=frame)
                self.character_label.image = frame
                self.master.update()
                pygame.time.delay(200)  # Adjust the delay for the desired animation speed

    def send_message(self):
        user_input = self.user_input_entry.get()
        if user_input.lower() == 'quit':
            self.quit_application()
        else:
            response = self.chatbot.respond(user_input)
            self.display_message("You: " + user_input, 'user')
            self.display_message("Chatbot: " + response, 'chatbot')
            self.user_input_entry.delete(0, tk.END)

    def display_message(self, message, role):
        tag = 'user' if role == 'user' else 'chatbot'
        self.message_text.insert(tk.END, message + "\n", tag)
        self.message_text.tag_config(tag, foreground='#2C3E50')  # Dark gray font color
        self.message_text.see(tk.END)  # Scroll to the bottom

    def quit_application(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    chatbot_ui = ChatbotUI(root)
    root.mainloop()
