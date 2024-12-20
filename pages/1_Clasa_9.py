import streamlit as st

st.set_page_config(
    page_title="C++ | Clasa a IX-a",
    page_icon="🎯",
    layout="wide"
)

st.title("Programa pentru Clasa a IX-a 🎯")

# Sidebar navigation
st.sidebar.title("Navigare Clasa a IX-a")
main_topic = st.sidebar.selectbox(
    "Alege un capitol:",
    ["Introducere în Informatică",
     "Bazele Programării C++",
     "Structuri de Control",
     "Prelucrarea Numerelor",
     "Prelucrarea Secvențelor",
     "Tablouri",
     "Fișiere și Aplicații Practice"]
)

# Main content based on selection
if main_topic == "Introducere în Informatică":
    st.header("Introducere în Informatică")
    st.markdown("""
    ### 1. Ce este informatica?
    - Definiție și concepte fundamentale
    - Rolul informaticii în societatea modernă
    - Domenii de aplicare
    
    ### 2. Despre C++
    - Istoric și evoluție
    - Avantaje și utilizări
    - Comparație cu alte limbaje de programare
    
    ### 3. Medii de dezvoltare (IDE-uri)
    - Ce este un IDE?
    - Instalarea CodeBlocks
    - Configurare și primii pași
    """)

elif main_topic == "Bazele Programării C++":
    st.header("Bazele Programării C++")
    st.markdown("""
    ### 1. Primul program - Hello World
    - Structura unui program C++
    - Compilare și execuție
    
    ### 2. Comentarii în programare
    - Comentarii pe o singură linie (//)
    - Comentarii pe mai multe linii (/* */)
    - Bune practici în documentare
    
    ### 3. Variabile și tipuri de date
    - Variabile locale și globale
    - Tipuri de date fundamentale
    - Declarare și inițializare
    
    ### 4. Input/Output
    - Afișarea (cout)
    - Citirea de la tastatură (cin)
    - Formatarea output-ului
    """)

elif main_topic == "Structuri de Control":
    st.header("Structuri de Control")
    st.markdown("""
    ### 1. Structuri de decizie
    - Instrucțiunea IF
    - IF-ELSE
    - IF-ELSE IF-ELSE
    - Operatori logici și relaționali
    
    ### 2. Structuri repetitive
    - Instrucțiunea WHILE
    - Instrucțiunea FOR
    - Când să folosim fiecare tip de buclă
    - Break și Continue
    """)

elif main_topic == "Prelucrarea Numerelor":
    st.header("Prelucrarea Numerelor")
    st.markdown("""
    ### 1. Prelucrarea cifrelor unui număr
    - Algoritm pentru descompunerea în cifre
    - Operații cu cifrele unui număr
    
    ### 2. Divizibilitate
    - Verificare număr prim
    - Algoritmul de determinare a divizorilor
    - Descompunerea în factori primi
    
    ### 3. Baze de numerație
    - Conversia din baza 10 în baza 2
    - Alte conversii între baze
    """)

elif main_topic == "Prelucrarea Secvențelor":
    st.header("Prelucrarea Secvențelor")
    st.markdown("""
    ### 1. Operații fundamentale
    - Determinare minim/maxim
    - Verificarea proprietăților
    - Calcul expresii
    
    ### 2. Șiruri speciale
    - Șirul lui Fibonacci
    - Generarea șirurilor recurente
    """)

elif main_topic == "Tablouri":
    st.header("Tablouri")
    st.markdown("""
    ### 1. Tablouri unidimensionale (Vectori)
    - Declarare și inițializare
    - Parcurgere și prelucrare
    - Vectori de frecvență/apariții
    
    ### 2. Tablouri bidimensionale (Matrice)
    - Declarare și parcurgere
    - Operații pe linii și coloane
    
    ### 3. Algoritmi fundamentali
    - Căutare secvențială și binară
    - Algoritmi de sortare
    - Interclasarea vectorilor
    """)

else:  # Fișiere și Aplicații Practice
    st.header("Fișiere și Aplicații Practice")
    st.markdown("""
    ### 1. Fișiere text
    - Definire și operații de bază
    - Citire și scriere
    
    ### 2. Aplicații matematice
    - Rezolvarea ecuațiilor de gradul I și II
    - Simplificarea fracțiilor
    
    ### 3. Aplicații geometrice
    - Distanța dintre două puncte
    - Aria și perimetrul triunghiului
    - Volumul corpurilor regulate
    - Centrul de greutate
    """)

# Add a code example section
with st.expander("Vezi exemplu de cod"):
    if main_topic == "Bazele Programării C++":
        st.code('''
// Primul program C++
#include <iostream>
using namespace std;

int main() {
    cout << "Hello World!" << endl;
    return 0;
}
''', language='cpp')
    elif main_topic == "Structuri de Control":
        st.code('''
// Exemplu de structuri de control
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Introduceti un numar: ";
    cin >> n;
    
    if (n > 0) {
        cout << "Numarul este pozitiv" << endl;
    } else if (n < 0) {
        cout << "Numarul este negativ" << endl;
    } else {
        cout << "Numarul este zero" << endl;
    }
    return 0;
}
''', language='cpp')
