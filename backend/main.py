import data_processing
import distance_metrics


def consider_locations(locations_list, br=0, aff_lim=0, aff_on=False):
    res_df = data_processing.get_city_overview_by_br(data_processing.df, br, aff_lim, aff_lim)

    # locations_list = [locations_list[0]] #TODO: in place only for quick debugging, remove after
    weights = []
    
    for dest_loc in locations_list:
        travel_time = []
        for origin_loc in res_df['PostalCode']:
            travel_time_instance = distance_metrics.get_dist(int(origin_loc), int(dest_loc))
            travel_time.append(travel_time_instance)

        res_df[f'Travelto_{dest_loc}'] = travel_time
        
    res_df['location_score'] = res_df.apply(assign_location_score, args=(locations_list,), axis=1)

    
    return res_df

def assign_location_score(row, locations_list):
    # Calculate the average travel time to all destination locations with weights
    weighted_avg_travel_time = sum([
        row[f'Travelto_{dest_loc}'] * (i + 1) 
        for i, dest_loc in enumerate(locations_list)
    ]) / len(locations_list)
    
    if weighted_avg_travel_time < 1200:
        return 1
    elif weighted_avg_travel_time < 2100:
        return 2
    elif weighted_avg_travel_time < 2700:
        return 3
    else:
        return 4 

def score_view(df):
    df_c = df.copy()
    df_c['final_score'] = (df_c['Affordability'] + df_c['location_score']) / 2
    df_c = df_c[['PostalCode', 'Localities', 'final_score' ]]
    df_c = df_c.sort_values(by='final_score')
    return df_c


if __name__ == '__main__':
    locations_list = [2000]
    result = consider_locations(locations_list=locations_list, br=3, aff_lim=900, aff_on=True)
    resultant = score_view(result)
    best_loc = resultant.iloc[0]
    print(best_loc)



