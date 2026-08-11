import base64
import streamlit as st

st.set_page_config(page_title="МОЕ ПОЗДРАВЛЕНИЕ)))", page_icon="🙈", layout="centered")



def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()



try:
    img_base64 = get_base64_image("photo.jpg")

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
        }}
        .stElementContainer {{
            background-color: rgba(255, 255, 255, 0.92) !important;
            padding: 15px 20px !important;
            border-radius: 12px !important;
            margin-bottom: 15px !important;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.15);
        }}
        h1, h2, h3, p, label, .stMarkdown, p[data-testid="stWidgetLabel"] {{
            color: #000000 !important;
            font-weight: 600 !important;
        }}

        input {{
            color: #000000 !important;
            background-color: #ffffff !important;
            font-weight: 500 !important;
        }}
        div[data-testid="stButton"] button {{
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 2px solid #000000 !important;
            font-weight: bold !important;
            border-radius: 10px !important;
            padding: 10px 25px !important;
            transition: all 0.3s ease;
        }}
        div[data-testid="stButton"] button:hover {{
            background-color: #000000 !important;
            color: #ffffff !important;
            transform: scale(1.02);
        }}
        div[data-testid="stVideo"], div[data-testid="stNotification"] {{
            background-color: transparent !important;
            padding: 0 !important;
            box-shadow: none !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
except FileNotFoundError:
    st.error(
        "Ой! Не нашли файл 'photo.jpg'. Пожалуйста, переименовайте сохраненное фото в 'photo.jpg' и положите его в папку со скриптом."
    )

st.title("вход разрешен одной единственной 🫠")
st.subheader("ответь на 4 вопроса, чтобы войти:")

age = st.number_input(
    "1. Сколько тебе исполнилось сегодня?",
    min_value=0,
    max_value=120,
    value=0,
    step=1,
)
color = st.text_input("2. Какой твой любимый цвет?", value="")
nickname = st.text_input("3. Кто ты по профессии? ", value="")
lakab = st.text_input("4. Как ты называешь 'странного' человека?", value="")

if st.button("я - та самая, войти"):
    clean_color = color.strip().lower().replace("ё", "е")
    clean_nickname = nickname.strip().lower().replace("ё", "е")
    clean_lakab = lakab.strip().lower().replace("ё", "е")

    if (
        age == 23
        and clean_color == "зеленый"
        and clean_nickname == "дезигнер"
        and clean_lakab == "волшебный"
    ):
        st.success("ЕСССССС , это ты!!!!")
        st.video("0001-0800.mp4")
    elif age == 0 or color == "" or nickname == "" or lakab == "":
        st.warning("А нужно то ответить на все вопросы 🙃")
    else:
        st.error("ойойойой, ты не та самая 🥱, кыш кыш")



