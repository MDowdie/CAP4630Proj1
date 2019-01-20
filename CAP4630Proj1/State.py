class State(object):
    """description of class"""

    StateName = ""
    @property
    def StateName(self):
        return self._StateName
    @StateName.setter
    def StateName(self,state):
        self._StateName = state

    CapitalCity = ""
    @property
    def CapitalCity(self):
        return self._CapitalCity
    @CapitalCity.setter
    def CapitalCity(self,cap):
        self._CapitalCity = cap

    Abbreviation = ""
    @property
    def Abbreviation(self):
        return self._Abbreviation
    @Abbreviation.setter
    def Abbreviation(self,abbr):
        self._Abbreviation = abbr

    Population = 0
    @property
    def Population(self):
        return self._Population
    @Population.setter
    def Population(self,popul):
        self._Population = popul
        self._PopWithCommas = '{:,}'.format(popul)

    PopWithCommas = ""
    @property
    def PopWithCommas(self):
        return self._PopWithCommas
    @PopWithCommas.setter
    def PopWithCommas(self,popul):
        self._PopWithCommas = popul


    Region = ""
    @property
    def Region(self):
        return self._Region
    @Region.setter
    def Region(self,reg):
        self._Region = reg

    USHouseSeats = 0
    @property
    def USHouseSeats(self):
        return self._USHouseSeats
    @USHouseSeats.setter
    def USHouseSeats(self,inval):
        self._USHouseSeats = inval


    def __init__(self,name,Capital,abbr,popul,region,houseseats):
        self.StateName = name
        self.CapitalCity = Capital
        self.Abbreviation = abbr
        self.Population = popul
        self.PopWithCommas = '{:,}'.format(popul)
        self.Region = region
        self.USHouseSeats = houseseats


    def __gt__(a,b):
        """Based on State Names, does a occur before b when placed in alphabetical order?"""
        if a.StateName > b.StateName:
            return True
        return False

    def __lt__(a,b):
        """Based on State Names, does a occur before b when placed in alphabetical order?"""
        if a.StateName < b.StateName:
            return True
        return False

    def __le__(a,b):
        if a.StateName <= b.StateName:
            return True
        return False

    def __ge__(a,b):
        if a.StateName >= b.StateName:
            return True
        return False

    def __eq__(a,b):
        if a.StateName == b.StateName:
            return True
        return False

    def __ne__(a,b):
        if a.StateName != b.StateName:
            return True
        return False

    def __str__(self):
        """Return string representative of entire State object"""

        output = "State Name:        "
        output += self._StateName
        output += "\nCapital City:      "
        output += self._CapitalCity
        output += "\nState Abbr:        "
        output += self._Abbreviation
        output += "\nState Population:  "
        output += self._PopWithCommas
        output += "\nRegion:            "
        output += self._Region
        output += "\nUS House Seats:    "
        output += str(self._USHouseSeats)
        return output