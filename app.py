from flask import Flask, render_template, request
from itertools import product

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    groups = {
        "A": ["해당없음", "국내제조", "해외수입"],
        "B": ["해당없음", "교류전원", "직류전원", "배터리", "건전지", "전원없음"],
        "C": ["해당없음", "3세미만", "3세이상", "8세미만"],
        "D": ["해당없음", "성인용"]
    }

    selected_items = {group: groups[group][:] for group in groups}

    if request.method == 'POST':
        selected_items = {
            group: request.form.getlist(group) for group in groups
        }

    # 조합 생성
    combinations = list(product(*[selected_items[group] for group in groups if selected_items[group]]))

    # '해당없음' 제거 및 빈 튜플 필터링
    def remove_irrelevant(combination):
        filtered = tuple(item for item in combination if item != "해당없음")
        return filtered if filtered else None

    non_empty_combinations = [combo for combo in map(remove_irrelevant, combinations) if combo]

    return render_template('index.html', groups=groups, selected_items=selected_items, combinations=non_empty_combinations)

if __name__ == '__main__':
    app.run(debug=True)






##############################################################################################





    
# from flask import Flask, render_template, request
# from itertools import product

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     groups = {
#         "A": ["해당없음", "교류전원", "직류전원", "배터리", "건전지", "전원없음"],
#         "B": ["해당없음", "국내", "해외"],
#         "C": ["해당없음", "3세미만", "3세이상", "8세미만"],
#         "D": ["해당없음", "성인용"]
#     }

#     selected_items = {group: groups[group][:] for group in groups}

#     if request.method == 'POST':
#         selected_items = {
#             group: request.form.getlist(group) for group in groups
#         }

#     # 조합 생성
#     combinations = list(product(*[selected_items[group] for group in groups if selected_items[group]]))

#     # 첫 번째 요소가 '해당없음'인 튜플 제거 및 '해당없음' 필터링
#     def remove_irrelevant(combination):
#         if combination and combination[0] == "해당없음":
#             return None  # 첫 번째 요소가 '해당없음'인 경우 제거
#         return tuple(item for item in combination if item != "해당없음")

#     non_empty_combinations = [combo for combo in map(remove_irrelevant, combinations) if combo]

#     return render_template('index.html', groups=groups, selected_items=selected_items, combinations=non_empty_combinations)

# if __name__ == '__main__':
#     app.run(debug=True)
