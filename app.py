# -*- coding: utf-8 -*-
import streamlit as st
from chatglm_api import ask_chatglm
import datetime

st.set_page_config(page_title="🔮 AI 命理大师", layout="centered")
st.title("🧙‍♂️ AI 命理大师（八字 + 紫微斗数）")

# 输入区
name = st.text_input("姓名")
gender = st.radio("性别", ["男", "女"])
birthday = st.date_input(
    "出生日期",
    value=datetime.date(1990,1,1),
    min_value=datetime.date(1900,1,1),
    max_value=datetime.date(2035,12,31)
)
birthtime = st.time_input("出生时间")
user_question = st.text_input("你想咨询的方面？例如：财运、爱情、家庭、事业...", "")

# 生成八字分析
if st.button("生成八字命理"):
    birth_str = f"{birthday} {birthtime}"
    prompt = f"""
请扮演资深八字命理师，结合以下信息进行详细分析：
姓名：{name}
性别：{gender}
出生时间：{birth_str}
重点解析：{user_question}
请输出八字排盘、命格、五行、运势、事业事业婚姻建议，内容深入且通俗。
"""
    with st.spinner("八字分析中…"):
        result = ask_chatglm(prompt, st.secrets["SECRET_ID"], st.secrets["SECRET_KEY"], model="hunyuan-lite")
    st.subheader("八字分析结果")
    st.markdown(result)

# 紫微斗数按钮触发
if st.button("解析紫微斗数"):
    birth_str = f"{birthday} {birthtime}"
    prompt = f"""
请你扮演紫微斗数老师，以非常通俗易懂的方式解释：
- 紫微斗数的基本原理（例如：十二宫、主星、四化等）
- 根据出生时间如何排盘？
- 结合“{user_question}”进行紫微斗数层面的分析。
请深入分析核心宫位，例如命宫、事业宫、财帛宫等，并用生活化比喻说明。
"""
    with st.spinner("紫微斗数解释中…"):
        result = ask_chatglm(prompt, st.secrets["SECRET_ID"], st.secrets["SECRET_KEY"], model="hunyuan-lite")
    st.subheader("紫微斗数通俗解析")
    st.markdown(result)
