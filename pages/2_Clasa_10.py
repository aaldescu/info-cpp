import streamlit as st

st.set_page_config(
    page_title="C++ | Clasa a X-a",
    page_icon="📚",
    layout="wide"
)

st.title("Programa pentru Clasa a X-a 📚")

# Sidebar navigation
st.sidebar.title("Navigare Clasa a X-a")
main_topic = st.sidebar.selectbox(
    "Alege un capitol:",
    ["Șiruri de Caractere",
     "Structuri și Tipuri de Date",
     "Structuri Dinamice",
     "Subprograme",
     "Divide et Impera",
     "Analiza Algoritmilor"]
)

# Main content based on selection
if main_topic == "Șiruri de Caractere":
    st.header("Șiruri de Caractere")
    st.markdown("""
    ### 1. Noțiuni de Bază
    - Declararea șirurilor de caractere
    - Citirea șirurilor de caractere
    - Particularități și limitări
    
    ### 2. Funcții Predefinite
    - strlen() - lungimea șirului
    - strcpy() - copierea șirurilor
    - strtok() - separarea șirurilor în tokens
    - Alte funcții utile
    
    ### 3. Prelucrări de Text
    - Căutarea unui subșir într-un șir
    - Transformări de text
    - Delimitarea cuvintelor
    - Operații complexe cu șiruri
    """)

elif main_topic == "Structuri și Tipuri de Date":
    st.header("Structuri și Tipuri de Date")
    st.markdown("""
    ### 1. Tipul struct
    - Definirea unei structuri
    - Declararea variabilelor de tip structură
    - Accesarea câmpurilor
    - Structuri imbricate
    
    ### 2. Stivă (Stack)
    - Conceptul de stivă
    - Operații specifice (push, pop)
    - Implementare statică
    
    ### 3. Coadă (Queue)
    - Conceptul de coadă
    - Operații specifice (enqueue, dequeue)
    - Implementare statică
    """)

elif main_topic == "Structuri Dinamice":
    st.header("Structuri de Date Alocate Dinamic")
    st.markdown("""
    ### 1. Liste Simplu Înlănțuite
    - Conceptul de listă înlănțuită
    - Operații de bază
    - Parcurgere și manipulare
    
    ### 2. Liste Dublu Înlănțuite
    - Structura nodurilor
    - Operații specifice
    - Avantaje și dezavantaje
    
    ### 3. Liste Circulare
    - Conceptul de listă circulară
    - Implementare și operații
    - Aplicații practice
    """)

elif main_topic == "Subprograme":
    st.header("Subprograme")
    st.markdown("""
    ### 1. Noțiuni Fundamentale
    - Declararea și definirea subprogramelor
    - Apelul subprogramelor
    - Transferul parametrilor
    
    ### 2. Variabile și Returnare
    - Returnarea valorilor
    - Variabile locale și globale
    - Vizibilitatea variabilelor
    
    ### 3. Recursivitate
    - Conceptul de recursivitate
    - Mecanismul recursivității
    - Implementare recursivă vs. iterativă
    - Exemple practice
    """)

elif main_topic == "Divide et Impera":
    st.header("Metoda Divide et Impera")
    st.markdown("""
    ### 1. Conceptul Divide et Impera
    - Principiul metodei
    - Etapele rezolvării
    - Aplicabilitate
    
    ### 2. Algoritmi de Sortare
    - Sortarea Rapidă (QuickSort)
    - Sortarea prin Interclasare (MergeSort)
    - Comparație și eficiență
    
    ### 3. Aplicații Practice
    - Căutare binară
    - Alte aplicații
    """)

else:  # Analiza Algoritmilor
    st.header("Analiza Algoritmilor")
    st.markdown("""
    ### 1. Eficiența Algoritmilor
    - Criterii de analiză
    - Complexitate temporală
    - Complexitate spațială
    
    ### 2. Alegerea Algoritmilor
    - Factori de decizie
    - Compararea algoritmilor
    - Optimizare
    
    ### 3. Studii de Caz
    - Analiza algoritmilor de sortare
    - Comparații practice
    - Recomandări de utilizare
    """)

# Add a code example section
with st.expander("Vezi exemplu de cod"):
    if main_topic == "Șiruri de Caractere":
        st.code('''
// Exemple de funcții pentru șiruri de caractere
#include <iostream>
#include <cstring>
using namespace std;

int main() {
    char str1[100], str2[100];
    
    // Citire șir
    cout << "Introduceți un șir: ";
    cin.getline(str1, 100);
    
    // Lungime șir
    cout << "Lungime: " << strlen(str1) << endl;
    
    // Copiere șir
    strcpy(str2, str1);
    cout << "Șirul copiat: " << str2 << endl;
    
    return 0;
}
''', language='cpp')
    elif main_topic == "Structuri Dinamice":
        st.code('''
// Exemplu de listă simplu înlănțuită
#include <iostream>
using namespace std;

struct Nod {
    int info;
    Nod* next;
};

void adaugaNod(Nod*& prim, int valoare) {
    Nod* nou = new Nod;
    nou->info = valoare;
    nou->next = prim;
    prim = nou;
}

int main() {
    Nod* prim = nullptr;
    adaugaNod(prim, 10);
    adaugaNod(prim, 20);
    
    // Parcurgere listă
    Nod* p = prim;
    while (p != nullptr) {
        cout << p->info << " ";
        p = p->next;
    }
    return 0;
}
''', language='cpp')
