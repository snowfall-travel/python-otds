import datetime
from collections.abc import Mapping
from decimal import Decimal
from typing import Literal, NewType, TypeAlias, TypedDict
from typing_extensions import Required

from . import enums as e

Age = NewType("Age", int)
AgencyCode = NewType("AgencyCode", str)
AvailabilityOpen = NewType("AvailabilityOpen", int)
AvailabilityRequest = NewType("AvailabilityRequest", int)
BrandCode = NewType("BrandCode", str)
CheckInOutOffset = NewType("CheckInOutOffset", int)
CheckOutDateOffset = NewType("CheckOutDateOffset", int)
DayAllocationIndex = NewType("DayAllocationIndex", int)
DayAllocationLevel = NewType("DayAllocationLevel", int)
IataAirlineCode = NewType("IataAirlineCode", str)  # 2 char IATA or 3 char ICAO
IataAirportCode = NewType("IataAirportCode", str)  # [A-Z]{3}
Identifier = NewType("Identifier", str)  # [A-Za-z0-9\.\-_|\+]+
ISO3166Country = NewType("ISO3166Country", str)  # [A-Z]{2}
Key = NewType("Key", str)  # [A-Za-z0-9\.\-_|\+]+
LanguageText = NewType("LanguageText", str)  # Indicates localised text.
LayerLevel = NewType("LayerLevel", int)
Token = NewType("Token", str)  # [\S]{1,128}  # Usually used for Class attribute
Name = NewType("Name", str)  # [A-Za-z0-9]+
Offset = NewType("Offset", int)
OWGS84Latitude = NewType("OWGS84Latitude", float)  # -90.0 to 90.0
OWGS84Longitude = NewType("OWGS84Longitude", float)  # -180.0 to 180.0
PersonAge = NewType("PersonAge", int)
PriceItemClass = NewType("PriceItemClass", str)  # Same restriction as Token
SeparatorLeft = NewType("SeparatorLeft", str)
SeparatorRight = NewType("SeparatorRight", str)
ShortServiceAnnotation = NewType("ShortServiceAnnotation", str)  # 1-50 characters
SimpleNodeIataAirportCode = NewType("SimpleNodeIataAirportCode", str)
Size = NewType("Size", tuple[float, str | None])  # (value, unit)
SourceAttribute = NewType("SourceAttribute", str)
StringSlice = NewType("StringSlice", tuple[int, int | None])

_AbsoluteConditionAppliedBy = tuple[Literal[e.Absolute.AppliedBy], str]
_AbsoluteConditionDayBase = tuple[Literal[e.Absolute.DayBase], tuple[SourceAttribute, int | Literal[e.X.x]]]
_AbsoluteConditionPersonBase = tuple[Literal[e.Absolute.PersonBase], int | Literal[e.X.x]]
AbsoluteCondition = _AbsoluteConditionAppliedBy | _AbsoluteConditionDayBase | _AbsoluteConditionPersonBase

PercentCondition = tuple[Literal[e.Percent.ApplyTo], tuple[PriceItemClass, ...]]

AccommodationCategory = tuple[Literal[0, 1, 2, 3, 4, 5, 6], Literal[0, 5]] | tuple[Literal[7], Literal[0]]

class AgeCondition(TypedDict, total=False):
    max: int
    min: int

class BookingDateCondition(TypedDict, total=False):
    min: datetime.date
    max: datetime.date

class BookingOffsetCondition(TypedDict, total=False):
    min: int
    max: int

class DateCondition(TypedDict, total=False):
    min: datetime.date
    max: datetime.date
    dates: tuple[datetime.date, ...]

_DayImpactDate = tuple[Literal[e.DayImpact.Date], tuple[e.DayType, SourceAttribute, DateCondition]]
_DayImpactDayIndex = tuple[Literal[e.DayImpact.DayIndex], tuple[SourceAttribute, tuple[tuple[e.DayIndex, int], ...]], int | None]
_DayImpactWeekdays = tuple[Literal[e.DayImpact.Weekdays], tuple[SourceAttribute, e.DayType, tuple[e.Weekday, ...]]]
DayImpact = _DayImpactDate | _DayImpactDayIndex | _DayImpactWeekdays

