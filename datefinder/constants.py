import regex as re

NUMBERS_PATTERN = r"seventh|second|fourth|eighth|nineth|first|third|fifth|sixth|tenth"
POSITIONNAL_TOKENS = r"next|last"
DIGITS_PATTERN = r"\d+"
DIGITS_SUFFIXES = r"st|th|rd|nd"
DAYS_PATTERN = "wednesday|thursday|saturday|tuesday|tirsdag|torsdag|monday|friday|sunday|mandag|onsdag|fredag|lørdag|søndag|thurs|tues|thur|tirs|tors|mon|tue|wed|thu|fri|sat|sun|man|tir|ons|tor|fre|lør|søn"
MONTHS_PATTERN = r"septiembre|september|noviembre|diciembre|september|february|november|december|november|december|january|october|febrero|octubre|februar|oktober|august|agosto|januar|august|march|april|enero|marzo|abril|junio|julio|marts|april|sept[\.\s]|june|july|mayo|juni|juli|jan[\.\s]|ene[\.\s]|feb[\.\s]|mar[\.\s]|apr[\.\s]|abr[\.\s]|may[\.\s]|maj[\.\s]|jun[\.\s]|jul[\.\s]|aug[\.\s]|ago[\.\s]|sep[^A-Za-z]|oct[\.\s]|okt[\.\s]|nov[\.\s]|dec[\.\s]|dic[\.\s]|may|maj"
TIMEZONES_PATTERN = "ACWDT|ACWST|AKTST|ALMST|ANAST|AQTST|ASHST|AZOMT|AZOST|BAKST|BEAUT|CHADT|CHAST|CHOST|CKHST|DUSST|EASST|FRUST|HOVST|IRKST|KIZST|KRAST|KUYST|MADMT|MADST|MAGST|MALST|NOVST|OMSST|ORAST|PETST|QYZST|SAKST|SHEST|SVEST|TASST|TBIST|ULAST|URAST|UYHST|VLAST|VOLST|WARST|YAKST|YEKST|YEKST|YERST|ACDT|ACST|ADDT|ADMT|AEDT|AEST|AHDT|AHST|AKDT|AKST|AKTT|ALMT|AMST|ANAT|AQTT|ARST|ASHT|AWDT|AWST|AZOT|AZST|BAKT|BDST|BEAT|BIOT|BORT|BOST|BRST|BURT|CANT|CAPT|CAST|CAWT|CDDT|CEDT|CEMT|CEST|CGST|CHDT|CHOT|CIST|CLST|COST|CVST|ChST|DACT|DAVT|DDUT|DUST|EAST|EDDT|EEDT|EEST|EGST|EHDT|FFMT|FJST|FKST|FNST|FORT|FRUT|GALT|GAMT|GBGT|GEST|GHST|GILT|HADT|HAST|HKST|HOVT|IDDT|IHST|IRDT|IRKT|IRST|ISST|JAVT|JCST|JWST|KART|KGST|KIZT|KOST|KRAT|KUYT|KWAT|LHDT|LHST|LINT|MADT|MAGT|MALT|MART|MAWT|MDDT|MDST|MEST|MIST|MOST|MUST|NCST|NDDT|NEGT|NEST|NOVT|NZDT|NZMT|NZST|OMST|ORAT|PDDT|PEST|PETT|PHOT|PHST|PKST|PLMT|PMDT|PMMT|PMST|PONT|PPMT|PYST|QYZT|ROTT|SAKT|SAMT|SAST|SDMT|SHET|SJMT|SRET|STAT|SVET|SWAT|SYOT|TAHT|TAST|TBIT|TBMT|TOST|TRST|TSAT|ULAT|URAT|UYST|UZST|VLAT|VOLT|VOST|VUST|WART|WAST|WEDT|WEMT|WEST|WGST|WITA|WSDT|WSST|YAKT|YAPT|YDDT|YEKT|YEKT|YERT|ACT|ADT|AFT|AMT|ANT|APT|ART|AST|AWT|AZT|BDT|BMT|BNT|BOT|BRT|BST|BTT|CAT|CCT|CDT|CET|CGT|CKT|CLT|CMT|COT|CPT|CST|CUT|CVT|CWT|CXT|DFT|DMT|EAT|ECT|EDT|EET|EGT|EMT|EPT|EST|EWT|FET|FJT|FKT|FMT|FNT|GET|GFT|GIT|GMT|GST|GYT|HAA|HAC|HAE|HAP|HAR|HAT|HAY|HDT|HKT|HLV|HMT|HNA|HNC|HNE|HNP|HNR|HNT|HNY|HST|ICT|IDT|IMT|IOT|IST|JDT|JMT|JST|KDT|KGT|KMT|KST|LKT|LMT|LMT|LMT|LMT|LRT|LST|MDT|MET|MHT|MIT|MMT|MOT|MPT|MSD|MSK|MSM|MST|MUT|MVT|MWT|MYT|NCT|NDT|NET|NFT|NMT|NPT|NRT|NST|NUT|NWT|PDT|PET|PGT|PHT|PKT|PMT|PNT|PPT|PST|PWT|PYT|QMT|RET|RMT|SBT|SCT|SDT|SET|SGT|SLT|SMT|SRT|SST|TFT|THA|TJT|TKT|TLT|TMT|TOT|TRT|TVT|UTC|UYT|UZT|VET|VUT|WAT|WDT|WET|WFT|WGT|WIB|WIT|WMT|WST|XJT|YDT|YPT|YST|YWT|zzz|ET|NT|PT|WT"
## explicit north american timezones that get replaced
NA_TIMEZONES_PATTERN = "pacific|eastern|mountain|central"
# na timezones are longer
ALL_TIMEZONES_PATTERN = NA_TIMEZONES_PATTERN + "|" + TIMEZONES_PATTERN

