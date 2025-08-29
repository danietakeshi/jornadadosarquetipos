import streamlit as st
from collections import Counter
# from io import BytesIO
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib.utils import ImageReader
import questions as qt

st.markdown("""
<style>
body {
    background-color: #3d3d3d;
}
</style>
""", unsafe_allow_html=True)


# [theme]
# base="light"
# backgroundColor="#3d3d3d"
# textColor="#e4efef"

# Descrições dos arquétipos
archetype_descriptions = {
    "Herói": "🔥 Você é uma pessoa que tende a buscar superação e resultados. Tem coragem, determinação e não mede esforços para alcançar suas metas, inspirando os outros pela sua força e disciplina.",
    "Mago": "🧙 Você é uma pessoa que tende a acreditar na transformação e no poder de criar novas realidades. Enxerga possibilidades onde outros veem limites e tem uma visão inovadora, capaz de gerar mudanças profundas.",
    "Inocente": "🕊 Você é uma pessoa que tende a valorizar a simplicidade, a pureza e a fé. Vê o lado bom das situações e transmite esperança, otimismo e autenticidade.",
    "Explorador": "🧭 Você é uma pessoa que tende a buscar liberdade e novas experiências. Gosta de sair da zona de conforto, valoriza a autenticidade e está sempre em movimento, em busca de descobertas.",
    "Cuidador": "🤝 Você é uma pessoa que tende a colocar o bem-estar dos outros em primeiro lugar. Generosa, empática e atenta às necessidades alheias, sente prazer em apoiar, acolher e proteger.",
    "Governante": "👑 Você é uma pessoa que tende a gostar de ordem, estrutura e liderança. Tem postura firme, visão estratégica e transmite segurança, inspirando confiança em quem está ao seu redor.",
    "Criador": "🎨 Você é uma pessoa que tende a ter originalidade e imaginação fértil. Busca expressar suas ideias no mundo, valoriza a estética e gosta de transformar conceitos em algo único e criativo.",
    "Amante": "💃 Você é uma pessoa que tende a valorizar conexões profundas, beleza e prazer. Vive com intensidade, entrega-se de coração e busca relacionamentos que tragam paixão e significado.",
    "Bobo da Corte": "🤡 Você é uma pessoa que tende a enxergar leveza em tudo. Usa humor, espontaneidade e diversão para criar conexões e aliviar tensões, trazendo alegria para quem está à sua volta.",
    "Cara Comum": "🙋 Você é uma pessoa que tende a valorizar igualdade e pertencimento. Gosta de simplicidade, autenticidade e acredita que todos têm valor, conectando-se com facilidade ao dia a dia das pessoas.",
    "Rebelde": "🛡 Você é uma pessoa que tende a questionar regras e padrões. Tem coragem de romper com o estabelecido e busca transformar o que não faz sentido, trazendo inovação e autenticidade.",
    "Sábio": "📚 Você é uma pessoa que tende a buscar conhecimento e clareza. Observadora, reflexiva e analítica, gosta de compreender profundamente as situações e compartilhar sabedoria com os outros."
    }

# Categories
categories = [
    "Rebelde", "Mago", "Herói", "Cuidador", 
    "Criador", "Governante", "Amante", "Bobo da Corte", 
    "Cara Comum", "Inocente", "Explorador", "Sábio"
]

