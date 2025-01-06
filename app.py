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

    flower_folders=[]

    # List of folders in the folder
    for f in os.listdir(folder) :
        f_path = os.path.join(folder,f)
        # insert folders containing files
        if os.path.isdir(f_path) and len(os.listdir(f_path))>0:
            flower_folders.append(f)
        # Delete empty folders
        elif os.path.isdir(f_path) and len(os.listdir(f_path))==0:
            try :
                os.rmdir(f_path)
            except Exception as e:
                print(f"error while removing empty folders : {e}")    

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
            image_path = os.path.join(repertoire_images, image)
            col.image(image_path)

            # Delete Button (delete the associated picture)
            is_pressed = col.button("🗑️ Delete", key=i, use_container_width=True)
            if is_pressed :
                try :
                    os.remove(image_path)
                    images.remove(image)
                    # run the application again to apply the changes
                    st.rerun()

                except Exception as e :
                    col.error(e)
            col.markdown(f"""<div style="margin-bottom: 2em"></div>""", unsafe_allow_html=True)
        
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