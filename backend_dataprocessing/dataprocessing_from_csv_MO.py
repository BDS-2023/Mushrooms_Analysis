#Script to transform the updated raw data and add then to the global dB

import pandas as pd
import numpy as np
import sys
from tqdm import tqdm
pd.options.mode.chained_assignment = None


#---------------------------------------------------------LOAD DATA-----------------------------------------------------------------
# Load csv datas. You need a file name data_MO in your script directory where you put the 8 csv from MO.
# You need GBIF_tax.csv in the same file directory as the script​

file_path = sys.path[0]
Path = file_path + '\\data_MO\\'


df_observations = pd.read_csv(Path+'observations.csv',sep='\t')
df_images_observation = pd.read_csv(Path+'images_observations.csv',sep='\t')
df_locations = pd.read_csv(Path+'locations.csv',sep='\t')
df_names = pd.read_csv(Path+'names.csv',sep='\t')
df_name_descriptions = pd.read_csv(Path+'name_descriptions.csv',sep='\t')
df_name_classification = pd.read_csv(Path+'name_classifications.csv',sep='\t')
df_location_descriptions = pd.read_csv(Path+'location_descriptions.csv',sep='\t')
df_images = pd.read_csv(Path+'images.csv',sep='\t')

df = pd.read_csv(file_path+'\\GBIF_tax.csv',sep='\t')

#----------------------------------------------------------------------------------------------------------------------------​




#---------------------------------------------------------Preprocess: real name-----------------------------------------------------------------
# In the names.csv, we grab the real name from mushroom with name deprecated = 1. 
# Put 'no_real_name_yet' if all the same mushroom have deprecated =1.

df_names['real_name'] = np.nan

for syn in df_names.synonym_id.dropna().unique():
    df_same_names = df_names[df_names.synonym_id == syn]
    try:
        real_name = df_same_names.text_name[df_same_names.deprecated == 0].values[0]
        df_names.real_name[df_names.synonym_id == syn] = real_name
    except:
        df_names.real_name[df_names.synonym_id == syn] = 'no_real_name_yet'


real_names_temp = df_names[(df_names.synonym_id.isna())&(df_names.deprecated==0)].text_name
df_names.real_name[(df_names.synonym_id.isna())&(df_names.deprecated==0)] = real_names_temp

df_names.real_name[(df_names.synonym_id.isna())&(df_names.deprecated==1)] = 'no_real_name_yet'


df_names = df_names[df_names.real_name != 'no_real_name_yet']

#----------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------Preprocess: taxon------------------------------------------------------------------------------------
# For every real_name in names.csv find the taxonomy from the GBIF csv and create a temp dataframe to store all the taxon.

taxonomie = ["kingdom", "phylum", "class", "order", "family", "genus",'Subgenus' 
                 ,'section','subsection','stirps','species','subspecies'
                 ,'variety','form']
taxonomie = taxonomie[::-1]

taxonomie_maj = [taxon.upper() for taxon in taxonomie]


