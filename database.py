# ==========================================================
# IIT Bombay Academic Advisor Database
# ==========================================================

COURSES = {

    # ======================================================
    # Semester 3 Compulsory Courses
    # ======================================================

    "EC101": {
        "code": "EC101",
        "name": "Economics",
        "department": "EC",
        "credits": 6,
        "slot": ["2"],
        "duration": "FullSemester",
        "semester": 3,
        "type": "Compulsory",
        "is_minor": False,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Economics"
        ]
    },

    "EE204": {
        "code": "EE204",
        "name": "Analog Circuits",
        "department": "EE",
        "credits": 6,
        "slot": ["6"],
        "duration": "FullSemester",
        "semester": 3,
        "type": "Compulsory",
        "is_minor": False,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Core EE",
            "Analog Electronics"
        ]
    },

    "EE224": {
        "code": "EE224",
        "name": "Digital Systems",
        "department": "EE",
        "credits": 6,
        "slot": ["3"],
        "duration": "FullSemester",
        "semester": 3,
        "type": "Compulsory",
        "is_minor": False,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Core EE",
            "Digital Electronics"
        ]
    },

    "EE214": {
        "code": "EE214",
        "name": "Digital Circuits Lab",
        "department": "EE",
        "credits": 3,
        "slot": ["L3"],
        "duration": "FullSemester",
        "semester": 3,
        "type": "Compulsory",
        "is_minor": False,
        "is_elective": False,
        "is_lab": True,
        "tags": [
            "Core EE",
            "Digital Electronics"
        ]
    },

    "EE325": {
        "code": "EE325",
        "name": "Probability and Random Processes",
        "department": "EE",
        "credits": 6,
        "slot": ["4"],
        "duration": "FullSemester",
        "semester": 3,
        "type": "Compulsory",
        "is_minor": False,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Probability",
            "Mathematics",
            "Signal Processing"
        ]
    },

    "EE229": {
        "code": "EE229",
        "name": "Signal Processing - I",
        "department": "EE",
        "credits": 6,
        "slot": ["1"],
        "duration": "FullSemester",
        "semester": 3,
        "type": "Compulsory",
        "is_minor": False,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Signal Processing",
            "Core EE"
        ]
    },

    "EE240": {
        "code": "EE240",
        "name": "Power Engineering Lab",
        "department": "EE",
        "credits": 3,
        "slot": ["L2"],
        "duration": "FullSemester",
        "semester": 3,
        "type": "Compulsory",
        "is_minor": False,
        "is_elective": False,
        "is_lab": True,
        "tags": [
            "Power Systems",
            "Core EE"
        ]
    },

    # ======================================================
    # Data Science Courses
    # ======================================================

    "DS203": {
        "code": "DS203",
        "name": "Programming for Data Science",
        "department": "DS",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Artificial Intelligence",
            "Data Science",
            "Programming",
            "Machine Learning"
        ]
    },

    # ======================================================
    # Computer Science Courses
    # ======================================================

    "CS409": {
        "code": "CS409",
        "name": "Introduction to Cryptography",
        "department": "CS",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Cryptography",
            "Security",
            "Mathematics"
        ]
    },

    "CS419": {
        "code": "CS419",
        "name": "Introduction to Machine Learning",
        "department": "CS",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Artificial Intelligence",
            "Machine Learning",
            "Data Science"
        ]
    },

    # ======================================================
    # Entrepreneurship Courses
    # ======================================================

    "ENT602": {
        "code": "ENT602",
        "name": "Technology Venture Creation",
        "department": "ENT",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Availaible as both Minor and Institute Elective",
        "is_minor": True,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Entrepreneurship",
            "Startup",
            "Innovation",
            "Business"
        ]
    },

    "ENT609": {
        "code": "ENT609",
        "name": "Marketing & Finance for Entrepreneurs",
        "department": "ENT",
        "credits": 6,
        "slot": ["12"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Availaible as both Minor and Institute Elective",
        "is_minor": True,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Entrepreneurship",
            "Finance",
            "Marketing",
            "Business"
        ]
    },

    "ENT614": {
        "code": "ENT614",
        "name": "Business to Business (B2B) Sales and Marketing",
        "department": "ENT",
        "credits": 3,
        "slot": ["14"],
        "duration": "SecondHalf",
        "semester": None,
        "type": "Availaible as both Minor and Institute Elective",
        "is_minor": True,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Entrepreneurship",
            "Marketing",
            "Sales",
            "Business"
        ]
    },

    "ENT615": {
        "code": "ENT615",
        "name": "Strategy and Leadership for Entrepreneurs",
        "department": "ENT",
        "credits": 3,
        "slot": ["X"],
        "duration": "SecondHalf",
        "semester": None,
        "type": "Availaible as both Minor and Institute Elective",
        "is_minor": True,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Entrepreneurship",
            "Leadership",
            "Management",
            "Strategy"
        ]
    },

    "ENT617": {
        "code": "ENT617",
        "name": "Tech-Opportunities Identification",
        "department": "ENT",
        "credits": 3,
        "slot": ["6"],
        "duration": "SecondHalf",
        "semester": None,
        "type": "Availaible as both Minor and Institute Elective",
        "is_minor": True,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Entrepreneurship",
            "Innovation",
            "Technology",
            "Startup"
        ]
    },

    "ENT620": {
        "code": "ENT620",
        "name": "AI for Business and Entrepreneurs",
        "department": "ENT",
        "credits": 3,
        "slot": ["L3"],
        "duration": "FirstHalf",
        "semester": None,
        "type": "Availaible as both Minor and Institute Elective",
        "is_minor": True,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Artificial Intelligence",
            "Entrepreneurship",
            "Business",
            "Technology"
        ]
    },
        # ======================================================
    # Mathematics Courses
    # ======================================================

    "MA401": {
        "code": "MA401",
        "name": "Linear Algebra",
        "department": "MA",
        "credits": 8,
        "slot": ["9","7"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Mathematics",
            "Linear Algebra"
        ]
    },

    "MA403": {
        "code": "MA403",
        "name": "Real Analysis",
        "department": "MA",
        "credits": 8,
        "slot": ["5","XD"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Mathematics",
            "Real Analysis",
            "Fourier Series",
            "Basics of Calculus,Series and Introduction to Real Domain"
        ]
    },

    "MA417": {
        "code": "MA417",
        "name": "Ordinary Differential Equations",
        "department": "MA",
        "credits": 8,
        "slot": ["11","2"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Mathematics",
            "Differential Equations"
        ]
    },

    "MA419": {
        "code": "MA419",
        "name": "Basic Algebra",
        "department": "MA",
        "credits": 8,
        "slot": ["5","XD"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Mathematics",
            "Algebra"
        ]
    },

    # ======================================================
    # Management Courses
    # ======================================================

    "MG401": {
        "code": "MG401",
        "name": "Marketing Management",
        "department": "MG",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Management",
            "Marketing",
            "Business"
        ]
    },

    "MG402": {
        "code": "MG402",
        "name": "Human Resource Management",
        "department": "MG",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Management",
            "Human Resources",
            "Business"
        ]
    },

    "MG403": {
        "code": "MG403",
        "name": "Accounting and Finance",
        "department": "MG",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Finance",
            "Management",
            "Accounting"
        ]
    },

    # ======================================================
    # Physics Courses
    # ======================================================

    "PH251": {
        "code": "PH251",
        "name": "Classical Mechanics",
        "department": "PH",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Physics",
            "Mechanics"
        ]
    },

    "PH403": {
        "code": "PH403",
        "name": "Quantum Mechanics",
        "department": "PH",
        "credits": 8,
        "slot": ["5","9"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Physics",
            "Quantum Mechanics"
        ]
    },
    # ======================================================
    # Aerospace Engineering Courses
    # ======================================================

    "AE152": {
        "code": "AE152",
        "name": "Introduction to Aerospace Engineering",
        "department": "AE",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Aerospace Engineering",
            "Aircraft",
            "Aerodynamics"
        ]
    },

    # ======================================================
    # Biosciences & Bioengineering Courses
    # ======================================================

    "BB405": {
        "code": "BB405",
        "name": "Molecular Biology",
        "department": "BB",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Molecular Biology",
            "Biotechnology",
            "Biology"
        ]
    },

    "BB414": {
        "code": "BB414",
        "name": "Molecular Diagnostics",
        "department": "BB",
        "credits": 3,
        "slot": ["8"],
        "duration": "FirstHalf",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Molecular Diagnostics",
            "Biotechnology",
            "Biomedical Engineering"
        ]
    },

    "BB603": {
        "code": "BB603",
        "name": "Physiology for Engineers",
        "department": "BB",
        "credits": 6,
        "slot": ["10"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Physiology",
            "Biomedical Engineering",
            "Biology"
        ]
    },

    # ======================================================
    # Civil Engineering Courses
    # ======================================================

    "CE209": {
        "code": "CE209",
        "name": "Building Materials and Construction",
        "department": "CE",
        "credits": 6,
        "slot": ["8"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Civil Engineering",
            "Construction",
            "Building Materials"
        ]
    },

    "CE324": {
        "code": "CE324",
        "name": "Engineering Law",
        "department": "CE",
        "credits": 6,
        "slot": ["12"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Engineering Law",
            "Contracts",
            "Legal Systems"
        ]
    },

    "CE482": {
        "code": "CE482",
        "name": "Construction Management",
        "department": "CE",
        "credits": 6,
        "slot": ["14"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Construction Management",
            "Project Management",
            "Civil Engineering"
        ]
    },
    # ======================================================
    # Chemistry Courses
    # ======================================================

    "CH481": {
        "code": "CH481",
        "name": "Chemistry and Computers",
        "department": "CH",
        "credits": 4,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Chemistry",
            "Computational Chemistry",
            "Computing"
        ]
    },

    "CH521": {
        "code": "CH521",
        "name": "Interpretative Molecular Spectroscopy",
        "department": "CH",
        "credits": 6,
        "slot": ["8"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Chemistry",
            "Spectroscopy",
            "Molecular Analysis"
        ]
    },

    "CH546": {
        "code": "CH546",
        "name": "Introduction to Biomolecules",
        "department": "CH",
        "credits": 6,
        "slot": ["12"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Chemistry",
            "Biochemistry",
            "Biomolecules"
        ]
    },

    "CH547": {
        "code": "CH547",
        "name": "Organometallic Chemistry",
        "department": "CH",
        "credits": 6,
        "slot": ["9"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Chemistry",
            "Organometallic Chemistry",
            "Catalysis"
        ]
    },

    # ======================================================
    # Chemical Engineering Courses
    # ======================================================

    "CL464": {
        "code": "CL464",
        "name": "Process Safety and Risk Management",
        "department": "CL",
        "credits": 6,
        "slot": ["9"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Chemical Engineering",
            "Process Safety",
            "Risk Management"
        ]
    },

    "CL501": {
        "code": "CL501",
        "name": "Computational Methods in Catalysis",
        "department": "CL",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Chemical Engineering",
            "Catalysis",
            "Computational Methods"
        ]
    },

    # ======================================================
    # Climate Studies Courses
    # ======================================================

    "CM507": {
        "code": "CM507",
        "name": "Numerical Methods for Climate Science",
        "department": "CM",
        "credits": 6,
        "slot": ["10"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Climate Science",
            "Numerical Methods",
            "Scientific Computing"
        ]
    },
    # ======================================================
    # Economics Courses
    # ======================================================

    "EC602": {
        "code": "EC602",
        "name": "Time Series Econometrics for Economic Analysis-I",
        "department": "EC",
        "credits": 6,
        "slot": ["11"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Economics",
            "Econometrics",
            "Time Series",
            "Statistics"
        ]
    },

    "EC607": {
        "code": "EC607",
        "name": "Health Econometrics",
        "department": "EC",
        "credits": 6,
        "slot": ["12"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Economics",
            "Econometrics",
            "Health Economics"
        ]
    },

    # ======================================================
    # Electrical Engineering Department Electives
    # ======================================================

    "EE635": {
        "code": "EE635",
        "name": "Applied Linear Algebra",
        "department": "EE",
        "credits": 6,
        "slot": ["9"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Department Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Department Elective",
            "Linear Algebra",
            "Mathematics",
            "Electrical Engineering"
        ]
    },

    # ======================================================
    # Energy Science & Engineering Courses
    # ======================================================

    "EN323": {
        "code": "EN323",
        "name": "Renewable Energy Generation and Storage",
        "department": "EN",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Renewable Energy",
            "Energy Storage",
            "Energy Systems"
        ]
    },

    "EN411": {
        "code": "EN411",
        "name": "Physics for Energy Science",
        "department": "EN",
        "credits": 6,
        "slot": ["14"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Energy Science",
            "Physics",
            "Energy Systems"
        ]
    },

    "EN413": {
        "code": "EN413",
        "name": "Materials Science for Energy",
        "department": "EN",
        "credits": 6,
        "slot": ["13"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Materials Science",
            "Energy",
            "Materials"
        ]
    },

    "EN601": {
        "code": "EN601",
        "name": "Nonconventional Energy Sources",
        "department": "EN",
        "credits": 6,
        "slot": ["13"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Renewable Energy",
            "Energy Systems",
            "Energy Sources"
        ]
    },

    "EN602": {
        "code": "EN602",
        "name": "Foundation for Energy Engineering",
        "department": "EN",
        "credits": 6,
        "slot": ["12"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Energy Engineering",
            "Energy Systems",
            "Engineering"
        ]
    },

    "EN613": {
        "code": "EN613",
        "name": "Nuclear Reactor Theory",
        "department": "EN",
        "credits": 6,
        "slot": ["9"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Nuclear Engineering",
            "Nuclear Reactor",
            "Energy"
        ]
    },

    "EN624": {
        "code": "EN624",
        "name": "Conservation of Energy in Buildings",
        "department": "EN",
        "credits": 6,
        "slot": ["10"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Energy Efficiency",
            "Buildings",
            "Energy Conservation"
        ]
    },

    "EN657": {
        "code": "EN657",
        "name": "IC Engine, Alternate Fuels and Emissions",
        "department": "EN",
        "credits": 6,
        "slot": ["8"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Internal Combustion Engine",
            "Alternate Fuels",
            "Emissions"
        ]
    },

    "EN658": {
        "code": "EN658",
        "name": "Electrochemical Energy Storage",
        "department": "EN",
        "credits": 6,
        "slot": ["11"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Electrochemical Energy Storage",
            "Battery",
            "Energy Storage"
        ]
    },

    "EN665": {
        "code": "EN665",
        "name": "Power Converters for Electric Vehicle Charging",
        "department": "EN",
        "credits": 6,
        "slot": ["14"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Electric Vehicles",
            "Power Electronics",
            "EV Charging"
        ]
    },
    # ======================================================
    # Environmental Science & Engineering Courses
    # ======================================================

    "ES303": {
        "code": "ES303",
        "name": "Municipal Waste and Biomedical Waste Management",
        "department": "ES",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Minor",
        "is_minor": True,
        "is_elective": False,
        "is_lab": False,
        "tags": [
            "Waste Management",
            "Biomedical Waste",
            "Environmental Engineering"
        ]
    },

    "ES601": {
        "code": "ES601",
        "name": "Environmental Health and Safety",
        "department": "ES",
        "credits": 6,
        "slot": ["12"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Environmental Engineering",
            "Health and Safety",
            "Industrial Safety"
        ]
    },

    "ES630": {
        "code": "ES630",
        "name": "Environmental Nanotechnology",
        "department": "ES",
        "credits": 6,
        "slot": ["9"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Environmental Engineering",
            "Nanotechnology",
            "Nanomaterials"
        ]
    },

    "ES655": {
        "code": "ES655",
        "name": "Environmental Management",
        "department": "ES",
        "credits": 6,
        "slot": ["8"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Environmental Management",
            "Sustainability",
            "Environmental Engineering"
        ]
    },

    # ======================================================
    # Humanities & Social Sciences Courses
    # ======================================================

    "HS449": {
        "code": "HS449",
        "name": "Capitalism: Theories, Histories, Varieties",
        "department": "HS",
        "credits": 6,
        "slot": ["12"],
        "duration": "FullSemester",
        "semester": None,
        "type": "HASMED Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "HASMED Elective",
            "Capitalism",
            "Economics",
            "Political Economy",
            "History"
        ]
    },

    "HS459": {
        "code": "HS459",
        "name": "Cognitive and Psychological Testing: Labs to Life",
        "department": "HS",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Available as Minor and HASMED Elective",
        "is_minor": True,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "HASMED Elective",
            "Psychology",
            "Cognitive Science",
            "Psychological Testing"
        ]
    },
