#%pip install streamlit pandas plotly openpyxl
import streamlit as st
import pandas as pd
import plotly.express as px


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="CO₂ & Greenhouse Gas Emissions",
    page_icon="🌍",
    layout="wide",
)


# =========================================================
# COLORS / STYLING
# =========================================================

ORANGE_SCALE = [
    "#fff0e0",
    "#ffd9b3",
    "#ffc285",
    "#ffab57",
    "#ff9430",
    "#e36b1f",
    "#b55317",
]

ORANGE_MED = "#ffb547"
ORANGE_DARK = "#cc5500"

CARD_BG = "#3b4a59"
APP_BG = "#2b3e50"


st.markdown(
    f"""
    <style>

    .stApp {{
        background-color: {APP_BG};
        color: white;
    }}

    .block-container {{
        max-width: 1500px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}

    h1, h2, h3, h4, p, label {{
        color: white;
    }}

    .metric-card {{
        background-color: {CARD_BG};
        border-radius: 16px;
        padding: 22px 18px;
        min-height: 180px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.18);
        text-align: center;
        margin-bottom: 12px;
    }}

    .metric-title {{
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 10px;
    }}

    .metric-value {{
        color: {ORANGE_MED};
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 8px;
    }}

    .metric-subtitle {{
        font-size: 0.95rem;
        opacity: 0.92;
    }}

    .dashboard-header {{
    text-align: center;
    margin-bottom: 25px;
    }}

    .dashboard-title {{
    font-size: 3rem;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 25px;
    color: white;
    }}

    .dashboard-description {{
    text-align: center;
    font-size: 1.08rem;
    color: white;
    margin: 0 auto;
    max-width: 1200px;
    }}

    .figure-header {{
    text-align: center;
    margin-bottom: 20px;
    }}

     .figure-title {{
    font-size: 1.75rem;
    font-weight: 700;
    color: white;
    margin-bottom: 10px;
     }}

     .figure-description {{
    text-align: center;
    font-size: 1rem;
    color: white;
    margin: 0 auto 18px auto;
    max-width: 1000px;
     }}

     .year-label {{
    text-align: center;
    color: white;
    font-size: 0.95rem;
    margin-bottom: 5px;
    }}

/* Center horizontal radio buttons */
div[data-testid="stRadio"] > div {{
    justify-content: center;
}}

div[data-testid="stRadio"] [role="radiogroup"] {{
    justify-content: center;
}}
    
    .dashboard-intro {{
        text-align: center;
        font-size: 1.08rem;
        margin-bottom: 25px;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# LOAD DATA
# =========================================================

DATA_FILE = "owid-co2-data.xlsx"


@st.cache_data
def load_data():
    df = pd.read_excel(
        DATA_FILE,
        sheet_name="Data"
    )

    return df


df_co2 = load_data()


# =========================================================
# CONTINENT MAPPING
# =========================================================

continent_map = {

    # Africa
    "DZA": "Africa",
    "AGO": "Africa",
    "BEN": "Africa",
    "BWA": "Africa",
    "BFA": "Africa",
    "BDI": "Africa",
    "CMR": "Africa",
    "CPV": "Africa",
    "CAF": "Africa",
    "TCD": "Africa",
    "COM": "Africa",
    "COG": "Africa",
    "COD": "Africa",
    "DJI": "Africa",
    "EGY": "Africa",
    "GNQ": "Africa",
    "ERI": "Africa",
    "SWZ": "Africa",
    "ETH": "Africa",
    "GAB": "Africa",
    "GMB": "Africa",
    "GHA": "Africa",
    "GIN": "Africa",
    "GNB": "Africa",
    "CIV": "Africa",
    "KEN": "Africa",
    "LSO": "Africa",
    "LBR": "Africa",
    "LBY": "Africa",
    "MDG": "Africa",
    "MWI": "Africa",
    "MLI": "Africa",
    "MRT": "Africa",
    "MUS": "Africa",
    "MYT": "Africa",
    "MOZ": "Africa",
    "NAM": "Africa",
    "NER": "Africa",
    "NGA": "Africa",
    "REU": "Africa",
    "RWA": "Africa",
    "STP": "Africa",
    "SEN": "Africa",
    "SYC": "Africa",
    "SLE": "Africa",
    "SOM": "Africa",
    "ZAF": "Africa",
    "SSD": "Africa",
    "SDN": "Africa",
    "TZA": "Africa",
    "TGO": "Africa",
    "UGA": "Africa",
    "ZMB": "Africa",
    "ZWE": "Africa",
    "MAR": "Africa",
    "TUN": "Africa",
    "ESH": "Africa",
    "SHN": "Africa",

    # Asia
    "AFG": "Asia",
    "ARM": "Asia",
    "AZE": "Asia",
    "BHR": "Asia",
    "BGD": "Asia",
    "BTN": "Asia",
    "BRN": "Asia",
    "KHM": "Asia",
    "CHN": "Asia",
    "CYP": "Asia",
    "GEO": "Asia",
    "HKG": "Asia",
    "IND": "Asia",
    "IDN": "Asia",
    "IRN": "Asia",
    "IRQ": "Asia",
    "ISR": "Asia",
    "JPN": "Asia",
    "JOR": "Asia",
    "KAZ": "Asia",
    "KWT": "Asia",
    "KGZ": "Asia",
    "LAO": "Asia",
    "LBN": "Asia",
    "MAC": "Asia",
    "MYS": "Asia",
    "MDV": "Asia",
    "MNG": "Asia",
    "MMR": "Asia",
    "NPL": "Asia",
    "PRK": "Asia",
    "OMN": "Asia",
    "PAK": "Asia",
    "PSE": "Asia",
    "PHL": "Asia",
    "QAT": "Asia",
    "SAU": "Asia",
    "SGP": "Asia",
    "KOR": "Asia",
    "LKA": "Asia",
    "SYR": "Asia",
    "TWN": "Asia",
    "TJK": "Asia",
    "THA": "Asia",
    "TLS": "Asia",
    "TUR": "Asia",
    "TKM": "Asia",
    "ARE": "Asia",
    "UZB": "Asia",
    "VNM": "Asia",
    "YEM": "Asia",
    "CXR": "Asia",

    # Europe
    "ALB": "Europe",
    "AND": "Europe",
    "AUT": "Europe",
    "BLR": "Europe",
    "BEL": "Europe",
    "BIH": "Europe",
    "BGR": "Europe",
    "HRV": "Europe",
    "CZE": "Europe",
    "DNK": "Europe",
    "EST": "Europe",
    "FIN": "Europe",
    "FRA": "Europe",
    "DEU": "Europe",
    "GRC": "Europe",
    "HUN": "Europe",
    "ISL": "Europe",
    "IRL": "Europe",
    "ITA": "Europe",
    "LVA": "Europe",
    "LIE": "Europe",
    "LTU": "Europe",
    "LUX": "Europe",
    "MLT": "Europe",
    "MDA": "Europe",
    "MCO": "Europe",
    "MNE": "Europe",
    "NLD": "Europe",
    "MKD": "Europe",
    "NOR": "Europe",
    "POL": "Europe",
    "PRT": "Europe",
    "ROU": "Europe",
    "RUS": "Europe",
    "SMR": "Europe",
    "SRB": "Europe",
    "SVK": "Europe",
    "SVN": "Europe",
    "ESP": "Europe",
    "SWE": "Europe",
    "CHE": "Europe",
    "UKR": "Europe",
    "GBR": "Europe",
    "VAT": "Europe",
    "KOS": "Europe",
    "FRO": "Europe",
    "GRL": "Europe",

    # North America
    "AIA": "North America",
    "ATG": "North America",
    "ABW": "North America",
    "BHS": "North America",
    "BRB": "North America",
    "BLZ": "North America",
    "BMU": "North America",
    "CAN": "North America",
    "CYM": "North America",
    "CRI": "North America",
    "CUB": "North America",
    "CUW": "North America",
    "DMA": "North America",
    "DOM": "North America",
    "SLV": "North America",
    "GRD": "North America",
    "GLP": "North America",
    "GTM": "North America",
    "HTI": "North America",
    "HND": "North America",
    "JAM": "North America",
    "MTQ": "North America",
    "MEX": "North America",
    "MSR": "North America",
    "NIC": "North America",
    "PAN": "North America",
    "PRI": "North America",
    "KNA": "North America",
    "LCA": "North America",
    "SPM": "North America",
    "VCT": "North America",
    "TTO": "North America",
    "USA": "North America",
    "VGB": "North America",
    "VIR": "North America",
    "BES": "North America",
    "SXM": "North America",
    "TCA": "North America",

    # South America
    "ARG": "South America",
    "BOL": "South America",
    "BRA": "South America",
    "CHL": "South America",
    "COL": "South America",
    "ECU": "South America",
    "GUY": "South America",
    "PRY": "South America",
    "PER": "South America",
    "SUR": "South America",
    "URY": "South America",
    "VEN": "South America",

    # Oceania
    "ASM": "Oceania",
    "AUS": "Oceania",
    "COK": "Oceania",
    "FJI": "Oceania",
    "PYF": "Oceania",
    "GUM": "Oceania",
    "KIR": "Oceania",
    "MHL": "Oceania",
    "FSM": "Oceania",
    "NRU": "Oceania",
    "NCL": "Oceania",
    "NZL": "Oceania",
    "NIU": "Oceania",
    "NFK": "Oceania",
    "PLW": "Oceania",
    "PNG": "Oceania",
    "WSM": "Oceania",
    "SLB": "Oceania",
    "TKL": "Oceania",
    "TON": "Oceania",
    "TUV": "Oceania",
    "VUT": "Oceania",
    "WLF": "Oceania",

    # Antarctica
    "ATA": "Antarctica",
}


df_co2["continent"] = df_co2["iso_code"].map(
    continent_map
)

df_co2["gdp_per_capita"] = (
    df_co2["gdp"] /
    df_co2["population"]
)


CONTINENTS = [
    "Africa",
    "Asia",
    "Europe",
    "North America",
    "Oceania",
    "South America",
]


# =========================================================
# FUEL VARIABLES
# =========================================================

fuel_cols = [
    "coal_co2",
    "oil_co2",
    "gas_co2",
    "cement_co2",
    "flaring_co2",
    "other_industry_co2",
]


fuel_labels = {
    "coal_co2": "Coal",
    "oil_co2": "Oil",
    "gas_co2": "Gas",
    "cement_co2": "Cement",
    "flaring_co2": "Flaring",
    "other_industry_co2": "Other industry",
}


have_fuels = all(
    col in df_co2.columns
    for col in fuel_cols
)


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def drop_unknown_continents(df):

    return (
        df
        .dropna(subset=["continent"])
        .loc[
            ~df["continent"].isin(
                [
                    "Unknown",
                    "Other/Unknown",
                    "Other"
                ]
            )
        ]
    )


def apply_plot_style(fig, height=520):

    fig.update_layout(
        autosize=True,
        height=height,
        plot_bgcolor=CARD_BG,
        paper_bgcolor=CARD_BG,
        font=dict(
            color="white",
            size=16
        ),
        margin=dict(
            t=40,
            r=30,
            b=60,
            l=70
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            borderwidth=0
        ),
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="rgba(255,255,255,0.25)",
        gridwidth=0.5,
        zeroline=False,
        automargin=True,
        tickfont=dict(
            color="white"
        ),
        title=dict(
            font=dict(
                color="white"
            )
        ),
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(255,255,255,0.25)",
        gridwidth=0.5,
        zeroline=False,
        automargin=True,
        tickfont=dict(
            color="white"
        ),
        title=dict(
            font=dict(
                color="white"
            )
        ),
    )

    return fig


def metric_card(title, value, subtitle):
    st.html(
        f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-subtitle">{subtitle}</div>
        </div>
        """
    )


