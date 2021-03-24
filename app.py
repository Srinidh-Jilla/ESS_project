import pandas as pd
import altair as alt
import streamlit as st
from PIL import Image

st.title('Interactive Dashboard To Visualize Cost Of Solar PV And Wind Energy')
st.sidebar.header('Dashboard Functionalities')
st.sidebar.markdown('''
This Dashboard is built to give insights about cost of solar PV and wind energy for different countries.\n
The data considerd for this analysis for 10 Years starting from 2010 to 2019.\n
Click below to know more about cost of solar PV and wind energy\n''')
if st.sidebar.checkbox("Know More", True):
    img = Image.open("photo-1.jpeg")
    st.image(img, width=700)
    st.header("Renewable Power Generation Costs")
    st.markdown('''
    Newly installed renewable power capacity increasingly costs less than the cheapest power generation options based on fossil fuels.
    The cost data presented in this comprehensive study from the International Renewable Energy Agency (IRENA) confirms how decisively the tables have turned.\n
    More than half of the renewable capacity added in 2019 achieved lower electricity costs than new coal.
    New solar and wind projects are undercutting the cheapest of existing coal-fired plants, the report finds.\n
    Solar and wind power costs have continued to fall, complementing the more mature bioenergy, geothermal and hydropower technologies.
    Solar photovoltaics (PV) shows the sharpest cost decline over 2010-2019 at 82%, followed by concentrating solar power (CSP) at 47%, onshore wind at 40% and offshore wind at 29%.\n
    Electricity costs from utility-scale solar PV fell 13% year-on-year, reaching nearly seven cents (USD 0.068) per kilowatt-hour (kWh) in 2019.
    Onshore and offshore wind both fell about 9% year-on-year, reaching USD 0.053/kWh and USD 0.115/kWh, respectively, for newly commissioned projects.
    Costs for CSP, still the least-developed among solar and wind technologies, fell 1% to USD 0.182/kWh.\n

    Among other implications:\n
    - Replacing the costliest 500 gigawatts of coal capacity with solar and wind would cut annual system costs by up to USD 23 billion per year and yield a stimulus worth USD 940 billion, or around 1% of global GDP.\n
    - Replacing the costliest coal capacity with renewables would also reduce annual carbon dioxide (CO2) emissions by around 1.8 gigatonnes, or 5% of last year’s global total.\n
    - By 2021, up to 1 200 gigawatts of existing coal-fired capacity would cost more to operate than new utility-scale solar PV would cost to install.\n
    - Continuing cost declines confirm the need for renewable power as a low-cost climate and decarbonisation solution, aligning short-term economic needs with medium- and long-term sustainable development goals.\n
    - Renewable power installations could form a key component of economic stimulus packages in the wake of the COVID-19 pandemic.\n
    - Along with reviewing overall cost trends and their drivers, the report analyses cost components in detail. The analysis spans around 17 000 renewable power generation projects from around the world, along with data from 10 700 auctions and power purchase agreements for renewables.\n
    ''')

st.sidebar.markdown('''
Select the different options provided to vary the Visualization.
All the Charts are interactive.
''')


################################################################################## DATA ####################################################################################
@st.cache(persist=True)
def load_data_world_s():
    df = pd.read_csv("SolarProjects.csv")
    return df

@st.cache(persist=True)
def load_data_world_w():
    df = pd.read_csv("WindProjects.csv")
    return df
################################################################################## DATA ####################################################################################



################################################################################ NUMBERS ##################################################################################
def s_number():
    nc = st.slider("Select Year using the slider below",2009,2019,2009,1)
    df_solar_world = load_data_world_s()
    country = st.selectbox("Select country",["Australia","China","France","Germany","India","Italy","Japan","Netherlands","Republic of Korea","Spain","Turkey","Ukraine","United Kingdom","United States","Vietnam"])

    s_avg_data = df_solar_world[df_solar_world["Country"]==country]

    s_year = s_avg_data[s_avg_data["Year"]==nc]
    st.dataframe(s_year)

