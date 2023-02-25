from deepClassifier.entity.config_entity import DataIngestionConfig
from deepClassifier.utils import get_size
from deepClassifier import logger
from zipfile import ZipFile
from tqdm import tqdm
from pathlib import Path
import gdown
import os

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info(f"Trying to download file")
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Download Started...")
            gdown.download(url=self.config.source_URL, output=self.config.local_data_file, quiet=True)
            filename = os.path.split(self.config.local_data_file)[-1]
            logger.info(f"{filename} downloaded ")
        else:
            logger.info(f"File already exists of size {get_size(Path(self.config.local_data_file))}")

    def _get_updated_list_of_files(self, list_of_files):
        list_of_species = ['Acer_Campestre', 'Acer_Capillipes', 'Acer_Circinatum', 'Acer_Mono', 'Acer_Opalus', 'Acer_Palmatum', 'Acer_Pictum', 'Acer_Platanoids', 'Acer_Rubrum', 'Acer_Rufinerve', 'Acer_Saccharinum', 'Alnus_Cordata', 'Alnus_Maximowiczii', 'Alnus_Rubra', 'Alnus_Sieboldiana', 'Alnus_Viridis', 'Arundinaria_Simonii', 'Betula_Austrosinensis', 'Betula_Pendula', 'Callicarpa_Bodinieri', 'Castanea_Sativa', 'Celtis_Koraiensis', 'Cercis_Siliquastrum', 'Cornus_Chinensis', 'Cornus_Controversa', 'Cornus_Macrophylla', 'Cotinus_Coggygria', 'Crataegus_Monogyna', 'Cytisus_Battandieri', 'Eucalyptus_Glaucescens', 'Eucalyptus_Neglecta', 'Eucalyptus_Urnigera', 'Fagus_Sylvatica', 'Ginkgo_Biloba', 'Ilex_Aquifolium', 'Ilex_Cornuta', 'Liquidambar_Styraciflua', 'Liriodendron_Tulipifera', 'Lithocarpus_Cleistocarpus', 'Lithocarpus_Edulis', 'Magnolia_Heptapeta', 'Magnolia_Salicifolia', 'Morus_Nigra', 'Olea_Europaea', 'Phildelphus', 'Populus_Adenopoda', 'Populus_Grandidentata', 'Populus_Nigra', 'Prunus_Avium', 'Prunus_X_Shmittii', 'Pterocarya_Stenoptera', 'Quercus_Afares', 'Quercus_Agrifolia', 'Quercus_Alnifolia', 'Quercus_Brantii', 'Quercus_Canariensis', 'Quercus_Castaneifolia', 'Quercus_Cerris', 'Quercus_Chrysolepis', 'Quercus_Coccifera', 'Quercus_Coccinea', 'Quercus_Crassifolia', 'Quercus_Crassipes', 'Quercus_Dolicholepis', 'Quercus_Ellipsoidalis', 'Quercus_Greggii', 'Quercus_Hartwissiana', 'Quercus_Ilex', 'Quercus_Imbricaria', 'Quercus_Infectoria_sub', 'Quercus_Kewensis', 'Quercus_Nigra', 'Quercus_Palustris', 'Quercus_Phellos', 'Quercus_Phillyraeoides', 'Quercus_Pontica', 'Quercus_Pubescens', 'Quercus_Pyrenaica', 'Quercus_Rhysophylla', 'Quercus_Rubra', 'Quercus_Semecarpifolia', 'Quercus_Shumardii', 'Quercus_Suber', 'Quercus_Texana', 'Quercus_Trojana', 'Quercus_Variabilis', 'Quercus_Vulcanica', 'Quercus_x_Hispanica', 'Quercus_x_Turneri', 'Rhododendron_x_Russellianum', 'Salix_Fragilis', 'Salix_Intergra', 'Sorbus_Aria', 'Tilia_Oliveri', 'Tilia_Platyphyllos', 'Tilia_Tomentosa', 'Ulmus_Bergmanniana', 'Viburnum_Tinus', 'Viburnum_x_Rhytidophylloides', 'Zelkova_Serrata']
        return [f for f in list_of_files if f.endswith(".jpg") and (True for i in list_of_species if i in f)]
    
    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir,f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)

        if os.path.getsize(target_filepath) == 0:
            logger.info(f"Removing file: {target_filepath} of size {get_size(Path(target_filepath))}")
            os.remove(target_filepath)
            

    def unzip_and_clean(self):
        logger.info(f"Unzipping and Removing unwanted files")
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)