# =========================================================
# KPI CALCULATIONS
# =========================================================

world_kpi = df_co2.loc[
    df_co2["country"] == "World",
    [
        "year",
        "total_ghg",
        "temperature_change_from_co2"
    ],
].dropna(
    subset=["total_ghg"]
)


base_year = 2000

preferred_compare_year = 2023


available_world_years = set(
    world_kpi["year"]
    .dropna()
    .astype(int)
)


if preferred_compare_year in available_world_years:

    compare_year = preferred_compare_year

else:

    compare_year = int(
        world_kpi["year"].max()
    )


row_base = world_kpi.loc[
    world_kpi["year"] == base_year
].iloc[0]


row_compare = world_kpi.loc[
    world_kpi["year"] == compare_year
].iloc[0]


ghg_base_Gt = (
    row_base["total_ghg"] /
    1000
)


ghg_compare_Gt = (
    row_compare["total_ghg"] /
    1000
)


change_pct = (

    (
        row_compare["total_ghg"]
        -
        row_base["total_ghg"]
    )

    /

    row_base["total_ghg"]

    *

    100
)


temp_base_C = (
    row_base[
        "temperature_change_from_co2"
    ]
)


temp_compare_C = (
    row_compare[
        "temperature_change_from_co2"
    ]
)


delta_temp_F = (

    temp_compare_C
    -
    temp_base_C

) * 9 / 5