def w_number():
    nc = st.slider("Select Year using the slider below",2009,2019,2009,1)
    df_wind_world = load_data_world_w()
    country = st.selectbox("Select country",["Brazil","Canada","China","Denmark","France","Germany","India","Italy","Japan","Mexico","Spain","Sweden","Turkey","United Kingdom","United States"])

    w_avg_data = df_wind_world[df_wind_world["Country"]==country]

    w_year = w_avg_data[w_avg_data["Year"]==nc]
    st.dataframe(w_year)

def s_avg_graph():
	df_solar_world = load_data_world_s()
	brush = alt.selection(type='interval', encodings=['x'])

	bars = alt.Chart().mark_bar().encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    y='mean(Solar_LCOE (2019 USD/kWh))',
	    opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.7)),
	).add_selection(
	    brush
	).properties(
	    title='Utility-scale solar PV weighted average cost of electricity',
	    width=700,
	    height=350
	)

	line = alt.Chart().mark_rule(color='firebrick').encode(
	    y='mean(Solar_LCOE (2019 USD/kWh))',
	    size=alt.SizeValue(3),
	    tooltip=["mean(Solar_LCOE (2019 USD/kWh))"]
	).transform_filter(
	    brush
	)

	country = st.selectbox("Select country",["Australia","China","France","Germany","India","Italy","Japan","Netherlands","Republic of Korea","Spain","Turkey","Ukraine","United Kingdom","United States","Vietnam"])
	xyz = alt.layer(bars, line, data= df_solar_world[df_solar_world["Country"]==country])
	st.altair_chart(xyz)


def s_inst_graph():
	df_solar_world = load_data_world_s()
	brush = alt.selection(type='interval', encodings=['x'])

	bars = alt.Chart().mark_bar().encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    y='mean(Total installed cost (2019 USD/kW))',
	    opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.7)),
	).add_selection(
	    brush
	).properties(
	    title='Utility-scale solar PV weighted average cost of electricity',
	    width=700,
	    height=350
	)

	line = alt.Chart().mark_rule(color='firebrick').encode(
	    y='mean(Total installed cost (2019 USD/kW))',
	    size=alt.SizeValue(3),
	    tooltip=["mean(Total installed cost (2019 USD/kW))"]
	).transform_filter(
	    brush
	)

	country = st.selectbox("Select country",["Australia","China","France","Germany","India","Italy","Japan","Netherlands","Republic of Korea","Spain","Turkey","Ukraine","United Kingdom","United States","Vietnam"])
	xyz = alt.layer(bars, line, data= df_solar_world[df_solar_world["Country"]==country])
	st.altair_chart(xyz)


def w_avg_graph():
	df_wind_world = load_data_world_w()
	brush = alt.selection(type='interval', encodings=['x'])

	bars = alt.Chart().mark_bar().encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    y='mean(Wind_LCOE (2019 USD/kWh))',
	    opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.7)),
	).add_selection(
	    brush
	).properties(
	    title='Utility-scale solar PV weighted average cost of electricity',
	    width=700,
	    height=350
	)

	line = alt.Chart().mark_rule(color='firebrick').encode(
	    y='mean(Wind_LCOE (2019 USD/kWh))',
	    size=alt.SizeValue(3),
	    tooltip=["mean(Wind_LCOE (2019 USD/kWh))"]
	).transform_filter(
	    brush
	)

	country = st.selectbox("Select country",["Brazil","Canada","China","Denmark","France","Germany","India","Italy","Japan","Mexico","Spain","Sweden","Turkey","United Kingdom","United States"])
	xyz = alt.layer(bars, line, data= df_wind_world[df_wind_world["Country"]==country])
	st.altair_chart(xyz)

