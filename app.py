import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(page_title="JAMB PRO MAX - No.1 CBT", page_icon="🎓", layout="centered")

# === LIVELY ANIMATED CSS ===
st.markdown("""
<style>
.card { padding:15px; border-radius:18px; margin:8px 0; box-shadow:0 4px 15px rgba(0,0,0,0.12); animation: pop 0.6s ease; transition:0.3s; cursor:pointer; }
.card:hover { transform: translateY(-3px) scale(1.02); }
@keyframes pop { 0%{opacity:0; transform: scale(0.9);} 100%{opacity:1; transform: scale(1);} }
.blue{background:#DBEAFE;} .pink{background:#FCE7F3;} .green{background:#D1FAE5;} .yellow{background:#FEF3C7;} .purple{background:#EDE9FE;} .orange{background:#FFEDD5;}
.banner { background: linear-gradient(90deg, #10B981, #065F46); color:white; padding:18px; border-radius:16px; text-align:center; font-weight:bold; }
.progress-ring { font-size:20px; text-align:center; }
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page='home'
if 'score' not in st.session_state: st.session_state.score=0
if 'q_index' not in st.session_state: st.session_state.q_index=0
if 'history' not in st.session_state: st.session_state.history=[]
if 'streak' not in st.session_state: st.session_state.streak=0

# === HEADER ===
c1,c2,c3 = st.columns([1,3,1])
with c1: st.write("🎓")
with c2: st.markdown("**TestDriller UTME** - JAMB PRO MAX")
with c3: 
    if st.button("🌙"): st.toast("Dark mode coming soon!")

st.markdown('<div class="banner">🏆 NIGERIA\'S NO.1 LEARNING APP<br>USED BY TOP SCORER - SCORE 375</div>', unsafe_allow_html=True)

# === HOME - 8 CARDS LIKE TESTDRILLER ===
if st.session_state.page=='home':
    st.markdown("#### Nigeria's No.1 Learning & Practice App!")
    r1c1,r1c2 = st.columns(2)
    with r1c1:
        if st.button("🎯 Practice For UTME\n33,500 Qs offline", use_container_width=True): 
            st.session_state.page='practice'; st.rerun()
        if st.button("🔬 Science Note\nIntelligent Note for Maths", use_container_width=True):
            st.session_state.page='note'; st.rerun()
        if st.button("📜 Result History", use_container_width=True):
            st.session_state.page='history'; st.rerun()
        if st.button("🎮 Educational Games", use_container_width=True):
            st.session_state.page='games'; st.rerun()
    with r1c2:
        if st.button("🏫 Classroom\nMaterials + AI Tutor", use_container_width=True):
            st.session_state.page='classroom'; st.rerun()
        if st.button("🔍 Question Search\nSearch quickly", use_container_width=True):
            st.session_state.page='search'; st.rerun()
        if st.button("📈 Performance Analysis", use_container_width=True):
            st.session_state.page='analysis'; st.rerun()
        if st.button("🤖 Round-the-Clock AI Tutor", use_container_width=True):
            st.session_state.page='aitutor'; st.rerun()
    
    st.divider()
    # DAILY STREAK - keeps users coming back = more ad money
    st.markdown(f'<div class="card orange">🔥 Daily Streak: <b>{st.session_state.streak} days</b> | Keep learning to keep streak!</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card purple">💰 Earn & Learn - Play games to win airtime | Ads support free learning</div>', unsafe_allow_html=True)
    
    # --- YOUR 3 AD NETWORKS ---
    # Paste codes in streamlit.components.v1.html() below after you create accounts
    # AdCash + Monetag + HilltopAds -> Paxum -> OPay

# === PRACTICE - SMOOTH INTERFACE ===
elif st.session_state.page=='practice':
    if st.button("← Back to Home"): st.session_state.page='home'; st.rerun()
    QUESTIONS = [
        {"q":"OXYZW pyramid with square base... OX=6cm, XY=4cm. Find height OT", "o":["2√5","3","4","3√2"], "a":0, "exp":"OT = √(OX² - (XY√2/2)²) = 2√5"},
        {"q":"Solve: 2x + 3y = 6, 3x - 2y = 10", "o":["x=3,y=0","x=2,y=1","x=0,y=2","x=1,y=2"], "a":0, "exp":"AI Tutor: Substitute y = (6-2x)/3..."},
        {"q":"I ___ admission to the university this year", "o":["seeking for","seeking","seeking at","seeking of"], "a":1, "exp":"'Seek' does not need 'for' when object is admission"},
        {"q":"Calculate P=2πr, r=3, π=3.142", "o":["18.85","28.27","18.84","9.42"], "a":0, "exp":"P=2×3.142×3=18.85"},
    ]
    q = QUESTIONS[st.session_state.q_index % len(QUESTIONS)]
    st.progress((st.session_state.q_index+1)/len(QUESTIONS))
    c1,c2,c3 = st.columns(3)
    c1.write(f"Q {st.session_state.q_index+1}/4"); c2.write("⏱ 00:45"); c3.write(f"Score: {st.session_state.score}")
    
    st.markdown(f'<div class="card" style="background:white; border-left:5px solid #10B981;"><b>{q["q"]}</b></div>', unsafe_allow_html=True)
    for i, opt in enumerate(q['o']):
        if st.button(f"{chr(65+i)}. {opt}", use_container_width=True, key=f"q{i}{st.session_state.q_index}"):
            if i==q['a']: 
                st.success("✅ Correct!"); st.balloons(); st.session_state.score+=10; st.session_state.streak+=1
            else: st.error(f"❌ Correct: {q['o'][q['a']]}")
            st.info(f"🤖 **AI Tutor Explanation:** {q['exp']}")
            st.session_state.history.append(1 if i==q['a'] else 0)
            time.sleep(0.5)
            st.session_state.q_index+=1
            st.rerun()

# === CLASSROOM ===
elif st.session_state.page=='classroom':
    if st.button("← Back"): st.session_state.page='home'; st.rerun()
    st.markdown("### 📚 Syllabus-based learning, crystal clear videos!")
    subjects = {"English": "🎤", "Mathematics": "🔢", "Physics": "⚛️", "Chemistry": "🧪", "Biology": "🧬", "Agric Science": "🌾"}
    for subj, icon in subjects.items():
        with st.expander(f"{icon} {subj} - 12 topics"):
            st.write("1. Comprehension 2. Lexis 3. Structure")
            if st.button(f"▶️ Watch {subj} Video", key=subj): st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# === SCIENCE NOTE - SOLVE MATH OFFLINE ===
elif st.session_state.page=='note':
    if st.button("← Back"): st.session_state.page='home'; st.rerun()
    st.markdown("### 🔬 Solve math & science equations offline with Intelligent Note")
    r = st.number_input("Enter radius r", value=3.0)
    P = 2 * 3.142 * r
    A = 3.142 * r**2
    st.markdown(f'<div class="card green">r = {r}<br>P = 2πr = {P:.2f}<br>A = πr² = {A:.2f}<br><br>Writing pad: <i>P = 2πr = {P:.2f}</i></div>', unsafe_allow_html=True)
    st.caption("✍️ Draw like real notebook - like TestDriller screenshot")

# === QUESTION SEARCH ===
elif st.session_state.page=='search':
    if st.button("← Back"): st.session_state.page='home'; st.rerun()
    query = st.text_input("🔍 Search past JAMB questions (e.g., 'pyramid', 'osmosis')")
    if query:
        st.markdown(f'<div class="card blue">Found 12 questions for "{query}"<br>1. {query} - definition?<br>2. Calculate {query}...</div>', unsafe_allow_html=True)

# === PERFORMANCE ANALYSIS - GRAPH ===
elif st.session_state.page=='analysis':
    if st.button("← Back"): st.session_state.page='home'; st.rerun()
    st.markdown("### 📈 Stay on top with detailed performance analysis!")
    # FAKE DATA FOR CHART
    df = pd.DataFrame({"Practice": [1,2,3,4,5], "Score": [45,60, st.session_state.score if st.session_state.score>0 else 65, 78, 85], "English": [40,55,60,70,80]})
    st.line_chart(df, x="Practice", y=["Score","English"])
    st.markdown(f'<div class="card yellow"><b>Practice Score</b><br>Highest: {max(df["Score"])} | Latest: {st.session_state.score}<br>Progress Trend: Going up! 🚀</div>', unsafe_allow_html=True)
    st.metric("Subject Score Trend", f"{st.session_state.score}%", "+5%")

# === RESULT HISTORY ===
elif st.session_state.page=='history':
    if st.button("← Back"): st.session_state.page='home'; st.rerun()
    st.markdown("### 📜 Result History")
    if not st.session_state.history: st.write("No history yet. Play to see here.")
    else:
        for i, s in enumerate(st.session_state.history[-10:]): st.write(f"Practice {i+1}: {'✅' if s else '❌'}")

# === AI TUTOR ROUND THE CLOCK ===
elif st.session_state.page=='aitutor':
    if st.button("← Back"): st.session_state.page='home'; st.rerun()
    st.markdown("### 🤖 Round-the-Clock AI Tutor")
    q = st.text_input("Ask anything: Solve 2x + y = 6, 3x - y = 10")
    if q:
        st.markdown("""
        **To solve system of equations:**
        1. 2x + y = 6
        2. 3x - y = 10
        **Step 1:** Add both equations
        5x = 16 => x = 3.2
        **Step 2:** Substitute for y
        y = 6 - 2(3.2) = -0.4
        """)
        st.caption("Like TestDriller AI Tutor screenshot")

# === GAMES - MILLIONAIRE ===
elif st.session_state.page=='games':
    if st.button("← Back"): st.session_state.page='home'; st.rerun()
    st.markdown("### 🎮 Boost your learning with fun educational games!")
    st.markdown('<div class="card yellow" style="text-align:center;"><h2>$ 1000</h2>2/15<br>Fill gap: I ___ admission...</div>', unsafe_allow_html=True)
    for opt in ["seeking for","seeking","seeking at","seeking of"]:
        if st.button(opt, use_container_width=True, key=f"game{opt}"): 
            st.success("Correct! Next question...") if opt=="seeking" else st.error("Try again")

# === BOTTOM NAV ===
st.divider()
c1,c2,c3,c4 = st.columns(4)
if c1.button("🎯"): st.session_state.page='practice'; st.rerun()
if c2.button("🏫"): st.session_state.page='classroom'; st.rerun()
if c3.button("📊"): st.session_state.page='analysis'; st.rerun()
if c4.button("👤"): st.toast("Profile: JAMB PRO User - Score 375 target!")

# === FOOTER FOR ADS + OPAY PAYOUT ===
st.caption("Ads: AdCash + Monetag + HilltopAds → Paxum → OPay = N37k/week per $10")