# =========================================================
# DASHBOARD HEADER
# =========================================================

st.html(
    """
    <div class="dashboard-header">
        <div class="dashboard-title">
            Insights on CO₂ & Greenhouse Gas Emissions
        </div>

        <div class="dashboard-description">
            This dashboard explores how greenhouse gas (GHG) and CO₂ emissions
            evolve over time across continents, GDP per person, and fuel type.
        </div>
    </div>
    """
)


# =========================================================
# KPI CARDS
# =========================================================

kpi1, kpi2, kpi3 = st.columns(3)


with kpi1:

    metric_card(
        f"Global GHG incl. land use: "
        f"{base_year} vs {compare_year}",

        f"{ghg_base_Gt:,.1f} Gt "
        f"→ {ghg_compare_Gt:,.1f} Gt",

        "Global greenhouse gas emissions "
        "including land-use change",
    )


with kpi2:

    metric_card(
        f"Global GHG change since {base_year}",

        f"{change_pct:+.1f}%",

        f"Percentage change from "
        f"{base_year} to {compare_year}",
    )


with kpi3:

    metric_card(
        f"CO₂ warming increase: "
        f"{base_year} → {compare_year}",

        f"{delta_temp_F:+.2f} °F",

        "Change in model-based warming "
        "attributed to CO₂",
    )


