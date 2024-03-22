import pandas as pd


def show_lines(fn, n):
    """
    :param fn: name file
    :param n: number of lines
    :return: show data each line
    """

    df = pd.read_csv(fn, sep='\t', nrows=n)
    print(df)


def count_row_column(fn):
    df = pd.read_csv(fn, sep="\t")
    num_rows, num_columns = df.shape
    print("Number of rows:", num_rows)
    print("Number of columns:", num_columns)


def show_column_name(fn):
    df = pd.read_csv(fn, sep='\t')
    columns = df.columns
    for col in columns:
        print(col)


def show_type_column(fn):
    df = pd.read_csv(fn, sep='\t')
    column_types = df.dtypes
    print(column_types)


if __name__ == '__main__':
    file_name = '04_gap-merged.tsv'
    # show_lines(file_name, 5)
    # count_row_column(file_name)
    # show_column_name(file_name)
    show_type_column(file_name)