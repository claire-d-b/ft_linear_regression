from matplotlib.pyplot import legend, savefig, tight_layout, subplots, show, plot
from matplotlib.animation import FuncAnimation
from pandas import DataFrame, read_csv


def load(path: str) -> DataFrame:
    """Function that opens a file and display inner data in the shape of a datatable"""
    num_rows, num_cols = 0, 0
    try:
        # Ici open est un gestionnaire de contexte qui retourne un object-fichier
        file = read_csv(path)  # Replace with the actual file path

    except Exception as e:
        raise AssertionError(f"Error: {e}")
    return file


def get_values(df: DataFrame, keyword: str) -> DataFrame:
    """Search for two keyword in the entire DataFrame, then compare
    the two keywords (countries) data"""
    try:
        isinstance(df, DataFrame)
        # Search for a keyword in the entire DataFrame

        # lambda function sets all char to lowercase do we
        # talk about case-insensititvity then it searches for the
        # keyword in all lowercase words
        # axis=1 means "row-wise"
        # Finally, df[...] filters the rows where the condition is True.
        # In other words, it selects the rows where the keyword was found
        # in at least one of the columns.

        # To reindex a boolean Series so that it matches a DataFrame's
        # index, you can use the .reindex() method in pandas.
        # This method adjusts the index of the boolean Series to match the
        # DataFrame’s index, filling any missing values with False
        # (or another value of your choice) to ensure proper alignment.
        # print(df.columns)

        col = df[keyword]


    except Exception as e:
        raise AssertionError(f"Error: {e}")

    return col

def normalize(values: DataFrame) -> DataFrame:

    nvalues = []
    for i, unit in enumerate(values):
        nvalues.insert(i, unit / values.max())

    return DataFrame(nvalues)


def normalize_list(values: list) -> list:
    # flattened_values = [item for sublist in values for item in sublist]
    nvalues = []
    for i, unit in enumerate(values):
        try:
            nvalues.insert(i, unit / max(values))
        except Exception as e:
            raise AssertionError(f"Error: {e}")

    return nvalues

def display_points(frame_x: DataFrame, frame_y: DataFrame, b: float, coeff: float) -> None:

    y_pred = []

    fig, ax = subplots()

    for i, unit in enumerate(frame_x):
        y_pred.insert(i, coeff * unit + b)
    ax.plot(normalize(frame_x), normalize_list(y_pred))
    ax.scatter(normalize(frame_x), normalize(frame_y))
    # print("nonox", normalize(frame_x))
    # print("nonoy", normalize(frame_y))

    tight_layout()
    savefig('output_normalized', dpi=100)

    fig, ax = subplots()
    ax.scatter(frame_x, frame_y)

    tight_layout()
    savefig('output_real', dpi=100)