# Allows for straightforward datestamps e.g 2017, 201712, 20171223. Created with:
#  YYYYMM_PATTERN = '|'.join(['19\d\d'+'{:0>2}'.format(mon)+'|20\d\d'+'{:0>2}'.format(mon) for mon in range(1, 13)])
#  YYYYMMDD_PATTERN = '|'.join(['19\d\d'+'{:0>2}'.format(mon)+'[0123]\d|20\d\d'+'{:0>2}'.format(mon)+'[0123]\d' for mon in range(1, 13)])
YYYY_PATTERN = r"19\d\d|20\d\d"
YYYYMM_PATTERN = r"19\d\d01|20\d\d01|19\d\d02|20\d\d02|19\d\d03|20\d\d03|19\d\d04|20\d\d04|19\d\d05|20\d\d05|19\d\d06|20\d\d06|19\d\d07|20\d\d07|19\d\d08|20\d\d08|19\d\d09|20\d\d09|19\d\d10|20\d\d10|19\d\d11|20\d\d11|19\d\d12|20\d\d12"
YYYYMMDD_PATTERN = r"19\d\d01[0123]\d|20\d\d01[0123]\d|19\d\d02[0123]\d|20\d\d02[0123]\d|19\d\d03[0123]\d|20\d\d03[0123]\d|19\d\d04[0123]\d|20\d\d04[0123]\d|19\d\d05[0123]\d|20\d\d05[0123]\d|19\d\d06[0123]\d|20\d\d06[0123]\d|19\d\d07[0123]\d|20\d\d07[0123]\d|19\d\d08[0123]\d|20\d\d08[0123]\d|19\d\d09[0123]\d|20\d\d09[0123]\d|19\d\d10[0123]\d|20\d\d10[0123]\d|19\d\d11[0123]\d|20\d\d11[0123]\d|19\d\d12[0123]\d|20\d\d12[0123]\d"
YYYYMMDDHHMMSS_PATTERN = "|".join(
    [
        r"19\d\d"
        + "{:0>2}".format(mon)
        + r"[0-3]\d[0-5]\d[0-5]\d[0-5]\d|20\d\d"
        + "{:0>2}".format(mon)
        + r"[0-3]\d[0-5]\d[0-5]\d[0-5]\d"
        for mon in range(1, 13)
    ]
)
ISO8601_PATTERN = r"(?P<years>-?(\:[1-9][0-9]*)?[0-9]{4})\-(?P<months>1[0-2]|0[1-9])\-(?P<days>3[01]|0[1-9]|[12][0-9])T(?P<hours>2[0-3]|[01][0-9])\:(?P<minutes>[0-5][0-9]):(?P<seconds>[0-5][0-9])(?:[\.,]+(?P<microseconds>[0-9]+))?(?P<offset>(?:Z|[+-](?:2[0-3]|[01][0-9])\:[0-5][0-9]))?"
UNDELIMITED_STAMPS_PATTERN = "|".join(
    [YYYYMMDDHHMMSS_PATTERN, YYYYMMDD_PATTERN, YYYYMM_PATTERN, ISO8601_PATTERN]
)
DELIMITERS_PATTERN = r"[/\:\-\,\.\s\_\+\@]+"
TIME_PERIOD_PATTERN = r"a\.m\.|am|p\.m\.|pm"
## can be in date strings but not recognized by dateutils
EXTRA_TOKENS_PATTERN = r"standard|daylight|savings|through|between|during|dated|until|time|date|due|day|by|on|of|to|at"

