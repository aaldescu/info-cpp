import streamlit as st

st.set_page_config(
    page_title="C++ | Clasa a XI-a",
    page_icon="💡",
    layout="wide"
)

st.title("Programa pentru Clasa a XI-a 💡")

# Sidebar navigation
st.sidebar.title("Navigare Clasa a XI-a")
main_topic = st.sidebar.selectbox(
    "Alege un capitol:",
    ["Teoria Grafurilor - Concepte",
     "Teoria Grafurilor - Algoritmi",
     "Structuri Arborescente",
     "Metode de Programare",
     "Programare Orientată pe Obiecte"]
)

# Main content based on selection
if main_topic == "Teoria Grafurilor - Concepte":
    st.header("Teoria Grafurilor - Concepte Fundamentale")
    st.markdown("""
    ### 1. Terminologie de Bază
    - Graf neorientat și orientat
    - Lanț și drum (elementar/neelementar)
    - Ciclu și circuit (elementar/neelementar)
    - Grad, conexitate, tare conexitate
    - Arbore și arbore parțial
    
    ### 2. Tipuri Speciale de Grafuri
    - Graf complet
    - Graf hamiltonian
    - Graf eulerian
    - Graf bipartit
    - Graf turneu
    
    ### 3. Reprezentarea Grafurilor
    - Matrice de adiacență
    - Liste de adiacență
    - Lista muchiilor
    - Matricea costurilor
    """)

elif main_topic == "Teoria Grafurilor - Algoritmi":
    st.header("Teoria Grafurilor - Algoritmi")
    st.markdown("""
    ### 1. Parcurgerea Grafurilor
    - Algoritmul BFS (Breadth-First Search)
    - Algoritmul DFS (Depth-First Search)
    - Implementare și aplicații
    
    ### 2. Componente Conexe
    - Determinarea componentelor conexe (graf neorientat)
    - Determinarea componentelor tare conexe (graf orientat)
    - Matricea lanțurilor/drumurilor
    
    ### 3. Drumuri de Cost Minim
    - Algoritmul lui Dijkstra
    - Algoritmul Roy-Floyd
    - Arbori parțiali de cost minim
    - Algoritmul lui Kruskal
    - Algoritmul lui Prim
    """)

elif main_topic == "Structuri Arborescente":
    st.header("Structuri de Date Arborescente")
    st.markdown("""
    ### 1. Arbori cu Rădăcină
    - Definiție și proprietăți
    - Reprezentare cu referințe ascendente
    - Reprezentare cu referințe descendente
    
    ### 2. Arbori Binari
    - Definiție și proprietăți specifice
    - Reprezentare cu referințe descendente
    - Operații specifice
    
    ### 3. Tipuri Speciale de Arbori
    - Arbore binar complet
    - Arbore binar de căutare (BST)
    - Heap-uri
    """)

elif main_topic == "Metode de Programare":
    st.header("Metode de Programare")
    st.markdown("""
    ### 1. Metoda Greedy
    - Descriere generală
    - Principii de funcționare
    - Aplicații practice
    
    ### 2. Metoda Backtracking
    - Descriere și principii
    - Implementare recursivă și nerecursivă
    - Aplicații
    
    ### 3. Programare Dinamică
    - Principii și caracteristici
    - Memorare vs. Timp
    - Aplicații clasice
    """)

else:  # Programare Orientată pe Obiecte
    st.header("Programare Orientată pe Obiecte")
    st.markdown("""
    ### 1. Clase și Obiecte
    - Definirea claselor
    - Crearea obiectelor
    - Membri și metode
    
    ### 2. Principii POO
    - Încapsulare
    - Moștenire
    - Polimorfism
    - Abstractizare
    """)

# Add a code example section
with st.expander("Vezi exemplu de cod"):
    if main_topic == "Teoria Grafurilor - Algoritmi":
        st.code('''
// Implementare BFS în C++
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

class Graf {
    int V; // număr de noduri
    vector<vector<int>> adj; // liste de adiacență
    
public:
    Graf(int V) {
        this->V = V;
        adj.resize(V);
    }
    
    void adaugaMuchie(int v, int w) {
        adj[v].push_back(w);
    }
    
    void BFS(int s) {
        vector<bool> vizitat(V, false);
        queue<int> coada;
        
        vizitat[s] = true;
        coada.push(s);
        
        while(!coada.empty()) {
            s = coada.front();
            cout << s << " ";
            coada.pop();
            
            for(int i : adj[s]) {
                if(!vizitat[i]) {
                    vizitat[i] = true;
                    coada.push(i);
                }
            }
        }
    }
};

int main() {
    Graf g(4);
    g.adaugaMuchie(0, 1);
    g.adaugaMuchie(0, 2);
    g.adaugaMuchie(1, 2);
    g.adaugaMuchie(2, 0);
    g.adaugaMuchie(2, 3);
    g.adaugaMuchie(3, 3);
    
    cout << "Parcurgere BFS începând cu nodul 2: ";
    g.BFS(2);
    return 0;
}
''', language='cpp')
    elif main_topic == "Structuri Arborescente":
        st.code('''
// Implementare Arbore Binar de Căutare
#include <iostream>
using namespace std;

struct Nod {
    int cheie;
    Nod *stanga, *dreapta;
    
    Nod(int item) {
        cheie = item;
        stanga = dreapta = nullptr;
    }
};

class ArboreBinarCautare {
    Nod* radacina;
    
    Nod* insereazaRec(Nod* nod, int cheie) {
        if (nod == nullptr)
            return new Nod(cheie);
            
        if (cheie < nod->cheie)
            nod->stanga = insereazaRec(nod->stanga, cheie);
        else if (cheie > nod->cheie)
            nod->dreapta = insereazaRec(nod->dreapta, cheie);
            
        return nod;
    }
    
public:
    ArboreBinarCautare() { radacina = nullptr; }
    
    void insereaza(int cheie) {
        radacina = insereazaRec(radacina, cheie);
    }
};
''', language='cpp')
