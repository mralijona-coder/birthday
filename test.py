import base64
import streamlit as st

st.set_page_config(page_title="МОЕ ПОЗДРАВЛЕНИЕ)))", page_icon="🙈", layout="centered")


# --- ФУНКЦИЯ ДЛЯ КОДИРОВАНИЯ ВАШЕЙ КАРТИНКИ ---
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Картинка 'photo.jpg' должна лежать в одной папке с этим скриптом!
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
        /* Плотная белая подложка под каждый блок с текстом для идеальной читаемости */
        .stElementContainer {{
            background-color: rgba(255, 255, 255, 0.92) !important;
            padding: 15px 20px !important;
            border-radius: 12px !important;
            margin-bottom: 15px !important;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.15);
        }}
        /* Принудительно красим ВСЕ тексты, заголовки и вопросы в глубокий черный цвет */
        h1, h2, h3, p, label, .stMarkdown, p[data-testid="stWidgetLabel"] {{
            color: #000000 !important;
            font-weight: 600 !important;
        }}
        /* Настройка текста внутри самих полей ввода */
        input {{
            color: #000000 !important;
            background-color: #ffffff !important;
            font-weight: 500 !important;
        }}
        /* Кнопки, видео и сообщения об ошибках оставляем без белых рамок */
        div[data-testid="stButton"], div[data-testid="stVideo"], div[data-testid="stNotification"] {{
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
        "Ой! Не нашли файл 'photo.jpg'. Пожалуйста, переименуйте сохраненное фото в 'photo.jpg' и положите его в папку со скриптом."
    )
# -----------------------------------------------

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
nickname = st.text_input("3. Ты и есть на самом деле - ?", value="")
lakab = st.text_input("4. Как ты называешь 'странного' человека?", value="")

if st.button("я - та самая, войти"):
    clean_color = color.strip().lower().replace("ё", "е")
    clean_nickname = nickname.strip().lower().replace("ё", "е")
    clean_lakab = lakab.strip().lower().replace("ё", "е")

    if (
        age == 23
        and clean_color == "зеленый"
        and clean_nickname == "ангелок"
        and clean_lakab == "волшебный"
    ):
        st.balloons()  # Эффектный взлет шариков при правильном ответе!
        st.success("ЕСССССС , это ты!!!!")
        st.video("0001-0800.mp4")
    elif age == 0 or color == "" or nickname == "" or lakab == "":
        st.warning("А нужно то ответить на все вопросы 🙃")
    else:
        st.error("ойойойой, ты не та самая 🥱, кыш кыш")


