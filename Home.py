import streamlit as st
from st_supabase_connection import SupabaseConnection

# Initialize connection
conn = st.connection("supabase", type=SupabaseConnection)

# Set page configuration
st.set_page_config(
    page_title="Învățare C++ | Acasă",
    page_icon="🏠",
    layout="wide"
)

# Title and Introduction
st.title("Învățare C++ pentru Liceu 📚")

st.markdown("""
## Bine ați venit la platforma de învățare C++!

Această platformă este concepută pentru a ajuta elevii de liceu să învețe programare în C++, 
urmând programa școlară pentru clasele a IX-a, a X-a și a XI-a.

### Ce oferim:

#### 🎯 Clasa a IX-a
- Introducere în programare
- Structuri de control
- Tipuri de date fundamentale
- Operatori și expresii
- Algoritmi elementari

#### 📚 Clasa a X-a
- Tablouri unidimensionale și bidimensionale
- Funcții și modularizare
- Șiruri de caractere
- Structuri de date complexe
- Recursivitate

#### 💡 Clasa a XI-a
- Programare orientată pe obiecte
- Structuri de date dinamice
- Fișiere
- Algoritmi avansați
- Tehnici de programare

### Cum să folosești platforma:
1. Alege clasa ta din meniul din stânga
2. Urmărește lecțiile în ordine
3. Rezolvă exercițiile propuse
4. Verifică soluțiile tale

### Sfaturi pentru învățare:
- Practică în mod regulat
- Încearcă să rezolvi exercițiile singur înainte de a verifica soluțiile
- Participă activ la discuții și pune întrebări
- Creează-ți propriile programe pentru a-ți testa cunoștințele

> "Programarea nu este despre taste, ci despre gândire." - Edsger Dijkstra
""")

# Footer
st.markdown("---")
st.markdown("Dezvoltat cu ❤️ pentru elevii pasionați de informatică")
