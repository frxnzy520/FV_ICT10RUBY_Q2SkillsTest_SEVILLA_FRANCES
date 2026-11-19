from pyscript import document, display


# Dictionary information about elements
# Element Symbol: Element Detail, Atomic Number, # of Electrons
elements = {"H": ('Hydrogen', 1, 1),
            #Key:          0       1  2
            "HE": ('Helium', 2, 2),
            "LI": ('Lithium', 3, 2),
            "BE": ('Beryllium', 4, 2),
            "B": ('Boron', 5, 2),
            "C": ('Carbon', 6, 2),
            "N": ('Nitrogen', 7, 2),
            "O": ('Oxygen', 8, 2),
            "F": ('Fluorine', 9, 2),
            "NE": ('Neon', 10, 2),
            "NA": ('Sodium', 11, 2),
            "MG": ('Magnesium', 12, 2),
            "AL": ('Aluminum', 13, 2),
            "SI": ('Silicon', 14, 2),
            "P": ('Phosphorus', 15, 2),
            "S": ('Sulfur', 16, 2),
            "Cl": ('Chlorine', 17, 2),
            "Ar": ('Argon', 18, 2),
            "K": ('Potassium', 19, 2),
            "Ca": ('Calcium', 20, 2),
            "Sc": ('Scandium', 21, 2),
            "Ti": ('Titanium', 22, 2),
            "V": ('Vanadium', 23, 2),
            "Cr": ('Chromium', 24, 2),
            "Mn": ('Manganese', 25, 2),
            "Fe": ('Iron', 26, 2),
            "Co": ('Cobalt', 27, 2),
            "Ni": ('Nickel', 28, 2),
            "Cu": ('Copper', 29, 2),
            "Zn": ('Zinc', 30, 2)}

    





# function to search your element
def search_element(e):
    #Get the input from HTML


    Element1 = document.getElementById("element").value.upper()
    # retrieve information forom the dictionary
    result = elements.get(Element1, ('Element not found', "-", "-"))
    # Display the result in HTML
    document.getElementById("code").innerText = Element1
    document.getElementById("name").innerText = result[0]
    document.getElementById("order").innerText = result[1]
    document.getElementById("elements").innerText = result[2]