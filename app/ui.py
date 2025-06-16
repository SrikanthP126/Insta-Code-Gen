import streamlit as st
from app.llm_chain import get_llm_response
from app.mcp import build_mcp_context

def run():
    st.set_page_config(page_title='Insta Code Gen 🚀', layout='centered')
    st.title("💻 Insta Code Gen")
    st.write("Multilingual AI coding assistant powered by Groq + LangChain")

    # Sidebar config
    st.sidebar.header('⚙️ Settings')
    task_type = st.sidebar.selectbox('Task Type', ['generate_code', 'explain_code', 'debug_code'])
    code_lang = st.sidebar.selectbox('Programming Language', ['Python', 'JavaScript', 'Java', 'C++', 'Go', 'Rust', 'C#', 'Swift'])
    user_level = st.sidebar.radio('User Level', ['beginner', 'intermediate', 'expert'])

    # Prompt Input
    user_prompt = st.text_area('Enter your prompt', height=150)

    # Button to trigger
    if st.button('Generate'):
        with st.spinner('Generating with Groq...'):
            # Build structured system prompt using MCP
            system_context = build_mcp_context(
                task_type=task_type,
                language=code_lang,
                user_level=user_level,
                user_input=user_prompt
            )

            # Send to LLM
            response = get_llm_response(user_prompt, system_context=system_context)

            # Show output
            st.success('Here is your result:')
            st.code(response, language=code_lang.lower())
