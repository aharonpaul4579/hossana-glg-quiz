import streamlit as st

# 🔹 Page setup
st.set_page_config(page_title="తెలుగు బైబిల్ క్విజ్", page_icon="📖")

# 🔹 Colorful background
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(to right, #fbc2eb, #a6c1ee);
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)

# 🔹 Bold headline
st.markdown("<h1 style='text-align: center; color: #FF5733;'>HOSSANA GLG MINISTRES</h1>", unsafe_allow_html=True)
st.markdown("### కఠినమైన బైబిల్ ప్రశ్నలు. ప్రతి ప్రశ్నకు ఒకసారి మాత్రమే సమాధానం ఎంచుకోవచ్చు. సమర్పించిన తర్వాత మీ స్కోర్ మరియు సరైన ప్రశ్నల సంఖ్యలు చూపబడతాయి.")

# 🔹 Hard-level questions
questions = [
    {"q": "ప్రకటన గ్రంథంలో ఏ సంఖ్య ఎక్కువగా ప్రస్తావించబడుతుంది?", "options": ["7", "12", "40"], "answer": 0},
    {"q": "యోహాను ప్రకటనలో ఏ దేవదూతలు శంఖాలు ఊదతారు?", "options": ["7", "4", "10"], "answer": 0},
    {"q": "యెషయా ప్రవక్త గ్రంథంలో మషీయకు సంబంధించిన ప్రవచనం ఏ అధ్యాయంలో ఉంది?", "options": ["53", "40", "9"], "answer": 0},
    {"q": "యేసు శిలువ వేయబడినప్పుడు ఎన్ని గంటలు చీకటి ఏర్పడింది?", "options": ["3", "6", "9"], "answer": 0},
    {"q": "బైబిల్ ప్రకారం 'అన్యజనుల లైటు'గా ఎవరు పిలవబడ్డారు?", "options": ["పౌలు", "పేతురు", "యోహాను"], "answer": 0},
    {"q": "యోహాను సువార్తలో 'ఆది'లో ఉన్న వాక్యం ఏమిటి?", "options": ["ఆది లో వాక్యం ఉన్నది", "ఆది లో దేవుడు ఉన్నాడు", "ఆది లో దేవుని వాక్యం"], "answer": 0},
    {"q": "యేసు ఎన్ని శాపన వాక్యాలు పలికాడు?", "options": ["7", "8", "9"], "answer": 1},
    {"q": "యేసు ఎవరిని 'సత్యం, మార్గం, జీవం' అని పిలిచాడు?", "options": ["తనను", "పౌలు", "యోహాను"], "answer": 0},
    {"q": "యేసు ఎన్ని సార్లు గెత్సెమనే తోటలో ప్రార్థించాడు?", "options": ["1", "2", "3"], "answer": 2},
    {"q": "యోహాను ప్రకటనలో 'బబులోను'కు సంబంధించిన దృష్టి ఎక్కడ ఉంది?", "options": ["అధ్యాయం 17", "అధ్యాయం 12", "అధ్యాయం 20"], "answer": 0},
    {"q": "యేసు శిలువపై పలికిన చివరి మాట ఏమిటి?", "options": ["ఇది పూర్తయింది", "నన్ను క్షమించు", "నా ఆత్మను నీకు అప్పగిస్తున్నాను"], "answer": 0},
    {"q": "యేసు పునరుత్థానమైన తర్వాత ఎవరికి మొదట కనిపించాడు?", "options": ["పేతురు", "మేరీ మగ్దలేనా", "యోహాను"], "answer": 1},
    {"q": "యేసు ఎన్ని సార్లు తన పునరుత్థానాన్ని ముందుగా ప్రకటించాడు?", "options": ["2", "3", "4"], "answer": 1},
    {"q": "యేసు ఎన్ని శిష్యులకు పునరుత్థానమైన తర్వాత కనిపించాడు?", "options": ["11", "12", "500"], "answer": 2},
    {"q": "యేసు ఎక్కడ నుండి పరలోకానికి ఎక్కాడు?", "options": ["బేతానీ", "గలిలయ", "యెరూషలేము"], "answer": 0}
]

# 🔹 Collect locked answers
user_answers = []

for i, q in enumerate(questions):
    st.subheader(f"ప్రశ్న {i+1}")

    if f"locked_{i}" not in st.session_state:
        selected = st.radio(q["q"], q["options"], key=f"q{i}")
        if st.button(f"ఎంచుకోండి {i+1}", key=f"lock{i}"):
            st.session_state[f"locked_{i}"] = selected
    else:
        st.markdown(f"**మీ ఎంపిక:** {st.session_state[f'locked_{i}']} ✅")

    user_answers.append(st.session_state.get(f"locked_{i}", None))

# 🔹 Submit button and scoring
if st.button("✅ సమర్పించండి"):
    score = 0
    correct_numbers = []

    for i, q in enumerate(questions):
        if user_answers[i] == q["options"][q["answer"]]:
            score += 1
            correct_numbers.append(str(i + 1))

    st.success(f"🎉 మీ స్కోర్: {score} పాయింట్లు")

    if correct_numbers:
        st.markdown("✅ attempt చేసిన ప్రశ్నల్లో సరైన ప్రశ్నల సంఖ్యలు:")
        st.markdown("**" + ", ".join(correct_numbers) + "**")