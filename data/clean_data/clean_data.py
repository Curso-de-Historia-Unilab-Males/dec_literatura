# script to prepare the raw data to be imported to Omeka S
# The scripts reads the xlsx files, cleans, concatenates and saves the data in a csv file
# The csv files will use ';' as separater and will be saved in the 'clean_data' folder
# we have 3 collections: 'africa', 'ingigena' and 'afro-br', but the first collection is divided into 2 differente csv, that have to be concatenated

import pandas as pd


def read_xlsx(file):
    """Read the xlsx file and return a pandas dataframe
    """
    df = pd.read_excel(file)
    return df


def clean_df(df):
    """Clean the dataframe removing unnamed columns, changing column names
       to lower case and replacing spaces by underscores.
       Change all ';' to ',' in the df to avoid problems with csv files.
    """
    # strip and lower the column names
    df.columns = df.columns.str.strip().str.lower()
    # replace spaces by underscores
    df.columns = df.columns.str.replace(' ', '_')
    # if column has 'unnamed:' in the name, drop it
    df = df.loc[:, ~df.columns.str.contains('^unnamed:', case=False)]
    # change all ';' to ',' in the df
    df = df.replace(';', ',', regex=True)
    df.loc[df['tipo'].notnull(), 'tipo'] = 'Físico'
    df['identificador'] = df['identificador'].str.replace('-','').str.strip()
    df['idioma'] = df['idioma'].str.replace('pt-br', 'pt-BR')
    df['idioma'] = df['idioma'].str.replace('Pt-BR', 'pt-BR')
    df['extensão'] = df['extensão'].str.lower().str.replace('p','').str.strip()
    df['extensão'] = df['extensão'].fillna('não consta')
    
    return df


def concat_df(*dfs):
    """Concatenate the dataframes in the list
       Return a single dataframe
    """
    df = pd.concat(dfs)
    return df


def add_collection(df, collection):
    """Add a column with the collection name to the dataframe
    """
    df['coleção'] = collection
    return df


def save_df(df, file):
    """Save the dataframe in a csv file. Use ';' as separater.
    """
    df.to_csv(file, sep=';', index=False)


# call the functions using input and output files
def main():
    # read the xlsx files
    africa1 = read_xlsx('../raw_data/africa1.xlsx')
    africa2 = read_xlsx('../raw_data/africa2.xlsx')
    indigena = read_xlsx('../raw_data/indigena.xlsx')
    afro_br = read_xlsx('../raw_data/afrbr.xlsx')

    # clean the data
    africa1 = clean_df(africa1)
    africa2 = clean_df(africa2)
    indigena = clean_df(indigena)
    afro_br = clean_df(afro_br)

    # concatenate the data
    africa = concat_df(africa1, africa2)

    # add the collection name to the data
    africa = add_collection(africa, 'Africana')
    indigena = add_collection(indigena, 'Indígena')
    afro_br = add_collection(afro_br, 'Afro-brasileira')

    # concatenate the data from the 3 collections
    full_data = concat_df(africa, indigena, afro_br)

    # save the data in a csv file
    save_df(africa, 'africa.csv')
    save_df(indigena, 'indigena.csv')
    save_df(afro_br, 'afro-br.csv')
    save_df(full_data, 'full_data.csv')


if __name__ == '__main__':
    main()

