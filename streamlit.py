import streamlit as st


def main():

    language = st.sidebar.selectbox(
            "Мова / Language",
            ["Українська", "English"],
            key="language"
        )

    if language == 'Українська':
        model_dem_title = 'Моделі використання '

    else:
        model_dem_title = 'Usage models'
       
    model_demonstration_page = st.Page("model_demonstration.py",title=model_dem_title)

    pg = st.navigation([model_demonstration_page])
    pg.run()

if __name__ == '__main__':
    main()



