import numpy as np


def main(array1, array2):

    """
    Perform various checks on arrays

    Parameters
    ----------
    array1: int/float/array
    array2: int/float/array

    Returns
    -------
    None
    """

    # Perform checks
    if isinstance(array1, (list, np.ndarray)) is False:
        print("Must be a list or an array")
    isinstance(array2, (list, np.ndarray))
    try:
        assert len(array1) == len(array2), "Arrays must have the same number of elements"
    except TypeError as error:
        print(error)


if __name__ == "__main__":

    # Create some data to check
    # array1 = np.linspace(0, 10, 10)
    array1 = 2.0
    array2 = np.linspace(0, 20, 10)

    main(array1, array2)
