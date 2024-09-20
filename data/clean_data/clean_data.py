# script to prepare the raw data to be imported to Omeka S
# The scripts reads the xlsx files, cleans, concatenates and saves the data in a csv file
# The csv files will use ';' as separater and will be saved in the 'clean_data' folder
# we have 3 collections: 'africa', 'ingigena' and 'afro-br', but the first collection is divided into 2 differente csv, that have to be concatenated

import pandas as pd


# function to read the xlsx
def read_xlsx(file):
    data = pd.read_excel(file)
    return data


# function to clean the data
def clean_data(data):
    # strip and lower the column names
    data.columns = data.columns.str.strip().str.lower()
    # replace spaces by underscores
    data.columns = data.columns.str.replace(' ', '_')
    # if column has 'unnamed:' in the name, drop it
    data = data.loc[:, ~data.columns.str.contains('^unnamed:', case=False)]
    return data


# function to concatenate the dataframes
def concat_data(*dfs):
    data = pd.concat(dfs)
    return data


# function to ad a column with the collection name to the data
def add_collection(data, collection):
    data['collection'] = collection
    return data


# function to save the data in a csv file
def save_data(data, file):
    data.to_csv(file, sep=';', index=False)


# call the functions using input and output files
def main():
    # read the xlsx files
    africa1 = read_xlsx('../raw_data/africa1.xlsx')
    africa2 = read_xlsx('../raw_data/africa2.xlsx')
    indigena = read_xlsx('../raw_data/indigena.xlsx')
    afro_br = read_xlsx('../raw_data/afrbr.xlsx')

    # clean the data
    africa1 = clean_data(africa1)
    africa2 = clean_data(africa2)
    indigena = clean_data(indigena)
    afro_br = clean_data(afro_br)

    # concatenate the data
    africa = concat_data(africa1, africa2)

    # add the collection name to the data
    africa = add_collection(africa, 'africana')
    indigena = add_collection(indigena, 'indigena')
    afro_br = add_collection(afro_br, 'afro-brasileira')

    # concatenate the data from the 3 collections
    full_data = concat_data(africa, indigena, afro_br)

    # save the data in a csv file
    save_data(africa, 'africa.csv')
    save_data(indigena, 'indigena.csv')
    save_data(afro_br, 'afro-br.csv')
    save_data(full_data, 'full_data.csv')


if __name__ == '__main__':
    main()

