import streamlit as st
import math

st.set_page_config(page_title="계산기", page_icon="🧮", layout="centered")

st.title("🧮 계산기")

# ---------- CSS 스타일 ----------
st.markdown("""
<style>
button {
    height: 60px;
    font-size: 20px !important;
    font-weight: bold;
}

.num-btn button {
    background-color: #f0f0f0;
    color: black;
}

.op-btn button {
    background-color: #ffb703;
    color: black;
}

.func-btn button {
    background-color: #fb8500;
    color: white;
}

.eq-btn button {
    background-color: #219ebc;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------- 세션 상태 ----------
if "expression" not in st.session_state:
    st.session_state.expression = ""

# ---------- 계산 함수 ----------
def calculate(expr):
    try:
        expr = expr.replace("^", "**")
        return str(eval(expr))
    except:
        return "Error"

# ---------- 디스플레이 ----------
st.text_input(
    "",
    st.session_state.expression,
    disabled=True
)

# ---------- 버튼 정의 ----------
buttons = [
    [("7","num"), ("8","num"), ("9","num"), ("/","op")],
    [("4","num"), ("5","num"), ("6","num"), ("*","op")],
    [("1","num"), ("2","num"), ("3","num"), ("-","op")],
    [("0","num"), (".","num"), ("%","op"), ("+","op")],
    [("^","op"), ("log","func"), ("C","func"), ("=","eq")]
]

# ---------- 버튼 렌더링 ----------
for row in buttons:
    cols = st.columns(4)
    for i, (label, btn_type) in enumerate(row):
        with cols[i]:
            if st.container().button(
                label,
                key=f"{label}_{i}",
                use_container_width=True
            ):
                if label == "C":
                    st.session_state.expression = ""
                elif label == "=":
                    st.session_state.expression = calculate(st.session_state.expression)
                elif label == "log":
                    st.session_state.expression += "math.log("
                else:
                    st.session_state.expression += label
