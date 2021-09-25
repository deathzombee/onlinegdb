# <Function Calls and User Defined Functions>

# Copyright © <2021> <Captain_dz>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import re

shortCode = {"ALABAMA": "AL", "ALASKA": "AK", "AMERICAN SAMOA": "AS", "ARIZONA": "AZ", "ARKANSAS": "AR",
             "CALIFORNIA": "CA", "COLORADO": "CO", "CONNECTICUT": "CT", "DELAWARE": "DE", "DISTRICT OF COLUMBIA": "DC",
             "FLORIDA": "FL", "GEORGIA": "GA", "GUAM": "GU", "HAWAII": "HI", "IDAHO": "ID", "ILLINOIS": "IL",
             "INDIANA": "IN", "IOWA": "IA", "KANSAS": "KS", "KENTUCKY": "KY", "LOUISIANA": "LA", "MAINE": "ME",
             "MARYLAND": "MD", "MASSACHUSETTS": "MA", "MICHIGAN": "MI", "MINNESOTA": "MN", "MISSISSIPPI": "MS",
             "MISSOURI": "MO", "MONTANA": "MT", "NEBRASKA": "NE", "NEVADA": "NV", "NEW HAMPSHIRE": "NH",
             "NEW JERSEY": "NJ", "NEW MEXICO": "NM", "NEW YORK": "NY", "NORTH CAROLINA": "NC", "NORTH DAKOTA": "ND",
             "NORTHERN MARIANA IS": "MP", "OHIO": "OH", "OKLAHOMA": "OK", "OREGON": "OR", "PENNSYLVANIA": "PA",
             "PUERTO RICO": "PR", "RHODE ISLAND": "RI", "SOUTH CAROLINA": "SC", "SOUTH DAKOTA": "SD", "TENNESSEE": "TN",
             "TEXAS": "TX", "UTAH": "UT", "VERMONT": "VT", "VIRGINIA": "VA", "VIRGIN ISLANDS": "VI", "WASHINGTON": "WA",
             "WEST VIRGINIA": "WV", "WISCONSIN": "WI", "WYOMING": "WY"}
name = input("Name?: ")
street = input("House number and street?: ")
city = input("City?: ")
state = input("State/Territory of USA? Full or Two letter code works: ")
zipC = input("Zip Code?: ")


def errorName():
    name = input("sorry I didn\'t get your name: ")
    nameO = nameA(name)
    return nameO


def nameA(name):
    if len(name) > 0:
        names = name.split()
        nameO = []
        for x in names:
            if re.search('^[A-Za-z]+$', x[0]):
                nameO += x.capitalize() + " "
            else:
                nameO += x + " "
    else:
        return errorName()
    nameO = "".join(nameO)
    nameO = nameO.rstrip()
    return nameO

def errorStreet():
    street = input("street addr: must have at least 3 characters: ")
    streetO = streetA(street)
    return streetO


def streetA(street):
    if len(street.split()) >= 3:
        streets = street.split()
        streetO = []
        for x in streets:
            if re.search('^[A-Za-z]+$', x[0]):
                streetO += x.capitalize() + " "
            else:
                streetO += x + " "
    else:
        return errorStreet()
    streetO = "".join(streetO)
    streetO = streetO.rstrip()
    return streetO


def errorCity():
    city = input("city must have at least 3 characters: ")
    cityO = cityA(city)
    return cityO


def cityA(city):
    if len(city) >= 3:
        citys = city.split()
        cityO = []
        for x in citys:
            if re.search('^[A-Za-z]+$', x[0]):
                cityO += x.capitalize() + " "
            else:
                cityO += x + " "
    else:
        return errorCity()
    cityO = "".join(cityO)
    cityO = cityO.rstrip()
    return cityO


def errorState():
    state = input("State did not match, try again?: ")
    stateCode = states(state)
    return stateCode


def states(state):
    if len(state) > 2 and state.upper() in shortCode.keys():
        stateCode = shortCode[state.upper()]
        return stateCode
    elif len(state) == 2 and state.upper() in shortCode.values():
        stateCode = state.upper()
        return stateCode
    else:
        return errorState()


def errorZip():
    zipC = input("zip code in 5 or 5+4 format again?: ")
    zipCode = checkZip(zipC)
    return zipCode


def checkZip(zipC):
    x = re.search('^[0-9]{5}(?:-[0-9]{4})?$', zipC)
    if x:
        zipCode = zipC
        return zipCode
    else:
        return errorZip()


def printAddress(nameO, streetO, cityO, stateCode, zipCode):
    print("\r\n" + nameO)
    print(streetO + ".")
    print(cityO + ', ' + stateCode + " " + zipCode)


printAddress(nameA(name), streetA(street), cityA(city), states(state), checkZip(zipC))