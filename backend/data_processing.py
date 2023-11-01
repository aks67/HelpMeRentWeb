import pandas as pd
import numpy as np
import matplotlib.pyplot


data_loc = '..\\data\\cleaned_data.csv'
post_data_loc = r'..\\data\\pc_df.csv'

# Read data from CSV files
df = pd.read_csv(data_loc)
pc_df = pd.read_csv(post_data_loc)

def filter_by_postcode(postCode, df):
    postCode = int(postCode)
    post_view = df[df['PostalCode'] == postCode]
    return post_view

def filter_by_bedrooms(bedrooms, df):
    bedrooms = int(bedrooms)
    post_view = df[df['Bedrooms'] == bedrooms]
    return post_view

'''
   Given a postcode, #bedrooms, return expected rent
'''
def average_rent(postCode, bedrooms, df):
    compute_df = filter_by_postcode(postCode, df)
    compute_df = filter_by_bedrooms(bedrooms, compute_df)
    means = compute_df.mean().astype(int)
    return means

def median_rent_locality(locality, bedrooms, df):
    postcode = get_postcode(locality)
    compute_df = filter_by_postcode(postcode, df)
    compute_df = filter_by_bedrooms(bedrooms, compute_df)
    return compute_df['MedianRent'].mean()

def get_median_rent_post(postcode, bedrooms, df):
    compute_df = filter_by_postcode(postcode, df)
    compute_df = filter_by_bedrooms(bedrooms, compute_df)
    return compute_df['MedianRent'].mean()

def get_postcode(locality):
    locality = locality.upper()
    result = pc_df[pc_df['Locality'] == locality]
    if not result.empty:
        return result.iloc[0]['PostalCode']
    else:
        return None
    
def get_locality(postcode):
    result = pc_df[pc_df['PostalCode'] == postcode]
    if not result.empty:
        return result.iloc[0]['locality']
    else:
        return None
    
def df_median_rent(df, bedrooms):
    result_df = pd.DataFrame(columns=['PostalCode', 'MedianRent', 'bedrooms'])
    unique_postcodes = df['PostalCode'].unique()

    for postcode in unique_postcodes:
        subset_df = df[df['PostalCode'] == postcode]
        subset_df = subset_df[subset_df['Bedrooms'] == bedrooms]
        median_rent = get_median_rent_post(postcode, bedrooms, subset_df)
        result_df = pd.concat([result_df, pd.DataFrame({'PostalCode': [postcode], 'MedianRent': [median_rent], 'bedrooms': [bedrooms]})], ignore_index=True)
        result_df = result_df.dropna()
    return result_df
        
def assign_affordability(df, value):
    df_copy = df.copy()
    
    def assign_colour(median_val, value):
        if median_val >= 1.25 * value:
            return 5
        elif 1 * value <= median_val < 1.25 * value:
            return 4
        elif 0.8 * value <= median_val < 1 * value:
            return 3
        elif 0.7 * value <= median_val < 0.8 * value:
            return 2
        else:
            return 1
    
    affordabilities = []

    for median_val in df_copy['MedianRent']:
        affordabilities.append(assign_colour(median_val, value))
    
    df_copy['Affordability'] = affordabilities
    return df_copy

def get_affordable_posts(df, afford_rating):
    result_df = df[df['Affordability'] <= afford_rating]
    return result_df

def add_locality(df, post_code_data):
    df_copy = df.copy()
    merged_df = pd.merge(df_copy, post_code_data, on='PostalCode', how='left')
    localities_grouped = merged_df.groupby('PostalCode')['Locality'].apply(lambda x: ', '.join(x.dropna())).reset_index()
    df_copy = pd.merge(df_copy, localities_grouped, on='PostalCode', how='left')
    df_copy = pd.merge(df_copy, post_code_data[['PostalCode', 'lat', 'long']], on='PostalCode', how='left')
    df_copy = df_copy.rename(columns={'Locality': 'Localities'})
    return df_copy

def get_city_overview_by_br(df, br, aff_lim=0, aff_on=False):
    median_rent_data = df_median_rent(df, br)
    if aff_on:
        df_compute = assign_affordability(median_rent_data, aff_lim)
        result_df = get_affordable_posts(df_compute, 4)
    else:
        result_df = median_rent_data

    final_data_with_local = add_locality(result_df, pc_df)
    # TODO: remove the following line for long result
    final_data_with_local = final_data_with_local.head(20)
    final_data_with_local = final_data_with_local.sort_values(by='MedianRent')
    return final_data_with_local

'''
    Given Postcode, return {long, lat}
'''
def get_coord(postcode:int):
    result = pc_df[pc_df['PostalCode'] == postcode]
    if not result.empty:
        return (result.iloc[0]['long'], result.iloc[0]['lat'])
    else:
        return None
'''
    Given locality, return {long, lat}
'''
# def get_coord(locality:str):
#     locality = locality.upper()
#     result = pc_df[pc_df['Locality'] == locality]
#     if not result.empty:
#        return (result.iloc[0]['long'], result.iloc[0]['lat'])
#     else:
#         return None

if __name__ == '__main__':
    print(median_rent_locality('waterloo', 2, df))