import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# fonte do emoji icone da pagina: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Paraquedismo", page_icon=":parachute:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_xgv9sjxn.json")
img_idosa_paraquedas = Image.open("images/idosa_paraquedas.png")
img_salto_duplo = Image.open("images/salto_duplo.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Paraquedismo :parachute:")
    st.title("Um esporte radical e seguro")
    st.write(
        "O paraquedismo, ao contrário do que muitos pensam é um esporte seguro."
    )
    st.write("[Veja mais >](https://skydivecalifornia.com/blog/skydiving-statistics/)")

# ---- ESTATISTICAS ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Estatísticas")
        st.write("##")
        st.write(
            """
            Segundo estatísticas oficiais da USPA (Associação de Paraquedismo Americana):
            - Em 2022 42.491 membros da USPA realizaram 3,9 milhões de saltos nos EUA.
            - Em 2022 a USPA registrou 20 acidentes fatais na prática do paraquedismo.
            - Em 2022 a taxa de fatalidade ficou em 0,51 a cada 100.000 saltos.
            - 98,3% dos acidendes foram decorrentes de falhas humanas."

            O paraquedismo é praticado com 2 paraquedas, um principal e um resarva para caso necessite, o que torna o esporte mais seguro ainda.
            """
        )
        st.write("[USPA(Fonte dos dados) >](https://www.uspa.org/discover/faqs/safety#:~:text=In%202019%2C%20USPA%20recorded%2015,jumps%20over%20the%20past%20decade.)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- VIDEOS PARAQUEDISMO ----
with st.container():
    st.write("---")
    st.header("Um esporte apaixonante!!!")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_idosa_paraquedas)
    with text_column:
        st.subheader("Um esporte para todas as idades!")
        st.write(
            """
            Paraquedismo, um esporte radical sem preconceitos!!
            Feito para todos!
            """
        )
        st.markdown("[Assita ao vídeo](https://www.youtube.com/watch?v=gzNjwsJBQ_8&pp=ygUZaWRvc2Egc2FsdGEgZGUgcGFyYXF1ZWRhcw%3D%3D)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_salto_duplo)
    with text_column:
        st.subheader("PURA ADRENALINAAA!")
        st.write(
            """
            Um esporte que te faz feliz!
            """
        )
        st.markdown("[Assita ao vídeo](https://www.youtube.com/watch?v=e2m7wzOgmgs&pp=ygUebWluaGEgbWFlIHNhbHRvdSBkZSBwYXJhcXVlZGFz)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Tire a sua dúvida sobre paraquedismo")
    st.write("##")

    # Documentaçao do fomulario: https://formsubmit.co/ 
    contact_form = """
    <form action="https://formsubmit.co/cassiianoo98@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Seu nome" required>
     <input type="email" name="email" placeholder = "Seu email" required>
     <textarea name="message" placeholder="Ecreva a sua mensagem aqui" required></textarea>
     <button type="submit">Enviar</button>
    </form>  
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