# Questions data structure (each question with 12 possible answers)
questions = [
    {
        "question": "Sobre a sua personalidade, qual desses caracteristicas se parecem mais com você?",
        "answers": [
            ( "Questionador e desafiador.", "Rebelde"),
            ( "Inovador e transformador.", "Mago"),
            ( "Corajoso e assertivo.", "Herói"),
            ( "Acolhedor e compassivo.", "Cuidador"),
            ( "Criativo e original.", "Criador"),
            ( "Líder e autoritário.", "Governante"),
            ( "Apaixonado e empático.", "Amante"),
            ( "Engraçado e extrovertido.", "Bobo da Corte"),
            ( "Confiável e realista.", "Cara Comum"),
            ( "Otimista e puro.", "Inocente"),
            ( "Aventureiro e curioso.", "Explorador"),
            ( "Sábio e reflexivo.", "Sábio"),
        ]
    },
    # Repeat the structure for 12 more questions
    {
        "question": "O que você mais valoriza na vida?",
        "answers": [
            ( "Independência e a capacidade de fazer mudanças.", "Rebelde"),
            ( "Inovação e a descoberta de novas possibilidades.", "Mago"),
            ( "Coragem e a oportunidade de fazer a diferença.", "Herói"),
            ( "Relacionamentos e o bem-estar dos outros.", "Cuidador"),
            ( "Expressão criativa e autenticidade.", "Criador"),
            ( "Controle e liderança eficaz.", "Governante"),
            ( "Relacionamentos íntimos e conexões profundas.", "Amante"),
            ( "Alegria, diversão e não levar a vida tão a sério.", "Bobo da Corte"),
            ( "Simplicidade, comunidade e pertencimento.", "Cara Comum"),
            ( "Felicidade, otimismo e viver uma vida sem culpa.", "Inocente"),
            ( "Aventura e novas experiências.", "Explorador"),
            ( "Conhecimento, sabedoria e verdade.", "Sábio"),
        ]
    },
    # Repeat similarly until Question 13
    {
        "question": "Seu lugar favorito tem quais caracteristicas?",
        "answers": [
            ( "Um lugar onde posso ser eu mesmo, sem regras ou restrições.", "Rebelde"),
            ( "Um espaço criativo e inspirador, cheio de mistérios e possibilidades.", "Mago"),
            ( "Um ambiente desafiador e emocionante, onde posso testar minhas habilidades.", "Herói"),
            ( "Um ambiente acolhedor e confortável, onde posso cuidar e ser cuidado.", "Cuidador"),
            ( "Um espaço artístico e original, que estimula a expressão e a inovação.", "Criador"),
            ( "Um local imponente e bem organizado, que reflete status e controle.", "Governante"),
            ( "Um ambiente romântico e belo, que favorece conexões íntimas.", "Amante"),
            ( "Um lugar divertido e cheio de vida, onde a diversão nunca acaba.", "Bobo da Corte"),
            ( "Um local familiar e acolhedor, onde me sinto parte de uma comunidade.", "Cara Comum"),
            ( "Um espaço seguro e tranquilo, onde posso ser feliz e livre de preocupações.", "Inocente"),
            ( "Um ambiente repleto de aventura e descobertas, sempre diferente e estimulante.", "Explorador"),
            ( "Um local calmo e repleto de conhecimento, ideal para aprendizado e reflexão.", "Sábio"),
        ]
    },
    {
        "question": "Se você fosse líder de uma organização, como você acredita que você seria?",
        "answers": [
            ( "Inovador e desafiador, sempre buscando quebrar as regras e reformular o sistema.", "Rebelde"),
            ( "Visionário e inspirador, capaz de transformar ideias em realidade através da criatividade.", "Mago"),
            ( "Assertivo e corajoso, sempre na linha de frente para defender e motivar minha equipe.", "Herói"),
            ( "Apoiador e empático, focado no bem-estar e no crescimento pessoal dos membros da equipe.", "Cuidador"),
            ( "Criativo e original, incentivando a inovação e a expressão individual no ambiente de trabalho.", "Criador"),
            ( "Autoritário e decisivo, mantendo ordem e eficiência com uma liderança forte.", "Governante"),
            ( "Carismático e motivador, cultivando relacionamentos fortes e um ambiente de trabalho harmonioso.", "Amante"),
            ( "Divertido e acessível, criando um ambiente de trabalho leve e estimulante para todos.", "Bobo da Corte"),
            ( "Prático e inclusivo, focando em construir uma cultura de igualdade e colaboração.", "Cara Comum"),
            ( "Idealista e otimista, sempre buscando o melhor nos outros e promovendo um ambiente positivo.", "Inocente"),
            ( "Aventureiro e flexível, encorajando a equipe a pensar fora da caixa e a explorar novas oportunidades.", "Explorador"),
            ( "Reflexivo e informado, liderando com sabedoria e buscando sempre compartilhar conhecimentos.", "Sábio"),
        ]
    },
        {
        "question": "Você tem um dom, qual dessas opções abaixo mais diz sobre você?",
        "answers": [
            ( "Capacidade de questionar e mudar o que muitos aceitam como certo.", "Rebelde"),
            ( "Habilidade de enxergar e criar soluções onde outros veem problemas.", "Mago"),
            ( "Força para enfrentar desafios e proteger os outros.", "Herói"),
            ( "Empatia para entender e cuidar profundamente das necessidades alheias.", "Cuidador"),
            ( "Criatividade para manifestar ideias e trazer novidade ao mundo.", "Criador"),
            ( "Liderança para dirigir e inspirar pessoas em direção a um objetivo comum.", "Governante"),
            ( "Capacidade de criar e manter conexões profundas e significativas.", "Amante"),
            ( "Alegria contagiante e habilidade para ver o lado positivo da vida.", "Bobo da Corte"),
            ( "Honestidade e autenticidade que inspiram confiança e respeito.", "Cara Comum"),
            ( "Visão otimista e pura que traz esperança para os ambientes.", "Inocente"),
            ( "Curiosidade insaciável e desejo de explorar o desconhecido.", "Explorador"),
            ( "Sabedoria profunda e a capacidade de compartilhar conhecimento de forma clara e útil.", "Sábio"),
        ]
    },
]

