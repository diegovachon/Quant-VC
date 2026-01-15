import streamlit as st
import ollama
import time

# Page configuration
st.set_page_config(
    page_title="Deal Flow Analyzer AI",
    layout="wide"
)

st.title("Deal Flow Analyzer (Edge AI)")
st.markdown("""
Propulsé par Raspberry Pi 5 and Llama-3
Collez la description de la startup ci-dessous pour générer un mémo d'investissement structuré en temps réel.
""")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Description de la startup")
    startup_pitch = st.text_area(
        "Collez le texte ici :",
        height=400,
        placeholder="Ex: UberForDogs est une application mobile qui permet de trouver un promeneur"
    )
    analyze_button = st.button("Générer le mémo d'investissement", type="primary")

with col2:
    st.subheader("Mémo structuré")
    memo_container = st.empty()

    if analyze_button and startup_pitch:
        memo_container.info("Analyse en cours sur le Neural Engine du Pi 5... Veuillez patienter.")
        start_time = time.time()

        try:
           response = ollama.chat(model='vc-bot', messages=[
             {
               'role': 'user',
               'content': startup_pitch,
             },
           ])

           end_time = time.time()
           duration = round(end_time - start_time, 2)

           memo_container.success(f"Analyse terminée en {duration} secondes.")
           st.markdown("---")
           st.markdown(response['message']['content'])

        except Exception as e:
           memo_container.error(f"Erreur lors de l'analyse : {e}")

    elif analyze_button and not startup_pitch:
        memo_container.warning("Veuillez coller une description avant de lancer l'analyse")

st.markdown("---")
st.caption("Système d'aide à la décision 'Due Diligence' - Edge Computing Prototype")