def w_inst_graph():
	df_wind_world = load_data_world_w()
	brush = alt.selection(type='interval', encodings=['x'])

	bars = alt.Chart().mark_bar().encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    y='mean(Total installed costs (2019 USD/kW))',
	    opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.7)),
	).add_selection(
	    brush
	).properties(
	    title='Utility-scale solar PV weighted average cost of electricity',
	    width=700,
	    height=350
	)

	line = alt.Chart().mark_rule(color='firebrick').encode(
	    y='mean(Total installed costs (2019 USD/kW))',
	    size=alt.SizeValue(3),
	    tooltip=["mean(Total installed costs (2019 USD/kW))"]
	).transform_filter(
	    brush
	)

	country = st.selectbox("Select country",["Brazil","Canada","China","Denmark","France","Germany","India","Italy","Japan","Mexico","Spain","Sweden","Turkey","United Kingdom","United States"])
	xyz = alt.layer(bars, line, data= df_wind_world[df_wind_world["Country"]==country])
	st.altair_chart(xyz)


if st.sidebar.checkbox("View Raw Data",False):
	if st.checkbox("View the dataset",False):
		dat = st.radio("Select the option",("Full dataset","Specific data entry"))
		if dat == "Full dataset":
			temp = st.selectbox("Select energy",["Wind","Solar"])
			if temp == "Solar":
				solar_raw = load_data_world_s()
				solar_raw
			else:
				wind_raw = load_data_world_w()
				wind_raw

		else:
			temp = st.selectbox("Select energy",["Wind","Solar"])
			if temp == "Solar":
				s_number()
			else:
				w_number()

	if st.checkbox("Visualize the dataset",False):
		temp = st.selectbox("Select energy",["Wind","Solar"])
		typ = st.selectbox("Select Cost type",["Average Cost","Installation Cost"])
		if temp == "Solar":
			if typ == "Average Cost":
				s_avg_graph()
			else:
				s_inst_graph()
		else:
			if typ == "Average Cost":
				w_avg_graph()
			else:
				w_inst_graph()
################################################################################ NUMBERS ##################################################################################



############################################################################## Country Wise ###############################################################################
def solar_world_avg():
	df_solar_world = load_data_world_s()
	country = st.sidebar.selectbox("Select country",["Australia","China","France","Germany","India","Italy","Japan","Netherlands","Republic of Korea","Spain","Turkey","Ukraine","United Kingdom","United States","Vietnam"])
	typ = st.sidebar.radio("Select the type of Chart",("Line Chart","Scatter Chart"))

	country_line = alt.Chart(df_solar_world[df_solar_world["Country"]==country]).encode(

	    alt.X("Year",scale=alt.Scale(zero=False)),
	    y="Solar_LCOE (2019 USD/kWh)",
	    tooltip=["Year","Solar_LCOE (2019 USD/kWh)"]

	).properties(
	    title='Utility-scale solar PV weighted average cost of electricity',
	    width=700,
	    height=350
	).interactive()

	if typ == "Line Chart":
	    st.altair_chart(country_line.mark_line(color='firebrick'))
	else:
	    st.altair_chart(country_line.mark_circle(color='firebrick'))

def solar_world_inst():
	df_solar_world = load_data_world_s()
	country = st.sidebar.selectbox("Select country",["Australia","China","France","Germany","India","Italy","Japan","Netherlands","Republic of Korea","Spain","Turkey","Ukraine","United Kingdom","United States","Vietnam"])
	typ = st.sidebar.radio("Select the type of Chart",("Line Chart","Scatter Chart"))

	country_line = alt.Chart(df_solar_world[df_solar_world["Country"]==country]).encode(

	    alt.X("Year",scale=alt.Scale(zero=False)),
	    y="Total installed cost (2019 USD/kW)",
	    tooltip=["Year","Total installed cost (2019 USD/kW)"]

	).properties(
	    title='Utility-scale solar PV weighted average cost of electricity',
	    width=700,
	    height=350
	).interactive()

	if typ == "Line Chart":
	    st.altair_chart(country_line.mark_line(color='firebrick'))
	else:
	    st.altair_chart(country_line.mark_circle(color='firebrick'))