class DurationCondition(TypedDict, total=False):
    durations: tuple[int, ...]
    min: datetime.timedelta
    max: datetime.timedelta
    multiples: int

_MatchElement = tuple[Literal[e.Match.Element], tuple[e.MatchElement, SourceAttribute]]
_MatchKey = tuple[Literal[e.Match.Key], tuple[SourceAttribute]]
_MatchTag = tuple[Literal[e.Match.Tag], tuple[SourceAttribute, Token]]
Match = _MatchElement | _MatchKey | _MatchTag

class OccupancyConditionPerson(TypedDict, total=False):
    min_age: PersonAge
    min_count: int

class OccupancyPerson(TypedDict, total=False):
    count: int
    max_age: Age
    min_age: Age
    max_count: int
    min_count: int

class PersonCount(TypedDict, total=False):
    filter: tuple[Literal[e.PersonFilter.Impact], tuple[SourceAttribute, Token, tuple[str, ...]]]
    min: int

class PersonIndex(TypedDict, total=False):
    filter: tuple[tuple[e.PersonIndexFilter, tuple[SourceAttribute, Token, tuple[str, ...]]], ...]
    from_: int
    indices: tuple[int, ...]
    until: int

_PersonImpactAge = tuple[Literal[e.PersonImpact.Age], tuple[SourceAttribute, AgeCondition]]
_PersonImpactIndex = tuple[Literal[e.PersonImpact.Index], tuple[SourceAttribute, PersonIndex]]
_PersonImpactGender = tuple[Literal[e.PersonImpact.Genders], tuple[SourceAttribute, tuple[e.PersonGender, ...]]]
PersonImpact = _PersonImpactAge | _PersonImpactIndex | _PersonImpactGender

_ConditionAndOr = tuple[Literal[e.Condition.And, e.Condition.Or], tuple["ConditionGroup", ...]]
_ConditionNot = tuple[Literal[e.Condition.Not], "ConditionGroup"]
_ConditionAirports = tuple[Literal[e.Condition.Airports], tuple[SourceAttribute, e.AirportType, tuple[str, ...]]]
_ConditionBookingDate = tuple[Literal[e.Condition.BookingDate], tuple[SourceAttribute, BookingDateCondition]]
_ConditionBookingDateOffset = tuple[Literal[e.Condition.BookingDateOffset], tuple[SourceAttribute, BookingOffsetCondition]]
_ConditionConditionalTags = tuple[Literal[e.Condition.ConditionalTags], tuple[SourceAttribute, Token, tuple[str, ...]]]
_ConditionDate = tuple[Literal[e.Condition.Date], tuple[e.DayType, SourceAttribute, DateCondition]]
_ConditionDayImpact = tuple[Literal[e.Condition.DayImpact], DayImpact]
_ConditionDuration = tuple[Literal[e.Condition.Duration], tuple[SourceAttribute, DurationCondition]]
_ConditionImpact = tuple[Literal[e.Condition.Impact], tuple[SourceAttribute, Token, tuple[str, ...]]]
_ConditionImply = tuple[Literal[e.Condition.Imply], tuple["ConditionGroup", "ConditionGroup"]]
_ConditionKeys = tuple[Literal[e.Condition.Keys], tuple[SourceAttribute, str, e.DayAllocation | None]]
_ConditionMatchEqual = tuple[Literal[e.Condition.MatchEqual], tuple[Match, ...]]
_ConditionPersonCount = tuple[Literal[e.Condition.PersonCount], tuple[SourceAttribute, PersonCount]]
_ConditionPersonGroup = tuple[Literal[e.Condition.PersonGroup], tuple[SourceAttribute, tuple[OccupancyConditionPerson, ...]]]
_ConditionPersonImpact = tuple[Literal[e.Condition.PersonImpact], PersonImpact]
_ConditionTags = tuple[Literal[e.Condition.Tags], tuple[SourceAttribute, Token, tuple[str, ...], StringSlice, e.EvaluationMode, e.DayAllocation]]
_ConditionWeekdays = tuple[Literal[e.Condition.Weekdays], tuple[SourceAttribute, e.DayType, tuple[e.Weekday, ...]]]
ConditionGroup: TypeAlias = _ConditionAndOr | _ConditionNot | _ConditionAirports | _ConditionBookingDate | _ConditionBookingDateOffset | _ConditionConditionalTags | _ConditionDayImpact | _ConditionDate | _ConditionDuration | _ConditionImpact | _ConditionImply | _ConditionKeys | _ConditionMatchEqual | _ConditionPersonCount | _ConditionPersonGroup | _ConditionPersonImpact | _ConditionTags | _ConditionWeekdays

