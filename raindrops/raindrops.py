# def convert(number: int) -> str:
#     sound = ""
#     if number % 3 == 0:
#         sound += "Pling"
#     if number % 5 == 0:
#         sound += "Plang"
#     if number % 7 == 0:
#         sound += "Plong"
#     return sound if sound else str(number)


def convert(number: int) -> str:
    factors = {3: "Pling",
               5: "Plang",
               7: "Plong"}

    sound = "".join(value for key, value in factors.items() if not number % key)
    return sound if sound else str(number)
