import streamlit as st
from chatglm_api import ask_chatglm
import datetime

st.set_page_config(page_title="🔮 AI 命理大师", layout="centered")
st.title("🧙‍♂️ AI 命理大师（基于腾讯云 ChatGLM）")

name = st.text_input("姓名")
gender = st.radio("性别", ["男", "女"])
birthday = st.date_input(
    "出生日期", value=datetime.date(1990, 1, 1),
    min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2035, 12, 31)
)
birthtime = st.time_input("出生时间")

if st.button("开始算命"):
    birth_str = f"{birthday} {birthtime}"
    prompt = f"""
你是一位专业八字命理师，请根据以下信息分析命主运势：
姓名：{name}
性别：{gender}
出生时间：{birth_str}
请提供八字排盘、命格分析、五行强弱、事业财运婚姻建议。
    """
    with st.spinner("正在占卜中，请稍候..."):
        result = ask_chatglm(
            prompt=prompt,
            secret_id=st.secrets["SECRET_ID"],
            secret_key=st.secrets["SECRET_KEY"]
        )
        st.success("分析完成！")
        st.markdown(result)
