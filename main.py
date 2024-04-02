import datetime
import json
import logging
from decimal import Decimal
from enum import Enum
from pathlib import Path
from types import MappingProxyType as MPT
from typing import Literal, TypedDict

from lxml import etree

ROOT_PATH = Path(__file__).parent
DATA_PATH = Path.home() / "Downloads" / "otds_big_debug"
NS = MPT({None: "http://otds-group.org/otds"})

class X(Enum):
    x = "x"

class Absolute(Enum):
    AppliedBy = "AppliedBy"
    DayBase = "DayBase"
    PersonBase = "PersonBase"

class AccommodationType(Enum):
    Hotel = "Hotel"

class AgeType(Enum):
    DateOfBirth = "DateOfBirth"
    TravelAge = "TravelAge"
    BookingAge = "BookingAge"

class AirportType(Enum):
    Arrival = "Arrival"
    Catchment = "Catchment"
    Departure = "Departure"

class BoardType(Enum):
    none = "None"
    SelfCatering = "SelfCatering"
    Breakfast = "Breakfast"
    HalfBoard = "HalfBoard"
    HalfBoardPlus = "HalfBoardPlus"
    FullBoard = "FullBoard"
    FullBoardPlus = "FullBoardPlus"
    AllInclusive = "AllInclusive"
    AllInclusivePlus = "AllInclusivePlus"
    AllInclusiveLight = "AllInclusiveLight"

class Booking(Enum):
    Group = "Group"

class BookingGroup(Enum):
    Condition = "Condition"
    Parameter = "Parameter"

class BookingGroupArea(Enum):
    GlobalArea = "GlobalArea"
    ServiceArea = "ServiceArea"
    PersonArea = "PersonArea"

class BookingParameterField(Enum):
    Title = "Title"
    BrandCode = "BrandCode"
    TravelType = "TravelType"
    RequestCode = "RequestCode"
    ServiceCode = "ServiceCode"
    ServiceFeatureCode = "ServiceFeatureCode"
    BoardCode = "BoardCode"
    Assignment = "Assignment"
    DateStart = "DateStart"
    DateEnd = "DateEnd"
    Age = "Age"

class CombinableWhen(Enum):
    Code = "CombinationCode"
    Or = "Or"

class Component(Enum):
    Accommodation = "Accommodation"
    CombiComponent = "CombiComponent"
    DefinedComponent = "DefinedComponent"
    OnewayFlight = "OnewayFlight"

class Condition(Enum):
    And = "And"
    Or = "Or"
    Not = "Not"
    Airports = "Airports"
    BookingDateOffset = "BookingDateOffset"
    ConditionalTags = "ConditionalTags"
    Date = "Date"
    DayImpact = "DayImpact"
    Duration = "Duration"
    Impact = "Impact"
    Imply = "Imply"
    Keys = "Keys"
    MatchEqual = "MatchEqual"
    PersonCount = "PersonCount"
    PersonImpact = "PersonImpact"
    Tags = "Tags"

class CrsSystem(Enum):
    Merlin = "Merlin"
    Toma = "Toma"

class DateFormat(Enum):
    Dotted = "[D01].[M01].[Y0001]"
    Short = "[D01][M01][Y01]"
    Day = "[D01][M01]"
    ISO = "[Y0001]-[M01]-[D01]"
    Long = "[D01][M01][Y0001]"

class DayAllocation(Enum):
    All = "All"
    First = "First"
    Last = "Last"

class DayImpact(Enum):
    Date = "Date"
    DayIndex = "DayIndex"

class DayIndex(Enum):
    Indices = "Indices"
    Until = "Until"

class DayReference(Enum):
    CheckIn = "CheckIn"
    CheckOut = "CheckOut"

class DayType(Enum):
    CheckIn = "CheckIn"
    CheckOut = "CheckOut"
    Stay = "Stay"

class DayState(Enum):
    Closed = "Closed"
    Open = "Open"

class DefaultDayState(Enum):
    CheckOut = "CheckOut"
    Closed = "Closed"
    Open = "Open"

class DistributionChannel(Enum):
    Bewotec = "Bewotec"
    Check24 = "Check24"
    Peakwork = "Peakwork"
    TravelTainment = "TravelTainment"
    Traffics = "Traffics"
    Schmetterling = "Schmetterling"

class DurationUnit(Enum):
    Nights = "Nights"
    Hours = "Hours"
    Minutes = "Minutes"
    Weeks = "Weeks"

class EvaluationBase(Enum):
    PersonDay = "Person Day"
    Person = "Person"
    Day = "Day"

class GeneralIncludedService(Enum):
    Transfer = "Transfer"
    CheckInTransfer = "CheckInTransfer"
    CheckOutTransfer = "CheckOutTransfer"
    GolfArrangement = "GolfArrangement"
    CarRental = "CarRental"
    WellnessArrangement = "WellnessArrangement"
    SportsArrangement = "SportsArrangement"
    Skipass = "Skipass"
    TourArrangement = "TourArrangement"
    HotelServices = "HotelServices"
    GuidedTour = "GuidedTour"
    OtherServices = "OtherServices"
    none = "None"
    Parking = "Parking"
    CookService = "CookService"
    LaundryService = "LaundryService"
    RollService = "RollService"
    CleaningService = "CleaningService"
    FinalCleanUp = "FinalCleanUp"
    RailAndFly = "RailAndFly"
    SkiLessons = "SkiLessons"
    SnowboardLessons = "SnowboardLessons"
    FreeCancellation = "FreeCancellation"
    FreeRebooking = "FreeRebooking"
    FreeCancellationWithFee = "FreeCancellationWithFee"
    FreeRebookingWithFee = "FreeRebookingWithFee"
    PrivateTransfer = "PrivateTransfer"

class Match(Enum):
    Element = "Element"
    Tag = "Tag"

class MatchElement(Enum):
    CatchmentAirport = "CatchmentAirport"
    DepartureAirport = "DepartureAirport"
    ArrivalAirport = "ArrivalAirport"

class Occupancy(Enum):
    Person = "Person"

class OptionalBookableAddonType(Enum):
    TransferOptions = "TransferOptions"
    GolfArrangements = "GolfArrangements"
    CarRentalOptions = "CarRentalOptions"
    WellnessArrangements = "WellnessArrangements"
    SportsArrangements = "SportsArrangements"
    SkipassOptions = "SkipassOptions"
    TourArrangements = "TourArrangements"
    GuidedTours = "GuidedTours"
    ParkingOptions = "ParkingOptions"
    RailAndFlyOptions = "RailAndFlyOptions"
    SkiLessons = "SkiLessons"
    SnowboardLessons = "SnowboardLessons"
    FlexibleCancellationOptions = "FlexibleCancellationOptions"

class ParameterSet(Enum):
    DistributionChannel = "DistributionChannel"
    DistributorIdentificationGroup = "DistributorIdentificationGroup"
    SalesChannel = "SalesChannel"
    SalesMarket = "SalesMarket"

class PersonFilter(Enum):
    Impact = "Impact"

class PersonGender(Enum):
    Male = "Male"
    Female = "Female"
    Undefined = "Undefined"

class PersonImpact(Enum):
    Age = "Age"
    Genders = "Genders"
    Index = "Index"

class ProductType(Enum):
    AccommodationOnly = "AccommodationOnly"
    OnewayFlightOnly = "OnewayFlightOnly"
    ReturnFlightOnly = "ReturnFlightOnly"
    FlightAccommodation = "FlightAccommodation"
    Addon = "Addon"

class Role(Enum):
    ReturnFlight = "ReturnFlight"
    OnewayFlight = "OnewayFlight"
    Outbound = "Outbound"
    Inbound = "Inbound"
    Accommodation = "Accommodation"
    Addon = "Addon"
    AccommodationWrapper = "AccommodationWrapper"
    FlightWrapper = "FlightWrapper"
    AddonWrapper = "AddonWrapper"

class SalesChannel(Enum):
    OnlineTravelAgency = "OnlineTravelAgency"  # Selling of travel via webpages
    TravelAgency = "TravelAgency"  # Selling of travel via travel agencies
    Intern = "Intern"  # Selling of travel intra-companies

class Shift(Enum):
    none = "None"
    Auto = "Auto"
    External = "External"

