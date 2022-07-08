import streamlit as st
import json
import requests as re
import pandas as pd

try:

    from streamlit_functions.helper_functions import *

    # app design
    app_meta('🖼️')
    set_bg_hack('./images/Manga.png')

    # hide warning for st.pyplot() deprecation
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Main panel setup
    display_app_header(main_txt='Manga Recommendation App',
                       sub_txt='Get suggestions on what to read, read or listen to next using this recommendations web app!')

    st.markdown("""---""")

    st.write("""
        ## About
        This App using machine learning algorithms to suggest what Manga you should read next!

        The API was built with FastAPI and can be found [here.](https://credit-fraud-ml-api.herokuapp.com/)

        The notebook, model and documentation(Dockerfiles, FastAPI script, Streamlit App script) are available on [GitHub.](https://github.com/Nneji123/Media-Recommendation-Engine)        

        """)

    # provide options to user to navigate to other dqw apps

    st.markdown("""---""")

    intro_text = """


    """
    intro = st.expander(
        "Click here for more info on the Media Recommendation Engine ✨")

    with intro:
        sub_text(intro_text)
except KeyError:
    st.error("Please select a key value from the dropdown to continue.")

except ValueError:
    st.error(
        "Oops, something went wrong. Please check previous steps for inconsistent input.")

except TypeError:
    st.error(
        "Oops, something went wrong. Please check previous steps for inconsistent input.")


input_query = st.text_input("Input the Manga you last readed: ")
values = {"Manga": input_query}

res = re.post(
    f"http://backend.docker:8000/manga", json=values)
json_str = json.dumps(res.json())
resp = json.loads(json_str)
resp = list(resp.values())
resp = pd.DataFrame(resp, index=None).T
st.write("These are the Manga you should read next:")
resp = st.dataframe(resp)


#st.write(f"These are the Manga you should read next: {resp}.")
