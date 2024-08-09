import streamlit as st
from streamlit_chat import message
from ui_components.pages import code_chat, evaluate

st.title("AI-Powered Node Generation")
st.subheader("A node generation engine by Vishwaas")


# Initialise session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "assistant"}
    ]
if 'model_name' not in st.session_state:
    st.session_state['model_name'] = []


clear_button = st.button("Clear Conversation", key="clear")

base_path = None
create_collection_id = None
create_collection_button = None


if clear_button:
    st.session_state['generated'] = []
    st.session_state['past'] = []
    st.session_state['messages'] = [
        {"role": "assistant"}
    ]
    st.session_state['model_name'] = []

def generate_response(prompt):
    """
    Runs the model with the user prompt and appends to the chat window in the UI
    :param prompt: User prompt
    :type prompt: str
    :return: response from the system
    :rtype: str
    """
    st.session_state['messages'].append({"role": "user", "content": prompt})
    response = code_chat(st.session_state['messages'][-1]["content"])
    st.session_state['messages'].append({"role": "assistant", "content": response['response']})
    return response['response']

# container for chat history
response_container = st.container()
# container for text box
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("You:", key='input', height=100)
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        output = generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
        st.session_state['model_name'].append('llama3.1')


if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))

st.write("Evaluate:")
actual = st.text_input("Actual Node Sequence (Space separated)", placeholder="[OnClick] [Delay] [Navigate] ...")
predicted = st.text_input("Predicted Node Sequence (Space separated)", placeholder="[OnClick] [Delay] [Navigate] ...")
evaluate_btn = st.button("Evaluate", key="evaluate_btn")

if evaluate_btn:
    if actual and predicted:
        scores = evaluate(actual, predicted)
        bleu = scores['BLEU']
        rouge = scores['ROUGE']
        ed_dist = scores['EDIT_DISTANCE']
        st.write(f'Evaluation Result: ')
        st.write(f'\nBLEU: {bleu}')
        st.write(f'\nROUGE: {rouge}')
        st.write(f'\nEDIT DISTANCE: {ed_dist}')
    else:
        st.write(f'Input cannot be empty!')
