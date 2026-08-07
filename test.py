import streamlit as st

st.set_page_config(page_title="МОЕ ПОЗДРАВЛЕНИЕ)))", page_icon="🙈", layout="centered")


st.title("вход разрешен одной единственной 🫠")
st.subheader("ответь на 4 вопроса, чтобы войти:")

age = st.number_input("1. Сколько тебе исполнилось сегодня?", min_value=0, max_value=120, value=0, step=1)
color = st.text_input("2. Какой твой любимый цвет?", value="")
nickname = st.text_input("3. Ты и есть на самом деле - ?", value="")
lakab = st.text_input("4. Как ты называешь 'странного' человека?", value="")


if st.button("я - та самая, войти"):

    clean_color = color.strip().lower().replace("ё", "е")
    clean_nickname = nickname.strip().lower().replace("ё", "е")
    
    
    if age == 23 and clean_color == "зеленый" and clean_nickname == "ангелок" and lakab == "волшебный":

        st.success("ЕСССССС , это ты!!!!")
    
        st.video("0001-0800.mp4")
        
    elif age == 0 or color == "" or nickname == "" or lakab == "":
        st.warning("А нужно то ответить на все вопросы 🙃")
    else:
        st.error("ойойойой, ты не та самая 🥱, кыш кыш")

