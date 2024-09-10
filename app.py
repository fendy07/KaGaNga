import streamlit as st
from streamlit_navigation_bar import st_navbar

st.set_page_config(page_title = 'KaGaNga', page_icon = "✍️", layout = "wide")

# PAGE SETUP
about_page = st.Page(
    page = 'pages/about.py',
    title = 'About Project',
    icon = '✍️',
    default = True
)

# PAGE PROJECT
project_page = st.Page(
    page = 'pages/model.py',
    title = 'Project',
    icon = '🤖'
)

#----NAVIGATION PAGE SETUP WITH SECTION-----
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_page],
    }
)

#----LOGO-------
#st.logo('images/')
st.sidebar.text(f'Created by Fendy Hendriyanto 👨🏼‍💻')
st.sidebar.info("Untuk codingnya, bisa ditemukan di my GitHub:")
st.sidebar.link_button("GitHub Source","https://github.com/fendy07")

pg.run()
