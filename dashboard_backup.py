import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

# =========================================================
# CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Retail Analytics | Dashboard",
    page_icon="📊",
    layout="wide"
)

DB_PATH = "data/processed/superstore.db"

# =========================================================
# CUSTOM DESIGN
# =========================================================
st.markdown("""
<style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }
    div[data-testid="stMetric"] {
        background-color: #111827;
        border: 1px solid #263244;
        padding: 18px;
        border-radius: 12px;
    }
    div[data-testid="stMetricLabel"] {
        color: #9CA3AF;
    }
    div[data-testid="stMetricValue"] {
        color: #F9FAFB;
    }
    h1, h2, h3 {
        letter-spacing: -0.5px;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA LOADING
# =========================================================
@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    data = pd.read_sql_query("SELECT * FROM superstore", conn)
    conn.close()

    data.columns = data.columns.str.strip()

    data["Order Date"] = pd.to_datetime(data["Order Date"], errors="coerce")
    data["Ship Date"] = pd.to_datetime(data["Ship Date"], errors="coerce")

    return data

try:
    df = load_data()
except Exception as e:
    st.error(f"Unable to load the database: {e}")
    st.stop()

# =========================================================
# HEADER
# =========================================================
st.title("📊 E-commerce Sales Analytics")
st.caption("Interactive business intelligence dashboard | Sales • Profit • Customers • Products")
st.divider()

# =========================================================
# SIDEBAR FILTERS
# =========================================================
st.sidebar.title("Dashboard Filters")

all_regions = sorted(df["Region"].dropna().unique())
all_categories = sorted(df["Category"].dropna().unique())
all_segments = sorted(df["Segment"].dropna().unique())

selected_regions = st.sidebar.multiselect(
    "Region",
    all_regions,
    default=all_regions
)

selected_categories = st.sidebar.multiselect(
    "Category",
    all_categories,
    default=all_categories
)

selected_segments = st.sidebar.multiselect(
    "Customer Segment",
    all_segments,
    default=all_segments
)

valid_dates = df["Order Date"].dropna()

if valid_dates.empty:
    st.error("No valid order dates were found in the database.")
    st.stop()

min_date = valid_dates.min().date()
max_date = valid_dates.max().date()

selected_date_range = st.sidebar.date_input(
    "Order Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

st.sidebar.divider()
if st.sidebar.button("Reset Filters"):
    st.rerun()

# =========================================================
# FILTER DATA
# =========================================================
filtered_df = df[
    df["Region"].isin(selected_regions)
    & df["Category"].isin(selected_categories)
    & df["Segment"].isin(selected_segments)
].copy()

if isinstance(selected_date_range, (tuple, list)) and len(selected_date_range) == 2:
    start_date, end_date = selected_date_range

    filtered_df = filtered_df[
        (filtered_df["Order Date"].dt.date >= start_date)
        & (filtered_df["Order Date"].dt.date <= end_date)
    ]

elif isinstance(selected_date_range, (tuple, list)) and len(selected_date_range) == 1:
    selected_day = selected_date_range[0]

    filtered_df = filtered_df[
        filtered_df["Order Date"].dt.date == selected_day
    ]

# =========================================================
# KPI CALCULATIONS
# =========================================================
sales = filtered_df["Sales"].sum()
profit = filtered_df["Profit"].sum()
orders = filtered_df["Order ID"].nunique()
margin = (profit / sales * 100) if sales != 0 else 0
quantity = filtered_df["Quantity"].sum()

# =========================================================
# KPI DISPLAY
# =========================================================
st.subheader("Overview")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Sales", f"${sales:,.0f}")
k2.metric("Total Profit", f"${profit:,.0f}")
k3.metric("Total Orders", f"{orders:,}")
k4.metric("Profit Margin", f"{margin:.2f}%")

st.caption(f"Units sold: {quantity:,}  |  Records analyzed: {len(filtered_df):,}")

st.divider()

# =========================================================
# MONTHLY SALES TREND
# =========================================================
st.subheader("Sales & Profit Trend")

monthly = filtered_df.copy()
monthly["Month"] = monthly["Order Date"].dt.to_period("M").astype(str)

monthly_summary = (
    monthly.groupby("Month", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Month")
)

if not monthly_summary.empty:
    fig_trend = px.line(
        monthly_summary,
        x="Month",
        y=["Sales", "Profit"],
        markers=True,
        labels={"value": "Amount ($)", "variable": "Metric"},
        template="plotly_dark"
    )
    fig_trend.update_layout(
        legend_title="Metric",
        hovermode="x unified"
    )
    st.plotly_chart(fig_trend, use_container_width=True)
else:
    st.info("No data available for the selected filters.")

st.divider()

# =========================================================
# CATEGORY ANALYSIS
# =========================================================
left, right = st.columns(2)

with left:
    st.subheader("Category Sales")

    category_summary = (
        filtered_df.groupby("Category", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum")
        )
    )

    if not category_summary.empty:
        fig_category_sales = px.bar(
            category_summary,
            x="Category",
            y="Sales",
            color="Category",
            template="plotly_dark",
            title="Sales by Category"
        )
        st.plotly_chart(fig_category_sales, use_container_width=True)

with right:
    st.subheader("Category Profit")

    if not category_summary.empty:
        fig_category_profit = px.bar(
            category_summary,
            x="Category",
            y="Profit",
            color="Profit",
            color_continuous_scale="RdYlGn",
            template="plotly_dark",
            title="Profit by Category"
        )
        st.plotly_chart(fig_category_profit, use_container_width=True)

if not category_summary.empty:
    category_summary["Profit Margin (%)"] = (
        category_summary["Profit"] / category_summary["Sales"] * 100
    )

    st.dataframe(
        category_summary.style.format({
            "Sales": "${:,.2f}",
            "Profit": "${:,.2f}",
            "Profit Margin (%)": "{:.2f}%"
        }),
        use_container_width=True,
        hide_index=True
    )

st.divider()

# =========================================================
# REGIONAL ANALYSIS
# =========================================================
st.subheader("Regional Performance")

region_summary = (
    filtered_df.groupby("Region", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
)

if not region_summary.empty:
    region_summary["Profit Margin (%)"] = (
        region_summary["Profit"] / region_summary["Sales"] * 100
    )

    fig_region = px.bar(
        region_summary,
        x="Region",
        y=["Sales", "Profit"],
        barmode="group",
        template="plotly_dark",
        title="Sales vs Profit by Region"
    )
    st.plotly_chart(fig_region, use_container_width=True)

    st.dataframe(
        region_summary.style.format({
            "Sales": "${:,.2f}",
            "Profit": "${:,.2f}",
            "Orders": "{:,}",
            "Profit Margin (%)": "{:.2f}%"
        }),
        use_container_width=True,
        hide_index=True
    )

st.divider()

# =========================================================
# TOP PRODUCTS
# =========================================================
left, right = st.columns(2)

with left:
    st.subheader("Top 10 Products by Sales")

    product_summary = (
        filtered_df.groupby("Product Name", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum")
        )
        .sort_values("Sales", ascending=False)
        .head(10)
        .sort_values("Sales")
    )

    if not product_summary.empty:
        fig_top = px.bar(
            product_summary,
            x="Sales",
            y="Product Name",
            orientation="h",
            template="plotly_dark",
            color="Sales",
            title="Top Selling Products"
        )
        st.plotly_chart(fig_top, use_container_width=True)

with right:
    st.subheader("10 Lowest-Profit Products")

    loss_summary = (
        filtered_df.groupby("Product Name", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum")
        )
        .sort_values("Profit")
        .head(10)
        .sort_values("Profit", ascending=True)
    )

    if not loss_summary.empty:
        fig_loss = px.bar(
            loss_summary,
            x="Profit",
            y="Product Name",
            orientation="h",
            template="plotly_dark",
            color="Profit",
            color_continuous_scale="RdYlGn",
            title="Loss-Making / Lowest-Profit Products"
        )
        st.plotly_chart(fig_loss, use_container_width=True)

st.divider()

# =========================================================
# CUSTOMER SEGMENT ANALYSIS
# =========================================================
st.subheader("Customer Segment Analysis")

segment_summary = (
    filtered_df.groupby("Segment", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique"),
        Quantity=("Quantity", "sum")
    )
)

if not segment_summary.empty:
    segment_summary["Profit Margin (%)"] = (
        segment_summary["Profit"] / segment_summary["Sales"] * 100
    )

    left, right = st.columns(2)

    with left:
        fig_segment_sales = px.pie(
            segment_summary,
            names="Segment",
            values="Sales",
            hole=0.45,
            template="plotly_dark",
            title="Sales Share by Segment"
        )
        st.plotly_chart(fig_segment_sales, use_container_width=True)

    with right:
        fig_segment_profit = px.bar(
            segment_summary,
            x="Segment",
            y="Profit",
            color="Segment",
            template="plotly_dark",
            title="Profit by Customer Segment"
        )
        st.plotly_chart(fig_segment_profit, use_container_width=True)

    st.dataframe(
        segment_summary.style.format({
            "Sales": "${:,.2f}",
            "Profit": "${:,.2f}",
            "Orders": "{:,}",
            "Quantity": "{:,}",
            "Profit Margin (%)": "{:.2f}%"
        }),
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# DISCOUNT ANALYSIS
# =========================================================
st.divider()
st.subheader("Discount Analysis")

discount_summary = (
    filtered_df.groupby("Discount", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Discount")
)

if not discount_summary.empty:
    discount_summary["Profit Margin (%)"] = (
        discount_summary["Profit"] / discount_summary["Sales"] * 100
    )

    fig_discount = px.bar(
        discount_summary,
        x="Discount",
        y="Profit",
        color="Profit",
        color_continuous_scale="RdYlGn",
        template="plotly_dark",
        title="Profit by Discount Level"
    )
    st.plotly_chart(fig_discount, use_container_width=True)

    st.dataframe(
        discount_summary.style.format({
            "Discount": "{:.0%}",
            "Sales": "${:,.2f}",
            "Profit": "${:,.2f}",
            "Quantity": "{:,}",
            "Profit Margin (%)": "{:.2f}%"
        }),
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# DATA TABLE
# =========================================================
with st.expander("View Filtered Dataset"):
    st.dataframe(filtered_df, use_container_width=True)

# =========================================================
# FOOTER
# =========================================================
st.divider()
st.caption("E-commerce Sales Analytics | Built with Python, Pandas, SQLite, Streamlit & Plotly")