# Function to generate the PDF
# def generate_pdf(top_3_categories):
#     buffer = BytesIO()
#     p = canvas.Canvas(buffer, pagesize=letter)
    
#     logo_path = "img/Logo fundo branco 2.png"  # Replace with your logo image path
#     p.drawImage(ImageReader(logo_path), x=100, y=625, width=400, height=200)  # Adjust position and size as needed
    
#     p.drawString(100, 550, "Parabéns por completar a Jornada dos Arquétipos!")
#     p.drawString(100, 530, "")
#     p.drawString(100, 510, "Seus resultados revelaram os arquétipos que dominam sua personalidade e influenciam")
#     p.drawString(100, 490, "suas escolhas e estilo de vida.")
    
#     for idx, (category, count) in enumerate(top_3_categories, start=1):
#         p.drawString(100, 480 - idx * 20, f"{idx}. {category} - {count / len(qt.questions):.0%}")
    
#     p.save()
#     buffer.seek(0)
#     return buffer

def get_whatsapp_link(top_3_categories):
    # Monta a mensagem com os 3 arquétipos
    msg = "Olá, descobri os meus arquétipos dominantes e quero saber como posso usa-los para ter mais autenticidade no digital.\n"
    for idx, (category, count) in enumerate(top_3_categories, start=1):
        msg += f"{idx}. {category} ({count / max_points:.0%})\n"
    # Codifica a mensagem para URL
    import urllib.parse
    encoded_msg = urllib.parse.quote(msg)
    # Retorna o link do WhatsApp com a mensagem preenchida
    return f"https://wa.me/5511988418211?text={encoded_msg}"  # Troque pelo número desejado

# Initialize session state variables if not set
if 'question_index' not in st.session_state:
    st.session_state['question_index'] = 0

if 'responses' not in st.session_state:
    st.session_state['responses'] = []
    
if 'survey_started' not in st.session_state:
    st.session_state['survey_started'] = False
    
double_index = [0, 9, 10, 11]
max_points = len(qt.questions) + len(double_index)

# Helper function to display a question
def display_question(question_index):
    question_data = qt.questions[question_index]
    question_text = question_data["question"]
    answer_options = question_data["answers"]

    st.image('img/mapa_do_posicionamento.png')
    st.header(f"{question_text}")
    
    selected_answer = st.radio(
        ' ',
        [answer[0] for answer in answer_options],
        key=f"question_{question_index}"
    )

    # Handle the "Next" button without needing a form
    if st.button("Próxima", key=f"next_{question_index}"):
        if selected_answer:
            weight = 2 if question_index in double_index else 1
            
            # Save the selected category in the responses list
            for answer, category in answer_options:
                if selected_answer == answer:
                    st.session_state['responses'].append((category, weight))
                    break

            # Move to the next question
            st.session_state['question_index'] += 1
            st.rerun()