"PS632": {
    "code": "PS632",
    "name": "Contemporary Issues in Data Policy and Management",
    "department": "PS",
    "credits": 6,
    "slot": ["8"],
    "duration": "FullSemester",
    "semester": None,
    "type": "Institute Elective",
    "is_minor": False,
    "is_elective": True,
    "is_lab": False,
    "tags": [
        "Institute Elective",
        "Data Policy",
        "Data Management",
        "Public Policy"
    ]
},

"PS649": {
    "code": "PS649",
    "name": "Making Documentaries for Policy Change",
    "department": "PS",
    "credits": 3,
    "slot": ["12"],
    "duration": "SecondHalf",
    "semester": None,
    "type": "Institute Elective",
    "is_minor": False,
    "is_elective": True,
    "is_lab": False,
    "tags": [
        "Institute Elective",
        "Public Policy",
        "Documentary",
        "Media",
        "Policy Communication"
    ]
},

"PS661": {
    "code": "PS661",
    "name": "Data Science for Policy Studies",
    "department": "PS",
    "credits": 6,
    "slot": ["10"],
    "duration": "FullSemester",
    "semester": None,
    "type": "Institute Elective",
    "is_minor": False,
    "is_elective": True,
    "is_lab": False,
    "tags": [
        "Institute Elective",
        "Data Science",
        "Public Policy",
        "Data Analytics"
    ]
},

