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