class UnitFacilities(Enum):
    Airconditioning = "Airconditioning"
    Balcony = "Balcony"
    BalconyTerrace = "BalconyTerrace"
    Basement = "Basement"
    BathShower = "BathShower"
    BathOnFloor = "BathOnFloor"
    BathToiletteInCorridor = "BathToiletteInCorridor"
    BathTub = "BathTub"
    CentralHeating = "CentralHeating"
    ChargedHeating = "ChargedHeating"
    CityView = "CityView"
    Deluxe = "Deluxe"
    Dishwasher = "Dishwasher"
    Duplex = "Duplex"
    Family = "Family"
    Fireplace = "Fireplace"
    FloorHeating = "FloorHeating"
    Freezer = "Freezer"
    GardenView = "GardenView"
    GroundFloor = "GroundFloor"
    Hairdryer = "Hairdryer"
    HandicappedAccessible = "HandicappedAccessible"
    HourlyHeating = "HourlyHeating"
    InnercourtView = "InnercourtView"
    Iron = "Iron"
    Kitchen = "Kitchen"
    Kitchenette = "Kitchenette"
    LandView = "LandView"
    LakeView = "LakeView"
    LaundryDryer = "LaundryDryer"
    Loft = "Loft"
    Maisonette = "Maisonette"
    Minibar = "Minibar"
    MoreSeparateBedrooms = "MoreSeparateBedrooms"
    NonSmokerRoom = "NonSmokerRoom"
    PetsAllowed = "PetsAllowed"
    PetsProhibited = "PetsProhibited"
    PoolView = "PoolView"
    PremiumSuperior = "PremiumSuperior"
    PremiumView = "PremiumView"
    PrivatePool = "PrivatePool"
    PrivateSauna = "PrivateSauna"
    PrivateSolarium = "PrivateSolarium"
    PrivateTennisCourt = "PrivateTennisCourt"
    PrivateWhirlpool = "PrivateWhirlpool"
    RoofedTerrace = "RoofedTerrace"
    RoomSafe = "RoomSafe"
    SatTV = "SatTV"
    SeaView = "SeaView"
    SeaViewSideSeaView = "SeaViewSideSeaView"
    SeparateBedroom = "SeparateBedroom"
    SharedBathRoom = "SharedBathRoom"
    SharedToilette = "SharedToilette"
    ShortenedSeaView = "ShortenedSeaView"
    Shower = "Shower"
    SideSeaView = "SideSeaView"
    StreetView = "StreetView"
    Terrace = "Terrace"
    TV = "TV"
    TwoBedroomsWithConnectingDoor = "TwoBedroomsWithConnectingDoor"
    UpperFloor = "UpperFloor"
    ValleyView = "ValleyView"
    Veranda = "Veranda"
    WashingMachine = "WashingMachine"
    Budget = "Budget"
    DirectSharedPoolAccess = "DirectSharedPoolAccess"
    PrivateToilette = "PrivateToilette"
    Fridge = "Fridge"

class UnitType(Enum):
    Single = "Single"
    Double = "Double"
    Apartment = "Apartment"
    Studio = "Studio"
    Bungalow = "Bungalow"
    Triple = "Triple"
    Suite = "Suite"
    Other = "Other"
    Family = "Family"
    Villa = "Villa"
    HolidayHome = "HolidayHome"
    SemidetachedHouse = "SemidetachedHouse"
    Quad = "Quad"
    SingleWithChild = "SingleWithChild"
    MobileHome = "MobileHome"
    Tent = "Tent"
    JuniorSuite = "JuniorSuite"
    HolidayFlat = "HolidayFlat"

class UpdateMode(Enum):
    New = "New"
    Merge = "Merge"
    Delete = "Delete"

def validate(xml_path: Path, xsd_path: Path) -> bool:
    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    #if not xmlschema.validate(xml_doc):
    #    print(xmlschema.error_log.last_error)

    return xml_doc

"""rows = []
for path, dirnames, filenames in DATA_PATH.walk():
    if path == DATA_PATH:  # Skip files in root directory.
        continue
    if "accommodation" in path.stem:
        continue
    for filename in filenames:
        p = path / filename
        if p.suffix != ".xml":
            continue
        #print(path, dirnames, filenames)
        xml = validate(p, ROOT_PATH / "OTDS" / "xsd" / "otds.xsd")
        NS = xml.getroot().nsmap

        tags = xml.find("//OnewayFlights/OnewayFlight/Tags", namespaces=NS)
        if tags is None or not tags.getparent().get("Key").startswith("H_"):
            continue #raise RuntimeError("Should be header")
        origin = tags.find("Tag[@Class='VON3L']", namespaces=NS).text
        destination = tags.find("Tag[@Class='NACH3L']", namespaces=NS).text
        rows.append({"origin": origin, "destination": destination})

(ROOT_PATH / "output.json").write_text(json.dumps(rows))
exit()"""


PREFIX = "{http://otds-group.org/otds}"


class Accommodation(TypedDict):
    tags: dict[str, dict[str, str]]

class AccommodationInfo(TypedDict, total=False):
    giata: tuple[str, str]
    geonames: tuple[str, str]

class Geocode(TypedDict):
    latitude: float
    longitude: float
    accuracy_km: float

class Geo(TypedDict, total=False):
    geocode: Geocode

class Address(TypedDict, total=False):
    city: str
    country: str
    geo: Geo
    phone: str
    street: str
    zip: str

class Property(TypedDict, total=False):
    address: Address
    city: str
    info: AccommodationInfo
    name: str
    official_category: str
    operator_category: str

class SellingAccom(TypedDict, total=False):
    tags: dict[str, dict[str, str]]

_COMPONENT_NAME_LOOKUP = MPT({
    ProductType.AccommodationOnly: "Accommodation",
    ProductType.OnewayFlightOnly: "OnewayFlight",
    ProductType.ReturnFlightOnly: "ReturnFlight",
    ProductType.FlightAccommodation: "CombiComponent",
    ProductType.Addon: "Addon"
})
_NAME_COMPONENT_LOOKUP = MPT({v: k for k, v in _COMPONENT_NAME_LOOKUP.items()})

