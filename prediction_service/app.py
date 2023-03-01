import streamlit as st
import skimage
from skimage.io import imread
from skimage import data, color
from skimage.transform import resize
import tensorflow as tf
import numpy as np
import gdown
"""
# deep Classifier project

"""
gdown.download(url='https://drive.google.com/uc?export=download&id=1-Rvutw0DnXi4TjeicgLxOxLjrWWBpeo2', quiet=True) #DOWNLOADING MODEL WHICH WAS TRAINED IN COLAB


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
    if argmax_index[0] == 0:
        st.image(image, caption='predicted: Acer_Campestre')
    elif argmax_index[0] == 1:
        st.image(image, caption='predicted: Acer_Capillipes')
    elif argmax_index[0] == 2:
        st.image(image, caption='predicted: Acer_Circinatum')
    elif argmax_index[0] == 3:
        st.image(image, caption='predicted: Acer_Mono')
    elif argmax_index[0] == 4:
        st.image(image, caption='predicted: Acer_Opalus')
    elif argmax_index[0] == 5:
        st.image(image, caption='predicted: Acer_Palmatum')
    elif argmax_index[0] == 6:
        st.image(image, caption='predicted: Acer_Pictum')
    elif argmax_index[0] == 7:
        st.image(image, caption='predicted: Acer_Platanoids')
    elif argmax_index[0] == 8:
        st.image(image, caption='predicted: Acer_Rubrum')
    elif argmax_index[0] == 9:
        st.image(image, caption='predicted: Acer_Rufinerve')
    elif argmax_index[0] == 10:
        st.image(image, caption='predicted: Acer_Saccharinum')
    elif argmax_index[0] == 11:
        st.image(image, caption='predicted: Alnus_Cordata')
    elif argmax_index[0] == 12:
        st.image(image, caption='predicted: Alnus_Maximowiczii')
    elif argmax_index[0] == 13:
        st.image(image, caption='predicted: Alnus_Rubra')
    elif argmax_index[0] == 14:
        st.image(image, caption='predicted: Alnus_Sieboldiana')
    elif argmax_index[0] == 15:
        st.image(image, caption='predicted: Alnus_Viridis')
    elif argmax_index[0] == 16:
        st.image(image, caption='predicted: Arundinaria_Simonii')
    elif argmax_index[0] == 17:
        st.image(image, caption='predicted: Betula_Austrosinensis')
    elif argmax_index[0] == 18:
        st.image(image, caption='predicted: Betula_Pendula')
    elif argmax_index[0] == 19:
        st.image(image, caption='predicted: Callicarpa_Bodinieri')
    elif argmax_index[0] == 20:
        st.image(image, caption='predicted: Castanea_Sativa')
    elif argmax_index[0] == 21:
        st.image(image, caption='predicted: Celtis_Koraiensis')
    elif argmax_index[0] == 22:
        st.image(image, caption='predicted: Cercis_Siliquastrum')
    elif argmax_index[0] == 23:
        st.image(image, caption='predicted: Cornus_Chinensis')
    elif argmax_index[0] == 24:
        st.image(image, caption='predicted: Cornus_Controversa')
    elif argmax_index[0] == 25:
        st.image(image, caption='predicted: Cornus_Macrophylla')
    elif argmax_index[0] == 26:
        st.image(image, caption='predicted: Cotinus_Coggygria')
    elif argmax_index[0] == 27:
        st.image(image, caption='predicted: Crataegus_Monogyna')
    elif argmax_index[0] == 28:
        st.image(image, caption='predicted: Cytisus_Battandieri')
    elif argmax_index[0] == 29:
        st.image(image, caption='predicted: Eucalyptus_Glaucescens')
    elif argmax_index[0] == 30:
        st.image(image, caption='predicted: Eucalyptus_Neglecta')
    elif argmax_index[0] == 31:
        st.image(image, caption='predicted: Eucalyptus_Urnigera')
    elif argmax_index[0] == 32:
        st.image(image, caption='predicted: Fagus_Sylvatica')
    elif argmax_index[0] == 33:
        st.image(image, caption='predicted: Ginkgo_Biloba')
    elif argmax_index[0] == 34:
        st.image(image, caption='predicted: Ilex_Aquifolium')
    elif argmax_index[0] == 35:
        st.image(image, caption='predicted: Ilex_Cornuta')
    elif argmax_index[0] == 36:
        st.image(image, caption='predicted: Liquidambar_Styraciflua')
    elif argmax_index[0] == 37:
        st.image(image, caption='predicted: Liriodendron_Tulipifera')
    elif argmax_index[0] == 38:
        st.image(image, caption='predicted: Lithocarpus_Cleistocarpus')
    elif argmax_index[0] == 39:
        st.image(image, caption='predicted: Lithocarpus_Edulis')
    elif argmax_index[0] == 40:
        st.image(image, caption='predicted: Magnolia_Heptapeta')
    elif argmax_index[0] == 41:
        st.image(image, caption='predicted: Magnolia_Salicifolia')
    elif argmax_index[0] == 42:
        st.image(image, caption='predicted: Morus_Nigra')
    elif argmax_index[0] == 43:
        st.image(image, caption='predicted: Olea_Europaea')
    elif argmax_index[0] == 44:
        st.image(image, caption='predicted: Phildelphus')
    elif argmax_index[0] == 45:
        st.image(image, caption='predicted: Populus_Adenopoda')
    elif argmax_index[0] == 46:
        st.image(image, caption='predicted: Populus_Grandidentata')
    elif argmax_index[0] == 47:
        st.image(image, caption='predicted: Populus_Nigra')
    elif argmax_index[0] == 48:
        st.image(image, caption='predicted: Prunus_Avium')
    elif argmax_index[0] == 49:
        st.image(image, caption='predicted: Prunus_X_Shmittii')
    elif argmax_index[0] == 50:
        st.image(image, caption='predicted: Pterocarya_Stenoptera')
    elif argmax_index[0] == 51:
        st.image(image, caption='predicted: Quercus_Afares')
    elif argmax_index[0] == 52:
        st.image(image, caption='predicted: Quercus_Agrifolia')
    elif argmax_index[0] == 53:
        st.image(image, caption='predicted: Quercus_Alnifolia')
    elif argmax_index[0] == 54:
        st.image(image, caption='predicted: Quercus_Brantii')
    elif argmax_index[0] == 55:
        st.image(image, caption='predicted: Quercus_Canariensis')
    elif argmax_index[0] == 56:
        st.image(image, caption='predicted: Quercus_Castaneifolia')
    elif argmax_index[0] == 57:
        st.image(image, caption='predicted: Quercus_Cerris')
    elif argmax_index[0] == 58:
        st.image(image, caption='predicted: Quercus_Chrysolepis')
    elif argmax_index[0] == 59:
        st.image(image, caption='predicted: Quercus_Coccifera')
    elif argmax_index[0] == 60:
        st.image(image, caption='predicted: Quercus_Coccinea')
    elif argmax_index[0] == 61:
        st.image(image, caption='predicted: Quercus_Crassifolia')
    elif argmax_index[0] == 62:
        st.image(image, caption='predicted: Quercus_Crassipes')
    elif argmax_index[0] == 63:
        st.image(image, caption='predicted: Quercus_Dolicholepis')
    elif argmax_index[0] == 64:
        st.image(image, caption='predicted: Quercus_Ellipsoidalis')
    elif argmax_index[0] == 65:
        st.image(image, caption='predicted: Quercus_Greggii')
    elif argmax_index[0] == 66:
        st.image(image, caption='predicted: Quercus_Hartwissiana')
    elif argmax_index[0] == 67:
        st.image(image, caption='predicted: Quercus_Ilex')
    elif argmax_index[0] == 68:
        st.image(image, caption='predicted: Quercus_Imbricaria')
    elif argmax_index[0] == 69:
        st.image(image, caption='predicted: Quercus_Infectoria_sub')
    elif argmax_index[0] == 70:
        st.image(image, caption='predicted: Quercus_Kewensis')
    elif argmax_index[0] == 71:
        st.image(image, caption='predicted: Quercus_Nigra')
    elif argmax_index[0] == 72:
        st.image(image, caption='predicted: Quercus_Palustris')
    elif argmax_index[0] == 73:
        st.image(image, caption='predicted: Quercus_Phellos')
    elif argmax_index[0] == 74:
        st.image(image, caption='predicted: Quercus_Phillyraeoides')
    elif argmax_index[0] == 75:
        st.image(image, caption='predicted: Quercus_Pontica')
    elif argmax_index[0] == 76:
        st.image(image, caption='predicted: Quercus_Pubescens')
    elif argmax_index[0] == 77:
        st.image(image, caption='predicted: Quercus_Pyrenaica')
    elif argmax_index[0] == 78:
        st.image(image, caption='predicted: Quercus_Rhysophylla')
    elif argmax_index[0] == 79:
        st.image(image, caption='predicted: Quercus_Rubra')
    elif argmax_index[0] == 80:
        st.image(image, caption='predicted: Quercus_Semecarpifolia')
    elif argmax_index[0] == 81:
        st.image(image, caption='predicted: Quercus_Shumardii')
    elif argmax_index[0] == 82:
        st.image(image, caption='predicted: Quercus_Suber')
    elif argmax_index[0] == 83:
        st.image(image, caption='predicted: Quercus_Texana')
    elif argmax_index[0] == 84:
        st.image(image, caption='predicted: Quercus_Trojana')
    elif argmax_index[0] == 85:
        st.image(image, caption='predicted: Quercus_Variabilis')
    elif argmax_index[0] == 86:
        st.image(image, caption='predicted: Quercus_Vulcanica')
    elif argmax_index[0] == 87:
        st.image(image, caption='predicted: Quercus_x_Hispanica')
    elif argmax_index[0] == 88:
        st.image(image, caption='predicted: Quercus_x_Turneri')
    elif argmax_index[0] == 89:
        st.image(image, caption='predicted: Rhododendron_x_Russellianum')
    elif argmax_index[0] == 90:
        st.image(image, caption='predicted: Salix_Fragilis')
    elif argmax_index[0] == 91:
        st.image(image, caption='predicted: Salix_Intergra')
    elif argmax_index[0] == 92:
        st.image(image, caption='predicted: Sorbus_Aria')
    elif argmax_index[0] == 93:
        st.image(image, caption='predicted: Tilia_Oliveri')
    elif argmax_index[0] == 94:
        st.image(image, caption='predicted: Tilia_Platyphyllos')
    elif argmax_index[0] == 95:
        st.image(image, caption='predicted: Tilia_Tomentosa')
    elif argmax_index[0] == 96:
        st.image(image, caption='predicted: Ulmus_Bergmanniana')
    elif argmax_index[0] == 97:
        st.image(image, caption='predicted: Viburnum_Tinus')
    elif argmax_index[0] == 98:
        st.image(image, caption='predicted: Viburnum_x_Rhytidophylloides')
    else:
        st.image(image, caption='predicted: Zelkova_Serrata')
