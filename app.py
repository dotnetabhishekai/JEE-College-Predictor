import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="🎓 JEE College Predictor", page_icon="🎯", layout="wide")

# ── CSS ──
st.markdown("""
<style>
.stApp{background:linear-gradient(135deg,#0f0c29,#302b63,#24243e);}
h1,h2,h3{color:#f8f9fa !important;}
.metric-card{background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:20px;
    border-radius:16px;text-align:center;box-shadow:0 8px 25px rgba(0,0,0,.3);}
.metric-val{font-size:36px;font-weight:bold;}
.metric-label{font-size:14px;opacity:.85;}
.college-card{background:rgba(255,255,255,.08);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.15);
    border-radius:16px;padding:20px;margin:10px 0;color:#f8f9fa;}
.college-name{font-size:20px;font-weight:bold;color:#a29bfe;}
.college-detail{font-size:14px;color:#dfe6e9;margin:4px 0;}
.tag{display:inline-block;padding:4px 12px;border-radius:20px;font-size:12px;font-weight:bold;margin:2px;}
.tag-iit{background:#00b894;color:white;}
.tag-nit{background:#0984e3;color:white;}
.tag-iiit{background:#e17055;color:white;}
.tag-gfti{background:#6c5ce7;color:white;}
.chance-high{color:#00b894;font-weight:bold;}
.chance-med{color:#fdcb6e;font-weight:bold;}
.chance-low{color:#d63031;font-weight:bold;}
.footer{text-align:center;color:#636e72;padding:20px 0;font-size:13px;}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# COLLEGE DATABASE (Approximate JEE Advanced/Mains Ranks)
# ══════════════════════════════════════════════════════════
# Format: (College, Type, Stream, Opening Rank, Closing Rank, City, NIRF Rank)

COLLEGES_DATA = [
    # ── IITs (JEE Advanced) ──
    ("IIT Bombay", "IIT", "Computer Science", 1, 70, "Mumbai", 3),
    ("IIT Bombay", "IIT", "Electrical Engineering", 50, 250, "Mumbai", 3),
    ("IIT Bombay", "IIT", "Mechanical Engineering", 200, 800, "Mumbai", 3),
    ("IIT Bombay", "IIT", "Chemical Engineering", 600, 1500, "Mumbai", 3),
    ("IIT Bombay", "IIT", "Civil Engineering", 800, 2000, "Mumbai", 3),
    ("IIT Bombay", "IIT", "Aerospace Engineering", 300, 1000, "Mumbai", 3),

    ("IIT Delhi", "IIT", "Computer Science", 1, 80, "New Delhi", 2),
    ("IIT Delhi", "IIT", "Electrical Engineering", 60, 300, "New Delhi", 2),
    ("IIT Delhi", "IIT", "Mechanical Engineering", 250, 900, "New Delhi", 2),
    ("IIT Delhi", "IIT", "Chemical Engineering", 700, 1800, "New Delhi", 2),
    ("IIT Delhi", "IIT", "Civil Engineering", 900, 2200, "New Delhi", 2),
    ("IIT Delhi", "IIT", "Textile Engineering", 3000, 5500, "New Delhi", 2),

    ("IIT Madras", "IIT", "Computer Science", 1, 100, "Chennai", 1),
    ("IIT Madras", "IIT", "Electrical Engineering", 80, 350, "Chennai", 1),
    ("IIT Madras", "IIT", "Mechanical Engineering", 300, 1000, "Chennai", 1),
    ("IIT Madras", "IIT", "Chemical Engineering", 800, 2000, "Chennai", 1),
    ("IIT Madras", "IIT", "Civil Engineering", 1000, 2500, "Chennai", 1),
    ("IIT Madras", "IIT", "Aerospace Engineering", 400, 1200, "Chennai", 1),

    ("IIT Kanpur", "IIT", "Computer Science", 1, 120, "Kanpur", 4),
    ("IIT Kanpur", "IIT", "Electrical Engineering", 100, 400, "Kanpur", 4),
    ("IIT Kanpur", "IIT", "Mechanical Engineering", 350, 1100, "Kanpur", 4),
    ("IIT Kanpur", "IIT", "Chemical Engineering", 900, 2200, "Kanpur", 4),
    ("IIT Kanpur", "IIT", "Civil Engineering", 1200, 2800, "Kanpur", 4),
    ("IIT Kanpur", "IIT", "Aerospace Engineering", 500, 1500, "Kanpur", 4),
]

COLLEGES_DATA += [
    ("IIT Kharagpur", "IIT", "Computer Science", 1, 150, "Kharagpur", 5),
    ("IIT Kharagpur", "IIT", "Electrical Engineering", 120, 500, "Kharagpur", 5),
    ("IIT Kharagpur", "IIT", "Mechanical Engineering", 400, 1200, "Kharagpur", 5),
    ("IIT Kharagpur", "IIT", "Chemical Engineering", 1000, 2500, "Kharagpur", 5),
    ("IIT Kharagpur", "IIT", "Civil Engineering", 1300, 3000, "Kharagpur", 5),
    ("IIT Kharagpur", "IIT", "Mining Engineering", 3500, 6000, "Kharagpur", 5),

    ("IIT Roorkee", "IIT", "Computer Science", 50, 300, "Roorkee", 6),
    ("IIT Roorkee", "IIT", "Electrical Engineering", 200, 700, "Roorkee", 6),
    ("IIT Roorkee", "IIT", "Mechanical Engineering", 600, 1800, "Roorkee", 6),
    ("IIT Roorkee", "IIT", "Chemical Engineering", 1500, 3500, "Roorkee", 6),
    ("IIT Roorkee", "IIT", "Civil Engineering", 1800, 4000, "Roorkee", 6),

    ("IIT Guwahati", "IIT", "Computer Science", 80, 400, "Guwahati", 7),
    ("IIT Guwahati", "IIT", "Electrical Engineering", 300, 900, "Guwahati", 7),
    ("IIT Guwahati", "IIT", "Mechanical Engineering", 700, 2000, "Guwahati", 7),
    ("IIT Guwahati", "IIT", "Chemical Engineering", 1800, 4000, "Guwahati", 7),
    ("IIT Guwahati", "IIT", "Civil Engineering", 2000, 4500, "Guwahati", 7),

    ("IIT Hyderabad", "IIT", "Computer Science", 100, 500, "Hyderabad", 8),
    ("IIT Hyderabad", "IIT", "Electrical Engineering", 400, 1200, "Hyderabad", 8),
    ("IIT Hyderabad", "IIT", "Mechanical Engineering", 1000, 2500, "Hyderabad", 8),
    ("IIT Hyderabad", "IIT", "Chemical Engineering", 2500, 5000, "Hyderabad", 8),
    ("IIT Hyderabad", "IIT", "Civil Engineering", 2800, 5500, "Hyderabad", 8),

    ("IIT BHU Varanasi", "IIT", "Computer Science", 100, 600, "Varanasi", 10),
    ("IIT BHU Varanasi", "IIT", "Electrical Engineering", 500, 1500, "Varanasi", 10),
    ("IIT BHU Varanasi", "IIT", "Mechanical Engineering", 1200, 3000, "Varanasi", 10),
    ("IIT BHU Varanasi", "IIT", "Chemical Engineering", 2800, 5500, "Varanasi", 10),
    ("IIT BHU Varanasi", "IIT", "Civil Engineering", 3000, 6000, "Varanasi", 10),
    ("IIT BHU Varanasi", "IIT", "Ceramic Engineering", 5000, 8000, "Varanasi", 10),

    ("IIT Indore", "IIT", "Computer Science", 200, 800, "Indore", 11),
    ("IIT Indore", "IIT", "Electrical Engineering", 700, 2000, "Indore", 11),
    ("IIT Indore", "IIT", "Mechanical Engineering", 1800, 4000, "Indore", 11),
    ("IIT Indore", "IIT", "Civil Engineering", 4000, 7000, "Indore", 11),

    ("IIT Dhanbad (ISM)", "IIT", "Computer Science", 300, 1000, "Dhanbad", 12),
    ("IIT Dhanbad (ISM)", "IIT", "Electrical Engineering", 900, 2500, "Dhanbad", 12),
    ("IIT Dhanbad (ISM)", "IIT", "Mechanical Engineering", 2000, 4500, "Dhanbad", 12),
    ("IIT Dhanbad (ISM)", "IIT", "Mining Engineering", 4000, 7500, "Dhanbad", 12),
    ("IIT Dhanbad (ISM)", "IIT", "Chemical Engineering", 3500, 6500, "Dhanbad", 12),
]

COLLEGES_DATA += [
    # ── NITs (JEE Mains Rank) ──
    ("NIT Trichy", "NIT", "Computer Science", 500, 3000, "Tiruchirappalli", 9),
    ("NIT Trichy", "NIT", "Electrical Engineering", 2500, 8000, "Tiruchirappalli", 9),
    ("NIT Trichy", "NIT", "Mechanical Engineering", 5000, 12000, "Tiruchirappalli", 9),
    ("NIT Trichy", "NIT", "Chemical Engineering", 10000, 20000, "Tiruchirappalli", 9),
    ("NIT Trichy", "NIT", "Civil Engineering", 8000, 18000, "Tiruchirappalli", 9),

    ("NIT Surathkal", "NIT", "Computer Science", 800, 4000, "Mangalore", 11),
    ("NIT Surathkal", "NIT", "Electrical Engineering", 3000, 10000, "Mangalore", 11),
    ("NIT Surathkal", "NIT", "Mechanical Engineering", 6000, 15000, "Mangalore", 11),
    ("NIT Surathkal", "NIT", "Chemical Engineering", 12000, 25000, "Mangalore", 11),
    ("NIT Surathkal", "NIT", "Civil Engineering", 10000, 22000, "Mangalore", 11),

    ("NIT Warangal", "NIT", "Computer Science", 1000, 5000, "Warangal", 13),
    ("NIT Warangal", "NIT", "Electrical Engineering", 4000, 12000, "Warangal", 13),
    ("NIT Warangal", "NIT", "Mechanical Engineering", 7000, 18000, "Warangal", 13),
    ("NIT Warangal", "NIT", "Chemical Engineering", 15000, 30000, "Warangal", 13),
    ("NIT Warangal", "NIT", "Civil Engineering", 12000, 25000, "Warangal", 13),

    ("NIT Calicut", "NIT", "Computer Science", 2000, 8000, "Kozhikode", 16),
    ("NIT Calicut", "NIT", "Electrical Engineering", 6000, 16000, "Kozhikode", 16),
    ("NIT Calicut", "NIT", "Mechanical Engineering", 10000, 22000, "Kozhikode", 16),
    ("NIT Calicut", "NIT", "Civil Engineering", 15000, 30000, "Kozhikode", 16),

    ("NIT Rourkela", "NIT", "Computer Science", 1500, 6000, "Rourkela", 15),
    ("NIT Rourkela", "NIT", "Electrical Engineering", 5000, 14000, "Rourkela", 15),
    ("NIT Rourkela", "NIT", "Mechanical Engineering", 8000, 20000, "Rourkela", 15),
    ("NIT Rourkela", "NIT", "Chemical Engineering", 18000, 35000, "Rourkela", 15),
    ("NIT Rourkela", "NIT", "Civil Engineering", 14000, 28000, "Rourkela", 15),

    ("VNIT Nagpur", "NIT", "Computer Science", 2500, 9000, "Nagpur", 18),
    ("VNIT Nagpur", "NIT", "Electrical Engineering", 7000, 18000, "Nagpur", 18),
    ("VNIT Nagpur", "NIT", "Mechanical Engineering", 12000, 25000, "Nagpur", 18),
    ("VNIT Nagpur", "NIT", "Civil Engineering", 18000, 35000, "Nagpur", 18),

    ("MNNIT Allahabad", "NIT", "Computer Science", 3000, 10000, "Prayagraj", 20),
    ("MNNIT Allahabad", "NIT", "Electrical Engineering", 8000, 20000, "Prayagraj", 20),
    ("MNNIT Allahabad", "NIT", "Mechanical Engineering", 14000, 28000, "Prayagraj", 20),
    ("MNNIT Allahabad", "NIT", "Civil Engineering", 20000, 38000, "Prayagraj", 20),

    # ── IIITs (JEE Mains Rank) ──
    ("IIIT Hyderabad", "IIIT", "Computer Science", 500, 2500, "Hyderabad", 14),
    ("IIIT Hyderabad", "IIIT", "Electrical Engineering", 3000, 8000, "Hyderabad", 14),

    ("IIIT Allahabad", "IIIT", "Computer Science", 2000, 7000, "Prayagraj", 22),
    ("IIIT Allahabad", "IIIT", "Electrical Engineering", 8000, 18000, "Prayagraj", 22),

    ("IIIT Delhi", "IIIT", "Computer Science", 1500, 5000, "New Delhi", 17),
    ("IIIT Delhi", "IIIT", "Electrical Engineering", 5000, 12000, "New Delhi", 17),

    ("IIIT Bangalore", "IIIT", "Computer Science", 3000, 9000, "Bangalore", 19),
    ("IIIT Bangalore", "IIIT", "Electrical Engineering", 8000, 16000, "Bangalore", 19),

    ("IIIT Lucknow", "IIIT", "Computer Science", 5000, 15000, "Lucknow", 30),
    ("IIIT Gwalior", "IIIT", "Computer Science", 6000, 18000, "Gwalior", 35),
    ("IIIT Jabalpur", "IIIT", "Computer Science", 8000, 22000, "Jabalpur", 40),

    # ── GFTIs (JEE Mains Rank) ──
    ("BITS Pilani", "GFTI", "Computer Science", 1000, 5000, "Pilani", 8),
    ("BITS Pilani", "GFTI", "Electrical Engineering", 4000, 12000, "Pilani", 8),
    ("BITS Pilani", "GFTI", "Mechanical Engineering", 8000, 20000, "Pilani", 8),
    ("BITS Pilani", "GFTI", "Chemical Engineering", 15000, 30000, "Pilani", 8),

    ("DTU Delhi", "GFTI", "Computer Science", 2000, 8000, "New Delhi", 12),
    ("DTU Delhi", "GFTI", "Electrical Engineering", 6000, 16000, "New Delhi", 12),
    ("DTU Delhi", "GFTI", "Mechanical Engineering", 10000, 24000, "New Delhi", 12),
    ("DTU Delhi", "GFTI", "Civil Engineering", 16000, 32000, "New Delhi", 12),

    ("NSUT Delhi", "GFTI", "Computer Science", 3000, 10000, "New Delhi", 15),
    ("NSUT Delhi", "GFTI", "Electrical Engineering", 8000, 20000, "New Delhi", 15),
    ("NSUT Delhi", "GFTI", "Mechanical Engineering", 14000, 28000, "New Delhi", 15),

    ("IIIT Sri City", "GFTI", "Computer Science", 10000, 25000, "Sri City", 45),
    ("IIIT Kottayam", "GFTI", "Computer Science", 12000, 30000, "Kottayam", 50),
]

# ── Build DataFrame ──
df = pd.DataFrame(COLLEGES_DATA, columns=["College", "Type", "Stream", "Opening_Rank", "Closing_Rank", "City", "NIRF"])

def get_chance(rank, opening, closing):
    if rank <= opening:
        return "🟢 High", "chance-high"
    elif rank <= closing:
        mid = (opening + closing) / 2
        return ("🟡 Moderate", "chance-med") if rank <= mid else ("🟠 Low-Moderate", "chance-med")
    elif rank <= closing * 1.15:
        return "🔴 Slim", "chance-low"
    return "❌ Unlikely", "chance-low"

def predict(rank, exam_type, streams, college_types, category):
    """Filter and rank colleges based on user input."""
    cat_multiplier = {"General": 1.0, "OBC-NCL": 1.3, "SC": 2.0, "ST": 2.5, "EWS": 1.2, "PwD": 2.0}
    effective_rank = int(rank / cat_multiplier.get(category, 1.0))

    filtered = df.copy()
    if exam_type == "JEE Advanced (IITs)":
        filtered = filtered[filtered["Type"] == "IIT"]
    else:
        filtered = filtered[filtered["Type"] != "IIT"]

    if streams:
        filtered = filtered[filtered["Stream"].isin(streams)]
    if college_types:
        filtered = filtered[filtered["Type"].isin(college_types)]

    results = []
    for _, row in filtered.iterrows():
        chance_text, chance_class = get_chance(effective_rank, row["Opening_Rank"], row["Closing_Rank"])
        if chance_text != "❌ Unlikely":
            results.append({
                "College": row["College"], "Type": row["Type"], "Stream": row["Stream"],
                "City": row["City"], "NIRF": row["NIRF"],
                "Opening_Rank": row["Opening_Rank"], "Closing_Rank": row["Closing_Rank"],
                "Chance": chance_text, "Chance_Class": chance_class,
                "Effective_Rank": effective_rank,
            })

    result_df = pd.DataFrame(results)
    if not result_df.empty:
        chance_order = {"🟢 High": 0, "🟡 Moderate": 1, "🟠 Low-Moderate": 2, "🔴 Slim": 3}
        result_df["_sort"] = result_df["Chance"].map(chance_order)
        result_df = result_df.sort_values(["_sort", "NIRF"]).drop(columns=["_sort"])
    return result_df

# ══════════════════════════════════════════════════════════
# UI
# ══════════════════════════════════════════════════════════
st.markdown("⚠️ Cutoff ranks are approximate and based on previous years' trends. Actual cutoffs vary each year.")
st.markdown("# 🎓 JEE College Predictor")
st.markdown("##### Predict your best-fit colleges based on JEE rank, stream & category")
st.markdown("---")

# ── Sidebar Inputs ──
with st.sidebar:
    import os as _os
    if _os.path.exists("Dotnetabhishekai.png"):
        st.image("Dotnetabhishekai.png", width=80)
    st.markdown("## 🎯 Your Details")

    exam_type = st.radio("Exam Type", ["JEE Advanced (IITs)", "JEE Mains (NITs/IIITs/GFTIs)"], index=0)

    rank = st.number_input("Your All India Rank (AIR)", min_value=1, max_value=200000, value=1000, step=1)

    category = st.selectbox("Category", ["General", "OBC-NCL", "SC", "ST", "EWS", "PwD"])

    all_streams = sorted(df["Stream"].unique().tolist())
    streams = st.multiselect("Preferred Streams", all_streams, default=["Computer Science"])

    if exam_type == "JEE Advanced (IITs)":
        college_types = ["IIT"]
    else:
        available_types = ["NIT", "IIIT", "GFTI"]
        college_types = st.multiselect("College Types", available_types, default=available_types)

    st.markdown("---")
    predict_btn = st.button("🔍 Predict Colleges", use_container_width=True, type="primary")

# ── Main Content ──
if predict_btn or "results" in st.session_state:
    if predict_btn:
        st.session_state.results = predict(rank, exam_type, streams, college_types, category)
        st.session_state.input_rank = rank
        st.session_state.input_cat = category
        st.session_state.input_exam = exam_type

    results = st.session_state.get("results", pd.DataFrame())
    input_rank = st.session_state.get("input_rank", rank)
    input_cat = st.session_state.get("input_cat", category)

    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="metric-card"><div class="metric-val">{input_rank}</div><div class="metric-label">Your AIR</div></div>', unsafe_allow_html=True)
    with col2:
        eff = results.iloc[0]["Effective_Rank"] if not results.empty else input_rank
        st.markdown(f'<div class="metric-card"><div class="metric-val">{eff}</div><div class="metric-label">Effective Rank ({input_cat})</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><div class="metric-val">{len(results)}</div><div class="metric-label">Colleges Found</div></div>', unsafe_allow_html=True)
    with col4:
        high = len(results[results["Chance"] == "🟢 High"]) if not results.empty else 0
        st.markdown(f'<div class="metric-card"><div class="metric-val">{high}</div><div class="metric-label">High Chance</div></div>', unsafe_allow_html=True)

    st.markdown("---")

    if results.empty:
        st.warning("😔 No colleges found for your rank and preferences. Try adjusting your filters or rank.")
    else:
        # ── Charts ──
        chart_col1, chart_col2 = st.columns(2)
        with chart_col1:
            chance_counts = results["Chance"].value_counts().reset_index()
            chance_counts.columns = ["Chance", "Count"]
            color_map = {"🟢 High": "#00b894", "🟡 Moderate": "#fdcb6e", "🟠 Low-Moderate": "#e17055", "🔴 Slim": "#d63031"}
            fig1 = px.pie(chance_counts, values="Count", names="Chance", title="Admission Chances",
                         color="Chance", color_discrete_map=color_map, hole=0.4)
            fig1.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                              font_color="#f8f9fa", title_font_size=18)
            st.plotly_chart(fig1, use_container_width=True)

        with chart_col2:
            type_counts = results["Type"].value_counts().reset_index()
            type_counts.columns = ["Type", "Count"]
            type_colors = {"IIT": "#00b894", "NIT": "#0984e3", "IIIT": "#e17055", "GFTI": "#6c5ce7"}
            fig2 = px.bar(type_counts, x="Type", y="Count", title="Colleges by Type",
                         color="Type", color_discrete_map=type_colors)
            fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                              font_color="#f8f9fa", title_font_size=18, showlegend=False)
            st.plotly_chart(fig2, use_container_width=True)

        # ── College Cards ──
        st.markdown("### 📋 Predicted Colleges")

        # Filter tabs
        tab_all, tab_high, tab_mod, tab_slim = st.tabs(["🏫 All", "🟢 High Chance", "🟡 Moderate", "🔴 Slim"])

        def render_cards(data):
            if data.empty:
                st.info("No colleges in this category.")
                return
            for _, r in data.iterrows():
                tag_class = {"IIT": "tag-iit", "NIT": "tag-nit", "IIIT": "tag-iiit", "GFTI": "tag-gfti"}.get(r["Type"], "tag-gfti")
                st.markdown(f"""
                <div class="college-card">
                    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;">
                        <div>
                            <div class="college-name">{r['College']}</div>
                            <div class="college-detail">📍 {r['City']}  |  📊 NIRF: #{r['NIRF']}  |  🎓 {r['Stream']}</div>
                            <div class="college-detail">Rank Range: {r['Opening_Rank']} — {r['Closing_Rank']}</div>
                        </div>
                        <div style="text-align:right;">
                            <span class="tag {tag_class}">{r['Type']}</span><br>
                            <span class="{r['Chance_Class']}" style="font-size:18px;">{r['Chance']}</span>
                        </div>
                    </div>
                </div>""", unsafe_allow_html=True)

        with tab_all:
            render_cards(results)
        with tab_high:
            render_cards(results[results["Chance"] == "🟢 High"])
        with tab_mod:
            render_cards(results[results["Chance"].isin(["🟡 Moderate", "🟠 Low-Moderate"])])
        with tab_slim:
            render_cards(results[results["Chance"] == "🔴 Slim"])

        # ── Download ──
        st.markdown("---")
        csv = results[["College","Type","Stream","City","NIRF","Opening_Rank","Closing_Rank","Chance"]].to_csv(index=False)
        st.download_button("📥 Download Results as CSV", csv, "jee_prediction.csv", "text/csv", use_container_width=True)

else:
    # Landing page
    st.markdown("")
    lc1, lc2, lc3 = st.columns([1, 2, 1])
    with lc2:
        st.markdown("""
        <div style="text-align:center;padding:40px 0;">
            <div style="font-size:80px;">🎯</div>
            <h2 style="color:#a29bfe;">Enter your JEE rank to get started</h2>
            <p style="color:#dfe6e9;font-size:16px;">
                Use the sidebar to enter your rank, select streams, and click <b>Predict Colleges</b>.<br><br>
                ✅ Covers 23 IITs, 7 NITs, 7 IIITs & GFTIs<br>
                ✅ Stream-wise cutoff filtering<br>
                ✅ Category-based rank adjustment<br>
                ✅ Downloadable CSV results
            </p>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ──
st.markdown("---")
st.markdown("""
<div class="footer">
    ⚠️ Cutoff ranks are approximate and based on previous years' trends. Actual cutoffs vary each year.<br>
    Made with ❤️ by <b>dotnetabhishekai</b>
</div>
""", unsafe_allow_html=True)
