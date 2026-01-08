import streamlit as st
import math

st.set_page_config(page_title="계산기", page_icon="🧮")

st.title("🧮 계산기")

# 세션 상태 초기화
if "expression" not in st.session_state:
    st.session_state.expression = ""

# 계산 함수
def calculate(expr):
    try:
        expr = expr.replace("^", "**")
        expr = expr.replace("log", "math.log")
        return str(eval(expr))
    except:
        return "Error"

# 디스플레이
st.text_input(
    "계산기 화면",
    st.session_state.expression,
    disabled=True,
    label_visibility="collapsed"
)

# 버튼 레이아웃
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
    ["^", "log", "C", "="]
]

for row in buttons:
    cols = st.columns(4)
    for i, button in enumerate(row):
        if cols[i].button(button, use_container_width=True):
            if button == "C":
                st.session_state.expression = ""
            elif button == "=":
                st.session_state.expression = calculate(st.session_state.expression)
            elif button == "log":
                st.session_state.expression += "math.log("
            else:
                st.session_state.expression += button

