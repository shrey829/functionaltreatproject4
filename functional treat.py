print("Welcome to data analyzer and transformer program!!")

print("Menu driven interface is")
print("1. Data Analyzer input")
print("2. Display basic statistics")
print("3. Calculate factorial (Recursion)")
print("4. Filter data through threshold function (Lambda function)")
print("5. Sort data")
print("6. Displaying dataset statistics")
print("7. Exit")

num = int(input("Enter your choice: "))

twod = []
oned = []

arr2 = [1, 2, 3, 4, 5, 6]          # 1D sample data
arr3 = [[1, 2, 3], [4, 5, 6]]      # 2D sample data




def data_input():
    """
    This function allows the user to enter data manually
    or use the sample data.

    The user can select either a 1D array or a 2D array.
    """

    global twod, oned

    print("10 - You want to manually enter data")
    print("20 - You want to try the program with sample data")

    c = int(input("Enter your choice (10 or 20): "))

    match c:

        case 10:

            print("A. 1D array")
            print("B. 2D array")

            a = input("Enter your choice (A or B): ")

            match a:

                case "A":

                    oned = list(
                        map(
                            int,
                            input(
                                "Enter your elements separated by spaces: "
                            ).split()
                        )
                    )

                    twod = []

                    print("Your 1D array is:", oned)

                case "B":

                    oned = []
                    twod = []

                    print("Enter the elements of row 1")

                    rows1 = list(
                        map(
                            int,
                            input(
                                "Enter values separated by spaces: "
                            ).split()
                        )
                    )

                    twod.append(rows1)

                    print("Enter the elements of row 2")

                    rows2 = list(
                        map(
                            int,
                            input(
                                "Enter values separated by spaces: "
                            ).split()
                        )
                    )

                    twod.append(rows2)

                    print("Your 2D array is:", twod)

                case _:

                    print("Invalid choice")

        case 20:

            print("1. 1D sample array")
            print("2. 2D sample array")

            choice = input("Enter your choice (1 or 2): ")

            match choice:

                case "1":

                    print("Your 1D sample array is:")
                    print(arr2)

                case "2":

                    print("Your 2D sample array is:")
                    print(arr3)

                case _:

                    print("Invalid choice")

        case _:

            print("Invalid choice")




def displaydatabasicstatics(**kwargs):
    """
    This function displays basic statistics of the
    selected dataset.

    It uses built-in functions such as len(), sum(),
    min(), and max().

    **kwargs is used to take additional information
    about the dataset.
    """

    print("\nDataset information")

    if "name" in kwargs:
        print("Dataset name:", kwargs["name"])

    if "type" in kwargs:
        print("Dataset type:", kwargs["type"])

    summed = int(
        input(
            "Enter your choice "
            "(1 for manual 1D, "
            "2 for manual 2D, "
            "3 for sample 1D, "
            "4 for sample 2D): "
        )
    )

    match summed:

        case 1:

            if len(oned) > 0:

                print("Length is:", len(oned))
                print("Sum is:", sum(oned))
                print("Minimum value is:", min(oned))
                print("Maximum value is:", max(oned))
                print("Range is:", max(oned) - min(oned))
                print("Average is:", sum(oned) / len(oned))

            else:

                print("No manual 1D data available")

        case 2:

            if len(twod) > 0:

                flat = sum(twod, [])

                print("Length is:", len(twod))
                print("Sum is:", sum(flat))
                print("Minimum value is:", min(flat))
                print("Maximum value is:", max(flat))
                print("Range is:", max(flat) - min(flat))
                print("Average is:", sum(flat) / len(flat))

            else:

                print("No manual 2D data available")

        case 3:

            print("Length is:", len(arr2))
            print("Sum is:", sum(arr2))
            print("Minimum value is:", min(arr2))
            print("Maximum value is:", max(arr2))
            print("Range is:", max(arr2) - min(arr2))
            print("Average is:", sum(arr2) / len(arr2))

        case 4:

            flat = sum(arr3, [])

            print("Length is:", len(arr3))
            print("Sum is:", sum(flat))
            print("Minimum value is:", min(flat))
            print("Maximum value is:", max(flat))
            print("Range is:", max(flat) - min(flat))
            print("Average is:", sum(flat) / len(flat))

        case _:

            print("Invalid choice")




def factorial(n):
    """
    This function calculates the factorial of a number
    using recursion.

    Parameters:
        n: The number whose factorial is required.

    Returns:
        The factorial of the number.
    """

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)




def filtering():
    """
    This function filters the values of a dataset using
    a threshold value.

    It uses filter() and lambda functions.

    Values greater than the threshold are displayed.
    """

    threshold = int(
        input("Enter the threshold value: ")
    )

    a = input(
        "Enter your array type "
        "(oned / twod / sample1 / sample2): "
    )

    if a == "oned":

        c = list(
            filter(
                lambda x: x > threshold,
                oned
            )
        )

        print("Filtered data:", c)

    elif a == "twod":

        c = []

        for row in twod:

            result = list(
                filter(
                    lambda x: x > threshold,
                    row
                )
            )

            c.append(result)

        print("Filtered data:", c)

    elif a == "sample1":

        c = list(
            filter(
                lambda x: x > threshold,
                arr2
            )
        )

        print("Filtered sample 1D data:", c)

    elif a == "sample2":

        c = []

        for row in arr3:

            result = list(
                filter(
                    lambda x: x > threshold,
                    row
                )
            )

            c.append(result)

        print("Filtered sample 2D data:", c)

    else:

        print("Invalid array type")