"TD603": {
    "code": "TD603",
    "name": "Water Resources Management",
    "department": "TD",
    "credits": 6,
    "slot": ["9"],
    "duration": "FullSemester",
    "semester": None,
    "type": "Institute Elective",
    "is_minor": False,
    "is_elective": True,
    "is_lab": False,
    "tags": [
        "Institute Elective",
        "Water Resources",
        "Environmental Engineering",
        "Sustainability"
    ]
},

"TD638": {
    "code": "TD638",
    "name": "Development Perspectives: Ideas, Approaches, and Theories",
    "department": "TD",
    "credits": 6,
    "slot": ["5"],
    "duration": "FullSemester",
    "semester": None,
    "type": "Minor",
    "is_minor": True,
    "is_elective": False,
    "is_lab": False,
    "tags": [
        "Development Economics",
        "Public Policy",
        "Sustainable Development"
    ]
},
    # ======================================================
    # Mechanical Engineering Courses
    # ======================================================

    "ME6110": {
        "code": "ME6110",
        "name": "Nanomanufacturing Processes",
        "department": "ME",
        "credits": 6,
        "slot": ["11"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Institute Elective",
            "Nanomanufacturing",
            "Manufacturing",
            "Nanotechnology",
            "Materials Science"
        ]
    },

    # ======================================================
    # Metallurgical Engineering & Materials Science Courses
    # ======================================================

    "MM407": {
        "code": "MM407",
        "name": "Iron and Steelmaking",
        "department": "MM",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Institute Elective",
            "Iron and Steel",
            "Metallurgy",
            "Materials Science"
        ]
    },

    "MM409": {
        "code": "MM409",
        "name": "Colloidal and Interfacial Science",
        "department": "MM",
        "credits": 6,
        "slot": ["11"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Institute Elective",
            "Colloids",
            "Interfacial Science",
            "Materials Science"
        ]
    },

    "MM474": {
        "code": "MM474",
        "name": "Science and Technology of Thin Films",
        "department": "MM",
        "credits": 6,
        "slot": ["12"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Institute Elective",
            "Thin Films",
            "Materials Science",
            "Nanotechnology"
        ]
    },

    "MM477": {
        "code": "MM477",
        "name": "Ceramic Processing Techniques",
        "department": "MM",
        "credits": 6,
        "slot": ["9"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Institute Elective",
        "is_minor": False,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Institute Elective",
            "Ceramics",
            "Ceramic Processing",
            "Materials Engineering"
        ]
    },

    # ======================================================
    # Systems and Control Courses
    # ======================================================

    "SC625": {
        "code": "SC625",
        "name": "Systems Theory",
        "department": "SC",
        "credits": 6,
        "slot": ["9"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Available as Minor and Institute Elective",
        "is_minor": True,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Institute Elective",
            "Systems Theory",
            "Control Systems",
            "Linear Systems"
        ]
    },

    "SC639": {
        "code": "SC639",
        "name": "Mathematical Structures for Control",
        "department": "SC",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Available as Minor and Institute Elective",
        "is_minor": True,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Institute Elective",
            "Control Systems",
            "Mathematics",
            "Linear Systems"
        ]
    },

    "SC650": {
        "code": "SC650",
        "name": "High Energy Physics and Systems",
        "department": "SC",
        "credits": 6,
        "slot": ["5"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Available as Minor and Institute Elective",
        "is_minor": True,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Institute Elective",
            "High Energy Physics",
            "Systems",
            "Physics"
        ]
    },

    "SC654": {
        "code": "SC654",
        "name": "Social Learning and Herding",
        "department": "SC",
        "credits": 6,
        "slot": ["10"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Available as Minor and Institute Elective",
        "is_minor": True,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Institute Elective",
            "Social Learning",
            "Decision Making",
            "Game Theory"
        ]
    },

    "SC655": {
        "code": "SC655",
        "name": "Random Processes in Learning and Control",
        "department": "SC",
        "credits": 6,
        "slot": ["6"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Available as Minor and Institute Elective",
        "is_minor": True,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Institute Elective",
            "Random Processes",
            "Machine Learning",
            "Control Systems"
        ]
    },

    "SC658": {
        "code": "SC658",
        "name": "Modeling for Aero-Mechanical Systems (MAMS)",
        "department": "SC",
        "credits": 6,
        "slot": ["12"],
        "duration": "FullSemester",
        "semester": None,
        "type": "Available as Minor and Institute Elective",
        "is_minor": True,
        "is_elective": True,
        "is_lab": False,
        "tags": [
            "Institute Elective",
            "Modeling",
            "Mechanical Systems",
            "Aerospace"
        ]
    },
}

# ==========================================================
# Semester 3 Curriculum
# ==========================================================

SEMESTER_3 = [
    "EC101",
    "EE204",
    "EE224",
    "EE214",
    "EE325",
    "EE229",
    "EE240"
]


# ==========================================================
# Helper Functions
# ==========================================================

def get_course(course_code):
    return COURSES.get(course_code)


def get_compulsory_courses():
    return [COURSES[code] for code in SEMESTER_3]


def get_all_courses():
    return list(COURSES.values())


def get_courses_by_department(department):
    return [
        course
        for course in COURSES.values()
        if course["department"] == department
    ]


def get_courses_by_interest(interests):

    recommended = []

    for course in COURSES.values():

        if any(
            tag in course["tags"]
            for tag in interests
        ):
            recommended.append(course)

    return recommended


def get_courses_by_slot(slot):

    return [
        course
        for course in COURSES.values()
        if slot in course["slot"]
    ]


def get_minor_courses():

    return [
        course
        for course in COURSES.values()
        if course["is_minor"]
    ]


def get_elective_courses():

    return [
        course
        for course in COURSES.values()
        if course["is_elective"]
    ]