st.divider()


# =========================================================
# GLOBAL MAP
# =========================================================

with st.container(border=True):

    st.html(
        """
        <div class="figure-header">
            <div class="figure-title">
                Global Annual GHG Emissions Including Land Use
            </div>

            <div class="figure-description">
                Annual greenhouse gas emissions including land-use change.
                Values are in million tonnes (Mt) of CO₂-equivalent per year.
            </div>
        </div>
        """
    )


    map_year_options = [

        year

        for year in [
            1960,
            1980,
            2000,
            2020
        ]

        if year in available_years
    ]


    st.html(
    """
    <div class="year-label">
        Select a year
    </div>
    """
)

selected_year = st.radio(
    "Select a year",
    options=map_year_options,
    horizontal=True,
    label_visibility="collapsed",
)


df_ghg_map = df_co2.loc[
        df_co2["iso_code"].notna(),
        [
            "country",
            "iso_code",
            "year",
            "total_ghg"
        ],
    ].dropna(
        subset=["total_ghg"]
    )


dff_map = df_ghg_map[
        df_ghg_map["year"]
        ==
        selected_year
    ]


min_emissions = float(
        df_ghg_map[
            "total_ghg"
        ].min()
    )


max_emissions = float(
        df_ghg_map[
            "total_ghg"
        ].max()
    )


fig_map = px.choropleth(
        dff_map,
        locations="iso_code",
        color="total_ghg",
        hover_name="country",
        color_continuous_scale="Oranges",

        range_color=(
            min_emissions,
            max_emissions
        ),

        labels={
            "total_ghg":
            "Annual GHG emissions incl. "
            "land use (million tonnes)"
        },

        scope="world",
    )


fig_map.update_geos(
        fitbounds="locations",
        projection_type="natural earth",
        projection_scale=1.4,
        showcountries=True,
        showcoastlines=True,
        bgcolor="rgba(0,0,0,0)",
    )


fig_map.update_layout(

        height=520,

        margin=dict(
            l=5,
            r=5,
            t=40,
            b=40
        ),

        geo=dict(
            bgcolor="rgba(0,0,0,0)"
        ),

        paper_bgcolor=CARD_BG,

        font=dict(
            color="white",
            size=16
        ),

        coloraxis_colorbar=dict(

            orientation="h",

            x=0.5,
            xanchor="center",

            y=-0.18,
            yanchor="top",

            len=0.6,
            thickness=12,

            title=dict(
                text="Million tonnes",
                font=dict(
                    color="white",
                    size=16
                )
            ),

            tickfont=dict(
                color="white",
                size=14
            ),
        ),
    )


st.plotly_chart(
        fig_map,
        width="stretch",
        theme=None
    )


st.divider()


# =========================================================
# CONTINENT FILTER
# =========================================================

st.subheader(
    "Explore Emissions by Continent"
)


continents_selected = st.multiselect(

    "Filter by continent "
    "(applies to the bubble and line charts)",

    options=CONTINENTS,

    default=CONTINENTS,
)


years_all = sorted(

    df_co2[
        "year"
    ]

    .dropna()

    .astype(int)

    .unique()

    .tolist()
)


