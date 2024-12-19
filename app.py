import streamlit as st
import shutil
import os
import sys

### History page

# init path to current folder
sys.path.append('.')
# check if there is history
try:
    folder = os.path.join('static','uploads')

    # List of folders in the folder
    flower_folders = [f for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f))]
except Exception as e:
    flower_folders = []

# Create the flower pages
pages=[]
for f in flower_folders :
    def make_flower_page(f=f):
        st.title(f)
        repertoire_images = os.path.join(folder,f)

        # List images on one flower repository
        images = [f for f in os.listdir(repertoire_images) if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]

        # Select the number of picture a line
        images_ligne = 3

        # Create gride and fill it with pictures
        colones = st.columns(images_ligne)
        for i, image in enumerate(images):
            col = colones[i % images_ligne]
            col.image(os.path.join(repertoire_images, image), caption=image)
        
    pages.append(st.Page(make_flower_page, url_path=f"/{f}", title=f"{f}"))

def delHistory(pages=pages):
    if os.path.exists(folder) and os.path.isdir(folder):
        try:
            shutil.rmtree(folder)
            st.sidebar.success('History deleted with success', icon="✅")
            print(f"History deleted with success")
        except Exception as e:
            print(f"Error while deleting history : {e}")


### Main application

st.set_page_config(page_title="FlowerFinder", page_icon="static/src/logo.jpeg")

pg = st.navigation({
    "": [
        st.Page("flower_finder_page.py", title="Flower Finder", icon="🔎"),
    ],
    "⏱️  History": pages,
    "📗 About": [
        st.Page("about_page.py", title="Flower Classes")
    ]
})

if len(flower_folders)>0:
    st.sidebar.button("Delete Histoiry", type="primary", on_click=delHistory)

pg.run()