def wind_world_avg():
	df_wind_world = load_data_world_w()
	country = st.sidebar.selectbox("Select country",["Brazil","Canada","China","Denmark","France","Germany","India","Italy","Japan","Mexico","Spain","Sweden","Turkey","United Kingdom","United States"])
	typ = st.sidebar.radio("Select the type of Chart",("Line Chart","Scatter Chart"))

	country_line = alt.Chart(df_wind_world[df_wind_world["Country"]==country]).encode(

	    alt.X("Year",scale=alt.Scale(zero=False)),
	    y='Wind_LCOE (2019 USD/kWh)',
	    tooltip=["Year","Wind_LCOE (2019 USD/kWh)"]

	).properties(
	    title='Onshore wind weighted average total installed costs',
	    width=700,
	    height=350
	).interactive()

	if typ == "Line Chart":
	    st.altair_chart(country_line.mark_line(color='firebrick'))
	else:
	    st.altair_chart(country_line.mark_circle(color='firebrick'))


def wind_world_inst():
	df_wind_world = load_data_world_w()
	country = st.sidebar.selectbox("Select country",["Brazil","Canada","China","Denmark","France","Germany","India","Italy","Japan","Mexico","Spain","Sweden","Turkey","United Kingdom","United States"])
	typ = st.sidebar.radio("Select the type of Chart",("Line Chart","Scatter Chart"))

	country_line = alt.Chart(df_wind_world[df_wind_world["Country"]==country]).encode(

	    alt.X("Year",scale=alt.Scale(zero=False)),
	    y= 'Total installed costs (2019 USD/kW)',
	    tooltip=["Year","Total installed costs (2019 USD/kW)"]

	).properties(
	    title='Onshore wind weighted average total installed costs',
	    width=700,
	    height=350
	).interactive()

	if typ == "Line Chart":
	    st.altair_chart(country_line.mark_line(color='firebrick'))
	else:
	    st.altair_chart(country_line.mark_circle(color='firebrick'))

if st.sidebar.checkbox("View Country Wise Data",False):
	energy = st.sidebar.selectbox("Select energy",["Wind","Solar"])
	typ = st.sidebar.selectbox("Select Cost type",["Average Cost","Installation Cost"])

	if energy == "Solar":
		if typ == "Average Cost":
			solar_world_avg()
		else:
			solar_world_inst()
	else:
		if typ == "Average Cost":
			wind_world_avg()
		else:
			wind_world_inst()
############################################################################## Country Wise ###############################################################################



################################################################################ Comparisions #############################################################################

def comparitve_s_avg():
	df_solar_world = load_data_world_s()

	brush = alt.selection_interval()

	points = alt.Chart(df_solar_world).mark_point().encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    y='Solar_LCOE (2019 USD/kWh)',
	    color=alt.condition(brush, 'Country', alt.value('lightgray')),
	    tooltip=["Year","Solar_LCOE (2019 USD/kWh)"]
	).add_selection(
	    brush
	).properties(
	    title='Utility-scale solar PV weighted average cost of electricity in selected countries, 2010-2019',
	    width=700,
	    height=350
	)

	bars = alt.Chart(df_solar_world).mark_bar().encode(
	    y='Country',
	    color='Country',
	    x='Solar_LCOE (2019 USD/kWh)',
	    tooltip=["Year","Solar_LCOE (2019 USD/kWh)"]
	).transform_filter(
	    brush
	)

	st.altair_chart(points & bars)

def comparitve_s_inst():
	df_solar_world = load_data_world_s()

	brush = alt.selection_interval()

	points = alt.Chart(df_solar_world).mark_point().encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    y='Total installed cost (2019 USD/kW)',
	    color=alt.condition(brush, 'Country', alt.value('lightgray')),
	    tooltip=["Year","Total installed cost (2019 USD/kW)"]
	).add_selection(
	    brush
	).properties(
	    title='Utility-scale solar PV total installed cost trends in selected countries, 2010-2019',
	    width=700,
	    height=350
	)

	bars = alt.Chart(df_solar_world).mark_bar().encode(
	    y='Country',
	    color='Country',
	    x='Total installed cost (2019 USD/kW)',
	    tooltip=["Year","Total installed cost (2019 USD/kW)"]
	).transform_filter(
	    brush
	)

	st.altair_chart(points & bars)