bubble_years = [

    year

    for year in years_all

    if 1990 <= year <= 2020
]


bubble_year = st.slider(

    "Year for GDP vs CO₂ bubble chart",

    min_value=min(
        bubble_years
    ),

    max_value=max(
        bubble_years
    ),

    value=min(
        bubble_years
    ),

    step=1,
)


# =========================================================
# BUBBLE + LINE CHARTS
# =========================================================

left, right = st.columns(2)


# -------------------------
# BUBBLE CHART
# -------------------------

with left:

    with st.container(border=True):

        st.subheader(
            "GDP per Person vs CO₂ per Person"
        )


        st.write(
            "Each bubble is a country in the selected year. "
            "X = GDP per person, Y = CO₂ per person, "
            "bubble size = population, and color = continent."
        )


        df_bubble = (

            df_co2[
                df_co2["year"]
                ==
                bubble_year
            ]

            .dropna(
                subset=[
                    "population",
                    "gdp_per_capita",
                    "consumption_co2_per_capita"
                ]
            )
        )


        df_bubble = drop_unknown_continents(
            df_bubble
        )


        if continents_selected:

            df_bubble = df_bubble[
                df_bubble[
                    "continent"
                ].isin(
                    continents_selected
                )
            ]

        else:

            df_bubble = df_bubble.iloc[0:0]


        if df_bubble.empty:

            st.info(
                "Select at least one continent "
                "to display this chart."
            )

        else:

            fig_bubble = px.scatter(

                df_bubble,

                x="gdp_per_capita",

                y="consumption_co2_per_capita",

                size="population",

                color="continent",

                hover_name="country",

                size_max=60,

                color_discrete_sequence=ORANGE_SCALE,

                labels={

                    "gdp_per_capita":
                    "GDP per person (US$)",

                    "consumption_co2_per_capita":
                    "CO₂ per person (tonnes)",

                    "continent":
                    "Continent",
                },
            )


            fig_bubble.update_yaxes(
                range=[0, None]
            )


            fig_bubble.update_traces(

                marker=dict(

                    line=dict(
                        width=0.5,
                        color="#444"
                    )

                )
            )


            fig_bubble = apply_plot_style(
                fig_bubble
            )


            st.plotly_chart(
                fig_bubble,
                width="stretch",
                theme=None
            )


# -------------------------
# LINE CHART
# -------------------------

with right:

    with st.container(border=True):

        st.subheader(
            "CO₂ Emissions per Person Over Time"
        )


        st.write(
            "CO₂ emissions per person for the "
            "selected continents over time."
        )


        line_continents = (

            continents_selected

            or

            CONTINENTS
        )


        df_line = df_co2.loc[

            (
                df_co2[
                    "country"
                ].isin(
                    line_continents
                )
            )

            &

            (
                df_co2[
                    "year"
                ]
                >=
                1800
            ),

            [
                "country",
                "year",
                "co2_per_capita"
            ],

        ].dropna(
            subset=[
                "co2_per_capita"
            ]
        )


        fig_line = px.line(

            df_line,

            x="year",

            y="co2_per_capita",

            color="country",

            color_discrete_sequence=
            ORANGE_SCALE,

            labels={

                "year":
                "Year",

                "co2_per_capita":
                "CO₂ per person (tonnes)",

                "country":
                "Continent",
            },
        )


        fig_line.update_traces(
            line=dict(
                width=3
            )
        )


        fig_line = apply_plot_style(
            fig_line
        )


        st.plotly_chart(
            fig_line,
            width="stretch",
            theme=None
        )


# =========================================================
# AREA + TEMPERATURE CHARTS
# =========================================================

left2, right2 = st.columns(2)


# -------------------------
# FUEL AREA CHART
# -------------------------

