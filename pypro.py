import tkinter as tk
from itertools import product

# 데이터 그룹 정의
groups = {
    "A": ["교류전원", "직류전원", "배터리", "건전지"],
    "B": ["3세미만", "3세이상", "8세미만"],
    "C": ["국내", "해외"],
    "D": ["성인용"]
}

# 토글 버튼 상태 업데이트 함수
def toggle(group, item):
    if item in selected_items[group]:
        selected_items[group].remove(item)
    else:
        selected_items[group].add(item)

# 결과 계산 및 표시 함수
def calculate_and_display():
    # 선택된 항목으로 조합 생성
    selected_groups = [list(selected_items[group]) for group in groups]
    combinations = list(product(*selected_groups))
    
    # 결과 텍스트 업데이트
    result_text.delete(1.0, tk.END)
    for combo in combinations:
        result_text.insert(tk.END, str(combo) + '\n')

# 초기 선택된 항목
selected_items = {group: set(items) for group, items in groups.items()}

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("Combination Generator")

# 토글 버튼 생성
for group, items in groups.items():
    frame = tk.Frame(window)
    frame.pack()
    tk.Label(frame, text=group).pack(side=tk.LEFT)
    for item in items:
        btn = tk.Checkbutton(frame, text=item, onvalue=item, offvalue="",
                             command=lambda g=group, i=item: toggle(g, i))
        btn.select()  # 기본적으로 선택
        btn.pack(side=tk.LEFT)

# 결과 표시 영역
result_text = tk.Text(window, height=10, width=50)
result_text.pack()

# 실행 버튼
execute_button = tk.Button(window, text="결과 보기", command=calculate_and_display)
execute_button.pack()

# 윈도우 실행
window.mainloop()
