import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# CONFIGURATION
# =========================
st.set_page_config(
    page_title="Retail Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# =========================
# THEME
# =========================
st.markdown("""
<style>
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}
[data-testid="stMetric"] {
    background: #111827;
    border: 1px solid #263247;
    padding: 18px;
    border-radius: 12px;
}
h1, h2, h3 {
    letter-spacing: -0.5px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv(
        "data/raw/Sample - Superstore.csv",
        encoding="latin1"
    )

    df.columns = df.columns.str.strip()

    df["Order Date"] = pd.to_datetime(
        df["Order Date"], errors="coerce"
    )

    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")

    return df

df = load_data()

# =========================
# HEADER
# =========================
st.title("📊 Retail Sales Analytics")
st.caption(
    "Interactive business intelligence dashboard | "
    "Sales, profitability, customers, products & discount performance"
)

# =========================
# SIDEBAR FILTERS
# =========================
st.sidebar.title("Dashboard Filters")

regions = sorted(df["Region"].dropna().unique())
categories = sorted(df["Category"].dropna().unique())
segments = sorted(df["Segment"].dropna().unique())

selected_regions = st.sidebar.multiselect(
    "Region",
    regions,
    default=regions
)

selected_categories = st.sidebar.multiselect(
    "Category",
    categories,
    default=categories
)

selected_segments = st.sidebar.multiselect(
    "Customer Segment",
    segments,
    default=segments
)

min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

selected_dates = st.sidebar.date_input(
    "Order Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# =========================
# FILTER DATA
# =========================
filtered_df = df[
    (df["Region"].isin(selected_regions)) &
    (df["Category"].isin(selected_categories)) &
    (df["Segment"].isin(selected_segments))
].copy()

if isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 2:
    start_date, end_date = selected_dates

    filtered_df = filtered_df[
        (filtered_df["Order Date"].dt.date >= start_date) &
        (filtered_df["Order Date"].dt.date <= end_date)
    ]

# =========================
# KPI CALCULATIONS
# =========================
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
total_quantity = filtered_df["Quantity"].sum()

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0 else 0
)

# =========================
# KPI HEADER
# =========================
st.subheader("Business Overview")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Sales", f"${total_sales:,.0f}")
k2.metric("Total Profit", f"${total_profit:,.0f}")
k3.metric("Total Orders", f"{total_orders:,}")
k4.metric("Profit Margin", f"{profit_margin:.2f}%")

st.caption(
    f"Units sold: {total_quantity:,.0f} | "
    f"Records analyzed: {len(filtered_df):,}"
)

st.divider()

# =========================
# SALES & PROFIT TREND
# =========================
st.subheader("Sales & Profit Trend")

monthly = (
    filtered_df.groupby(
        filtered_df["Order Date"].dt.to_period("M")
    )
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
)

monthly["Month"] = monthly["Order Date"].astype(str)

monthly_long = monthly.melt(
    id_vars="Month",
    value_vars=["Sales", "Profit"],
    var_name="Metric",
    value_name="Amount"
)

fig_trend = px.line(
    monthly_long,
    x="Month",
    y="Amount",
    color="Metric",
    markers=True,
    template="plotly_dark",
    color_discrete_map={
        "Sales": "#636EFA",
        "Profit": "#00CC96"
    }
)

fig_trend.update_layout(
    height=420,
    margin=dict(l=10, r=10, t=30, b=10),
    xaxis_title="Month",
    yaxis_title="Amount ($)",
    legend_title="",
    hovermode="x unified"
)

st.plotly_chart(fig_trend, use_container_width=True)

st.divider()

# =========================
# CATEGORY ANALYSIS
# =========================
st.subheader("Category Performance")

category_data = (
    filtered_df.groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
)

category_data["Profit Margin (%)"] = (
    category_data["Profit"] / category_data["Sales"] * 100
)

c1, c2 = st.columns(2)

with c1:
    fig_category_sales = px.bar(
        category_data.sort_values("Sales", ascending=True),
        x="Sales",
        y="Category",
        orientation="h",
        title="Sales by Category",
        text_auto=".3s",
        template="plotly_dark",
        color="Category"
    )

    fig_category_sales.update_layout(
        height=350,
        showlegend=False,
        margin=dict(l=10, r=10, t=50, b=10)
    )

    st.plotly_chart(fig_category_sales, use_container_width=True)

with c2:
    fig_category_profit = px.bar(
        category_data.sort_values("Profit", ascending=True),
        x="Profit",
        y="Category",
        orientation="h",
        title="Profit by Category",
        text_auto=".3s",
        template="plotly_dark",
        color="Profit",
        color_continuous_scale="RdYlGn"
    )

    fig_category_profit.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=50, b=10)
    )

    st.plotly_chart(fig_category_profit, use_container_width=True)

st.dataframe(
    category_data.style.format({
        "Sales": "${:,.2f}",
        "Profit": "${:,.2f}",
        "Profit Margin (%)": "{:.2f}%",
        "Quantity": "{:,.0f}"
    }),
    use_container_width=True,
    hide_index=True
)

st.divider()

# =========================
# REGIONAL ANALYSIS
# =========================
st.subheader("Regional Performance")

region_data = (
    filtered_df.groupby("Region")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
)

region_data["Profit Margin (%)"] = (
    region_data["Profit"] / region_data["Sales"] * 100
)

r1, r2 = st.columns(2)

with r1:
    fig_region_sales = px.bar(
        region_data.sort_values("Sales", ascending=True),
        x="Sales",
        y="Region",
        orientation="h",
        title="Sales by Region",
        template="plotly_dark",
        color="Sales",
        color_continuous_scale="Blues"
    )

    fig_region_sales.update_layout(
        height=370,
        margin=dict(l=10, r=10, t=50, b=10)
    )

    st.plotly_chart(fig_region_sales, use_container_width=True)

with r2:
    fig_region_margin = px.bar(
        region_data.sort_values("Profit Margin (%)", ascending=True),
        x="Profit Margin (%)",
        y="Region",
        orientation="h",
        title="Profit Margin by Region",
        template="plotly_dark",
        color="Profit Margin (%)",
        color_continuous_scale="RdYlGn"
    )

    fig_region_margin.update_layout(
        height=370,
        margin=dict(l=10, r=10, t=50, b=10)
    )

    st.plotly_chart(fig_region_margin, use_container_width=True)

st.dataframe(
    region_data.style.format({
        "Sales": "${:,.2f}",
        "Profit": "${:,.2f}",
        "Profit Margin (%)": "{:.2f}%",
        "Orders": "{:,.0f}",
        "Quantity": "{:,.0f}"
    }),
    use_container_width=True,
    hide_index=True
)

st.divider()

# =========================
# PRODUCT ANALYSIS
# =========================
st.subheader("Product Performance")

product_data = (
    filtered_df.groupby("Product Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
)

p1, p2 = st.columns(2)

with p1:
    top_products = product_data.nlargest(10, "Sales").sort_values("Sales")

    fig_top_products = px.bar(
        top_products,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="Top 10 Products by Sales",
        template="plotly_dark",
        color="Sales",
        color_continuous_scale="Blues"
    )

    fig_top_products.update_layout(
        height=520,
        yaxis_title="",
        margin=dict(l=10, r=10, t=50, b=10)
    )

    st.plotly_chart(fig_top_products, use_container_width=True)

with p2:
    bottom_products = product_data.nsmallest(10, "Profit").sort_values("Profit")

    fig_bottom_products = px.bar(
        bottom_products,
        x="Profit",
        y="Product Name",
        orientation="h",
        title="10 Lowest-Profit Products",
        template="plotly_dark",
        color="Profit",
        color_continuous_scale="Reds"
    )

    fig_bottom_products.update_layout(
        height=520,
        yaxis_title="",
        margin=dict(l=10, r=10, t=50, b=10)
    )

    st.plotly_chart(fig_bottom_products, use_container_width=True)

st.divider()

# =========================
# CUSTOMER ANALYSIS
# =========================
st.subheader("Customer Segment Analysis")

segment_data = (
    filtered_df.groupby("Segment")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
)

segment_data["Profit Margin (%)"] = (
    segment_data["Profit"] / segment_data["Sales"] * 100
)

s1, s2 = st.columns(2)

with s1:
    fig_segment_sales = px.pie(
        segment_data,
        names="Segment",
        values="Sales",
        hole=0.55,
        title="Sales Share by Segment",
        template="plotly_dark"
    )

    fig_segment_sales.update_traces(
        textposition="inside",
        textinfo="percent"
    )

    fig_segment_sales.update_layout(height=380)

    st.plotly_chart(fig_segment_sales, use_container_width=True)

with s2:
    fig_segment_profit = px.bar(
        segment_data,
        x="Segment",
        y="Profit",
        title="Profit by Customer Segment",
        template="plotly_dark",
        color="Profit",
        color_continuous_scale="Greens"
    )

    fig_segment_profit.update_layout(height=380)

    st.plotly_chart(fig_segment_profit, use_container_width=True)

st.dataframe(
    segment_data.style.format({
        "Sales": "${:,.2f}",
        "Profit": "${:,.2f}",
        "Profit Margin (%)": "{:.2f}%",
        "Orders": "{:,.0f}",
        "Quantity": "{:,.0f}"
    }),
    use_container_width=True,
    hide_index=True
)

# =========================
# CUSTOMER PROFITABILITY
# =========================
st.subheader("Customer Profitability")

customer_data = (
    filtered_df.groupby("Customer Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
    .reset_index()
)

top_customers = customer_data.nlargest(10, "Sales")

fig_customers = px.bar(
    top_customers.sort_values("Sales"),
    x="Sales",
    y="Customer Name",
    orientation="h",
    title="Top 10 Customers by Sales",
    template="plotly_dark",
    color="Sales",
    color_continuous_scale="Teal"
)

fig_customers.update_layout(height=480)

st.plotly_chart(fig_customers, use_container_width=True)

st.divider()

# =========================
# DISCOUNT ANALYSIS
# =========================
st.subheader("Discount Analysis")

discount_data = (
    filtered_df.groupby("Discount")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
)

discount_data["Discount Level"] = (
    discount_data["Discount"].map(lambda x: f"{x:.0%}")
)

discount_data["Profit Margin (%)"] = (
    discount_data["Profit"] / discount_data["Sales"] * 100
)

fig_discount = px.bar(
    discount_data,
    x="Discount Level",
    y="Profit",
    title="Profit by Discount Level",
    template="plotly_dark",
    color="Profit",
    color_continuous_scale="RdYlGn",
    hover_data=["Sales", "Quantity", "Profit Margin (%)"]
)

fig_discount.update_layout(
    height=420,
    xaxis_title="Discount",
    yaxis_title="Profit ($)",
    margin=dict(l=10, r=10, t=50, b=10)
)

st.plotly_chart(fig_discount, use_container_width=True)

st.dataframe(
    discount_data[[
        "Discount Level",
        "Sales",
        "Profit",
        "Quantity",
        "Profit Margin (%)"
    ]].style.format({
        "Sales": "${:,.2f}",
        "Profit": "${:,.2f}",
        "Quantity": "{:,.0f}",
        "Profit Margin (%)": "{:.2f}%"
    }),
    use_container_width=True,
    hide_index=True
)

# =========================
# FILTERED DATASET
# =========================
with st.expander("View Filtered Dataset"):
    st.dataframe(filtered_df, use_container_width=True)

# =========================
# FOOTER
# =========================
st.divider()

st.caption(
    "Retail Sales Analytics | "
    "Python • Pandas • SQL • SQLite • Streamlit • Plotly"
)
