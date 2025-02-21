import tkinter as tk
import random

# Thai consonants with their names
thai_consonants = [
    ("ก", "ก ไก่ - Gor Kai"), ("ข", "ข ไข่ - Kho Khai"), ("ค", "ค ควาย - Kho Khwai"),
    ("ง", "ง งู - Ngo Ngu"), ("จ", "จ จาน - Jo Jan"), ("ฉ", "ฉ ฉิ่ง - Cho Ching"),
    ("ช", "ช ช้าง - Cho Chang"), ("ซ", "ซ โซ่ - So So"), ("ญ", "ญ หญิง - Yo Ying"),
    ("ด", "ด เด็ก - Do Dek"), ("ต", "ต เต่า - To Tao"), ("ป", "ป ปลา - Po Pla"),
    ("พ", "พ พาน - Pho Phan"), ("ฟ", "ฟ ฟัน - Fo Fan"), ("ม", "ม ม้า - Mo Ma"),
    ("ร", "ร เรือ - Ro Ruea"), ("ล", "ล ลิง - Lo Ling"), ("ว", "ว แหวน - Wo Waen"),
    ("ส", "ส เสือ - So Suea"), ("ห", "ห หีบ - Ho Hip")
]

class ThaiFlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.card_frame = tk.Frame(root, width=300, height=200, bg="white")
        self.card_frame.pack(pady=50)
        
        self.label = tk.Label(self.card_frame, text="", font=("Arial", 50), bg="white", fg="black")
        self.label.pack(expand=True)
        
        self.show_consonant_button = tk.Button(root, text="Show Consonant", command=self.show_consonant, font=("Arial", 14))
        self.show_consonant_button.pack(pady=5)
        
        self.show_name_button = tk.Button(root, text="Show Name", command=self.show_name, font=("Arial", 14))
        self.show_name_button.pack(pady=5)
        
        self.next_card_button = tk.Button(root, text="Next Card", command=self.next_card, font=("Arial", 14))
        self.next_card_button.pack(pady=10)
        
        self.current_card = None
        self.next_card()

    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.label.config(text=self.current_card[0])  # Show Thai consonant by default

    def show_consonant(self):
        self.label.config(text=self.current_card[0])  # Show Thai consonant

    def show_name(self):
        self.label.config(text=self.current_card[1])  # Show consonant name

if __name__ == "__main__":
    root = tk.Tk()
    app = ThaiFlashcardGame(root)
    root.mainloop()


