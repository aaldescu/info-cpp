import streamlit as st
from st_supabase_connection import SupabaseConnection

# Initialize connection
conn = st.connection("supabase", type=SupabaseConnection)

# Your Streamlit app code starts here
st.title("My Streamlit App")

# Example: Query data from a table using SQL
@st.cache_data(ttl=600)  # Cache data for 10 minutes
def load_data(query):
    try:
        return conn.query(query).execute()
    except Exception as e:
        st.error(f"Error querying data: {str(e)}")
        return None

# Example: Insert data into a table
def insert_data(table_name, data):
    try:
        return conn.table(table_name).insert(data).execute()
    except Exception as e:
        st.error(f"Error inserting data: {str(e)}")
        return None

# Example: Get authenticated user
user = conn.auth.get_user() if conn.auth.get_session() else None

# Authentication status
if user:
    st.success("Authenticated!")
    st.write(f"Welcome, {user.email}")
    
    # Example: Display data from a table
    if st.button("Load Data"):
        # Replace with your actual table name
        data = load_data("SELECT * FROM your_table LIMIT 10")
        if data:
            st.dataframe(data)
            
    # Example: Real-time changes
    if st.toggle("Listen for changes"):
        subscription = conn.table("your_table").on("*", lambda x: st.write("New change:", x)).subscribe()
else:
    st.warning("Not authenticated")
    
    # Example: Sign in form
    with st.form("sign_in"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        
        if st.form_submit_button("Sign In"):
            try:
                res = conn.auth.sign_in_with_password({"email": email, "password": password})
                st.success("Successfully signed in!")
                st.rerun()
            except Exception as e:
                st.error(f"Error signing in: {str(e)}")