def sorting():
    """
    This function sorts the selected dataset in ascending
    or descending order.

    It supports manual and sample 1D and 2D arrays.
    """

    a = int(
        input(
            "Enter your array "
            "(1 = manual 1D, "
            "2 = manual 2D, "
            "3 = sample 1D, "
            "4 = sample 2D): "
        )
    )

    print("1. Ascending order")
    print("2. Descending order")

    x = int(input("Enter your choice: "))

    match a:

        case 1:

            if x == 1:

                oned.sort()
                print("Sorted data:", oned)

            elif x == 2:

                oned.sort(reverse=True)
                print("Sorted data:", oned)

            else:

                print("Invalid choice")

        case 2:

            if x == 1:

                result = list(
                    map(
                        lambda row: sorted(row),
                        twod
                    )
                )

                print("Sorted data:", result)

            elif x == 2:

                result = list(
                    map(
                        lambda row: sorted(
                            row,
                            reverse=True
                        ),
                        twod
                    )
                )

                print("Sorted data:", result)

            else:

                print("Invalid choice")

        case 3:

            if x == 1:

                result = sorted(arr2)

                print("Sorted sample 1D data:", result)

            elif x == 2:

                result = sorted(
                    arr2,
                    reverse=True
                )

                print("Sorted sample 1D data:", result)

            else:

                print("Invalid choice")

        case 4:

            if x == 1:

                result = list(
                    map(
                        lambda row: sorted(row),
                        arr3
                    )
                )

                print("Sorted sample 2D data:", result)

            elif x == 2:

                result = list(
                    map(
                        lambda row: sorted(
                            row,
                            reverse=True
                        ),
                        arr3
                    )
                )

                print("Sorted sample 2D data:", result)

            else:

                print("Invalid choice")

        case _:

            print("Invalid array choice")




def displaydatasetcharacteristics():
    """
    This function displays the characteristics of the
    selected dataset.

    The characteristics include:
    - Length
    - Sum
    - Minimum value
    - Maximum value
    - Range
    - Average

    For a 2D array, the data is flattened before
    calculating the statistics.

    This function displays the values using print()
    instead of returning them.
    """

    print("\nDataset characteristics are")

    summed = int(
        input(
            "Enter your choice "
            "(1 for manual 1D, "
            "2 for manual 2D, "
            "3 for sample 1D, "
            "4 for sample 2D): "
        )
    )

    match summed:

        case 1:

            if len(oned) > 0:

                print("Length is:", len(oned))
                print("Sum is:", sum(oned))
                print("Minimum value is:", min(oned))
                print("Maximum value is:", max(oned))
                print("Range is:", max(oned) - min(oned))
                print("Average is:", sum(oned) / len(oned))

            else:

                print("No manual 1D data available")

        case 2:

            if len(twod) > 0:

                flat = sum(twod, [])

                print("Length is:", len(twod))
                print("Sum is:", sum(flat))
                print("Minimum value is:", min(flat))
                print("Maximum value is:", max(flat))
                print("Range is:", max(flat) - min(flat))
                print("Average is:", sum(flat) / len(flat))

            else:

                print("No manual 2D data available")

        case 3:

            print("Length is:", len(arr2))
            print("Sum is:", sum(arr2))
            print("Minimum value is:", min(arr2))
            print("Maximum value is:", max(arr2))
            print("Range is:", max(arr2) - min(arr2))
            print("Average is:", sum(arr2) / len(arr2))

        case 4:

            flat = sum(arr3, [])

            print("Length is:", len(arr3))
            print("Sum is:", sum(flat))
            print("Minimum value is:", min(flat))
            print("Maximum value is:", max(flat))
            print("Range is:", max(flat) - min(flat))
            print("Average is:", sum(flat) / len(flat))

        case _:

            print("Invalid choice")



def exit_program():
    """
    This function displays an exit message and
    terminates the program.
    """

    print("Exiting the program...")




while num != 7:

    match num:

        case 1:

            data_input()

        case 2:

            displaydatabasicstatics(
                name="My Dataset",
                type="Current Dataset"
            )

        case 3:

            n = int(
                input("Enter your number for factorial: ")
            )

            if n < 0:

                print(
                    "Factorial is not possible for negative numbers"
                )

            else:

                print(
                    "Factorial is:",
                    factorial(n)
                )

        case 4:

            filtering()

        case 5:

            sorting()

        case 6:

            displaydatasetcharacteristics()

        case _:

            print("Invalid choice")

    print("\n----------------------------------")

    num = int(
        input("Enter your choice: ")
    )

print("Exiting the program...")