class OTDS:
    def __init__(self):
        self._accommodations: dict[str, Accommodation] = {}
        self._brands = {}
        self._defined_components = {}
        self._flights = {}
        self._products = {"product": {}}
        self._accommodations_price_items = {}

    def parse(self, path: Path) -> None:
        xml = validate(path, ROOT_PATH / "OTDS" / "xsd" / "otds.xsd")
        otds = xml.getroot()
        update_mode = self.get_update_mode(otds)
        if update_mode is UpdateMode.New:
            if self._accommodations or self._products != {"product": {}}:
                raise ValueError("Would overwrite all content")
        if update_mode is UpdateMode.Delete:
            raise NotImplementedError()

        for elem in otds.iterchildren():
            if elem.tag == f"{PREFIX}Brands":
                self.parse_brands(elem)
            elif elem.tag == f"{PREFIX}DefinedComponents":
                self.parse_defined_components(elem)
            elif elem.tag == f"{PREFIX}Flights":
                self.parse_flights(elem)
            elif elem.tag == f"{PREFIX}Accommodations":
                self.parse_accomodations(elem)
            elif elem.tag == f"{PREFIX}Products":
                self.parse_products(elem)
            else:
                raise NotImplementedError(elem.tag)

    def parse_airports(self, airports: etree.Element):
        a_type = AirportType(airports.attrib["AirportType"])
        return (airports.attrib["Source"], a_type, tuple(airports.text.split()))

    def parse_brand(self, brand: etree.Element) -> None:
        update_mode = self.get_update_mode(brand)
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        details = {}
        for elem in brand.iterchildren():
            if elem.tag == f"{PREFIX}Booking":
                details["booking"] = self.parse_booking(elem)
            elif elem.tag == f"{PREFIX}Tags":
                self.parse_tags(elem, details.setdefault("tags", {}))
            else:
                raise NotImplementedError(elem.tag)
        self._brands[brand.attrib["Key"]] = details

    def parse_brands(self, brands: etree.Element) -> None:
        update_mode = self.get_update_mode(brands)
        if update_mode is UpdateMode.New:
            if self._brands:
                raise ValueError("Would overwrite all brands")
        if update_mode is UpdateMode.Delete:
            raise NotImplementedError()

        for elem in brands.iterchildren():
            if elem.tag == f"{PREFIX}Brand":
                self.parse_brand(elem)
            else:
                assert False

    def parse_day_base(self, day_base: etree.Element) -> tuple[str, int | Literal[X.x]]:
        if day_base.get("IntervalType", "Stay") != "Stay":
            raise NotImplementedError()
        if day_base.text == "x":
            return X.x
        source = day_base.get("Source", "ThisComponent")
        return (source, int(day_base.text))

    def parse_flights(self, flights: etree.Element) -> None:
        update_mode = self.get_update_mode(flights)
        if update_mode is UpdateMode.New:
            if self._flights:
                raise ValueError("Would overwrite all flights")
        elif update_mode is UpdateMode.Delete:
            raise NotImplementedError()
        for elem in flights.iterchildren():
            if elem.tag != f"{PREFIX}OnewayFlights":
                raise NotImplementedError(elem.tag)
            self.parse_one_way_flights(elem, self._flights.setdefault("one_way", {}))

    def parse_one_way_flights(self, one_way_flights: etree.Element, flights_dict) -> None:
        update_mode = self.get_update_mode(one_way_flights)
        if update_mode is UpdateMode.New:
            if flights_dict:
                raise ValueError("Would overwrite all one way flights.")
        elif update_mode is UpdateMode.Delete:
            raise NotImplementedError()
        for elem in one_way_flights.iterchildren():
            assert elem.tag == f"{PREFIX}OnewayFlight"
            self.parse_one_way_flight(elem, flights_dict)

    def parse_one_way_flight(self, one_way_flight: etree.Element, flights_dict):
        update_mode = self.get_update_mode(one_way_flight)
        if update_mode is UpdateMode.New:
            if one_way_flight.attrib["Key"] in flights_dict:
                raise ValueError("Would overwrite flight.")
        elif update_mode is UpdateMode.Delete:
            raise NotImplementedError()

        flight = flights_dict.setdefault(one_way_flight.attrib["Key"], {})
        for elem in one_way_flight.iterchildren():
            if elem.tag == f"{PREFIX}ArrivalAirport":
                if self.get_update_mode(elem) is not UpdateMode.New:
                    raise NotImplementedError()
                flight["arrival"] = elem.text
            elif elem.tag == f"{PREFIX}DepartureAirport":
                if self.get_update_mode(elem) is not UpdateMode.New:
                    raise NotImplementedError()
                flight["departure"] = elem.text
            elif elem.tag == f"{PREFIX}Filter":
                self.parse_filter(elem, flight.setdefault("filter", {}))
            elif elem.tag == f"{PREFIX}BookingClass":
                self.parse_booking_class(elem, flight.setdefault("booking_class", {}))
            else:
                raise NotImplementedError(elem.tag)

    def parse_absolute(self, absolute: etree.Element):
        value = None
        conds = []
        for elem in absolute.iterchildren():
            if elem.tag == f"{PREFIX}Value":
                value = Decimal(elem.text)
            elif elem.tag == f"{PREFIX}DayBase":
                conds.append((Absolute.DayBase, self.parse_day_base(elem)))
            elif elem.tag == f"{PREFIX}PersonBase":
                if elem.text == "x":
                    raise NotImplementedError()
                conds.append((Absolute.PersonBase, int(elem.text)))
            elif elem.tag == f"{PREFIX}AppliedBy":
                if elem.get("Component") is not None:
                    raise NotImplementedError()
                if elem.get("Source") is not None:
                    raise NotImplementedError()
                if elem.get("LogicalRelation", "Or") != "Or":
                    raise NotImplementedError()
                conds.append((Absolute.AppliedBy, elem.text))
            else:
                raise NotImplementedError(elem.tag)
        assert value is not None
        return (value, conds)

    def parse_accomodations(self, accommodations: etree.Element) -> None:
        update_mode = self.get_update_mode(accommodations)
        if update_mode is UpdateMode.New:
            if self._accommodations:
                raise ValueError("Would overwrite all accommodations")
        elif update_mode is UpdateMode.Delete:
            raise NotImplementedError()
        for elem in accommodations.iterchildren():
            if elem.tag == f"{PREFIX}Accommodation":
                self.parse_accomodation(elem)
            elif elem.tag == f"{PREFIX}PriceItems":
                self.parse_price_items(elem, self._accommodations_price_items)
            else:
                raise NotImplementedError(elem.tag)

    def parse_accomodation(self, accommodation: etree.Element) -> None:
        update_mode = self.get_update_mode(accommodation)
        if update_mode is UpdateMode.New:
            if accommodation.attrib["Key"] in self._accommodations:
                raise ValueError("Would overwrite accommodation")
        elif update_mode is UpdateMode.Delete:
            raise NotImplementedError()
        accom = self._accommodations.setdefault(accommodation.attrib["Key"], {"selling": {}})
        for elem in accommodation.iterchildren():
            if elem.tag == f"{PREFIX}Tags":
                self.parse_tags(elem, accom.setdefault("tags", {}))
            elif elem.tag == f"{PREFIX}Properties":
                self.parse_properties(elem, accom.setdefault("properties", {}))
            elif elem.tag == f"{PREFIX}SellingAccom":
                self.parse_selling_accom(elem, accom["selling"])
            elif elem.tag == f"{PREFIX}CatchmentAirports":
                if elem.get("UpdateMode", "New") != "New":
                    raise NotImplementedError()
                accom["airports"] = tuple(elem.text.split())
            elif elem.tag == f"{PREFIX}Availabilities":
                self.parse_availabilities(elem, accom.setdefault("availabilities", {}))
            else:
                raise NotImplementedError(elem.tag)

    def parse_accomodation_address(self, addr: etree.Element, addr_dict: Address) -> None:
        for elem in addr.iterchildren():
            if elem.tag == f"{PREFIX}Street":
                addr_dict["street"] = elem.text
            elif elem.tag == f"{PREFIX}ZipCode":
                addr_dict["zip"] = elem.text
            elif elem.tag == f"{PREFIX}City":
                if elem.get("lang", "de") != "de":
                    raise NotImplementedError()
                if "city" in addr_dict:
                    raise NotImplementedError()
                addr_dict["city"] = elem.text
            elif elem.tag == f"{PREFIX}Country":
                if elem.get("lang", "de") != "de":
                    raise NotImplementedError()
                if "country" in addr_dict:
                    raise NotImplementedError()
                addr_dict["country"] = elem.text
            elif elem.tag == f"{PREFIX}Phone":
                addr_dict["phone"] = elem.text
            elif elem.tag == f"{PREFIX}GeoInfo":
                self.parse_geoinfo(elem, addr_dict.setdefault("geo", {}))
            else:
                raise NotImplementedError()

    def parse_accomodation_info(self, info: etree.Element, info_dict: AccommodationInfo) -> None:
        for elem in info.iterchildren():
            if elem.tag == f"{PREFIX}Reference":
                system = elem.attrib["ReferenceSystem"].lower()
                assert system in {"giata", "geocodes"}
                typ = elem.attrib["ReferenceType"]
                info_dict[system] = [typ, elem.text]
            else:
                raise NotImplementedError()

    def parse_availabilities(self, availabilities: etree.Element, avail_dict) -> None:
        update_mode = self.get_update_mode(availabilities)
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        avail = {}
        cond = None
        for elem in availabilities.iterchildren():
            if elem.tag == f"{PREFIX}Availability":
                self.parse_availability(elem, avail)
            elif elem.tag == f"{PREFIX}Condition":
                cond = self.parse_condition(elem)
            else:
                assert False
        avail_dict[availabilities.attrib["Key"]] = (cond, avail)

    def parse_availability(self, availability: etree.Element, avail_dict) -> None:
        update_mode = self.get_update_mode(availability)
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        start = datetime.date.fromisoformat(availability.attrib["StartDate"])
        end = datetime.date.fromisoformat(availability.attrib["EndDate"])

        state = {}
        default = None
        for elem in availability.iterchildren():
            if elem.tag == f"{PREFIX}DefaultDayState":
                default = self.parse_default_day_state(elem)
            elif elem.tag == f"{PREFIX}DayState":
                self.parse_day_state(elem, state)
            else:
                assert False

        assert default is not None
        avail_dict[availability.attrib["Key"]] = (start, end, default, state)

    def parse_board(self, board: etree.Element, board_dict):
        update_mode = self.get_update_mode(board)
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        b = {}
        for elem in board.iterchildren():
            if elem.tag == f"{PREFIX}Tags":
                self.parse_tags(elem, b.setdefault("tags", {}))
            elif elem.tag == f"{PREFIX}Booking":
                b["booking"] = self.parse_booking(elem)
            elif elem.tag == f"{PREFIX}Properties":
                self.parse_properties(elem, b.setdefault("properties", {}))
            else:
                raise NotImplementedError(elem.tag)
        board_dict[board.attrib["Key"]] = b

    def parse_booking(self, booking: etree.Element):
        update_mode = self.get_update_mode(booking)
        assert update_mode is not UpdateMode.Merge
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()
        bookings = []
        for elem in booking.iterchildren():
            if elem.tag == f"{PREFIX}BookingGroup":
                bookings.append((Booking.Group, *self.parse_booking_group(elem)))
            else:
                raise NotImplementedError()
        return tuple(bookings)

    def parse_booking_class(self, booking_class: etree.Element, booking_dict):
        update_mode = self.get_update_mode(booking_class)
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        booking = {}
        for elem in booking_class.iterchildren():
            if elem.tag == f"{PREFIX}Availabilities":
                self.parse_availabilities(elem, booking.setdefault("availabilities", {}))
            else:
                raise NotImplementedError(elem.tag)
        booking_dict[booking_class.attrib["Key"]] = booking

    def parse_booking_date_offset(self, date_offset: etree.Element) -> tuple[str, dict[str, int]]:
        source = date_offset.attrib["Source"]
        conds = {}
        for elem in date_offset.iterchildren():
            if elem.tag == f"{PREFIX}Min":
                conds["min"] = int(elem.text)
            elif elem.tag == f"{PREFIX}Max":
                conds["max"] = int(elem.text)
            else:
                assert False
        return (source, conds)

    def parse_booking_group(self, booking_group: etree.Element):
        if booking_group.get("Priority", 0) != 0:
            raise NotImplementedError()
        if booking_group.get("Class") is not None:
            raise NotImplementedError()
        _base = booking_group.get("EvaluationBase")
        eval_base = None if _base is None else EvaluationBase(_base)
        area = BookingGroupArea(booking_group.attrib["Area"])
        source = booking_group.get("Source", "ThisComponent")
        conds = []
        for elem in booking_group.iterchildren():
            if elem.tag == f"{PREFIX}BookingParameter":
                conds.append((BookingGroup.Parameter, self.parse_booking_parameter(elem)))
            elif elem.tag == f"{PREFIX}Condition":
                conds.append((BookingGroup.Condition, self.parse_condition(elem)))
            else:
                raise NotImplementedError(elem.tag)
        return (area, source, conds, eval_base)

    def parse_booking_parameter(self, booking_parameter: etree.Element):
        param = {
            "index": booking_parameter.get("Index", 0),
            "name": booking_parameter.get("Name", "Default"),
            "values": []
        }
        pad_length = int(booking_parameter.get("PadLength", 0))
        left_sep = booking_parameter.get("LeftSeparator", "")
        right_sep = booking_parameter.get("RightSeparator", "")
        if booking_parameter.get("PadOrientation", "Right") != "Right":
            raise NotImplementedError()
        if booking_parameter.get("Padding", " ") != " ":
            raise NotImplementedError()
        if booking_parameter.get("PadCondition", "Always") != "Always":
            raise NotImplementedError()
        for elem in booking_parameter.iterchildren():
            if elem.tag == f"{PREFIX}Value":
                param["values"].append(elem.text.ljust(pad_length))
            elif elem.tag == f"{PREFIX}Date":
                day_type = DayType(elem.attrib["DayType"])
                source = elem.get("Source", "ThisComponent")
                date_format = DateFormat(elem.get("DateFormat", "[D01][M01][Y01]"))
                param["date"] = (day_type, source, date_format)
            elif elem.tag == f"{PREFIX}PersonAge":
                age_type = AgeType(elem.get("AgeType", "TravelAge"))
                date_format = DateFormat(elem.get("DateFormat", "[D01][M01][Y01]"))
                param["person_age"] = (age_type, date_format)
            elif elem.tag == f"{PREFIX}Tag":
                if elem.get("DayAllocation") is not None:
                    raise NotImplementedError()
                if elem.get("EvaluationMode", "Any") != "Any":
                    raise NotImplementedError()
                if elem.get("Offset", 0) != 0:
                    raise NotImplementedError()
                if elem.get("Length") is not None:
                    raise NotImplementedError()
                if elem.get("TagValueType") is not None:
                    raise NotImplementedError()
                param["tag"] = (elem.attrib["Source"], elem.attrib["Class"])
            else:
                raise NotImplementedError(elem.tag)
        return (BookingParameterField(booking_parameter.attrib["Field"]), param, left_sep, right_sep)

    def parse_combi_components(self, combi: etree.Element, product_type: ProductType):
        # No idea what this is for, the element doesn't even have a Key...
        update_mode = self.get_update_mode(combi)
        assert update_mode is not UpdateMode.Merge
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        name = combi.get("Name")
        if name is None:
            raise NotImplementedError()
        _day_alloc = combi.get("DayAllocationIndex")
        if _day_alloc is None:
            raise NotImplementedError()
        day_alloc_index = int(_day_alloc)
        if combi.get("DayAllocationLevel", 0) != 0:
            raise NotImplementedError()

        comps = []
        for elem in combi.iterchildren():
            if elem.tag == f"{PREFIX}DefinedComponent":
                comps.append((Component.DefinedComponent, self.parse_rule_defined_component(elem, product_type)))
            else:
                raise NotImplementedError(elem.tag)

        return (combi.attrib["Role"], name, day_alloc_index, comps)

    def parse_combinable_when(self, combinable_when: etree.Element, _multi=False):
        conds = []
        for elem in combinable_when.iterchildren():
            if elem.tag == f"{PREFIX}CombinationCode":
                if elem.get("Component") is not None:
                    raise NotImplementedError()
                if elem.get("Source") is not None:
                    raise NotImplementedError()
                conds.append((CombinableWhen.Code, elem.get("Group", "Default")))
            elif elem.tag == f"{PREFIX}Or":
                conds.append((CombinableWhen.Or, self.parse_combinable_when(elem, _multi=True)))
            else:
                raise NotImplementedError(elem.tag)
        assert conds
        assert _multi or len(conds) == 1
        return conds if _multi else conds[0]

    def parse_combinatorics(self, combinatorics: etree.Element, combi_dict):
        key = (combinatorics.get("LayerName", "Default"), int(combinatorics.get("LayerLevel", 0)))
        assert key not in combi_dict
        c = {}
        for elem in combinatorics.iterchildren():
            if elem.tag == f"{PREFIX}CombinationCode":
                c["code"] = (elem.get("Group", "Default"), elem.text)
            elif elem.tag == f"{PREFIX}CombinationLevel":
                c["level"] = int(elem.text)
            elif elem.tag == f"{PREFIX}CombinableWhen":
                c["when"] = self.parse_combinable_when(elem)
            else:
                raise NotImplementedError(elem.tag)
        combi_dict[key] = c

    def parse_components(self, components: etree.Element, product_type: ProductType):
        update_mode = self.get_update_mode(components)
        assert update_mode is not UpdateMode.Merge
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        comps = []
        for elem in components.iterchildren():
            if elem.tag == f"{PREFIX}Accommodation":
                comps.append((Component.Accommodation, self.parse_rule_accommodation_component(elem, product_type)))
            elif elem.tag == f"{PREFIX}CombiComponent":
                comps.append((Component.CombiComponent, self.parse_combi_components(elem, product_type)))
            elif elem.tag == f"{PREFIX}DefinedComponent":
                comps.append((Component.DefinedComponent, self.parse_rule_defined_component(elem, product_type)))
            elif elem.tag == f"{PREFIX}OnewayFlight":
                name = elem.get("Name")
                if name is None:
                    raise NotImplementedError()
                _day_alloc = elem.get("DayAllocationIndex")
                if _day_alloc is None:
                    _day_alloc = 0  # TODO: The following default values are used depending on the component context:
                day_alloc_index = int(_day_alloc)
                day_alloc_lvl = int(elem.get("DayAllocationLevel", 0))
                comps.append((Component.OnewayFlight, (name, day_alloc_index, day_alloc_lvl)))
            else:
                raise NotImplementedError(elem.tag)
        return tuple(comps)

    def parse_condition(self, condition: etree.Element) -> tuple[tuple[Condition, tuple[str, ...]], ...]:
        cond = []
        for elem in condition.iterchildren():
            if elem.tag == f"{PREFIX}Or":
                cond.append((Condition.Or, self.parse_condition(elem)))
            elif elem.tag == f"{PREFIX}And":
                cond.append((Condition.And, self.parse_condition(elem)))
            elif elem.tag == f"{PREFIX}Not":
                not_cond = self.parse_condition(elem)
                assert len(not_cond) == 1
                cond.append((Condition.Not, not_cond[0]))
            elif elem.tag == f"{PREFIX}Airports":
                cond.append((Condition.Airports, self.parse_airports(elem)))
            elif elem.tag == f"{PREFIX}DayImpact":
                cond.append((Condition.DayImpact, self.parse_day_impact(elem)))
            elif elem.tag == f"{PREFIX}BookingDateOffset":
                cond.append((Condition.BookingDateOffset, self.parse_booking_date_offset(elem)))
            elif elem.tag == f"{PREFIX}ConditionalTags":
                cond.append((Condition.ConditionalTags, self.parse_conditional_tags(elem)))
            elif elem.tag == f"{PREFIX}Date":
                cond.append((Condition.Date, self.parse_date(elem)))
            elif elem.tag == f"{PREFIX}Duration":
                cond.append((Condition.Duration, self.parse_duration(elem)))
            elif elem.tag == f"{PREFIX}Impact":
                cond.append((Condition.Impact, self.parse_impact(elem)))
            elif elem.tag == f"{PREFIX}Imply":
                cond.append((Condition.Imply, self.parse_imply(elem)))
            elif elem.tag == f"{PREFIX}Keys":
                cond.append((Condition.Keys, self.parse_keys(elem)))
            elif elem.tag == f"{PREFIX}MatchEqual":
                cond.append((Condition.MatchEqual, self.parse_match_equal(elem)))
            elif elem.tag == f"{PREFIX}PersonCount":
                cond.append((Condition.PersonCount, self.parse_person_count(elem)))
            elif elem.tag == f"{PREFIX}PersonImpact":
                cond.append((Condition.PersonImpact, self.parse_person_impact(elem)))
            elif elem.tag == f"{PREFIX}Tags":
                cond.append((Condition.Tags, self.parse_tags_condition(elem)))
            else:
                raise NotImplementedError(elem.tag)
        return tuple(cond)

    def parse_conditional_tags(self, tags: etree.Element):
        if tags.get("DayAllocation", "All") != "All":  # Do not understand: The Default is "All" if the condition is not one of the following:
            raise NotImplementedError()
        if tags.get("EvaluationMode", "Any") != "Any":
            raise NotImplementedError()
        if tags.get("Offset", 0) != 0:
            raise NotImplementedError()
        if tags.get("Length") is not None:
            raise NotImplementedError()
        return (tags.attrib["Source"], tags.attrib["Class"], tuple(tags.text.split()))

    def parse_date(self, date: etree.Element) -> tuple[DayType, str, dict[str, datetime.date]]:
        source = date.attrib["Source"]
        dt = DayType(date.get("DayType", "Stay"))
        conds = {}
        for elem in date.iterchildren():
            if elem.tag == f"{PREFIX}Min":
                conds["min"] = datetime.date.fromisoformat(elem.text)
            elif elem.tag == f"{PREFIX}Max":
                conds["max"] = datetime.date.fromisoformat(elem.text)
            elif elem.tag == f"{PREFIX}Dates":
                conds["dates"] = tuple(datetime.date.fromisoformat(d) for d in elem.text.split())
            else:
                assert False
        return (dt, source, conds)

    def parse_day_allocation(self, day_allocation: etree.Element):
        update_mode = self.get_update_mode(day_allocation)
        assert update_mode is not UpdateMode.Merge
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        allocs = []
        for elem in day_allocation.iterchildren():
            if elem.tag == f"{PREFIX}DayAllocationStart":
                allocs.append(self.parse_day_allocation_start(elem))
            elif elem.tag == f"{PREFIX}DayAllocationEnd":
                allocs.append(self.parse_day_allocation_end(elem))
            else:
                assert False
        return tuple(allocs)

    def parse_day_allocation_end(self, day_alloc: etree.Element):
        return self._parse_day_allocation(day_alloc, "CheckOut")

    def parse_day_allocation_start(self, day_alloc: etree.Element):
        return self._parse_day_allocation(day_alloc, "CheckIn")

    def _parse_day_allocation(self, day_alloc: etree.Element, day_ref_default: str) -> tuple[int, str, DayReference, Shift]:
        if day_alloc.get("Offset", 0) != 0:
            raise NotImplementedError()

        source = day_alloc.get("Source", "Product")
        day_ref = DayReference(day_alloc.get("DayReference", day_ref_default))
        level = int(day_alloc.get("DayAllocationLevel", 0))
        shift = Shift(day_alloc.get("Shift", "None"))
        return (level, source, day_ref, shift)

    def parse_day_impact(self, day_impact: etree.Element) -> tuple[DayImpact, str, dict[str, datetime.date]]:
        if day_impact.get("ImpactExecutionOrder", "BeforeCombinatorics") != "BeforeCombinatorics":
            raise NotImplementedError()
        for elem in day_impact.iterchildren():
            if elem.tag == f"{PREFIX}Date":
                return (DayImpact.Date, *self.parse_date(elem))
            elif elem.tag == f"{PREFIX}DayIndex":
                return (DayImpact.DayIndex, *self.parse_day_index(elem))
            else:
                raise NotImplementedError()
        assert False

    def parse_day_index(self, day_index: etree.Element) -> tuple[str, tuple[DayIndex, int]]:
        if day_index.get("Repeat") is not None:
            raise NotImplementedError()
        if day_index.get("IntervalType", "Stay") != "Stay":
            raise NotImplementedError()
        conds = []
        for elem in day_index.iterchildren():
            if elem.tag == f"{PREFIX}Indices":
                conds.append((DayIndex.Indices, int(elem.text)))
            elif elem.tag == f"{PREFIX}Until":
                conds.append((DayIndex.Until, int(elem.text)))
            else:
                raise NotImplementedError(elem.tag)
        return (day_index.attrib["Source"], tuple(conds))

    def parse_day_state(self, day_state: etree.Element, state_dict) -> None:
        update_mode = self.get_update_mode(day_state)
        assert update_mode is not UpdateMode.Merge
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        state = None
        for elem in day_state.iterchildren():
            if elem.tag == f"{PREFIX}Closed":
                state = (DayState.Closed,)
            elif elem.tag == f"{PREFIX}Open":
                state = (DayState.Open, int(elem.text) if elem.text else None)
            else:
                raise NotImplementedError(elem.tag)
        state_dict[day_state.attrib["Key"]] = (int(day_state.attrib["Offset"]), *state)

    def parse_default_day_state(self, default_day_state: etree.Element):
        update_mode = self.get_update_mode(default_day_state)
        assert update_mode is not UpdateMode.Merge
        if update_mode is not UpdateMode.New:
            raise NotImplementedError

        state = None
        for elem in default_day_state.iterchildren():
            if elem.tag == f"{PREFIX}Closed":
                state = (DefaultDayState.Closed,)
            elif elem.tag == f"{PREFIX}Open":
                state = (DefaultDayState.Open, int(elem.text) if elem.text else None)
            elif elem.tag == f"{PREFIX}CheckOut":
                if elem.get("State", "Open") != "Open":
                    raise NotImplementedError()
                state = (DefaultDayState.CheckOut, int(elem.text) if elem.text else None)
            else:
                raise NotImplementedError(elem.tag)
        assert state is not None
        return state

    def parse_define_component(self, defined_component: etree.Element, components_dict) -> None:
        update_mode = self.get_update_mode(defined_component)
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        if defined_component.get("DayAllocationIndex") is not None:
            raise NotImplementedError()
        role = Role(defined_component.attrib["Role"])
        product_type = _NAME_COMPONENT_LOOKUP[defined_component.attrib["Role"]]

        comp = {}
        for elem in defined_component.iterchildren():
            if elem.tag == f"{PREFIX}Booking":
                comp["booking"] = self.parse_booking(elem)
            elif elem.tag == f"{PREFIX}Components":
                comp["components"] = self.parse_components(elem, product_type)
            elif elem.tag == f"{PREFIX}Filter":
                self.parse_filter(elem, comp.setdefault("filter", {}))
            else:
                assert False
        components_dict[defined_component.attrib["Key"]] = (role, comp)

    def parse_defined_components(self, defined_components: etree.Element) -> None:
        update_mode = self.get_update_mode(defined_components)
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        for elem in defined_components.iterchildren():
            assert elem.tag == f"{PREFIX}DefineComponent"
            self.parse_define_component(elem, self._defined_components)

    def parse_duration(self, duration: etree.Element) -> tuple[str, dict[str, datetime.timedelta]]:
        source = duration.attrib["Source"]
        du = DurationUnit(duration.get("DurationUnit", "Nights"))

        def delta(elem: etree.Element) -> datetime.timedelta:
            value = int(elem.text)
            if du is DurationUnit.Nights:
                return datetime.timedelta(days=value)
            elif du is DurationUnit.Hours:
                return datetime.timedelta(hours=value)
            elif du is DurationUnit.Minutes:
                return datetime.timedelta(minutes=value)
            elif du is DurationUnit.Weeks:
                return datetime.timedelta(weeks=value)
            assert False

        conds = {}
        for elem in duration.iterchildren():
            if elem.tag == f"{PREFIX}Min":
                conds["min"] = delta(elem)
            elif elem.tag == f"{PREFIX}Max":
                conds["max"] = delta(elem)
            elif elem.tag == f"{PREFIX}Durations":
                conds["durations"] = tuple(int(x) for x in elem.text.split())
            else:
                raise NotImplementedError(elem.tag)
        return (source, conds)

    def parse_element(self, element: etree.Element):
        if element.get("DayAllocation") is not None:
            raise NotImplementedError()
        if element.get("EvaluationMode", "Any") != "Any":
            raise NotImplementedError()

        return (MatchElement(element.text), element.attrib["Source"])

    def parse_empty_tag_condition(self, tag: etree.Element) -> tuple[str, str]:
        if tag.get("DayAllocation", "All") != "All":  # Do not understand: The Default is "All" if the condition is not one of the following:
            raise NotImplementedError()
        if tag.get("EvaluationMode", "Any") != "Any":
            raise NotImplementedError()
        if tag.get("Offset", 0) != 0:
            raise NotImplementedError()
        if tag.get("Length") is not None:
            raise NotImplementedError()
        if tag.get("TagValueType", "String") != "String":
            raise NotImplementedError()

        return (tag.attrib["Source"], tag.attrib["Class"])

    def parse_filter(self, filt: etree.Element, filter_dict: dict[str, tuple]):
        update_mode = self.get_update_mode(filt)
        assert update_mode is not UpdateMode.Merge
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()
        filter_dict[filt.get("Key", "default")] = self.parse_condition(filt)  # TODO(OTDS2+): Key must exist

    def parse_general_included_services(self, included_services: etree.Element):
        if included_services.get("Class") is not None:
            raise NotImplementedError()
        services = []
        for elem in included_services.iterchildren():
            assert elem.tag == f"{PREFIX}GeneralIncludedService"
            if elem.get("lang", "de") != "de":
                raise NotImplementedError()
            if elem.get("ShortServiceAnnotation") is not None:
                raise NotImplementedError()
            services.append(GeneralIncludedService(elem.text))
        return services

    def parse_geoinfo(self, geo: etree.Element, geo_dict: Geo) -> None:
        for elem in geo.iterchildren():
            if elem.tag == f"{PREFIX}GeoCode":
                geo_dict["geocode"] = {
                    "latitude": float(elem.findtext(f"{PREFIX}Latitude")),
                    "longitude": float(elem.findtext(f"{PREFIX}Longitude")),
                    "accuracy_km": float(elem.findtext(f"{PREFIX}Accuracy"))
                }
            else:
                raise NotImplementedError()

    def parse_global_value(self, global_value: etree.Element, globals_dict) -> None:
        update_mode = self.get_update_mode(global_value)
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        value = {"params": {}}
        for elem in global_value.iterchildren():
            if elem.tag == f"{PREFIX}ParameterSet":
                self.parse_parameter_set(elem, value["params"])
            else:
                raise NotImplementedError(elem.tag)
        assert value["params"]
        globals_dict[global_value.attrib["Key"]] = value

    def parse_global_values(self, global_values: etree.Element, products_dict) -> None:
        update_mode = self.get_update_mode(global_values)
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        g = {}
        for elem in global_values.iterchildren():
            assert elem.tag == f"{PREFIX}GlobalValue"
            self.parse_global_value(elem, g)
        assert g
        products_dict["globals"] = g

    def parse_impact(self, impact: etree.Element):
        if impact.get("ImpactExecutionOrder", "BeforeCombinatorics") != "BeforeCombinatorics":
            raise NotImplementedError()
        cond = None
        for elem in impact.iterchildren():
            assert cond is None
            if elem.tag == f"{PREFIX}ConditionalTags":
                cond = self.parse_conditional_tags(elem)
            else:
                raise NotImplementedError()
        assert cond is not None
        return cond

    def parse_imply(self, imply: etree.Element):
        if_cond = self.parse_condition(imply.find(f"{PREFIX}If"))
        then_cond = self.parse_condition(imply.find(f"{PREFIX}Then"))
        return (if_cond, then_cond)

    def parse_keys(self, keys: etree.Element):
        _day_alloc = keys.get("DayAllocation")
        day_alloc = None if _day_alloc is None else DayAllocation(_day_alloc)
        if keys.get("EvaluationMode", "Any") != "Any":
            raise NotImplementedError()
        return (keys.attrib["Source"], keys.text, _day_alloc)

    def parse_match_equal(self, match_equal: etree.Element):
        elems = []
        for elem in match_equal.iterchildren():
            if elem.tag == f"{PREFIX}Element":
                elems.append((Match.Element, self.parse_element(elem)))
            elif elem.tag == f"{PREFIX}Tag":
                elems.append((Match.Tag, self.parse_empty_tag_condition(elem)))
            else:
                raise NotImplementedError(elem.tag)
        assert len(elems) >= 2
        return tuple(elems)

    def parse_occupancy(self, occupancy: etree.Element, occupancies) -> None:
        update_mode = self.get_update_mode(occupancy)
        assert update_mode is not UpdateMode.Merge
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        occupancies[occupancy.attrib["Key"]] = occ = []
        for elem in occupancy.iterchildren():
            if elem.tag == f"{PREFIX}Person":
                occ.append((Occupancy.Person, self.parse_person(elem)))
            else:
                raise NotImplementedError(elem.tag)

    def parse_optional_bookable_addon_types(self, addon_types: etree.Element):
        if addon_types.get("Class") is not None:
            raise NotImplementedError()

        addons = []
        for elem in addon_types.iterchildren():
            assert elem.tag == f"{PREFIX}OptionalBookableAddonType"
            if elem.get("lang", "de") != "de":
                raise NotImplementedError()
            addons.append((OptionalBookableAddonType(elem.text), elem.get("ShortTeaserText")))
        print(addons)
        return tuple(addons)

    def parse_parameter_set(self, parameter_set: etree.Element, params_dict) -> None:
        update_mode = self.get_update_mode(parameter_set)
        assert update_mode is not UpdateMode.Merge
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        param = None
        agency = brand = crs = None
        for elem in parameter_set.iterchildren():
            if elem.tag == f"{PREFIX}AgencyCode":
                agency = elem.text
            elif elem.tag == f"{PREFIX}BrandCode":
                brand = elem.text
            elif elem.tag == f"{PREFIX}CrsSystem":
                crs = CrsSystem(elem.text)
            elif elem.tag == f"{PREFIX}DistributionChannel":
                param = (ParameterSet.DistributionChannel, DistributionChannel(elem.text))
            elif elem.tag == f"{PREFIX}SalesChannel":
                param = (ParameterSet.SalesChannel, SalesChannel(elem.text))
            elif elem.tag == f"{PREFIX}SalesMarket":
                param = (ParameterSet.SalesMarket, elem.text)
            else:
                raise NotImplementedError(elem.tag)
        if all(x is not None for x in (agency, brand, crs)):
            param = (ParameterSet.DistributorIdentificationGroup, crs, agency, brand)
        assert param is not None
        params_dict[parameter_set.attrib["Key"]] = param

    def parse_person(self, person: etree.Element):
        if person.get("MatchAvailability") is not None:
            raise NotImplementedError()

        conds = {}
        for elem in person.iterchildren():
            if elem.tag == f"{PREFIX}Count":
                conds["count"] = int(elem.text)
            elif elem.tag == f"{PREFIX}MaxAge":
                conds["max_age"] = int(elem.text)
            elif elem.tag == f"{PREFIX}MinAge":
                conds["min_age"] = int(elem.text)
            else:
                raise NotImplementedError(elem.tag)
        return conds

    def parse_person_age(self, person_age: etree.Element) -> tuple[str, dict[str, int]]:
        if person_age.get("DayAllocation") is not None:
            raise NotImplementedError()
        if person_age.get("EvaluationMode", "Any") != "Any":
            raise NotImplementedError()

        conds = {}
        for elem in person_age.iterchildren():
            if elem.tag == f"{PREFIX}Max":
                conds["max"] = int(elem.text)
            else:
                raise NotImplementedError(elem.tag)
        return (person_age.attrib["Source"], conds)

    def parse_person_count(self, person_count: etree.Element):
        if person_count.get("DayAllocation") is not None:
            raise NotImplementedError()
        if person_count.get("EvaluationMode", "Any") != "Any":
            raise NotImplementedError()

        conds = {}
        for elem in person_count.iterchildren():
            if elem.tag == f"{PREFIX}Min":
                conds["min"] = int(elem.text)
            elif elem.tag == f"{PREFIX}PersonFilter":
                conds["filter"] = self.parse_person_filter(elem)
            else:
                raise NotImplementedError(elem.tag)
        return (person_count.attrib["Source"], conds)

    def parse_person_filter(self, person_filter: etree.Element):
        cond = None
        for elem in person_filter.iterchildren():
            assert cond is None
            if elem.tag == f"{PREFIX}Impact":
                cond = (PersonFilter.Impact, self.parse_impact(elem))
            else:
                raise NotImplementedError(elem.tag)
        assert cond is not None
        return cond

    def parse_person_genders(self, person_genders: etree.Element) -> tuple[str, tuple[PersonGender, ...]]:
        if person_genders.get("DayAllocation") is not None:
            raise NotImplementedError()
        if person_genders.get("EvaluationMode", "Any") != "Any":
            raise NotImplementedError()

        values = tuple(PersonGender(v) for v in person_genders.text.split())
        return (person_genders.attrib["Source"], values)

    def parse_person_impact(self, person_impact: etree.Element):
        if person_impact.get("ImpactExecutionOrder", "BeforeCombinatorics") != "BeforeCombinatorics":
            raise NotImplementedError()

        cond = None
        for elem in person_impact.iterchildren():
            assert cond is None
            if elem.tag == f"{PREFIX}PersonAge":
                cond = (PersonImpact.Age, self.parse_person_age(elem))
            elif elem.tag == f"{PREFIX}PersonIndex":
                cond = (PersonImpact.Index, self.parse_person_index(elem))
            elif elem.tag == f"{PREFIX}PersonGenders":
                cond = (PersonImpact.Genders, self.parse_person_genders(elem))
            else:
                raise NotImplementedError(elem.tag)
        assert cond is not None
        return cond

    def parse_person_index(self, person_index: etree.Element) -> tuple[str, dict[str, int]]:
        if person_index.get("DayAllocation") is not None:
            raise NotImplementedError()
        if person_index.get("EvaluationMode", "Any") != "Any":
            raise NotImplementedError()

        conds = {}
        for elem in person_index.iterchildren():
            if elem.tag == f"{PREFIX}From":
                conds["from"] = int(elem.text)
            elif elem.tag == f"{PREFIX}Indices":
                conds["indices"] = tuple(int(t) for t in elem.text.split())
            elif elem.tag == f"{PREFIX}Until":
                conds["until"] = int(elem.text)
            else:
                raise NotImplementedError(elem.tag)
        return (person_index.attrib["Source"], conds)

    def parse_price_item(self, price_item: etree.Element, price_dict) -> None:
        p = {}
        for elem in price_item.iterchildren():
            if elem.tag == f"{PREFIX}Absolute":
                p["absolute"] = self.parse_absolute(elem)
            elif elem.tag == f"{PREFIX}Combinatorics":
                self.parse_combinatorics(elem, p.setdefault("combinatorics", {}))
            elif elem.tag == f"{PREFIX}Condition":
                p["condition"] = self.parse_condition(elem)
            else:
                raise NotImplementedError(elem.tag)
        price_dict.setdefault(price_item.attrib["Class"], []).append(p)

    def parse_price_items(self, price_items: etree.Element, prices_dict) -> None:
        update_mode = self.get_update_mode(price_items)
        assert update_mode is not UpdateMode.Merge
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        p = {}
        for elem in price_items.iterchildren():
            if elem.tag == f"{PREFIX}PriceItem":
                self.parse_price_item(elem, p)
            else:
                raise NotImplementedError(elem.tag)
        prices_dict[price_items.attrib["Key"]] = p

    def parse_product(self, product: etree.Element, product_dict):
        update_mode = self.get_update_mode(product)
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        product_type = ProductType(product.attrib["ProductType"])
        p = {}
        for elem in product.iterchildren():
            if elem.tag == f"{PREFIX}Tags":
                self.parse_tags(elem, p.setdefault("tags", {}))
            elif elem.tag == f"{PREFIX}Components":
                p["components"] = self.parse_components(elem, product_type)
            elif elem.tag == f"{PREFIX}DayAllocation":
                p["day_allocation"] = self.parse_day_allocation(elem)
            elif elem.tag == f"{PREFIX}Filter":
                self.parse_filter(elem, p.setdefault("filters", {}))
            else:
                raise NotImplementedError(elem.tag)
        assert "components" in p
        product_dict[product.attrib["Key"]] = (product_type, p)

    def parse_products(self, products: etree.Element) -> None:
        update_mode = self.get_update_mode(products)
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        for elem in products.iterchildren():
            if elem.tag == f"{PREFIX}GlobalValues":
                self.parse_global_values(elem, self._products)
            elif elem.tag == f"{PREFIX}Product":
                self.parse_product(elem, self._products["product"])
            else:
                raise NotImplementedError(elem.tag)

    def parse_properties(self, properties: etree.Element, properties_dict: dict[str, Property]) -> None:
        update_mode = self.get_update_mode(properties)
        assert update_mode is not UpdateMode.Merge
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()
        p = []
        for elem in properties.iterchildren():
            assert elem.tag == f"{PREFIX}PropertyGroup"
            p.append(self.parse_property_group(elem))
        properties_dict[properties.attrib["Key"]] = p

    def parse_property_group(self, property_group: etree.Element) -> Property:
        if property_group.get("Priority", 0) != 0:
            raise NotImplementedError()
        property: Property = {}
        for elem in property_group.iterchildren():
            if elem.tag == f"{PREFIX}AccommodationCity":
                if elem.get("lang", "de") != "de":
                    raise NotImplementedError()
                if "city" in property:
                    raise NotImplementedError()
                property["city"] = elem.text
            elif elem.tag == f"{PREFIX}AccommodationType":
                if elem.text != "Hotel":
                    raise NotImplementedError()
                #property["type"] = AccommodationType(elem.text)
            elif elem.tag == f"{PREFIX}AccommodationName":
                if elem.get("lang", "de") != "de":
                    raise NotImplementedError()
                if "name" in property:
                    raise NotImplementedError()
                property["name"] = elem.text
            elif elem.tag == f"{PREFIX}AccommodationInfo":
                self.parse_accomodation_info(elem, property.setdefault("info", {}))
            elif elem.tag == f"{PREFIX}AccommodationOfficialCategory":
                property["official_category"] = elem.text
            elif elem.tag == f"{PREFIX}AccommodationOperatorCategory":  # TODO: tuple value?
                property["operator_category"] = elem.text
            elif elem.tag == f"{PREFIX}AccommodationAddress":
                self.parse_accomodation_address(elem, property.setdefault("address", {}))
            elif elem.tag == f"{PREFIX}BoardName":
                if elem.get("lang", "de") != "de":
                    raise NotImplementedError()
                property["board_name"] = elem.text
            elif elem.tag == f"{PREFIX}BoardType":
                property["board_type"] = BoardType(elem.text)
            elif elem.tag == f"{PREFIX}UnitFacilities":
                property["unit_facilities"] = tuple(UnitFacilities(t) for t in elem.text.split())
            elif elem.tag == f"{PREFIX}UnitName":
                if elem.get("lang", "de") != "de":
                    raise NotImplementedError()
                property["unit_name"] = elem.text
            elif elem.tag == f"{PREFIX}UnitType":
                property["unit_types"] = tuple(UnitType(t) for t in elem.text.split())
            elif elem.tag == f"{PREFIX}GeneralIncludedServices":
                property["included_services"] = self.parse_general_included_services(elem)
            elif elem.tag == f"{PREFIX}Condition":
                property["condition"] = self.parse_condition(elem)
            elif elem.tag == f"{PREFIX}OptionalBookableAddonTypes":
                property["optional_addons"] = self.parse_optional_bookable_addon_types(elem)
            else:
                raise NotImplementedError(elem.tag)
        return property

    def parse_rule_accommodation_component(self, component: etree.Element, product_type: ProductType):
        name = component.get("Name")
        if any(component.get(a) is not None for a in ("Name", "DayAllocationIndex")):
            raise NotImplementedError()
        """if name is None:
            name = _COMPONENT_NAME_LOOKUP[product_type]

        _day_alloc = component.get("DayAllocationIndex")
        if _day_alloc is None:
            day_alloc = _COMPONENT_DAY_ALLOC_LOOKUP[product_type]
        else:
            day_alloc = int(_day_alloc)"""

        if component.get("DayAllocationLevel", 0) != 0:
            raise NotImplementedError()

        accoms = []
        for elem in component.iterchildren():
            if elem.tag == f"{PREFIX}SellingAccom":
                accoms.append(self.parse_rule_selling_accom_component(elem))
            else:
                assert False

        return tuple(accoms)

    def parse_rule_selling_accom_component(self, selling_accom: etree.Element) -> tuple[str, int]:
        name = selling_accom.get("Name")
        if name is None:
            raise NotImplementedError()

        _day_alloc = selling_accom.get("DayAllocationIndex")
        if _day_alloc is None:
            raise NotImplementedError()
        day_alloc_index = int(_day_alloc)

        if selling_accom.get("DayAllocationLevel", 0) != 0:
            raise NotImplementedError()

        return name, day_alloc_index

    def parse_rule_defined_component(self, component: etree.Element, product_type: ProductType):
        name = component.get("Name")
        if name is None:
            name = _COMPONENT_NAME_LOOKUP[product_type]  # TODO: Check this...

        if component.get("DayAllocationIndex") is not None:
            raise NotImplementedError()

        day_alloc_lvl = int(component.get("DayAllocationLevel", 0))
        role = Role(component.attrib["UseRole"])
        return (role, name, day_alloc_lvl)

    def parse_selling_accom(self, selling_accom: etree.Element, selling: dict[str, SellingAccom]) -> None:
        update_mode = self.get_update_mode(selling_accom)
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        selling[selling_accom.attrib["Key"]] = sell = {}
        for elem in selling_accom.iterchildren():
            if elem.tag == f"{PREFIX}Tags":
                self.parse_tags(elem, sell.setdefault("tags", {}))
            elif elem.tag == f"{PREFIX}Booking":
                sell["booking"] = self.parse_booking(elem)
            elif elem.tag == f"{PREFIX}Filter":
                self.parse_filter(elem, sell.setdefault("filter", {}))
            elif elem.tag == f"{PREFIX}Board":
                self.parse_board(elem, sell.setdefault("board", {}))
            elif elem.tag == f"{PREFIX}PriceItems":
                self.parse_price_items(elem, sell.setdefault("price_items", {}))
            elif elem.tag == f"{PREFIX}Unit":
                self.parse_unit(elem, sell.setdefault("unit", {}))
            else:
                raise NotImplementedError(elem.tag)

    def parse_selling_unit(self, selling_unit: etree.Element, selling) -> None:
        update_mode = self.get_update_mode(selling_unit)
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        selling[selling_unit.attrib["Key"]] = sell = {}
        for elem in selling_unit.iterchildren():
            if elem.tag == f"{PREFIX}Tags":
                self.parse_tags(elem, sell.setdefault("tags", {}))
            elif elem.tag == f"{PREFIX}Booking":
                sell["booking"] = self.parse_booking(elem)
            elif elem.tag == f"{PREFIX}Occupancy":
                self.parse_occupancy(elem, sell.setdefault("occupancy", {}))
            else:
                raise NotImplementedError(elem.tag)

    def parse_tags(self, tags: etree.Element, tags_dict: dict[str, dict[str, str]]) -> None:
        update_mode = self.get_update_mode(tags)
        assert update_mode is not UpdateMode.Merge
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()
        t = {}  # TODO(OTDS2+): Key must exist
        for elem in tags.iterchildren():
            if elem.tag == f"{PREFIX}Tag":
                self.parse_tag(elem, t)
            elif elem.tag == f"{PREFIX}ConditionalTag":
                self.parse_tag_conditional(elem, t)
            else:
                assert False
        tags_dict[tags.get("Key", "default")] = t

    def parse_tags_condition(self, tags: etree.Element):
        """<Tags> element within a <Condition> element."""
        if tags.get("DayAllocation", "All") != "All":  # Do not understand: The Default is "All" if the condition is not one of the following:
            raise NotImplementedError()
        if tags.get("EvaluationMode", "Any") != "Any":
            raise NotImplementedError()
        # Convert these to slice indexes, so they can be compared with value[start:end].
        start = int(tags.get("Offset", 0))
        length = tags.get("Length")
        end = None if length is None else start + int(length)
        return (tags.attrib["Source"], tags.attrib["Class"], tuple(tags.text.split()), start, end)

    def parse_tag(self, tag: etree.Element, tags: dict[str, str]) -> None:
        if tag.get("TagValueType", "String") != "String":
            raise NotImplementedError()
        tags[tag.attrib["Class"]] = tag.text

    def parse_tag_conditional(self, cond_tag: etree.Element, tags: dict[str, str]) -> None:
        for elem in cond_tag.iterchildren():
            if elem.tag == f"{PREFIX}Tag":
                self.parse_tag(elem, tags)  # TODO
            elif elem.tag == f"{PREFIX}Condition":
                cond = self.parse_condition(elem)
            else:
                assert False

    def parse_unit(self, unit: etree.Element, unit_dict) -> None:
        update_mode = self.get_update_mode(unit)
        if update_mode is not UpdateMode.New:
            raise NotImplementedError()

        u = {}
        for elem in unit.iterchildren():
            if elem.tag == f"{PREFIX}Tags":
                self.parse_tags(elem, u.setdefault("tags", {}))
            elif elem.tag == f"{PREFIX}Properties":
                self.parse_properties(elem, u.setdefault("properties", {}))
            elif elem.tag == f"{PREFIX}SellingUnit":
                self.parse_selling_unit(elem, u.setdefault("selling_units", {}))
            else:
                raise NotImplementedError(elem.tag)
        unit_dict[unit.attrib["Key"]] = u

    def get_update_mode(self, elem: etree.Element) -> None:
        return UpdateMode(elem.get("UpdateMode", "New"))

otds = OTDS()
otds.parse(ROOT_PATH / "001_basis.xml")
otds.parse(ROOT_PATH / "acc-test.xml")

import pprint
#with open("acc-output.json", "w") as f:
#    pprint.pprint(otds._accommodations, stream=f, compact=True, width=120)