def comparitve_w_avg():
	df_wind_world = load_data_world_w()

	brush = alt.selection_interval()

	points = alt.Chart(df_wind_world).mark_point().encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    y='Wind_LCOE (2019 USD/kWh)',
	    color=alt.condition(brush, 'Country', alt.value('lightgray')),
	    tooltip=["Year","Wind_LCOE (2019 USD/kWh)"]
	).add_selection(
	    brush
	).properties(
	    title='The weighted average LCOE of commissioned onshore wind projects in 15 countries, 2010–2019',
	    width=700,
	    height=350
	)

	bars = alt.Chart(df_wind_world).mark_bar().encode(
	    y='Country',
	    color='Country',
	    x='Wind_LCOE (2019 USD/kWh)',
	    tooltip=["Year","Wind_LCOE (2019 USD/kWh)"]
	).transform_filter(
	    brush
	)

	st.altair_chart(points & bars)


def comparitve_w_inst():
	df_wind_world = load_data_world_w()

	brush = alt.selection_interval()

	points = alt.Chart(df_wind_world).mark_point().encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    y='Total installed costs (2019 USD/kW)',
	    color=alt.condition(brush, 'Country', alt.value('lightgray')),
	    tooltip=["Year","Total installed costs (2019 USD/kW)"]
	).add_selection(
	    brush
	).properties(
	    title='Onshore wind weighted average total installed costs in 15 countries, 2010–2019',
	    width=700,
	    height=350
	)

	bars = alt.Chart(df_wind_world).mark_bar().encode(
	    y='Country',
	    color='Country',
	    x='Total installed costs (2019 USD/kW)',
	    tooltip=["Country","Total installed costs (2019 USD/kW)"]
	).transform_filter(
	    brush
	)

	st.altair_chart(points & bars)

def comparitve_s_avg_line():
	country = st.multiselect("Select country",["Australia","China","France","Germany","India","Italy","Japan","Netherlands","Republic of Korea","Spain","Turkey","Ukraine","United Kingdom","United States","Vietnam"])

	df_solar_world = load_data_world_s()
	highlight = alt.selection(type='single', on='mouseover',
		fields=['Country'], nearest=True)

	base = alt.Chart(df_solar_world[df_solar_world["Country"].isin(country)]).encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    y='Solar_LCOE (2019 USD/kWh)',
	    color= 'Country'
	)

	points = base.mark_circle().encode(
	    opacity=alt.value(0)
	).add_selection(
	    highlight
	).properties(
	    width=700,
	    height=350
	)

	lines = base.mark_line().encode(
	    size=alt.condition(~highlight, alt.value(1), alt.value(3))
	)

	bars = alt.Chart(df_solar_world[df_solar_world["Country"].isin(country)]).mark_bar().encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    color='Country',
	    y='Solar_LCOE (2019 USD/kWh)',
	    tooltip=["Year","Solar_LCOE (2019 USD/kWh)"]
	).transform_filter(
	    highlight
	)


	abc = alt.layer(points,lines)
	st.altair_chart(abc & bars)


def comparitve_s_inst_line():
	country = st.multiselect("Select country",["Australia","China","France","Germany","India","Italy","Japan","Netherlands","Republic of Korea","Spain","Turkey","Ukraine","United Kingdom","United States","Vietnam"])

	df_solar_world = load_data_world_s()
	highlight = alt.selection(type='single', on='mouseover',
		fields=['Country'], nearest=True)

	base = alt.Chart(df_solar_world[df_solar_world["Country"].isin(country)]).encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    y='Total installed cost (2019 USD/kW)',
	    color= 'Country'
	)

	points = base.mark_circle().encode(
	    opacity=alt.value(0)
	).add_selection(
	    highlight
	).properties(
	    width=700,
	    height=350
	)

	lines = base.mark_line().encode(
	    size=alt.condition(~highlight, alt.value(1), alt.value(3))
	)

	bars = alt.Chart(df_solar_world[df_solar_world["Country"].isin(country)]).mark_bar().encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    color='Country',
	    y='Total installed cost (2019 USD/kW)',
	    tooltip=["Year","Total installed cost (2019 USD/kW)"]
	).transform_filter(
	    highlight
	)


	abc = alt.layer(points,lines)
	st.altair_chart(abc & bars)

