# -*- coding: utf-8 -*-
import streamlit as st
from chatglm_api import ask_chatglm
import datetime

st.set_page_config(page_title="🔮 AI 命理大师", layout="centered")
st.title("🧙‍♂️ AI 算命大师（腾讯混元 GPT）")

name = st.text_input("姓名")
gender = st.radio("性别", ["男", "女"])
birthday = st.date_input(
    "出生日期",
    value=datetime.date(1990,1,1),
    min_value=datetime.date(1900,1,1),
    max_value=datetime.date(2035,12,31)
)
birthtime = st.time_input("出生时间")

if st.button("开始算命"):
    birth_str = f"{birthday} {birthtime}"
    prompt = f"""
请你扮演一位资深八字命理师，详细解析以下信息：
姓名：{name}
性别：{gender}
出生时间：{birth_str}
请给出八字排盘、五行强弱、命格分析、运势建议、事业财运婚姻方向。
"""
    with st.spinner("分析中…"):
        result = ask_chatglm(
            prompt=prompt,
            secret_id=st.secrets["SECRET_ID"],
            secret_key=st.secrets["SECRET_KEY"],
            model="hunyuan-lite"
        )
    st.success("分析完成")
    st.markdown(result)
