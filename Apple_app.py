# apple_brief_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Apple: 2015→2024 Strategic Brief", layout="wide")

# ---------- Header ----------
st.title("Apple: 2015 → 2024 — Strategic Evolution (Interactive Brief)")
st.markdown("An interactive, lightweight briefing that maps the 2015 Harvard case learnings to Apple's actions through 2024.")

# ---------- Key Financial Snapshot (editable) ----------
st.markdown("### FY 2024 Key Financial Figures (editable)")
col1, col2, col3,= st.columns(3)
with col1:
    revenue = st.metric("Annual Revenue (US$ bn)", "391")
with col2:
    net_income = st.metric("Net Income (US$ bn)", "93.7")
with col3:
    q4_rev = st.metric("Q4 2024 Revenue (US$ bn)","94.9")

st.divider()

# ---------- Controls / View selection ----------
view = st.radio("Choose view", options=["Overview", "Timeline", "Charts & Data", "Learnings"], index=0)

# ---------- Data (hardcoded but editable) ----------
asp_df = pd.DataFrame({
    "year": [2015, 2018, 2021, 2024],
    "asp": [600, 700, 800, 920]
})

rev_mix_2015 = pd.DataFrame({
    "segment": ["iPhone", "iPad", "Mac", "Other"],
    "share": [69, 15, 7, 9]
})

rev_mix_2024 = pd.DataFrame({
    "segment": ["iPhone", "Services", "Wearables,Home & Accessories","Mac","iPad"],
    "share": [51, 25, 9, 8, 7]
})

timeline_items = [
    (2015, "Case snapshot: iPhone ≈69% revenue — Watch & Pay introduced"),
    (2016, "Services push: Apple Music growth & App Store monetization"),
    (2019, "Wearables surge: AirPods & Watch mass adoption"),
    (2020, "Apple Silicon (M1) — vertical integration"),
    (2021, "Services & subscriptions scale up"),
    (2023, "Health & Wallet expansions"),
    (2024, "Spatial compute (Vision Pro) and AI initiatives")
]

# ---------- Views ----------
if view == "Overview":
    st.header("Overview — 2015 crossroad and 2024 outcomes")
    colA, = st.columns([2,1])
    with colA:
        st.markdown("""
        **2015 (Case):** heavy dependence on iPhone (~69% revenue), slowing iPad & iPod, new ecosystem plays (Watch, Pay), fierce competition (Samsung premium, Xiaomi low-cost).  
        
        **Strategy questions then:** How to reduce product concentration risk, keep innovation velocity, and sustain margins in price-sensitive markets like India?
        """)
        st.markdown("**2024 (Outcome highlights):**")
        st.write("- iPhone remains core but Services and Wearables have materially grown")
        st.write("- Apple Silicon improved margin control and product differentiation")
        st.write("- Services (App Store, Music, TV+, iCloud, Fitness+) provide recurring, high-margin revenue")

elif view == "Timeline":
    st.header("Strategic Timeline (2015 → 2024)")
    for y, note in timeline_items:
        st.markdown(f"**{y}** — {note}")

elif view == "Charts & Data":
    st.header("Charts & Data")

    st.subheader("ASP Trend (Average Selling Price)")
    fig = px.line(asp_df, x="year", y="asp", markers=True, title="iPhone ASP Trend (illustrative)")
    fig.update_layout(yaxis_title="ASP (US$)")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Revenue Mix — toggle between 2015 and 2024")
    choice = st.radio("Select year", options=["2015", "2024"], index=0)
    if choice == "2015":
        fig2 = px.bar(rev_mix_2015, x="share", y="segment", orientation="h", text="share",
                      labels={"share":"% of Revenue","segment":"Segment"}, title="Revenue Mix — 2015 (case)")
        fig2.update_traces(texttemplate='%{text}%', textposition='outside')
        st.plotly_chart(fig2, use_container_width=True)
    else:
        fig3 = px.bar(rev_mix_2024, x="share", y="segment", orientation="h", text="share",
                      labels={"share":"% of Revenue","segment":"Segment"}, title="Revenue Mix — 2024 (illustrative)")
        fig3.update_traces(texttemplate='%{text}%', textposition='outside')
        st.plotly_chart(fig3, use_container_width=True)

    st.markdown("**Tables (raw data)**")
    st.write("ASP data")
    st.table(asp_df)
    st.write("Rev mix 2015")
    st.table(rev_mix_2015)
    st.write("Rev mix 2024")
    st.table(rev_mix_2024)

elif view == "Learnings":
    st.header("Three Key Learnings (Case → Strategy)")
    st.markdown("**1) Ecosystem Innovation** — shift from single-hit product innovation to experience & platform orchestration (Watch, Wallet, Health).")
    st.markdown("**2) Value-Based Profitability** — maintain premium ASPs and margins while using profits to fund services and R&D.")
    st.markdown("**3) Diversification & R&D** — Apple Silicon, wearables, services and new platforms (spatial computing/AI) reduce single-product risk.")

    
st.markdown("---")
st.caption("This mini-app uses illustrative numbers for charts; replace data with official financials or company filings for final deliverable.")
