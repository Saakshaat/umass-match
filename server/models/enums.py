import enum


class UMassResidence(enum.Enum):
    # Central Halls
    baker = 'baker'
    brett = 'brett'
    brooks = 'brooks'
    butterfield = 'butterfield'
    chadbourne = 'chadbourne'
    gormon = 'gormon'
    greenough = 'greenough'
    van_meter = 'van_meter'
    wheeler = 'wheeler'

    # CHC Halls
    birch = 'birch'
    elm = 'elm'
    linden = 'linden'
    maple = 'maple'
    oak = 'oak'
    sycamore = 'sycamore'

    # North Apts
    north_apt_a = 'north_apt_a'
    north_apt_b = 'north_apt_b'
    north_apt_c = 'north_apt_c'
    north_apt_d = 'north_apt_d'

    # Northeast Halls
    crabtree = 'crabtree'
    dwight = 'dwight'
    hamlin = 'hamlin'
    johnson = 'johnson'
    knowlton = 'knowlton'
    leach = 'leach'
    lewis = 'lewis'
    mary_lyon = 'mary_lyon'
    thatcher = 'thatcher'

    # OHill Halls
    dickinson = 'dickinson'
    field = 'field'
    grayson = 'grayson'
    webster = 'webster'

    # Southwest Halls
    cance = 'cance'
    coolidge = 'coolidge'
    crampton = 'crampton'
    emerson = 'emerson'
    james = 'james'
    john_adams = 'john_adams'
    john_quincy_adams = 'john_quincy_adams'
    kennedy = 'kennedy'
    mackimmie = 'mackimmie'
    melville = 'melville'
    moore = 'moore'
    patterson = 'patterson'
    pierpont = 'pierpont'
    prince = 'prince'
    thoreau = 'thoreau'
    washington = 'washington'

    # Slyvan Halls
    brown = 'brown'
    cashin = 'cashin'
    mcnamara = 'mcnamara'

    # Misc
    unknown = 'unknown'

    def __str__(self):
        return self.value


class Club(enum.Enum):
    # CICS clubs
    acm = 'acm'
    build = 'build'
    cybersec = 'cybersec'
    dsc = 'dsc'

    # Isenberg clubs
    minute_man_fund = 'minute_man_fund'

    # TODO: complete clubs list

    def __str__(self):
        return self.value


class Major(enum.Enum):
    accounting = 'accounting'
    afro_american_studies = 'afro_american_studies'
    animal_science = 'animal_science'
    anthropology = 'anthropology'
    arboriculture_and_community_forest_management = 'arboriculture_and_community_forest_management'
    architecture = 'architecture'
    art = 'art'
    art_education = 'art_education'
    art_history = 'art_history'
    astronomy = 'astronomy'
    bdic = ' bdic'
    biology = 'biology'
    biomedical_engineering = 'biomedical_engineering'
    building_and_construction_technology = 'building_and_construction_technology'
    chemical_engineering = 'chemical_engineering'
    chemistry = 'chemistry'
    chinese_language_and_lit = 'chinese_language_and_lit'
    civil_engineering = 'civil_engineering'
    classics = 'classics'
    classics_and_phil = 'classics_and_phil'
    communication = 'communication'
    communication_disorders = 'communication_disorders'
    comparative_lit = 'comparative_lit'
    computer_science = 'computer_science'
    computer_systems_engineering = 'computer_systems_engineering'
    dance = 'dance'
    earth_systems = 'earth_systems'
    economics = 'economics'
    education = 'education'
    electrical_engineering = 'electrical_engineering'
    english = 'english'
    environmental_science = 'environmental_science'
    equine_concentration = 'equine_concentration'
    finance = 'finance'
    food_science = 'food_science'
    french_and_francophone_studies = 'french_and_francophone_studies'
    geography = 'geography'
    geology = 'geology'
    german_and_scandinavian_studies = 'german_and_scandinavian_studies'
    history = 'history'
    horticulture = 'horticulture'
    hospitality = 'hospitality'
    industrial_engineering = 'industrial_engineering'
    informatics = 'informatics'
    italian_studies = 'italian_studies'
    japanese_language_and_lit = 'japanese_language_and_lit'
    journalism = 'journalism'
    judaic_studies = 'judaic_studies'
    kinesiology = 'kinesiology'
    landscape_architecture = 'landscape_architecture'
    landscape_contracting = 'landscape_contracting'
    legal_studies = 'legal_studies'
    linguistics = 'linguistics'
    linguistics_and_anthropology = 'linguistics_and_anthropology'
    linguistics_and_chinese = 'linguistics_and_chinese'
    linguistics_and_german = 'linguistics_and_german'
    linguistics_and_japanese = 'linguistics_and_japanese'
    linguistics_and_phil = 'linguistics_and_phil'
    linguistics_and_portugese = 'linguistics_and_portugese'
    linguistics_and_psycology = 'linguistics_and_psycology'
    linguistics_and_russian = 'linguistics_and_russian'
    linguistics_and_spanish = 'linguistics_and_spanish'
    management = 'management'
    marketing = 'marketing'
    mathematics = 'mathematics'
    mech_engineering = 'mech_engineering'
    microbiology = 'microbiology'
    middle_eastern_studies = 'middle_eastern_studies'
    music = 'music'
    natural_resources_conservation = 'natural_resources_conservation'
    nursing = 'nursing'
    nutrition = 'nutrition'
    operations_and_information_management = 'operations_and_information_management'
    philosophy = 'philosophy'
    physics = 'physics'
    plant_and_soil_science = 'plant_and_soil_science'
    political_science = 'political_science'
    portugese = 'portugese'
    premedical_prehealth = 'premedical_prehealth'
    pre_vertinary = 'pre_vertinary'
    psycology = 'psycology'
    public_health_sciences = 'public_health_sciences'
    resource_economics = 'resource_economics'
    russian_and_east_european_studies = 'russian_and_east_european_studies'
    science = 'science'
    social_thought_and_political_economy = 'social_thought_and_political_economy'
    sociology = 'sociology'
    spanish = 'spanish'
    sport_management = 'sport_management'
    sustainable_community_development = 'sustainable_community_development'
    sustainable_food_and_farming = 'sustainable_food_and_farming'
    theatre = 'theatre'
    turfgrass_management = 'turfgrass_management'
    turfgrass_science_and_management = 'turfgrass_science_and_management'
    university_without_walls = 'university_without_walls'
    women_gender_sexuality_studies = 'women_gender_sexuality_studies'

    def __str__(self):
        return self.value


class VideoGame(enum.Enum):
    rpg = 'rpg'
    shooter = 'shooter'
    strategy = 'strategy'
    rhythm = 'rhythm'
    puzzle = 'puzzle'
    visual = 'visual'
    novel = 'novel'
    action_adventure = 'action_adventure'
    platformer = 'platformer'
    mmo = 'mmo'

    def __str__(self):
        return self.value
