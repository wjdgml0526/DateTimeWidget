import tkinter as tk
from datetime import datetime
from tkinter import font

# 시간 업데이트 함수
def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time_label.config(text = current_time)
    root.after(1000, update_time)

# 메인 윈도우 설정
root = tk.Tk()
root.title('모각코 스트리밍 위젯')

# colors
bg = '#2B2B2B'
fg = '#A9B7C6'

# font
custom_font = font.Font(family = 'NanumGothicCoding', size = 24)
goal_font = font.Font(family = 'NanumGothicCoding', size = 12)

# 창 크기 및 색상 설정
root.geometry('300x200')
root.configure(bg = bg)

# Hello, World!
intro_label = tk.Label(root, text = 'Hello, World!', bg = bg, fg = '#6A8759', font = custom_font)
intro_label.pack(pady = (40, 10))

# 오늘 날짜 표시
today = datetime.now().strftime("%Y-%m-%d")
date_label = tk.Label(root, text=f"{today}", bg=bg, fg = fg, font=custom_font)
date_label.pack(pady = (10, 0))

# 현재 시간 표시
time_label = tk.Label(root, text="", bg=bg, fg = '#CC7832', font=custom_font)
time_label.pack(pady = (0, 10))

# 시간 업데이트 시작
update_time()

# GUI 이벤트 루프 시작
root.mainloop()