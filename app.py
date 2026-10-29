import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="JAMB PRO - Score 350+", page_icon="🎓", layout="centered")

# === PASTE YOUR 3 CODES HERE AFTER YOU CREATE ACCOUNTS ===
# Leave empty for now, app still works

ADCASH_ZONE = """PASTE ADCASH CODE HERE"""
MONETAG_ZONE = """PASTE MONETAG CODE HERE"""
HILLTOPADS_ZONE = """PASTE HILLTOPADS CODE HERE"""

PAYSTACK_LINK = "https://paystack.shop/pay/jambpro-premium"
WHATSAPP_LINK = "https://wa.me/234000000000?text=I%20want%20JAMB%20PRO%20Premium"

st.title("🎓 JAMB PRO")
st.caption("Earn while you learn - Ads support free JAMB prep")

# Ad 1 - HilltopAds Pop (invisible, pays highest - counts every visitor)
if "PASTE" not in HILLTOPADS_ZONE:
    components.html(HILLTOPADS_ZONE, height=0)

# Your questions - Add more to make students stay longer = more ad money
QUESTIONS = [
    {"q": "What is the capital of Nigeria?", "options": ["Lagos", "Abuja", "Kano", "Port Harcourt"], "a": 1},
    {"q": "Solve 2x+3=7", "options": ["1","2","3","4"], "a": 1},
    {"q": "JAMB means?", "options": ["Joint Admissions and Matriculation Board", "Joint Admission Board", "JAMB Board", "Admission Board"], "a": 0},
]

score = st.session_state.get('score', 0)
q_index = st.session_state.get('q_index', 0)

if q_index < len(QUESTIONS):
    q = QUESTIONS[q_index]
    st.subheader(f"Question {q_index+1}")
    st.write(f"**{q['q']}**")
    choice = st.radio("Choose:", q['options'], key=q_index)
    if st.button("Submit", type="primary", use_container_width=True):
        if q['options'].index(choice) == q['a']:
            st.success("Correct! +10")
            st.session_state['score'] = score + 10
        else:
            st.error(f"Answer: {q['options'][q['a']]}")
        st.session_state['q_index'] = q_index + 1
        st.rerun()

    # Ad 2 - Monetag Banner - shows after question = more views
    st.divider()
    if "PASTE" not in MONETAG_ZONE:
        components.html(MONETAG_ZONE, height=90)
else:
    st.balloons()
    st.success(f"Done! Score {score}/{len(QUESTIONS)*10}")
    if st.button("Restart Quiz", use_container_width=True):
        st.session_state['q_index'] = 0
        st.session_state['score'] = 0
        st.rerun()

# Ad 3 - AdCash Banner - bottom = counts again
if "PASTE" not in ADCASH_ZONE:
    components.html(ADCASH_ZONE, height=90)

st.divider()
st.subheader("🔓 Unlock Premium")
col1, col2 = st.columns(2)
with col1:
    st.link_button("Pay N1500 - Paystack", PAYSTACK_LINK, use_container_width=True)
with col2:
    st.link_button("VIP WhatsApp N1000", WHATSAPP_LINK, use_container_width=True)

st.caption("Weekly target: $10 per network = N41k/week to your OPay")