_DayStateClosed = tuple[Literal[e.DayState.Closed]]
_DayStateOpen = tuple[Literal[e.DayState.Open], AvailabilityOpen | None]
DayState = _DayStateClosed | _DayStateOpen

_DefaultDayStateClosed = tuple[Literal[e.DefaultDayState.Closed]]
_DefaultDayStateOpen = tuple[Literal[e.DefaultDayState.Open], AvailabilityOpen | None]
DefaultDayState = _DefaultDayStateClosed | _DefaultDayStateOpen

class DefaultDayStateExtra(TypedDict, total=False):
    check_out: AvailabilityRequest | None

_CheckIn = _CheckOut = e.AvailabilityState | Literal[False] | None
Availability = tuple[datetime.date, datetime.date, tuple[DefaultDayState, DefaultDayStateExtra], Mapping[Key, tuple[Offset, DayState, _CheckIn, _CheckOut]]]
Availabilities = tuple[ConditionGroup | None, Mapping[Key, Availability]]

_BookingParameterDate = tuple[Literal[e.BookingParameter.Date], e.DayType, SourceAttribute, e.DateFormat]
_BookingParameterPersonAge = tuple[Literal[e.BookingParameter.PersonAge], e.AgeType, e.DateFormat]
_BookingParameterTag = tuple[Literal[e.BookingParameter.Tag], SourceAttribute, Token]
_BookingParameterValue = tuple[Literal[e.BookingParameter.Value], str]
BookingParameterParam = _BookingParameterDate | _BookingParameterPersonAge | _BookingParameterTag | _BookingParameterValue

_CombinableWhenCode = tuple[Literal[e.CombinableWhen.Code], Identifier, Identifier]
_CombinableWhenIndexMin = tuple[Literal[e.CombinableWhen.IndexMin], Identifier, int]
_CombinableWhenCond = tuple[Literal[e.CombinableWhen.Or, e.CombinableWhen.Not], tuple["CombinableWhen", ...]]
CombinableWhen = _CombinableWhenCode | _CombinableWhenIndexMin | _CombinableWhenCond

class BookingParameter(TypedDict):
    field: e.Field
    index: int
    name: Name
    params: BookingParameterParam
    sep: tuple[SeparatorLeft, SeparatorRight]

_BookingGroupBookingParameter = tuple[Literal[e.BookingGroup.Parameter], BookingParameter]
_BookingGroupCondition = tuple[Literal[e.BookingGroup.Condition], ConditionGroup]
BookingGroupCondition = _BookingGroupBookingParameter | _BookingGroupCondition
BookingGroup = tuple[e.BookingGroupArea, SourceAttribute, tuple[BookingGroupCondition, ...], e.EvaluationBase | None, int]

DayAllocationStartEnd = tuple[DayAllocationLevel, SourceAttribute, e.DayReference, e.Shift]
_DayAllocationStart = tuple[Literal[e.DayAllocationPart.Start], DayAllocationStartEnd]
_DayAllocationEnd = tuple[Literal[e.DayAllocationPart.End], DayAllocationStartEnd]
DayAllocation = _DayAllocationStart | _DayAllocationEnd

