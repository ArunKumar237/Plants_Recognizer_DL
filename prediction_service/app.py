# for scrapping description
import selenium
import urllib3
import requests
from bs4 import BeautifulSoup as bs

# for input and output
import streamlit as st
import skimage
from skimage.io import imread
from skimage import data, color
from skimage.transform import resize
import tensorflow as tf
import webbrowser
import numpy as np
import gdown
import os

def download_model():
    print("Downloading model.................")
    gdown.download(url='https://drive.google.com/uc?export=download&id=1-Rvutw0DnXi4TjeicgLxOxLjrWWBpeo2', quiet=True) #DOWNLOADING MODEL WHICH WAS TRAINED IN COLAB
    print("Model Download Completed\n")

def download_desc(search_term):
    URL= 'https://en.wikipedia.org/wiki/'+search_term
    page = requests.get(URL)
    soup = bs(page.content, 'html.parser')
    desc = soup.find_all('p')[1].get_text()
    return desc

if os.path.isfile('final_model.h5') == False:
    download_model()
else:
    pass

model = tf.keras.models.load_model('final_model.h5') 
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:

    image = imread(uploaded_file)
    image = resize(image, (224,224), anti_aliasing=False)
    if len(image.shape) == 2: #checking wether image is gray or color
        img_array = skimage.color.gray2rgb(image)
        img_array = np.expand_dims(img_array, axis=0)
        result = model.predict(img_array) # [[0.99, 0.01], [0.99, 0.01]]
    else:
        img_array = np.expand_dims(image, axis=0)
        result = model.predict(img_array) # [[0.99, 0.01], [0.99, 0.01]]

    argmax_index = np.argmax(result, axis=1) # [0, 0]
    col1, col2 = st.columns([1,3])
    if argmax_index[0] == 0:
        with col1:
            st.image(image, caption='predicted: Acer_Campestre')
        with col2:
            st.markdown(download_desc('Acer_Campestre'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Acer_Campestre'.lower())
    elif argmax_index[0] == 1:
        with col1:
            st.image(image, caption='predicted: Acer_Capillipes')
        with col2:
            st.markdown(download_desc('Acer_Capillipes'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Acer_Capillipes'.lower())
    elif argmax_index[0] == 2:
        with col1:
            st.image(image, caption='predicted: Acer_Circinatum')
        with col2:
            st.markdown(download_desc('Acer_Circinatum'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Acer_Circinatum'.lower())
    elif argmax_index[0] == 3:
        with col1:
            st.image(image, caption='predicted: Acer_Mono')
        with col2:
            st.markdown(download_desc('Acer_Mono'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Acer_Mono'.lower())
    elif argmax_index[0] == 4:
        with col1:
            st.image(image, caption='predicted: Acer_Opalus')
        with col2:
            st.markdown(download_desc('Acer_Opalus'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Acer_Opalus'.lower())
    elif argmax_index[0] == 5:
        with col1:
            st.image(image, caption='predicted: Acer_Palmatum')
        with col2:
            st.markdown(download_desc('Acer_Palmatum'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Acer_Palmatum'.lower())
    elif argmax_index[0] == 6:
        with col1:
            st.image(image, caption='predicted: Acer_Pictum')
        with col2:
            st.markdown(download_desc('Acer_Pictum'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Acer_Pictum'.lower())
    elif argmax_index[0] == 7:
        with col1:
            st.image(image, caption='predicted: Acer_Platanoids')
        with col2:
            st.markdown(download_desc('Acer_Platanoids'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Acer_Platanoids'.lower())
    elif argmax_index[0] == 8:
        with col1:
            st.image(image, caption='predicted: Acer_Rubrum')
        with col2:
            st.markdown(download_desc('Acer_Rubrum'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Acer_Rubrum'.lower())
    elif argmax_index[0] == 9:
        with col1:
            st.image(image, caption='predicted: Acer_Rufinerve')
        with col2:
            st.markdown(download_desc('Acer_Rufinerve'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Acer_Rufinerve'.lower())
    elif argmax_index[0] == 10:
        with col1:
            st.image(image, caption='predicted: Acer_Saccharinum')
        with col2:
            st.markdown(download_desc('Acer_Saccharinum'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Acer_Saccharinum'.lower())
    elif argmax_index[0] == 11:
        with col1:
            st.image(image, caption='predicted: Alnus_Cordata')
        with col2:
            st.markdown(download_desc('Alnus_Cordata'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Alnus_Cordata'.lower())
    elif argmax_index[0] == 12:
        with col1:
            st.image(image, caption='predicted: Alnus_Maximowiczii')
        with col2:
            st.markdown(download_desc('Alnus_Maximowiczii'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Alnus_Maximowiczii'.lower())
    elif argmax_index[0] == 13:
        with col1:
            st.image(image, caption='predicted: Alnus_Rubra')
        with col2:
            st.markdown(download_desc('Alnus_Rubra'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Alnus_Rubra'.lower())
    elif argmax_index[0] == 14:
        with col1:
            st.image(image, caption='predicted: Alnus_Sieboldiana')
        with col2:
            st.markdown(download_desc('Alnus_Sieboldiana'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Alnus_Sieboldiana'.lower())
    elif argmax_index[0] == 15:
        with col1:
            st.image(image, caption='predicted: Alnus_Viridis')
        with col2:
            st.markdown(download_desc('Alnus_Viridis'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Alnus_Viridis'.lower())
    elif argmax_index[0] == 16:
        with col1:
            st.image(image, caption='predicted: Arundinaria_Simonii')
        with col2:
            st.markdown(download_desc('Arundinaria_Simonii'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Arundinaria_Simonii'.lower())
    elif argmax_index[0] == 17:
        with col1:
            st.image(image, caption='predicted: Betula_Austrosinensis')
        with col2:
            st.markdown(download_desc('Betula_Austrosinensis'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Betula_Austrosinensis'.lower())
    elif argmax_index[0] == 18:
        with col1:
            st.image(image, caption='predicted: Betula_Pendula')
        with col2:
            st.markdown(download_desc('Betula_Pendula'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Betula_Pendula'.lower())
    elif argmax_index[0] == 19:
        with col1:
            st.image(image, caption='predicted: Callicarpa_Bodinieri')
        with col2:
            st.markdown(download_desc('Callicarpa_Bodinieri'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Callicarpa_Bodinieri'.lower())
    elif argmax_index[0] == 20:
        with col1:
            st.image(image, caption='predicted: Castanea_Sativa')
        with col2:
            st.markdown(download_desc('Castanea_Sativa'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Castanea_Sativa'.lower())
    elif argmax_index[0] == 21:
        with col1:
            st.image(image, caption='predicted: Celtis_Koraiensis')
        with col2:
            st.markdown(download_desc('Celtis_Koraiensis'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Celtis_Koraiensis'.lower())
    elif argmax_index[0] == 22:
        with col1:
            st.image(image, caption='predicted: Cercis_Siliquastrum')
        with col2:
            st.markdown(download_desc('Cercis_Siliquastrum'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Cercis_Siliquastrum'.lower())
    elif argmax_index[0] == 23:
        with col1:
            st.image(image, caption='predicted: Cornus_Chinensis')
        with col2:
            st.markdown(download_desc('Cornus_Chinensis'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Cornus_Chinensis'.lower())
    elif argmax_index[0] == 24:
        with col1:
            st.image(image, caption='predicted: Cornus_Controversa')
        with col2:
            st.markdown(download_desc('Cornus_Controversa'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Cornus_Controversa'.lower())
    elif argmax_index[0] == 25:
        with col1:
            st.image(image, caption='predicted: Cornus_Macrophylla')
        with col2:
            st.markdown(download_desc('Cornus_Macrophylla'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Cornus_Macrophylla'.lower())
    elif argmax_index[0] == 26:
        with col1:
            st.image(image, caption='predicted: Cotinus_Coggygria')
        with col2:
            st.markdown(download_desc('Cotinus_Coggygria'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Cotinus_Coggygria'.lower())
    elif argmax_index[0] == 27:
        with col1:
            st.image(image, caption='predicted: Crataegus_Monogyna')
        with col2:
            st.markdown(download_desc('Crataegus_Monogyna'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Crataegus_Monogyna'.lower())
    elif argmax_index[0] == 28:
        with col1:
            st.image(image, caption='predicted: Cytisus_Battandieri')
        with col2:
            st.markdown(download_desc('Cytisus_Battandieri'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Cytisus_Battandieri'.lower())
    elif argmax_index[0] == 29:
        with col1:
            st.image(image, caption='predicted: Eucalyptus_Glaucescens')
        with col2:
            st.markdown(download_desc('Eucalyptus_Glaucescens'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Eucalyptus_Glaucescens'.lower())
    elif argmax_index[0] == 30:
        with col1:
            st.image(image, caption='predicted: Eucalyptus_Neglecta')
        with col2:
            st.markdown(download_desc('Eucalyptus_Neglecta'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Eucalyptus_Neglecta'.lower())
    elif argmax_index[0] == 31:
        with col1:
            st.image(image, caption='predicted: Eucalyptus_Urnigera')
        with col2:
            st.markdown(download_desc('Eucalyptus_Urnigera'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Eucalyptus_Urnigera'.lower())
    elif argmax_index[0] == 32:
        with col1:
            st.image(image, caption='predicted: Fagus_Sylvatica')
        with col2:
            st.markdown(download_desc('Fagus_Sylvatica'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Fagus_Sylvatica'.lower())
    elif argmax_index[0] == 33:
        with col1:
            st.image(image, caption='predicted: Ginkgo_Biloba')
        with col2:
            st.markdown(download_desc('Ginkgo_Biloba'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Ginkgo_Biloba'.lower())
    elif argmax_index[0] == 34:
        with col1:
            st.image(image, caption='predicted: Ilex_Aquifolium')
        with col2:
            st.markdown(download_desc('Ilex_Aquifolium'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Ilex_Aquifolium'.lower())
    elif argmax_index[0] == 35:
        with col1:
            st.image(image, caption='predicted: Ilex_Cornuta')
        with col2:
            st.markdown(download_desc('Ilex_Cornuta'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Ilex_Cornuta'.lower())
    elif argmax_index[0] == 36:
        with col1:
            st.image(image, caption='predicted: Liquidambar_Styraciflua')
        with col2:
            st.markdown(download_desc('Liquidambar_Styraciflua'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Liquidambar_Styraciflua'.lower())
    elif argmax_index[0] == 37:
        with col1:
            st.image(image, caption='predicted: Liriodendron_Tulipifera')
        with col2:
            st.markdown(download_desc('Liriodendron_Tulipifera'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Liriodendron_Tulipifera'.lower())
    elif argmax_index[0] == 38:
        with col1:
            st.image(image, caption='predicted: Lithocarpus_Cleistocarpus')
        with col2:
            st.markdown(download_desc('Lithocarpus_Cleistocarpus'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Lithocarpus_Cleistocarpus'.lower())
    elif argmax_index[0] == 39:
        with col1:
            st.image(image, caption='predicted: Lithocarpus_Edulis')
        with col2:
            st.markdown(download_desc('Lithocarpus_Edulis'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Lithocarpus_Edulis'.lower())
    elif argmax_index[0] == 40:
        with col1:
            st.image(image, caption='predicted: Magnolia_Heptapeta')
        with col2:
            st.markdown(download_desc('Magnolia_Heptapeta'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Magnolia_Heptapeta'.lower())
    elif argmax_index[0] == 41:
        with col1:
            st.image(image, caption='predicted: Magnolia_Salicifolia')
        with col2:
            st.markdown(download_desc('Magnolia_Salicifolia'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Magnolia_Salicifolia'.lower())
    elif argmax_index[0] == 42:
        with col1:
            st.image(image, caption='predicted: Morus_Nigra')
        with col2:
            st.markdown(download_desc('Morus_Nigra'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Morus_Nigra'.lower())
    elif argmax_index[0] == 43:
        with col1:
            st.image(image, caption='predicted: Olea_Europaea')
        with col2:
            st.markdown(download_desc('Olea_Europaea'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Olea_Europaea'.lower())
    elif argmax_index[0] == 44:
        with col1:
            st.image(image, caption='predicted: Phildelphus')
        with col2:
            st.markdown(download_desc('Phildelphus'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Phildelphus'.lower())
    elif argmax_index[0] == 45:
        with col1:
            st.image(image, caption='predicted: Populus_Adenopoda')
        with col2:
            st.markdown(download_desc('Populus_Adenopoda'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Populus_Adenopoda'.lower())
    elif argmax_index[0] == 46:
        with col1:
            st.image(image, caption='predicted: Populus_Grandidentata')
        with col2:
            st.markdown(download_desc('Populus_Grandidentata'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Populus_Grandidentata'.lower())
    elif argmax_index[0] == 47:
        with col1:
            st.image(image, caption='predicted: Populus_Nigra')
        with col2:
            st.markdown(download_desc('Populus_Nigra'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Populus_Nigra'.lower())
    elif argmax_index[0] == 48:
        with col1:
            st.image(image, caption='predicted: Prunus_Avium')
        with col2:
            st.markdown(download_desc('Prunus_Avium'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Prunus_Avium'.lower())
    elif argmax_index[0] == 49:
        with col1:
            st.image(image, caption='predicted: Prunus_X_Shmittii')
        with col2:
            st.markdown(download_desc('Prunus_X_Shmittii'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Prunus_X_Shmittii'.lower())
    elif argmax_index[0] == 50:
        with col1:
            st.image(image, caption='predicted: Pterocarya_Stenoptera')
        with col2:
            st.markdown(download_desc('Pterocarya_Stenoptera'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Pterocarya_Stenoptera'.lower())
    elif argmax_index[0] == 51:
        with col1:
            st.image(image, caption='predicted: Quercus_Afares')
        with col2:
            st.markdown(download_desc('Quercus_Afares'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Afares'.lower())
    elif argmax_index[0] == 52:
        with col1:
            st.image(image, caption='predicted: Quercus_Agrifolia')
        with col2:
            st.markdown(download_desc('Quercus_Agrifolia'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Agrifolia'.lower())
    elif argmax_index[0] == 53:
        with col1:
            st.image(image, caption='predicted: Quercus_Alnifolia')
        with col2:
            st.markdown(download_desc('Quercus_Alnifolia'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Alnifolia'.lower())
    elif argmax_index[0] == 54:
        with col1:
            st.image(image, caption='predicted: Quercus_Brantii')
        with col2:
            st.markdown(download_desc('Quercus_Brantii'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Brantii'.lower())
    elif argmax_index[0] == 55:
        with col1:
            st.image(image, caption='predicted: Quercus_Canariensis')
        with col2:
            st.markdown(download_desc('Quercus_Canariensis'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Canariensis'.lower())
    elif argmax_index[0] == 56:
        with col1:
            st.image(image, caption='predicted: Quercus_Castaneifolia')
        with col2:
            st.markdown(download_desc('Quercus_Castaneifolia'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Castaneifolia'.lower())
    elif argmax_index[0] == 57:
        with col1:
            st.image(image, caption='predicted: Quercus_Cerris')
        with col2:
            st.markdown(download_desc('Quercus_Cerris'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Cerris'.lower())
    elif argmax_index[0] == 58:
        with col1:
            st.image(image, caption='predicted: Quercus_Chrysolepis')
        with col2:
            st.markdown(download_desc('Quercus_Chrysolepis'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Chrysolepis'.lower())
    elif argmax_index[0] == 59:
        with col1:
            st.image(image, caption='predicted: Quercus_Coccifera')
        with col2:
            st.markdown(download_desc('Quercus_Coccifera'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Coccifera'.lower())
    elif argmax_index[0] == 60:
        with col1:
            st.image(image, caption='predicted: Quercus_Coccinea')
        with col2:
            st.markdown(download_desc('Quercus_Coccinea'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Coccinea'.lower())
    elif argmax_index[0] == 61:
        with col1:
            st.image(image, caption='predicted: Quercus_Crassifolia')
        with col2:
            st.markdown(download_desc('Quercus_Crassifolia'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Crassifolia'.lower())
    elif argmax_index[0] == 62:
        with col1:
            st.image(image, caption='predicted: Quercus_Crassipes')
        with col2:
            st.markdown(download_desc('Quercus_Crassipes'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Crassipes'.lower())
    elif argmax_index[0] == 63:
        with col1:
            st.image(image, caption='predicted: Quercus_Dolicholepis')
        with col2:
            st.markdown(download_desc('Quercus_Dolicholepis'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Dolicholepis'.lower())
    elif argmax_index[0] == 64:
        with col1:
            st.image(image, caption='predicted: Quercus_Ellipsoidalis')
        with col2:
            st.markdown(download_desc('Quercus_Ellipsoidalis'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Ellipsoidalis'.lower())
    elif argmax_index[0] == 65:
        with col1:
            st.image(image, caption='predicted: Quercus_Greggii')
        with col2:
            st.markdown(download_desc('Quercus_Greggii'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Greggii'.lower())
    elif argmax_index[0] == 66:
        with col1:
            st.image(image, caption='predicted: Quercus_Hartwissiana')
        with col2:
            st.markdown(download_desc('Quercus_Hartwissiana'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Hartwissiana'.lower())
    elif argmax_index[0] == 67:
        with col1:
            st.image(image, caption='predicted: Quercus_Ilex')
        with col2:
            st.markdown(download_desc('Quercus_Ilex'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Ilex'.lower())
    elif argmax_index[0] == 68:
        with col1:
            st.image(image, caption='predicted: Quercus_Imbricaria')
        with col2:
            st.markdown(download_desc('Quercus_Imbricaria'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Imbricaria'.lower())
    elif argmax_index[0] == 69:
        with col1:
            st.image(image, caption='predicted: Quercus_Infectoria_sub')
        with col2:
            st.markdown(download_desc('Quercus_Infectoria_sub'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Infectoria_sub'.lower())
    elif argmax_index[0] == 70:
        with col1:
            st.image(image, caption='predicted: Quercus_Kewensis')
        with col2:
            st.markdown(download_desc('Quercus_Kewensis'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Kewensis'.lower())
    elif argmax_index[0] == 71:
        with col1:
            st.image(image, caption='predicted: Quercus_Nigra')
        with col2:
            st.markdown(download_desc('Quercus_Nigra'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Nigra'.lower())
    elif argmax_index[0] == 72:
        with col1:
            st.image(image, caption='predicted: Quercus_Palustris')
        with col2:
            st.markdown(download_desc('Quercus_Palustris'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Palustris'.lower())
    elif argmax_index[0] == 73:
        with col1:
            st.image(image, caption='predicted: Quercus_Phellos')
        with col2:
            st.markdown(download_desc('Quercus_Phellos'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Phellos'.lower())
    elif argmax_index[0] == 74:
        with col1:
            st.image(image, caption='predicted: Quercus_Phillyraeoides')
        with col2:
            st.markdown(download_desc('Quercus_Phillyraeoides'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Phillyraeoides'.lower())
    elif argmax_index[0] == 75:
        with col1:
            st.image(image, caption='predicted: Quercus_Pontica')
        with col2:
            st.markdown(download_desc('Quercus_Pontica'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Pontica'.lower())
    elif argmax_index[0] == 76:
        with col1:
            st.image(image, caption='predicted: Quercus_Pubescens')
        with col2:
            st.markdown(download_desc('Quercus_Pubescens'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Pubescens'.lower())
    elif argmax_index[0] == 77:
        with col1:
            st.image(image, caption='predicted: Quercus_Pyrenaica')
        with col2:
            st.markdown(download_desc('Quercus_Pyrenaica'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Pyrenaica'.lower())
    elif argmax_index[0] == 78:
        with col1:
            st.image(image, caption='predicted: Quercus_Rhysophylla')
        with col2:
            st.markdown(download_desc('Quercus_Rhysophylla'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Rhysophylla'.lower())
    elif argmax_index[0] == 79:
        with col1:
            st.image(image, caption='predicted: Quercus_Rubra')
        with col2:
            st.markdown(download_desc('Quercus_Rubra'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Rubra'.lower())
    elif argmax_index[0] == 80:
        with col1:
            st.image(image, caption='predicted: Quercus_Semecarpifolia')
        with col2:
            st.markdown(download_desc('Quercus_Semecarpifolia'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Semecarpifolia'.lower())
    elif argmax_index[0] == 81:
        with col1:
            st.image(image, caption='predicted: Quercus_Shumardii')
        with col2:
            st.markdown(download_desc('Quercus_Shumardii'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Shumardii'.lower())
    elif argmax_index[0] == 82:
        with col1:
            st.image(image, caption='predicted: Quercus_Suber')
        with col2:
            st.markdown(download_desc('Quercus_Suber'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Suber'.lower())
    elif argmax_index[0] == 83:
        with col1:
            st.image(image, caption='predicted: Quercus_Texana')
        with col2:
            st.markdown(download_desc('Quercus_Texana'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Texana'.lower())
    elif argmax_index[0] == 84:
        with col1:
            st.image(image, caption='predicted: Quercus_Trojana')
        with col2:
            st.markdown(download_desc('Quercus_Trojana'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Trojana'.lower())
    elif argmax_index[0] == 85:
        with col1:
            st.image(image, caption='predicted: Quercus_Variabilis')
        with col2:
            st.markdown(download_desc('Quercus_Variabilis'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Variabilis'.lower())
    elif argmax_index[0] == 86:
        with col1:
            st.image(image, caption='predicted: Quercus_Vulcanica')
        with col2:
            st.markdown(download_desc('Quercus_Vulcanica'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_Vulcanica'.lower())
    elif argmax_index[0] == 87:
        with col1:
            st.image(image, caption='predicted: Quercus_x_Hispanica')
        with col2:
            st.markdown(download_desc('Quercus_x_Hispanica'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_x_Hispanica'.lower())
    elif argmax_index[0] == 88:
        with col1:
            st.image(image, caption='predicted: Quercus_x_Turneri')
        with col2:
            st.markdown(download_desc('Quercus_x_Turneri'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Quercus_x_Turneri'.lower())
    elif argmax_index[0] == 89:
        with col1:
            st.image(image, caption='predicted: Rhododendron_x_Russellianum')
        with col2:
            st.markdown(download_desc('Rhododendron_x_Russellianum'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Rhododendron_x_Russellianum'.lower())
    elif argmax_index[0] == 90:
        with col1:
            st.image(image, caption='predicted: Salix_Fragilis')
        with col2:
            st.markdown(download_desc('Salix_Fragilis'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Salix_Fragilis'.lower())
    elif argmax_index[0] == 91:
        with col1:
            st.image(image, caption='predicted: Salix_Intergra')
        with col2:
            st.markdown(download_desc('Salix_Intergra'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Salix_Intergra'.lower())
    elif argmax_index[0] == 92:
        with col1:
            st.image(image, caption='predicted: Sorbus_Aria')
        with col2:
            st.markdown(download_desc('Sorbus_Aria'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Sorbus_Aria'.lower())
    elif argmax_index[0] == 93:
        with col1:
            st.image(image, caption='predicted: Tilia_Oliveri')
        with col2:
            st.markdown(download_desc('Tilia_Oliveri'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Tilia_Oliveri'.lower())
    elif argmax_index[0] == 94:
        with col1:
            st.image(image, caption='predicted: Tilia_Platyphyllos')
        with col2:
            st.markdown(download_desc('Tilia_Platyphyllos'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Tilia_Platyphyllos'.lower())
    elif argmax_index[0] == 95:
        with col1:
            st.image(image, caption='predicted: Tilia_Tomentosa')
        with col2:
            st.markdown(download_desc('Tilia_Tomentosa'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Tilia_Tomentosa'.lower())
    elif argmax_index[0] == 96:
        with col1:
            st.image(image, caption='predicted: Ulmus_Bergmanniana')
        with col2:
            st.markdown(download_desc('Ulmus_Bergmanniana'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Ulmus_Bergmanniana'.lower())
    elif argmax_index[0] == 97:
        with col1:
            st.image(image, caption='predicted: Viburnum_Tinus')
        with col2:
            st.markdown(download_desc('Viburnum_Tinus'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Viburnum_Tinus'.lower())
    elif argmax_index[0] == 98:
        with col1:
            st.image(image, caption='predicted: Viburnum_x_Rhytidophylloides')
        with col2:
            st.markdown(download_desc('Viburnum_x_Rhytidophylloides'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Viburnum_x_Rhytidophylloides'.lower())
    else :
        with col1:
            st.image(image, caption='predicted: Zelkova_Serrata')
        with col2:
            st.markdown(download_desc('Zelkova_Serrata'.lower()))
            col3, col4 = st.columns([1,3])
            if st.button('Click for more'):
                webbrowser.open_new_tab(url='https://en.wikipedia.org/wiki/'+'Zelkova_Serrata'.lower())



col1, col2, col3 = st.columns([1,2,1])
with col1:
    if st.button('Git hub link'):
        webbrowser.open_new_tab(url='https://github.com/ArunKumar237/Plants_Recognizer_DL')
    if st.button('linkedin link'):
        webbrowser.open_new_tab(url='www.linkedin.com/in/panuganti-arun-kumar')


