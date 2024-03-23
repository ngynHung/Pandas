import pandas as pd


def show(fn):
    df = pd.read_csv(fn, sep='\t')
    print(df)


def show_rows(fn, n):
    """

    :param fn: name file
    :param n: number of lines
    :return: show data each line
    """

    df = pd.read_csv(fn, sep='\t', nrows=n)
    print(df)


def count_rows(fn):
    df = pd.read_csv(fn, sep='\t')
    num_rows, num_columns = df.shape
    return num_rows


def count_columns(fn):
    df = pd.read_csv(fn, sep='\t')
    num_rows, num_columns = df.shape
    return num_columns


def show_column_name(fn):
    df = pd.read_csv(fn, sep='\t')
    columns = df.columns
    for idx, col in enumerate(columns):
        print(f'{idx + 1}. ' + col)


def show_type_column(fn):
    df = pd.read_csv(fn, sep='\t')
    column_types = df.dtypes
    print(column_types)


def get_column(fn, col_name):
    """

    :param fn: name file
    :param col_name: name column
    :return: a object has 5 values head and 5 values tail
    """

    df = pd.read_csv(fn, sep='\t')
    return df[col_name]


def get_columns(fn, arr_col):
    df = pd.read_csv(fn, sep='\t')
    return df[arr_col]


def show_row_index(fn, n):
    """

    :param fn: name file
    :param n: number of row
    :return: print all values of n row
    """

    n_row = pd.read_csv(fn, sep='\t', skiprows=n, nrows=1)
    print(f'{n}th row:')
    print(n_row)


def show_column_index_loc(fn, idx):
    try:
        df = pd.read_csv(fn, sep='\t')
        column_index = df.iloc[:, idx]
        len_column = len(df.columns) - 1
        print(f'{idx} column:')
        print(column_index)
    except:
        print('Invalid column !')


def show_first_column(fn):
    df = pd.read_csv(fn, sep='\t')
    first_column = df.iloc[:, 0]
    print('First column:')
    print(first_column)


def show_last_column(fn):
    df = pd.read_csv(fn, sep='\t')
    len_column = len(df.columns) - 1
    last_column = df.iloc[:, len_column]
    print('Last column:')
    print(last_column)


def get_row_index(fn, idx):
    df = pd.read_csv(fn, sep='\t')
    # return df.iloc[idx] # Way 1: Column format
    return df.iloc[df.index == idx] # Way 2: Row format


def get_row_index_loc(fn, idx, col_name):
    df = pd.read_csv(fn, sep='\t')
    return df.loc[idx, col_name]


def get_row_index_iloc(fn, idx, col_name):
    df = pd.read_csv(fn, sep='\t')
    return df.iloc[idx][col_name]


def get_row_with_properties(fn, idx, arr_col):
    try:
        df = pd.read_csv(fn, sep='\t')
        return df.iloc[idx, arr_col]
    except:
        print('Please check indexes or arrays again !')


def get_rows(fn, n):
    df = pd.read_csv(fn, sep='\t')
    return df.head(n)


def get_average_with_properties(fn, name, prop):
    df = pd.read_csv(fn, sep='\t')
    return df.groupby(name)[prop].mean()


def get_average_with_properties_subset(fn, name, prop):
    df = pd.read_csv(fn, sep='\t')
    unique_years = df['year'].unique()

    average_life_expectancy = {}
    for year in unique_years:
        subset = df[df['year'] == year]
        average_life_expectancy[year] = subset['lifeExp'].mean()

    return average_life_expectancy




if __name__ == '__main__':
    file_name = '04_gap-merged.tsv'

    # # 1
    # show_lines(file_name, 5)

    # # 2
    # print(f'This file has {count_rows(file_name)} rows')
    # print(f'This file has {count_columns(file_name)} columns')

    # # 3
    # print(f'This file has {count_columns(file_name)} columns:')
    # show_column_name(file_name)

    # # 4
    # show_type_column(file_name)

    # # 5, 6
    # df = get_column(file_name, 'country')
    # print('Heading values:')
    # print(df.head())
    # print('Tailing values:')
    # print(df.tail())

    # # 7
    # name_columns = ['country', 'continent', 'year']
    # df = get_columns(file_name, name_columns)
    # print(df.head())
    # print(df.tail())

    # # 8
    # show_rows(file_name, 5)
    # show_row_index(file_name, 3) #auto print next row

    # # 9, 10
    # show_column_index_loc(file_name, -1) # # -1 is the last column
    # show_first_column(file_name)
    # show_last_column(file_name)

    # # 11
    # show(file_name)
    # df = get_row_index(file_name, 3308)
    # print(df)

    # # 12
    # df = get_row_index_loc(file_name, 43, 'country')
    # print(df)
    #
    # df2 = get_row_index_iloc(file_name, 43, 'country')
    # print(df2)

    # # 13
    # index_columns = [1, 4, 2]
    # indexes = [0, 100]
    # df = get_row_with_properties(file_name, indexes, index_columns)
    # print(df)

    # # 14
    # df = get_rows(file_name, 10)
    # print(df)

    # # 15
    # df = get_average_with_properties(file_name, 'year', 'lifeExp')
    # print('The average life expectation for each year is:')
    # print(df)

    # # 16
    # df = get_average_with_properties_subset(file_name, 'year', 'lifeExp')
    # for year, avg_lifeExp in df.items():
    #     print(f"Year {year}: {round(avg_lifeExp, 3)}")

    # # 17
    # data = {'0': 'banana', '1': '42'}
    # series = pd.Series(data)
    # print(series)

    # # 18
    # data = {
    #     '0': 'banana',
    #     '1': '42',
    #     'Person': 'Wes MCKinney',
    #     'Who': 'Creator of Pandas'
    # }
    # series = pd.Series(data)
    # print(series)

    # # 19
    # data = {
    #     'Occupation': ['Chemist', 'Statistician'],
    #     'Born': ['1920-07-25', '1876-06-13'],
    #     'Died': ['1958-04-16', '1937-10-16'],
    #     'Age': [37, 61]
    # }
    # index = ['Franklin', 'Gosset']
    # df = pd.DataFrame(data, index=index)
    # print(df)