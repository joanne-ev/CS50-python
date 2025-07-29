'''
In a file called `plates.py`, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein `is_valid` still expects a `str` as input and returns `True` if that str meets all requirements and `False` if it does not, but `main` is only called if the value of `__name__` is `"__main__":`

def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()

Then, in a file called `test_plates.py`, implement four or more functions that collectively test your implementation of `is_valid` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

pytest test_plates.py

'''


def main():
   plate = input('Plate: ')
   print(is_valid(plate))



def is_valid(plate):
    validity_score = 0

    ### Plates must have a maximum of six and a minimum of two characters ###
    if 2 <= len(plate) <= 6:

        ## Plates must start with at least two letters ##
        # Identify first two characters of the plate
        character1 = plate[0]
        character2 = plate[1]

        # Check whether the two beginning characters are alphabets
        if character1.isalpha() and character2.isalpha():
            validity_score += 0
        else:
            validity_score += 1


        ### Plates must not have periods, spaces, or punctuation marks ###
        if plate.isalnum():
            validity_score += 0
        else:
            validity_score += 1


        adj_len = len(plate) - 1

        for i in range(adj_len):
            curr = plate[i]
            next = plate[i+1]

            ### Numbers cannot be used in the middle of a plate (they must come at the end) ###
            if curr.isdigit() and next.isalpha():
                validity_score += 1

            ### Plates cannot have zero as the leading number ###
            elif curr.isalpha() and next == '0':
                validity_score += 1
            else:
                validity_score += 0

    else:
        validity_score =+ 1


    # Compare validity scores
    if validity_score > 0:
        return False
    else:
        return True



if __name__ == "__main__":
    main()
