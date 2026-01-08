import streamlit as st
import math

st.set_page_config(page_title="계산기 웹앱", page_icon="🧮")

st.title("🧮 계산기 웹앱")
st.write("사칙연산, 모듈러, 지수, 로그 연산을 지원합니다.")

# 숫자 입력
num1 = st.number_input("첫 번째 숫자", value=0.0)
num2 = st.number_input("두 번째 숫자", value=0.0)

# 연산 선택
operation = st.selectbox(
    "연산을 선택하세요",
    ("덧셈 (+)", "뺄셈 (-)", "곱셈 (×)", "나눗셈 (÷)",
     "모듈러 (%)", "지수 (xʸ)", "로그 (logₓy)")
)

# 계산 버튼
if st.button("계산하기"):
    try:
        if operation == "덧셈 (+)":
            result = num1 + num2

        elif operation == "뺄셈 (-)":
            result = num1 - num2

        elif operation == "곱셈 (×)":
            result = num1 * num2

        elif operation == "나눗셈 (÷)":
            if num2 == 0:
                st.error("0으로 나눌 수 없습니다.")
                result = None
            else:
                result = num1 / num2

        elif operation == "모듈러 (%)":
            result = num1 % num2

        elif operation == "지수 (xʸ)":
            result = num1 ** num2

        elif operation == "로그 (logₓy)":
            if num1 <= 0 or num2 <= 0 or num1 == 1:
                st.error("로그 연산 조건을 만족하지 않습니다.")
                result = None
            else:
                result = math.log(num2, num1)

        if result is not None:
            st.success(f"결과: {result}")

    except Exception as e:
        st.error(f"오류 발생: {e}")