def comparitve_w_avg_line():
	df_wind_world = load_data_world_w()
	country = st.multiselect("Select country",["Brazil","Canada","China","Denmark","France","Germany","India","Italy","Japan","Mexico","Spain","Sweden","Turkey","United Kingdom","United States"])

	highlight = alt.selection(type='single', on='mouseover',
		fields=['Country'], nearest=True)

	base = alt.Chart(df_wind_world[df_wind_world["Country"].isin(country)]).encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    y='Wind_LCOE (2019 USD/kWh)',
	    color= 'Country'
	)

	points = base.mark_circle().encode(
	    opacity=alt.value(0)
	).add_selection(
	    highlight
	).properties(
	    width=700,
	    height=350
	)

	lines = base.mark_line().encode(
	    size=alt.condition(~highlight, alt.value(1), alt.value(3))
	)

	bars = alt.Chart(df_wind_world[df_wind_world["Country"].isin(country)]).mark_bar().encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    color='Country',
	    y='Wind_LCOE (2019 USD/kWh)',
	    tooltip=["Year","Wind_LCOE (2019 USD/kWh)"]
	).transform_filter(
	    highlight
	)


	abc = alt.layer(points,lines)
	st.altair_chart(abc & bars)


def comparitve_w_inst_line():
	df_wind_world = load_data_world_w()
	country = st.multiselect("Select country",["Brazil","Canada","China","Denmark","France","Germany","India","Italy","Japan","Mexico","Spain","Sweden","Turkey","United Kingdom","United States"])

	highlight = alt.selection(type='single', on='mouseover',
		fields=['Country'], nearest=True)

	base = alt.Chart(df_wind_world[df_wind_world["Country"].isin(country)]).encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    y='Total installed cost (2019 USD/kW)',
	    color= 'Country'
	)

	points = base.mark_circle().encode(
	    opacity=alt.value(0)
	).add_selection(
	    highlight
	).properties(
	    width=700,
	    height=350
	)

	lines = base.mark_line().encode(
	    size=alt.condition(~highlight, alt.value(1), alt.value(3))
	)

	bars = alt.Chart(df_wind_world[df_wind_world["Country"].isin(country)]).mark_bar().encode(
	    alt.X('Year',scale=alt.Scale(zero=False)),
	    color='Country',
	    y='Total installed cost (2019 USD/kW)',
	    tooltip=["Year","Total installed cost (2019 USD/kW)"]
	).transform_filter(
	    highlight
	)


	abc = alt.layer(points,lines)
	st.altair_chart(abc & bars)


if st.sidebar.checkbox("View the Comparison for Countries",False):

	typ = st.sidebar.radio("Select the type of Chart",("Multiline and Bar Chart","Scatter and Bar Chart"))
	if typ == "Multiline and Bar Chart":
		temp = st.sidebar.selectbox("Select energy",["Wind","Solar"])
		temp1 = st.sidebar.selectbox("Select Cost type",["Average Cost","Installation Cost"])
		if temp == "Solar":
			if temp1 == "Average Cost":
				comparitve_s_avg_line()
			else:
				comparitve_s_inst_line()
		else:
			if temp1 == "Average Cost":
				comparitve_w_avg_line()
			else:
				comparitve_w_inst_line()

	else:
		temp = st.sidebar.selectbox("Select energy",["Wind","Solar"])
		temp1 = st.sidebar.selectbox("Select Cost type",["Average Cost","Installation Cost"])
		if temp == "Solar":
		    if temp1 == "Average Cost":
		    	comparitve_s_avg()
		    else:
		    	comparitve_s_inst()
		else:
		    if temp1 == "Average Cost":
		    	comparitve_w_avg()
		    else:
		    	comparitve_w_inst()
################################################################################ Comparisions #############################################################################
st.sidebar.markdown("Note: One checkbox at a time for better experience")