# Display the introduction page if the survey hasn't started yet
if not st.session_state['survey_started']:
    st.image('img/mapa_do_posicionamento.png')
    st.title("Seja bem-vinda!")
    st.markdown("""
        
        Parabéns por dar o primeiro passo em direção ao autoconhecimento e à sua verdadeira essência.
        Este teste foi criado para ajudá-la a descobrir seus três arquétipos dominantes — forças internas que influenciam sua forma de se expressar, de tomar decisões e de se relacionar com o mundo.

        📝 Como funciona?
        - Responda às perguntas com calma e sinceridade.
        - Não existe certo ou errado: escolha aquilo que mais ressoa com você.
        - Confie na sua primeira impressão — ela costuma ser a voz mais fiel da sua intuição.

        Ao final, você terá uma visão clara dos arquétipos que guiam sua jornada. Esse conhecimento vai iluminar não apenas quem você é, mas também como alinhar sua imagem, escolhas e posicionamento com seus valores mais autênticos.

        Está pronta? Vamos começar essa jornada de descoberta juntas!
    """)
    
    if st.button("Começar"):
        st.session_state['survey_started'] = True
        st.rerun()

# If the survey has started, display questions
elif st.session_state['question_index'] < len(qt.questions):
    display_question(st.session_state['question_index'])
else:
     # All questions answered, calculate the weighted results
    category_count = Counter()
    for category, weight in st.session_state['responses']:
        category_count[category] += weight
        
    # Get the top 3 categories
    top_3_categories = category_count.most_common(3)
    
    st.image('img/mapa_do_posicionamento.png')
    st.header("Aqui está o seu Mapa do Posicionamento!")
    st.markdown("""
            É bem importante você tirar um print deste resultado pois ele não ficará salvo.
            Com esses dados em mãos, você poderá alinhar sua imagem, comunicação e estratégias de marketing com os arquétipos que mais ressoam com você.
                """)
    
    for idx, (category, count) in enumerate(top_3_categories, start=1):
        # st.write(f"{idx}. {category} - {count / len(questions):.0%}")
        
        st.markdown("""
        <style>
        .big-font {
            font-size:30px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown(f'<p class="big-font">{idx}. {category} - {count / max_points:.0%}</p>', unsafe_allow_html=True)
        st.markdown(archetype_descriptions[category])
        st.markdown("---")
        
    st.markdown("""
            Você já deu o primeiro passo: entendeu quais arquétipos guiam sua essência.

            O próximo é aprender como aplicar seus arquétipos no seu posicionamento de imagem e comunicação.
                """)
        
    col1, col2 = st.columns(2)
    # with col1:
    #     # Option to download the PDF
    #     pdf_buffer = generate_pdf(top_3_categories)
    #     st.download_button(
    #         label="Baixar resultado",
    #         data=pdf_buffer,
    #         file_name="survey_results.pdf",
    #         mime="application/pdf"
    #     )
        
    # VIDEO_URL = "https://youtu.be/lIGBBWrSOd8?si=v84scV_p9YjQSFTt"
    # st.video(VIDEO_URL)
    
    # st.markdown("""
    # **Tenho uma proposta especial para você:**
 
    # Um acompanhamento por seis meses onde trabalharemos juntas para afinar sua marca e comunicação, alinhando tudo com os arquétipos que definem quem você é.
    # Este processo não apenas reforçará sua autenticidade, mas também atrairá o público certo para o seu negócio, transformando sua visibilidade e impacto no mercado.

    #             """)

    with col1:
        wa_link = get_whatsapp_link(top_3_categories)
        st.markdown(f"""
        <a href="{wa_link}" target="_blank">
            <button style="background-color:#25D366;color:white;padding:12px 24px;border:none;border-radius:6px;font-size:18px;cursor:pointer;">
                Descubra como!
            </button>
        </a>
        """, unsafe_allow_html=True)
        
    # Option to restart the quiz
    with col2:
        if st.button("Fazer novamente"):
            st.session_state['question_index'] = 0
            st.session_state['responses'] = [None] * len(qt.questions)
            st.session_state['survey_started'] = False
            st.rerun()