_OccupancyPerson = tuple[Literal[e.Occupancy.Person], OccupancyPerson]
_OccupancyExclude = tuple[Literal[e.Occupancy.Exclude], tuple[OccupancyPerson, ...]]
Occupancy = _OccupancyPerson | _OccupancyExclude

OptionalBookableAddonType = tuple[e.OptionalBookableAddonType, ShortServiceAnnotation]

_ParameterSetDistributorIdentificationGroup = tuple[Literal[e.ParameterSet.DistributorIdentificationGroup], e.CrsSystem, AgencyCode, BrandCode]
_ParameterSetDistributionChannel = tuple[Literal[e.ParameterSet.DistributionChannel], e.DistributionChannel]
_ParameterSetSalesChannel = tuple[Literal[e.ParameterSet.SalesChannel], e.SalesChannel]
_ParameterSetSalesMarket = tuple[Literal[e.ParameterSet.SalesMarket], ISO3166Country]
ParameterSet = _ParameterSetDistributorIdentificationGroup | _ParameterSetDistributionChannel | _ParameterSetSalesChannel | _ParameterSetSalesMarket

RuleDefinedComponent = tuple[e.Role, Name, DayAllocationLevel]
RuleOnewayFlightComponent = tuple[Name, DayAllocationIndex, DayAllocationLevel]
RuleSellingAccomComponent = tuple[Name, DayAllocationIndex]
RuleCombiComponent = tuple[e.Role, Name, DayAllocationIndex, tuple[RuleDefinedComponent, ...]]

_ComponentAccommodation = tuple[Literal[e.Component.Accommodation], tuple[RuleSellingAccomComponent, ...]]
_ComponentCombiComponent = tuple[Literal[e.Component.CombiComponent], RuleCombiComponent]
_ComponentDefinedComponent = tuple[Literal[e.Component.DefinedComponent], RuleDefinedComponent]
_ComponentOnewayFlight = tuple[Literal[e.Component.OnewayFlight], RuleOnewayFlightComponent]
Component = _ComponentAccommodation | _ComponentCombiComponent | _ComponentDefinedComponent | _ComponentOnewayFlight

_TagsDict = Mapping[Token, tuple[str, ConditionGroup | None]]
TagsDict = Mapping[Key, _TagsDict]

class Geocode(TypedDict):
    latitude: OWGS84Latitude
    longitude: OWGS84Longitude
    accuracy_km: int

class Geo(TypedDict, total=False):
    geocode: Geocode

class Address(TypedDict, total=False):
    city: LanguageText
    country: LanguageText
    fax: str
    geo: Geo
    phone: str
    street: str
    zip: str

class AccommodationInfo(TypedDict, total=False):
    giata: tuple[str, str]
    geonames: tuple[str, str]

class Baggage(TypedDict, total=False):
    pieces: int
    weight: Size

class Combinatorics(TypedDict, total=False):
    code: tuple[Identifier, str]
    index: tuple[Identifier, int]
    level: int
    when: CombinableWhen

class NeighbourComponentCorrection(TypedDict, total=False):
    check_in_offset: tuple[CheckInOutOffset, e.ComponentAttribute | None]
    check_out_offset: tuple[CheckInOutOffset, e.ComponentAttribute | None]

class Operating(TypedDict, total=False):
    carrier: IataAirlineCode
    flight_number: str

class PriceItem(TypedDict, total=False):
    absolute: tuple[Decimal, tuple[AbsoluteCondition, ...]]
    percent: tuple[Decimal, tuple[PercentCondition, ...]]
    combinatorics: Mapping[tuple[Identifier, LayerLevel], Combinatorics]
    condition: ConditionGroup

class RouteNode(TypedDict, total=False):
    airport: IataAirportCode
    date_offset: int
    time: datetime.time

class Route(TypedDict, total=False):
    arrival: RouteNode
    departure: RouteNode
    operating: Operating
    stop_overs: int

