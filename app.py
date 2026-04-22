import streamlit as st
import pandas as pd
import networkx as nx
import plotly.express as px
import plotly.graph_objects as go
import pickle
import os

# 1. Page Configuration
st.set_page_config(
    page_title="Supply Chain Optimizer", 
    layout="wide", 
    page_icon="☕"
)

# 2. Advanced UI Styling
st.markdown("""
    <style>
    /* Force main background to deep black */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }

    /* Style the Sidebar to match */
    section[data-testid="stSidebar"] {
        background-color: #111111 !important;
        border-right: 1px solid #333333;
    }

    /* Card-style containers for metrics and charts */
    div[data-testid="stMetric"] {
        background-color: #1a1a1a;
        border: 1px solid #333333;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }

    /* Adjust text colors for visibility on black */
    h1, h2, h3, p, span, label {
        color: #E0E0E0 !important;
    }

    /* Target metric values specifically */
    div[data-testid="stMetricValue"] {
        color: #00FF41 !important; /* "Terminal" Green for high-impact numbers */
    }

    /* Clean up the divider */
    hr {
        border: 1px solid #333333;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Supply Chain Transparency & Price Optimizer")
st.markdown("### Strategic Intervention Dashboard: Jimma Highlands → Djibouti Corridor")

# 3. Asset Loading
@st.cache_resource
def load_data():
    paths = ['data/processed/verified_logistics_graph.pkl', '../data/processed/verified_logistics_graph.pkl']
    for path in paths:
        if os.path.exists(path):
            with open(path, 'rb') as f:
                return pickle.load(f)
    return None

G = load_data()

# 4. Sidebar: Interventions
st.sidebar.header("Policy Interventions")
logistics_efficiency = st.sidebar.slider("Infrastructure Efficiency Gain (%)", 0, 50, 15)
leakage_reduction = st.sidebar.slider("Informal Leakage Reduction ($/kg)", 0.0, 0.30, 0.08)
market_price_cents = st.sidebar.number_input("Global FOB Price (US cents/lb)", value=385)

# 5. Calculation Engine
ELASTICITY = 0.72
BASE_COST = 1.65 
BASE_LEAKAGE = 0.15 
market_price_usd_kg = (market_price_cents / 100) * 2.20462 

opt_cost = BASE_COST * (1 - (logistics_efficiency / 100))
opt_leakage = BASE_LEAKAGE - leakage_reduction
opt_farmgate = (market_price_usd_kg * ELASTICITY) - opt_cost - opt_leakage
opt_share = (opt_farmgate / market_price_usd_kg) * 100

# 6. Top-Level Impact Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("Farmer Share", f"{opt_share:.1f}%", delta=f"{opt_share - 47.75:.1f}%")
m2.metric("Farmgate Price", f"${opt_farmgate:.2f}/kg")
m3.metric("Annual ROI", f"${(opt_share - 47.75) * 100:.0f}/ton")
m4.metric("Risk Status", "Moderate" if opt_share > 50 else "High-Risk", delta_color="inverse")

st.divider()

# 7. Visualization Row
left_col, right_col = st.columns([1.5, 1])

with left_col:
    st.subheader("Value Distribution Gauge")
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = opt_share,
        gauge = {
            'axis': {'range': [None, 100], 'tickcolor': "#FFFFFF"},
            'bar': {'color': "#00FF41"}, # Matrix Green for the actual value
            'bgcolor': "#111111",
            'steps': [
                {'range': [0, 50], 'color': "#4b0000"}, # Critical
                {'range': [50, 65], 'color': "#4b4b00"}, # Warning
                {'range': [65, 100], 'color': "#004b00"}], # Sustainable
            'threshold': {'line': {'color': "white", 'width': 4}, 'value': 60}
        }
    ))

    fig_gauge.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)', 
        font={'color': "white"},
        margin=dict(t=30, b=0, l=10, r=10)
    )
    st.plotly_chart(fig_gauge, use_container_width=True)

    # Color Legend (Ledger)
    st.markdown("""
    <div style="display: flex; justify-content: space-around; background-color: #1a1a1a; padding: 10px; border-radius: 8px; border: 1px solid #333333;">
        <div style="display: flex; align-items: center;">
            <div style="width: 12px; height: 12px; background-color: #4b0000; margin-right: 8px; border-radius: 2px;"></div>
            <span style="font-size: 0.85rem; color: #E0E0E0;"><b>CRITICAL:</b> < 50% Share</span>
        </div>
        <div style="display: flex; align-items: center;">
            <div style="width: 12px; height: 12px; background-color: #4b4b00; margin-right: 8px; border-radius: 2px;"></div>
            <span style="font-size: 0.85rem; color: #E0E0E0;"><b>WARNING:</b> 50-65% Share</span>
        </div>
        <div style="display: flex; align-items: center;">
            <div style="width: 12px; height: 12px; background-color: #004b00; margin-right: 8px; border-radius: 2px;"></div>
            <span style="font-size: 0.85rem; color: #E0E0E0;"><b>SUSTAINABLE:</b> > 65% Share</span>
        </div>
    </div>
    <p style="text-align: center; font-size: 0.75rem; color: #888; margin-top: 5px;">*Industry Target: 60% Farmgate Capture (White Threshold Line)</p>
    """, unsafe_allow_html=True)


with right_col:
    st.subheader("Bottleneck Friction Audit")
    if G is not None:
        edge_data = []
        for u, v, d in G.edges(data=True):
            cost = d.get('cost_usd', 0)
            dist = d.get('distance_km', 1)
            edge_data.append({'Route': f"{u} → {v}", 'Friction': cost / dist})

        friction_df = pd.DataFrame(edge_data).sort_values('Friction', ascending=True)

        fig_friction = px.bar(
            friction_df, x='Friction', y='Route', orientation='h',
            color='Friction', color_continuous_scale=['#4b0000', '#ff0000'],
            labels={'Friction': 'USD Cost per KM'}
        )
        fig_friction.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)', 
            font={'color': "white"},
            margin=dict(t=0, b=0)
        )
        st.plotly_chart(fig_friction, use_container_width=True)
    else:
        st.error("Graph data file missing.")

# 8. Executive Summary
st.divider()
st.subheader("Auditor's Strategic Conclusion")
st.markdown(f"""
<div style="background-color: #111111; padding: 20px; border-radius: 10px; border-left: 5px solid #00FF41;">
    <p style="color: #00FF41; font-weight: bold;">STRATEGIC ACTION DEPLOYED:</p>
    <p>Infrastructure intervention achieved. Current simulation yields a <b>{opt_share:.1f}%</b> farmer share. 
    Prioritize rural feeder road investment in the <b>Gera district</b> to minimize 'First-Mile' friction.</p>
</div>
""", unsafe_allow_html=True)

# 9. Footer / Signature
st.sidebar.markdown("---") # Visual separator
st.sidebar.caption("Developed by **Aklilu Abera Dana** | Supply Chain Data Analyst")

# Add a subtle footer to the main page as well
st.markdown("<br><br>", unsafe_allow_html=True) # Add some spacing
st.caption("© 2026 Logistics Frontier Model | Research & Analysis by Aklilu Abera Dana")
