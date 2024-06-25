from enum import Enum

class X(Enum):
    x = "x"

class Absolute(Enum):
    AppliedBy = "AppliedBy"
    DayBase = "DayBase"
    PersonBase = "PersonBase"

class Percent(Enum):
    ApplyTo = "ApplyTo"

class AccommodationTargetgroup(Enum):
    GourmetTravellers = "GourmetTravellers"
    Singles = "Singles"
    LuxuryTravellers = "LuxuryTravellers"
    Families = "Families"
    SeniorTravellers = "SeniorTravellers"
    RomanticCouples = "RomanticCouples"
    YoungPeople = "YoungPeople"
    AdultsOnly = "AdultsOnly"
    Homosexuals = "Homosexuals"
    AccomodationForCityTravellers = "AccomodationForCityTravellers"
    AccomodationForCulturalTravellers = "AccomodationForCulturalTravellers"
    AccomodationForNatureTravellers = "AccomodationForNatureTravellers"
    WellnessTravellers = "WellnessTravellers"
    SportTravellers = "SportTravellers"
    ShortstayTravellers = "ShortstayTravellers"
    DogOwner = "DogOwner"
    HoneyMooner = "HoneyMooner"
    Backpacker = "Backpacker"
    BusinessTravellers = "BusinessTravellers"
    ClubTourists = "ClubTourists"
    CruiseTravellers = "CruiseTravellers"
    GolfTourists = "GolfTourists"
    GroupTourists = "GroupTourists"
    LongTermTourists = "LongTermTourists"
    Cyclists = "Cyclists"
    Motorbiker = "Motorbiker"
    RoundtripTravellers = "RoundtripTravellers"
    SingleWithChild = "SingleWithChild"
    WheelchairUsers = "WheelchairUsers"
    BeachTravellers = "BeachTravellers"
    PartyTourists = "PartyTourists"

class AccommodationType(Enum):
    Hotel = "Hotel"
    Club = "Club"
    ApartmentHotel = "ApartmentHotel"
    HolidayPark = "HolidayPark"
    Villa = "Villa"
    HolidayFlat = "HolidayFlat"
    CaravanSite = "CaravanSite"
    Other = "Other"
    BungalowResort = "BungalowResort"
    Family = "Family"
    DetachedHouse = "DetachedHouse"
    RowHouse = "RowHouse"
    HolidayHome = "HolidayHome"
    ElegantAccommodationStyle = "ElegantAccommodationStyle"
    BoutiqueAccommodationStyle = "BoutiqueAccommodationStyle"
    DesignAccommodationStyle = "DesignAccommodationStyle"
    HistoricAccommodationStyle = "HistoricAccommodationStyle"
    RuralAccommodationStyle = "RuralAccommodationStyle"
    PalaceHotelStyle = "PalaceHotelStyle"

class AgeType(Enum):
    DateOfBirth = "DateOfBirth"
    TravelAge = "TravelAge"
    BookingAge = "BookingAge"

class AirportType(Enum):
    Arrival = "Arrival"
    Catchment = "Catchment"
    Departure = "Departure"

class AvailabilityState(Enum):
    Open = "Open"
    Closed = "Closed"
    Request = "Request"
    StopSales = "StopSales"
    Blacklisted = "Blacklisted"

class BaggageType(Enum):
    Cabin = "Cabin"
    Checked = "Checked"

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

class BookingParameter(Enum):
    Date = "Date"
    PersonAge = "PersonAge"
    Tag = "Tag"
    Value = "Value"

class CombinableWhen(Enum):
    Code = "CombinationCode"
    IndexMin = "IndexMin"
    Not = "Not"
    Or = "Or"

class Component(Enum):
    Accommodation = "Accommodation"
    CombiComponent = "CombiComponent"
    DefinedComponent = "DefinedComponent"
    OnewayFlight = "OnewayFlight"

class ComponentAttribute(Enum):
    ThisComponent = "ThisComponent"
    Accommodation = "Accommodation"
    OnewayFlight = "OnewayFlight"
    ReturnFlight = "ReturnFlight"
    Flight = "Flight"
    Addon = "Addon"

class Condition(Enum):
    And = "And"
    Or = "Or"
    Not = "Not"
    Airports = "Airports"
    BookingDate = "BookingDate"
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
    PersonGroup = "PersonGroup"
    PersonImpact = "PersonImpact"
    Tags = "Tags"
    Weekdays = "Weekdays"

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

class DayAllocationPart(Enum):
    Start = "Start"
    End = "End"

class DayImpact(Enum):
    Date = "Date"
    DayIndex = "DayIndex"
    Weekdays = "Weekdays"

class DayIndex(Enum):
    From = "From"
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
    Request = "Request"

class DefaultDayState(Enum):
    Closed = "Closed"
    Open = "Open"
    Request = "Request"

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

class EvaluationMode(Enum):
    Any = "Any"
    All = "All"

class Field(Enum):
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
    Key = "Key"
    Tag = "Tag"

class MatchElement(Enum):
    CatchmentAirport = "CatchmentAirport"
    DepartureAirport = "DepartureAirport"
    ArrivalAirport = "ArrivalAirport"

class Occupancy(Enum):
    Exclude = "Exclude"
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

class PersonIndexFilter(Enum):
    Tags = "Tags"

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

class Weekday(Enum):
    Mon = "Mon"
    Tue = "Tue"
    Wed = "Wed"
    Thu = "Thu"
    Fri = "Fri"
    Sat = "Sat"
    Sun = "Sun"