with left2:

    with st.container(border=True):

        st.subheader(
            "World CO₂ by Fuel / Industry"
        )


        st.write(
            "Stacked area chart of global CO₂ "
            "emissions split by fuel or industry type."
        )


        min_data_year = int(
            df_co2[
                "year"
            ].min()
        )


        max_data_year = int(
            df_co2[
                "year"
            ].max()
        )


        area_default_start = max(
            1950,
            min_data_year
        )


        area_years = st.slider(

            "Year range",

            min_value=min_data_year,

            max_value=max_data_year,

            value=(
                area_default_start,
                max_data_year
            ),

            step=1,

            key="area_years",
        )


        if not have_fuels:

            st.warning(
                "Fuel columns are missing "
                "from the dataset."
            )

        else:

            y0, y1 = area_years


            cols = (
                ["year"]
                +
                fuel_cols
            )


            df_world_fuels = df_co2.loc[

                (
                    df_co2[
                        "country"
                    ]
                    ==
                    "World"
                )

                &

                (
                    df_co2[
                        "year"
                    ].between(
                        y0,
                        y1
                    )
                ),

                cols,

            ].copy()


            df_long = df_world_fuels.melt(

                id_vars="year",

                value_vars=fuel_cols,

                var_name="fuel",

                value_name="co2_mt",
            )


            df_long["fuel"] = (
                df_long["fuel"]
                .map(
                    fuel_labels
                )
            )


            df_long["co2_Gt"] = (
                df_long["co2_mt"]
                /
                1000
            )


            fig_area = px.area(

                df_long,

                x="year",

                y="co2_Gt",

                color="fuel",

                color_discrete_sequence=
                ORANGE_SCALE,

                labels={

                    "year":
                    "Year",

                    "co2_Gt":
                    "CO₂ (billion tonnes)",

                    "fuel":
                    "Fuel / industry",
                },
            )


            fig_area = apply_plot_style(
                fig_area
            )


            st.plotly_chart(
                fig_area,
                width="stretch",
                theme=None
            )


# -------------------------
# TEMPERATURE BAR CHART
# -------------------------

with right2:

    with st.container(border=True):

        st.subheader(
            "Avg Temperature Change from CO₂ by Continent"
        )


        st.write(
            "Average temperature change from CO₂ "
            "emissions (°C) across continents for "
            "the selected time span."
        )


        bar_max_year = min(

            2023,

            int(
                df_co2[
                    "year"
                ].max()
            )
        )


        bar_temp_range = st.slider(

            "Year range",

            min_value=1800,

            max_value=bar_max_year,

            value=(
                1800,
                bar_max_year
            ),

            step=1,

            key="bar_temp_range",
        )


        y0, y1 = bar_temp_range


        df_temp = df_co2.loc[

            (
                df_co2[
                    "year"
                ].between(
                    y0,
                    y1
                )
            )

            &

            (
                df_co2[
                    "country"
                ].isin(
                    CONTINENTS
                )
            ),

            [
                "country",
                "temperature_change_from_co2"
            ],

        ].dropna(
            subset=[
                "temperature_change_from_co2"
            ]
        )


        df_bar = (

            df_temp

            .groupby(
                "country",
                as_index=False
            )

            .agg(
                avg_temp=(
                    "temperature_change_from_co2",
                    "mean"
                )
            )
        )


        if df_bar.empty:

            st.info(
                "No temperature-change data "
                "are available for this range."
            )

        else:

            fig_bar = px.bar(

                df_bar,

                x="country",

                y="avg_temp",

                text="avg_temp",

                color="country",

                color_discrete_sequence=
                ORANGE_SCALE,

                labels={

                    "country":
                    "Continent",

                    "avg_temp":
                    "Avg temperature change "
                    "from CO₂ (°C)",
                },
            )


            ymax = df_bar[
                "avg_temp"
            ].max()


            upper_bound = (

                ymax * 1.15

                if ymax > 0

                else 1
            )


            fig_bar.update_traces(

                texttemplate="%{text:.3f}",

                textposition="outside",

                cliponaxis=False,
            )


            fig_bar.update_yaxes(
                range=[
                    0,
                    upper_bound
                ]
            )


            fig_bar = apply_plot_style(
                fig_bar
            )


            st.plotly_chart(
                fig_bar,
                width="stretch",
                theme=None
            )


# =========================================================
# DEFINITIONS / SOURCE
# =========================================================

st.divider()


with st.expander(
    "Quick definitions"
):

    st.markdown(
        """
        **t (tonne):**  
        1 metric ton = 1,000 kg = 2,204.62 lb

        **Mt:**  
        Megatonne = 1,000,000 tonnes

        **Gt:**  
        Gigatonne = 1,000,000,000 tonnes

        **1 Gt = 1,000 Mt**

        **CO₂:**  
        Carbon dioxide

        **GHG:**  
        Greenhouse gases are atmospheric gases such as
        carbon dioxide and methane that trap heat in the
        atmosphere.
        """
    )


st.caption(
    "Data source: Our World in Data — "
    "CO₂ and Greenhouse Gas Emissions dataset."
)
