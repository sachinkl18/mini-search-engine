"""
config.py
---------
Central settings for the search engine.
More seed URLs = more pages crawled = better search results.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

DB_PATH = os.path.join(DATA_DIR, "pages.db")
INDEX_PATH = os.path.join(DATA_DIR, "index.json")

SEED_URLS = [

    # --- MAJOR TECH COMPANIES ---
    "https://en.wikipedia.org/wiki/Google",
    "https://en.wikipedia.org/wiki/Amazon_(company)",
    "https://en.wikipedia.org/wiki/Apple_Inc.",
    "https://en.wikipedia.org/wiki/Microsoft",
    "https://en.wikipedia.org/wiki/Meta_Platforms",
    "https://en.wikipedia.org/wiki/Netflix",
    "https://en.wikipedia.org/wiki/Tesla,_Inc.",
    "https://en.wikipedia.org/wiki/Twitter",
    "https://en.wikipedia.org/wiki/Instagram",
    "https://en.wikipedia.org/wiki/YouTube",
    "https://en.wikipedia.org/wiki/WhatsApp",
    "https://en.wikipedia.org/wiki/Uber",
    "https://en.wikipedia.org/wiki/Airbnb",
    "https://en.wikipedia.org/wiki/Spotify",
    "https://en.wikipedia.org/wiki/Snapchat",
    "https://en.wikipedia.org/wiki/LinkedIn",
    "https://en.wikipedia.org/wiki/Pinterest",
    "https://en.wikipedia.org/wiki/TikTok",
    "https://en.wikipedia.org/wiki/Reddit",
    "https://en.wikipedia.org/wiki/Zoom_Video_Communications",
    "https://en.wikipedia.org/wiki/Slack_(software)",
    "https://en.wikipedia.org/wiki/Dropbox",
    "https://en.wikipedia.org/wiki/Shopify",
    "https://en.wikipedia.org/wiki/PayPal",
    "https://en.wikipedia.org/wiki/Nvidia",
    "https://en.wikipedia.org/wiki/Intel",
    "https://en.wikipedia.org/wiki/Samsung",
    "https://en.wikipedia.org/wiki/Sony",
    "https://en.wikipedia.org/wiki/IBM",
    "https://en.wikipedia.org/wiki/Oracle_Corporation",

    # --- INDIA COMPANIES & STARTUPS ---
    "https://en.wikipedia.org/wiki/Flipkart",
    "https://en.wikipedia.org/wiki/Tata_Group",
    "https://en.wikipedia.org/wiki/Infosys",
    "https://en.wikipedia.org/wiki/Wipro",
    "https://en.wikipedia.org/wiki/Reliance_Industries",
    "https://en.wikipedia.org/wiki/HDFC_Bank",
    "https://en.wikipedia.org/wiki/Paytm",
    "https://en.wikipedia.org/wiki/Ola_Cabs",
    "https://en.wikipedia.org/wiki/Zomato",
    "https://en.wikipedia.org/wiki/Swiggy",
    "https://en.wikipedia.org/wiki/BYJU%27S",
    "https://en.wikipedia.org/wiki/Razorpay",
    "https://en.wikipedia.org/wiki/MakeMyTrip",
    "https://en.wikipedia.org/wiki/Nykaa",
    "https://en.wikipedia.org/wiki/Dream11",
    "https://en.wikipedia.org/wiki/PhonePe",
    "https://en.wikipedia.org/wiki/Zerodha",
    "https://en.wikipedia.org/wiki/ISRO",
    "https://en.wikipedia.org/wiki/Air_India",
    "https://en.wikipedia.org/wiki/State_Bank_of_India",

    # --- INDIA CITIES & PLACES ---
    "https://en.wikipedia.org/wiki/India",
    "https://en.wikipedia.org/wiki/Mumbai",
    "https://en.wikipedia.org/wiki/Delhi",
    "https://en.wikipedia.org/wiki/Bangalore",
    "https://en.wikipedia.org/wiki/Chennai",
    "https://en.wikipedia.org/wiki/Hyderabad",
    "https://en.wikipedia.org/wiki/Kolkata",
    "https://en.wikipedia.org/wiki/Pune",
    "https://en.wikipedia.org/wiki/Ahmedabad",
    "https://en.wikipedia.org/wiki/Jaipur",
    "https://en.wikipedia.org/wiki/Goa",
    "https://en.wikipedia.org/wiki/Kerala",
    "https://en.wikipedia.org/wiki/Tamil_Nadu",
    "https://en.wikipedia.org/wiki/Uttar_Pradesh",
    "https://en.wikipedia.org/wiki/Chikmagalur",
    "https://en.wikipedia.org/wiki/Mysore",
    "https://en.wikipedia.org/wiki/Taj_Mahal",
    "https://en.wikipedia.org/wiki/Himalaya",

    # --- FAMOUS PEOPLE ---
    "https://en.wikipedia.org/wiki/Elon_Musk",
    "https://en.wikipedia.org/wiki/Bill_Gates",
    "https://en.wikipedia.org/wiki/Steve_Jobs",
    "https://en.wikipedia.org/wiki/Jeff_Bezos",
    "https://en.wikipedia.org/wiki/Mark_Zuckerberg",
    "https://en.wikipedia.org/wiki/Sundar_Pichai",
    "https://en.wikipedia.org/wiki/Satya_Nadella",
    "https://en.wikipedia.org/wiki/Narendra_Modi",
    "https://en.wikipedia.org/wiki/Ratan_Tata",
    "https://en.wikipedia.org/wiki/Mukesh_Ambani",
    "https://en.wikipedia.org/wiki/Sachin_Tendulkar",
    "https://en.wikipedia.org/wiki/Virat_Kohli",
    "https://en.wikipedia.org/wiki/MS_Dhoni",
    "https://en.wikipedia.org/wiki/Rohit_Sharma",
    "https://en.wikipedia.org/wiki/Cristiano_Ronaldo",
    "https://en.wikipedia.org/wiki/Lionel_Messi",
    "https://en.wikipedia.org/wiki/Albert_Einstein",
    "https://en.wikipedia.org/wiki/Isaac_Newton",
    "https://en.wikipedia.org/wiki/Stephen_Hawking",
    "https://en.wikipedia.org/wiki/Mahatma_Gandhi",
    "https://en.wikipedia.org/wiki/APJ_Abdul_Kalam",
    "https://en.wikipedia.org/wiki/Nikola_Tesla",
    "https://en.wikipedia.org/wiki/Barack_Obama",
    "https://en.wikipedia.org/wiki/Donald_Trump",
    "https://en.wikipedia.org/wiki/Taylor_Swift",
    "https://en.wikipedia.org/wiki/Beyonc%C3%A9",
    "https://en.wikipedia.org/wiki/Shah_Rukh_Khan",
    "https://en.wikipedia.org/wiki/Amitabh_Bachchan",
    "https://en.wikipedia.org/wiki/Priyanka_Chopra",
    "https://en.wikipedia.org/wiki/Deepika_Padukone",

    # --- ARTIFICIAL INTELLIGENCE ---
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://en.wikipedia.org/wiki/Deep_learning",
    "https://en.wikipedia.org/wiki/ChatGPT",
    "https://en.wikipedia.org/wiki/OpenAI",
    "https://en.wikipedia.org/wiki/Large_language_model",
    "https://en.wikipedia.org/wiki/Neural_network",
    "https://en.wikipedia.org/wiki/Natural_language_processing",
    "https://en.wikipedia.org/wiki/Computer_vision",
    "https://en.wikipedia.org/wiki/Robotics",

    # --- PROGRAMMING & TECHNOLOGY ---
    "https://en.wikipedia.org/wiki/Python_(programming_language)",
    "https://en.wikipedia.org/wiki/JavaScript",
    "https://en.wikipedia.org/wiki/Java_(programming_language)",
    "https://en.wikipedia.org/wiki/C%2B%2B",
    "https://en.wikipedia.org/wiki/Rust_(programming_language)",
    "https://en.wikipedia.org/wiki/React_(JavaScript_library)",
    "https://en.wikipedia.org/wiki/Node.js",
    "https://en.wikipedia.org/wiki/Linux",
    "https://en.wikipedia.org/wiki/Android_(operating_system)",
    "https://en.wikipedia.org/wiki/IOS",
    "https://en.wikipedia.org/wiki/Cloud_computing",
    "https://en.wikipedia.org/wiki/Blockchain",
    "https://en.wikipedia.org/wiki/Internet_of_things",
    "https://en.wikipedia.org/wiki/Cybersecurity",
    "https://en.wikipedia.org/wiki/GitHub",
    "https://en.wikipedia.org/wiki/Docker_(software)",
    "https://en.wikipedia.org/wiki/Kubernetes",
    "https://en.wikipedia.org/wiki/Web_browser",
    "https://en.wikipedia.org/wiki/Internet",
    "https://en.wikipedia.org/wiki/5G",
    "https://en.wikipedia.org/wiki/Smartphone",
    "https://en.wikipedia.org/wiki/Laptop",
    "https://en.wikipedia.org/wiki/Semiconductor",

    # --- CRYPTO & FINANCE ---
    "https://en.wikipedia.org/wiki/Bitcoin",
    "https://en.wikipedia.org/wiki/Ethereum",
    "https://en.wikipedia.org/wiki/Cryptocurrency",
    "https://en.wikipedia.org/wiki/Stock_market",
    "https://en.wikipedia.org/wiki/Bombay_Stock_Exchange",
    "https://en.wikipedia.org/wiki/National_Stock_Exchange_of_India",
    "https://en.wikipedia.org/wiki/Gold",
    "https://en.wikipedia.org/wiki/Inflation",
    "https://en.wikipedia.org/wiki/Gross_domestic_product",
    "https://en.wikipedia.org/wiki/Reserve_Bank_of_India",
    "https://en.wikipedia.org/wiki/Income_tax",
    "https://en.wikipedia.org/wiki/Mutual_fund",

    # --- SPORTS ---
    "https://en.wikipedia.org/wiki/Cricket",
    "https://en.wikipedia.org/wiki/Indian_Premier_League",
    "https://en.wikipedia.org/wiki/Football",
    "https://en.wikipedia.org/wiki/FIFA_World_Cup",
    "https://en.wikipedia.org/wiki/Olympics",
    "https://en.wikipedia.org/wiki/Tennis",
    "https://en.wikipedia.org/wiki/Basketball",
    "https://en.wikipedia.org/wiki/Formula_One",
    "https://en.wikipedia.org/wiki/Chess",
    "https://en.wikipedia.org/wiki/Kabaddi",
    "https://en.wikipedia.org/wiki/Badminton",
    "https://en.wikipedia.org/wiki/Hockey",
    "https://en.wikipedia.org/wiki/WWE",

    # --- MOVIES & ENTERTAINMENT ---
    "https://en.wikipedia.org/wiki/Bollywood",
    "https://en.wikipedia.org/wiki/Hollywood",
    "https://en.wikipedia.org/wiki/Academy_Awards",
    "https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe",
    "https://en.wikipedia.org/wiki/Star_Wars",
    "https://en.wikipedia.org/wiki/The_Dark_Knight",
    "https://en.wikipedia.org/wiki/Avengers:_Endgame",
    "https://en.wikipedia.org/wiki/RRR_(film)",
    "https://en.wikipedia.org/wiki/Baahubali:_The_Beginning",
    "https://en.wikipedia.org/wiki/KGF:_Chapter_1",
    "https://en.wikipedia.org/wiki/3_Idiots",
    "https://en.wikipedia.org/wiki/Dilwale_Dulhania_Le_Jayenge",
    "https://en.wikipedia.org/wiki/Video_game",
    "https://en.wikipedia.org/wiki/PlayStation",
    "https://en.wikipedia.org/wiki/Xbox",

    # --- SCIENCE ---
    "https://en.wikipedia.org/wiki/Space_exploration",
    "https://en.wikipedia.org/wiki/NASA",
    "https://en.wikipedia.org/wiki/SpaceX",
    "https://en.wikipedia.org/wiki/Black_hole",
    "https://en.wikipedia.org/wiki/Solar_System",
    "https://en.wikipedia.org/wiki/Mars",
    "https://en.wikipedia.org/wiki/Moon",
    "https://en.wikipedia.org/wiki/DNA",
    "https://en.wikipedia.org/wiki/Evolution",
    "https://en.wikipedia.org/wiki/Climate_change",
    "https://en.wikipedia.org/wiki/Renewable_energy",
    "https://en.wikipedia.org/wiki/Solar_energy",
    "https://en.wikipedia.org/wiki/Electric_vehicle",
    "https://en.wikipedia.org/wiki/Vaccine",
    "https://en.wikipedia.org/wiki/COVID-19_pandemic",
    "https://en.wikipedia.org/wiki/Cancer",
    "https://en.wikipedia.org/wiki/Diabetes",

    # --- HISTORY ---
    "https://en.wikipedia.org/wiki/World_War_II",
    "https://en.wikipedia.org/wiki/World_War_I",
    "https://en.wikipedia.org/wiki/Indian_independence_movement",
    "https://en.wikipedia.org/wiki/British_Raj",
    "https://en.wikipedia.org/wiki/Mughal_Empire",
    "https://en.wikipedia.org/wiki/Roman_Empire",
    "https://en.wikipedia.org/wiki/Cold_War",
    "https://en.wikipedia.org/wiki/French_Revolution",
    "https://en.wikipedia.org/wiki/Renaissance",

    # --- FOOD ---
    "https://en.wikipedia.org/wiki/Pizza",
    "https://en.wikipedia.org/wiki/Biryani",
    "https://en.wikipedia.org/wiki/Sushi",
    "https://en.wikipedia.org/wiki/Coffee",
    "https://en.wikipedia.org/wiki/Tea",
    "https://en.wikipedia.org/wiki/Chocolate",
    "https://en.wikipedia.org/wiki/Vegetarianism",
    "https://en.wikipedia.org/wiki/Indian_cuisine",

    # --- HEALTH & FITNESS ---
    "https://en.wikipedia.org/wiki/Yoga",
    "https://en.wikipedia.org/wiki/Meditation",
    "https://en.wikipedia.org/wiki/Exercise",
    "https://en.wikipedia.org/wiki/Mental_health",
    "https://en.wikipedia.org/wiki/Nutrition",
    "https://en.wikipedia.org/wiki/Sleep",

    # --- WORLD COUNTRIES ---
    "https://en.wikipedia.org/wiki/United_States",
    "https://en.wikipedia.org/wiki/China",
    "https://en.wikipedia.org/wiki/United_Kingdom",
    "https://en.wikipedia.org/wiki/Japan",
    "https://en.wikipedia.org/wiki/Germany",
    "https://en.wikipedia.org/wiki/Australia",
    "https://en.wikipedia.org/wiki/Canada",
    "https://en.wikipedia.org/wiki/Russia",
    "https://en.wikipedia.org/wiki/Brazil",
    "https://en.wikipedia.org/wiki/South_Africa",
    "https://en.wikipedia.org/wiki/Pakistan",
    "https://en.wikipedia.org/wiki/Bangladesh",
    "https://en.wikipedia.org/wiki/Sri_Lanka",
    "https://en.wikipedia.org/wiki/Nepal",
    "https://en.wikipedia.org/wiki/Singapore",
    "https://en.wikipedia.org/wiki/Dubai",
]

ALLOWED_DOMAIN = "en.wikipedia.org"

# Crawl up to 500 pages (each seed + its links)
MAX_PAGES = 500

MAX_DEPTH = 1

CRAWL_DELAY_SECONDS = 0.5

HEADERS = {
    "User-Agent": "MiniSearchEngineBot/1.0"
}