## TODO: Get english numbers?
## http://www.rexegg.com/regex-trick-numbers-in-english.html

RELATIVE_PATTERN = "before|after|next|last|ago"
TIME_SHORTHAND_PATTERN = "noon|midnight|today|yesterday"
UNIT_PATTERN = "second|minute|hour|day|week|month|year"

## Time pattern is used independently, so specified here.
TIME_PATTERN = r"""
(?P<time>
    ## Captures in format XX:YY(:ZZ) (PM) (EST)
    (
        (?P<hours>\d{{1,2}})
        \:
        (?P<minutes>\d{{1,2}})
        (\:(?<seconds>\d{{1,2}}))?
        ([\.\,](?<microseconds>\d{{1,6}}))?
        \s*
        (?P<time_periods>{time_periods})?
        \s*
        (?P<timezones>{timezones})?
    )
    |
    ## Captures in format 11 AM (EST)
    ## Note with single digit capture requires time period
    (
        (?P<hours>\d{{1,2}})
        \s*
        (?P<time_periods>{time_periods})
        \s*
        (?P<timezones>{timezones})*
    )
)
""".format(
    time_periods=TIME_PERIOD_PATTERN, timezones=ALL_TIMEZONES_PATTERN
)

DATES_PATTERN = """
(
    ## Undelimited datestamps (treated independently)
    (?P<undelimited_stamps>{undelimited_stamps})
    |
    (
        {time}
        |
        ## Grab any four digit years
        (?P<years>{years})
        |
        ## Numbers
        (?P<numbers>{numbers})
        ## Grab any digits
        |
        (?P<digits>{digits})(?P<digits_suffixes>{digits_suffixes})?
        |
        (?P<days>{days})
        |
        (?P<months>{months})
        |
        ## Delimiters, ie Tuesday[,] July 18 or 6[/]17[/]2008
        ## as well as whitespace
        (?P<delimiters>{delimiters})
        |
        (?P<positionnal_tokens>{positionnal_tokens})
        |
        ## These tokens could be in phrases that dateutil does not yet recognize
        ## Some are US Centric
        (?P<extra_tokens>{extra_tokens})
    ## We need at least three items to match for minimal datetime parsing
    ## ie 10pm
    ){{1,1}}
)
"""

DATES_PATTERN = DATES_PATTERN.format(
    time=TIME_PATTERN,
    undelimited_stamps=UNDELIMITED_STAMPS_PATTERN,
    years=YYYY_PATTERN,
    numbers=NUMBERS_PATTERN,
    digits=DIGITS_PATTERN,
    digits_suffixes=DIGITS_SUFFIXES,
    days=DAYS_PATTERN,
    months=MONTHS_PATTERN,
    delimiters=DELIMITERS_PATTERN,
    positionnal_tokens=POSITIONNAL_TOKENS,
    extra_tokens=EXTRA_TOKENS_PATTERN,
)

ALL_GROUPS = ['time', 'years', 'numbers', 'digits', 'digits_suffixes', 'days',
              'months', 'delimiters', 'positionnal_tokens', 'extra_tokens',
              'undelimited_stamps', 'hours', 'minutes', 'seconds', 'microseconds',
              'time_periods', 'timezones']

DATE_REGEX = re.compile(
    DATES_PATTERN, re.IGNORECASE | re.MULTILINE | re.UNICODE | re.DOTALL | re.VERBOSE
)

TIME_REGEX = re.compile(
    TIME_PATTERN, re.IGNORECASE | re.MULTILINE | re.UNICODE | re.DOTALL | re.VERBOSE
)

## These tokens can be in original text but dateutil
## won't handle them without modification
REPLACEMENTS = {
    "standard": " ",
    "daylight": " ",
    "savings": " ",
    "time": " ",
    "date": " ",
    "by": " ",
    "due": " ",
    "on": " ",
    "to": " ",
    "day": " ",
}

TIMEZONE_REPLACEMENTS = {
    "pacific": "PST",
    "eastern": "EST",
    "mountain": "MST",
    "central": "CST",
}

## Characters that can be removed from ends of matched strings
STRIP_CHARS = " \n\t:-.,_"

# split ranges
RANGE_SPLIT_PATTERN = r'\Wto\W|\Wthrough\W|\W-\W'

RANGE_SPLIT_REGEX =  re.compile(RANGE_SPLIT_PATTERN,
    re.IGNORECASE | re.MULTILINE | re.UNICODE | re.DOTALL)