truc = pd.DataFrame()
for name,rank in tqdm(np.array(df_names[['real_name','rank']])):
    if rank in [14,13,12,11,10,9,4]:
        df_temp = df[(df[taxonomie[rank-1]] == name) & (df['taxonRank'] == taxonomie_maj[rank-1])]
        if df_temp.shape[0] != 0:
            try:
                df_temp = pd.DataFrame([df_temp.iloc[0,[7,9,11,13,15,17,19]]])
                df_temp.insert(0, "name_txt", name)
                truc = pd.concat([truc,df_temp])
            except:
                pass
        else:
            pass #print(name,taxonomie[rank-1])
    elif rank in [8,7,6]:
        name_genus = name.split(' ')[0]
        #print(name_genus)
        df_temp = df[(df['genus'] == name_genus) & (df['taxonRank'] == 'GENUS') & (df.taxonomicStatus == 'ACCEPTED')]
        if df_temp.shape[0] != 0:
            try:
                #print(df_temp)
                df_temp = pd.DataFrame([df_temp.iloc[0,[7,9,11,13,15,17,19]]])
                df_temp.insert(0, "name_txt", name)
                df_temp.species = np.nan
                truc = pd.concat([truc,df_temp])
            except:
                pass
        elif df_temp.shape[0] == 0:
            df_temp = df[(df['genus'] == name_genus) & (df['taxonRank'] == 'GENUS') & (df.taxonomicStatus == 'SYNONYM')]
            try:
                #print(df_temp)
                df_temp = pd.DataFrame([df_temp.iloc[0,[7,9,11,13,15,17,19]]])
                df_temp.insert(0, "name_txt", name)
                df_temp.species = np.nan
                truc = pd.concat([truc,df_temp])
            except:
                pass
        
            
    elif rank in [3,2,1]:
        name_species = ' '.join(name.split(' ')[:2])
        df_temp = df[(df['species'] == name_species) & (df['taxonRank'] == taxonomie_maj[rank-1])]
        if df_temp.shape[0] != 0:
            try:
                df_temp = pd.DataFrame([df_temp.iloc[0,[7,9,11,13,15,17,19]]])
                df_temp.insert(0, "name_txt", name)
                truc = pd.concat([truc,df_temp])
            except:
                pass
        elif df_temp.shape[0] == 0:
            df_temp = df[(df['species'] == name_species) & (df['taxonRank'] == 'SPECIES')]
            if df_temp.shape[0] !=0:
                try:
                    df_temp = pd.DataFrame([df_temp.iloc[0,[7,9,11,13,15,17,19]]])
                    df_temp.insert(0, "name_txt", name)
                    truc = pd.concat([truc,df_temp])
                except:
                    pass
            elif df_temp.shape[0] == 0:
                name_genus = name_species.split(' ')[0]
                df_temp = df[(df['genus'] == name_genus) & (df['taxonRank'] == 'GENUS')]
                if df_temp.shape[0] !=0:
                    try:
                        #print(df_temp)
                        df_temp = pd.DataFrame([df_temp.iloc[0,[7,9,11,13,15,17,19]]])
                        df_temp.insert(0, "name_txt", name)
                        df_temp.species = np.nan
                        truc = pd.concat([truc,df_temp])
                    except:
                        pass
                elif df_temp.shape[0] == 0:
                    df_temp = df[(df['genus'] == name_genus)]
                    try:
                        df_temp = pd.DataFrame([df_temp.iloc[0,[7,9,11,13,15,17,19]]])
                        df_temp.insert(0, "name_txt", name)
                        df_temp.species = np.nan
                        truc = pd.concat([truc,df_temp])
                    except:
                        pass
                    
#---------------------------------------------------------------------------------------------------------------------------------------------------           


#---------------------------------------------------------Preprocess: SQL --> noSQL ------------------------------------------------------------------------------------


df_names_new = df_names.merge(truc,left_on='text_name',right_on='name_txt')
df_names_new_clean = df_names_new.drop(['author','correct_spelling_id','name_txt',],axis=1)

df_observations_clean = df_observations.drop(['when','lat','long','alt','vote_cache','is_collection_location','thumb_image_id'],axis=1)

df_locations_clean = df_locations.drop(['name','south','west','high','low'],axis=1)
df_locations_clean = df_locations_clean.rename(columns={'id':'id_loc','north':'long','south':'alt'})

df_obs_loc = df_observations_clean.merge(df_locations_clean,left_on='location_id',right_on='id_loc')
df_obs_loc = df_obs_loc.drop(['id_loc'],axis=1)

df_obs_name = df_obs_loc.merge(df_names_new_clean,left_on='name_id',right_on='id')
df_images_name = df_images_observation.merge(df_obs_name,left_on='observation_id',right_on='id_x')
df_images_name = df_images_name.drop(['id_x','id_y'],axis=1)

df_images_name = df_images_name.drop_duplicates()
df_images_name['source'] = 'MO'
df_images_name['host'] = np.nan
df_images_name['gbif_id'] = np.nan

#--------------------------------------------------------------------------------------------------------------------------------------------------

#save final.csv
df_images_name.to_csv('images_names.csv',sep=',')