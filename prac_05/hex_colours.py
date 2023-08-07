# hex color codes dictionary
# """
# CP1404/CP5632 Practical
# Hexadecimal colour lookup
# """
#
COLOUR_TO_CODE = {
    "ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "ANTIQUEWHITE1": "#ffefdb", "ANTIQUEWHITE2": "#eedfcc",
    "ANTIQUEWHITE3": "#cdc0b0", "ANTIQUEWHITE4": "#8b8378", "AQUAMARINE1": "#7fffd4", "AQUAMARINE2": "#76eec6",
    "AQUAMARINE4": "#458b74", "AZURE1": "#f0ffff"}

print(COLOUR_TO_CODE)

colour_name = input("Enter colour name: ").upper()
while colour_name != "":
    if colour_name in COLOUR_TO_CODE:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").upper()