class Property(TypedDict, total=False):
    address: Address
    baggage_allowances: Mapping[e.BaggageType, Baggage]
    board_name: LanguageText
    board_type: e.BoardType
    city: tuple[LanguageText, ...]
    condition: ConditionGroup
    flight_routes: tuple[Route, ...]
    included_services: tuple[e.GeneralIncludedService, ...]
    info: AccommodationInfo
    name: LanguageText
    official_category: AccommodationCategory
    operator_category: AccommodationCategory
    optional_addons: tuple[OptionalBookableAddonType, ...]
    target_groups: tuple[e.AccommodationTargetgroup, ...]
    type: e.AccommodationType
    unit_facilities: tuple[e.UnitFacilities, ...]
    unit_name: LanguageText
    unit_types: tuple[e.UnitType, ...]

class Board(TypedDict, total=False):
    booking: tuple[BookingGroup, ...]
    price_items: Mapping[Key, Mapping[Token, tuple[PriceItem, ...]]]
    properties: Mapping[Key, tuple[Property, ...]]
    tags: TagsDict

class SellingUnit(TypedDict, total=False):
    booking: Required[tuple[BookingGroup, ...]]
    occupancy: Required[Mapping[Key, tuple[Occupancy, ...]]]
    tags: TagsDict

class Unit(TypedDict, total=False):
    properties: Mapping[Key, tuple[Property, ...]]
    selling_units: Required[Mapping[Key, SellingUnit]]
    tags: TagsDict

class SellingAccom(TypedDict, total=False):
    board: Mapping[Key, Board]
    booking: tuple[BookingGroup, ...]
    filter: Mapping[Key, ConditionGroup]
    price_items: Mapping[Key, Mapping[Token, tuple[PriceItem, ...]]]
    tags: TagsDict
    unit: Mapping[Key, Unit]

class Accommodation(TypedDict, total=False):
    airports: tuple[SimpleNodeIataAirportCode, ...]
    availabilities: Mapping[Key, Availabilities]
    properties: Mapping[Key, tuple[Property, ...]]
    selling: Required[Mapping[Key, SellingAccom]]
    tags: TagsDict

class BookingClass(TypedDict, total=False):
    availabilities: Mapping[Key, Availabilities]
    booking: tuple[BookingGroup, ...]
    occupancy: Mapping[Key, tuple[Occupancy, ...]]
    price_items: Mapping[Key, Mapping[Token, tuple[PriceItem, ...]]]
    properties: Mapping[Key, tuple[Property, ...]]
    tags: TagsDict

class Brand(TypedDict, total=False):
    booking: tuple[BookingGroup, ...]
    tags: TagsDict

class _DefineComponent(TypedDict, total=False):
    booking: tuple[BookingGroup, ...]
    components: Required[tuple[Component, ...]]
    filter: Mapping[Key, ConditionGroup]

DefineComponent = tuple[e.Role, _DefineComponent]

class Oneway(TypedDict, total=False):
    arrival: Required[SimpleNodeIataAirportCode]
    booking_class: Required[Mapping[Key, BookingClass]]
    check_out_date_offset: CheckOutDateOffset
    departure: Required[SimpleNodeIataAirportCode]
    filter: Mapping[Key, ConditionGroup]
    neighbour_component_correction: Mapping[Key, NeighbourComponentCorrection]
    price_items: Mapping[Key, Mapping[Token, tuple[PriceItem, ...]]]
    properties: Mapping[Key, tuple[Property, ...]]
    tags: TagsDict

class Flights(TypedDict, total=False):
    oneway: Mapping[Key, Oneway]

class GlobalValue(TypedDict):
    params: Mapping[Key, ParameterSet]

class Product(TypedDict, total=False):
    components: Required[tuple[Component, ...]]
    day_allocation: tuple[DayAllocation, ...]
    filters: Mapping[Key, ConditionGroup]
    tags: TagsDict

class Products(TypedDict, total=False):
    globals: Mapping[Key, GlobalValue]
    product: Mapping[Key, tuple[e.ProductType, Product]]

class PropertyGroup(TypedDict, total=False):
    info: tuple[str, str]
