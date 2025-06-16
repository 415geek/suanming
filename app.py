# -*- coding: utf-8 -*-
import streamlit as st
from chatglm_api import ask_chatglm
import datetime
# 在界面最顶部，引入 webbrowser 模块
import streamlit as st
import webbrowser

if st.button("⭐ 访问我的 LinkedIn 个人主页"):
    webbrowser.open_new_tab("https://www.linkedin.com/in/lingyu-maxwell-lai")
    st.set_page_config(page_title="🔮 AI大模型 命理大师", layout="centered")
st.title("AI大模型 命理大师（By c8geek）")

name = st.text_input("姓名")
gender = st.radio("性别", ["男", "女"])
birthday = st.date_input(
    "出生日期", 
    value=datetime.date(1990,1,1),
    min_value=datetime.date(1900,1,1),
    max_value=datetime.date(2035,12,31)
)
birthtime = st.time_input("出生时间")
user_question = st.text_input("你想咨询的内容？（如：财运、爱情、事业等）")

model_choice = st.selectbox(
    "选择分析模型", 
    ["hunyuan-turbos-latest", "hunyuan-pro", "hunyuan-lite"]
)

def analyze(prompt, title):
    with st.spinner(f"{title} 分析中…"):
        return ask_chatglm(
            prompt=prompt,
            secret_id=st.secrets["SECRET_ID"],
            secret_key=st.secrets["SECRET_KEY"],
            model=model_choice
        )

if st.button("生成八字命理"):
    birth_str = f"{birthday} {birthtime}"
    prompt = f"""
请扮演资深八字命理师，结合以下信息进行深入通俗分析：
姓名：{name}
性别：{gender}
出生时间：{birth_str}
问题方向：{user_question}
请给出八字排盘、五行强弱、命格分析、运势及事业婚姻建议。
"""
    result = analyze(prompt, "八字")
    st.subheader("八字分析结果")
    st.markdown(result)

if st.button("解析紫微斗数"):
    birth_str = f"{birthday} {birthtime}"
    prompt = f"""
请扮演紫微斗数老师，以通俗易懂方式讲解：
- 紫微斗数基础（宫位、主星、四化）
- 如何排盘
- 针对“{user_question}”进行分析，重点宫位和比喻说明。
"""
    result = analyze(prompt, "紫微斗数")
    st.subheader("紫微斗数解析结果")
    st.markdown(result)
