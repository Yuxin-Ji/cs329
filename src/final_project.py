from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum, auto
from emora_stdm import Macro


class State(Enum):
    S1 = auto()
    U1 = auto()
    S2a = auto()
    S2b = auto()
    S2c = auto()
    S2d = auto()
    S2e = auto()
    S2f = auto()
    S2g = auto()
    U2a = auto()
    S3a = auto()
    U3a = auto()
    CONSULT = auto()
    FINANCE = auto()
    TECH = auto()
    DK = auto()
    SAME = auto()
    U4a = auto()
    U4b = auto()
    U4c = auto()
    S5 = auto()
    S5b = auto()
    U5 = auto()
    U5b = auto()
    S6a = auto()
    S6b = auto()
    S6c = auto()
    U6 = auto()
    ERR1 = auto()
    ERR2 = auto()
    ERR3 = auto()
    ERR4 = auto()
    ERR5 = auto()
    END = auto()
    # -------------------
    S77 = auto()
    U77 = auto()
    Scon = auto()
    Sfin = auto()
    Stech = auto()
    Ua = auto()
    Swork = auto()
    Ub = auto()
    Sc = auto()
    Sclub = auto()
    Uclub = auto()
    Ud = auto()
    Sd = auto()
    Ue = auto()
    Se = auto()
    Uf = auto()
    Sf = auto()
    Sg = auto()
    Sh = auto()
    Si = auto()
    Ug = auto()
    Uh = auto()
    Ui = auto()
    Uaa = auto()
    Swwork = auto()
    Ubb = auto()
    Scc = auto()
    Scclub = auto()
    Ucclub = auto()
    Udd = auto()
    Sdd = auto()
    Uee = auto()
    See = auto()
    Uq1 = auto()
    Sy1 = auto()
    Sn1 = auto()
    Sn11 = auto()
    Sn111 = auto()
    Uq2 = auto()
    Sy2 = auto()
    Sn2 = auto()
    Uq3 = auto()
    Sy3 = auto()
    Sn3 = auto()
    Uq4 = auto()
    Sy4 = auto()
    Sn4 = auto()
    Uq5 = auto()
    Sy5 = auto()
    Sn5 = auto()
    Uq6 = auto()
    Sy6 = auto()
    Sn6 = auto()
    Uq7 = auto()
    Sy7 = auto()
    Sn7 = auto()
    Uq8 = auto()
    Sy8 = auto()
    Sn8 = auto()
    Uq9 = auto()
    Sy9 = auto()
    Sn9 = auto()
    Uq10 = auto()
    Uaa1 = auto()
    Uaa2 = auto()
    Udd1 = auto()
    Udd2 = auto()
    Udd3 = auto()
    Ua1 = auto()
    Ua2 = auto()
    Ud1 = auto()
    Ud2 = auto()
    Ud3 = auto()
    Uf1 = auto()
    Uf2 = auto()
    Uf3 = auto()
    Ug1 = auto()
    Uh1 = auto()
    Uh2 = auto()
    Uh3 = auto()
    Ui1 = auto()
    Ui2 = auto()
    Ui3 = auto()
    rr = auto()
    Sne = auto()
    Uhh = auto()
    Uhh1 = auto()
    Uhh2 = auto()
    Uhh3 = auto()
    U99 = auto()
    U01 = auto()
    U02 = auto()
    U03 = auto()
    U04 = auto()
    S01 = auto()
    ErrUa = auto()
    Sde = auto()
    Ude = auto()
    U05 = auto()
    S02 = auto()
    Sne1 = auto()
    Uj = auto()
    ERR6 = auto()

    # -----------------------
    # ================cs states start==============
    PROJECT = auto()
    DETAIL = auto()
    MACHL = auto()
    MLTOOL = auto()
    MACHL2 = auto()
    MACHLMODEL = auto()
    NLP = auto()
    NLP2 = auto()
    NLPTOOL = auto()
    NTOOL = auto()
    DB = auto()
    DB2 = auto()
    DBTOOL = auto()
    DTOOL = auto()
    SEC = auto()
    SECTOOL = auto()
    STOOL = auto()
    AI = auto()
    AIELAB = auto()
    TOOL = auto()
    WHYTOOL = auto()
    RATIONALE = auto()
    RATIONALE0 = auto()
    LANG = auto()
    SKILL = auto()
    FUTURE = auto()
    FUTURE1 = auto()
    AREA = auto()
    CORRECT = auto()
    WRONG = auto()
    ASKAREA = auto()
    PREFLANG = auto()
    UKLANG = auto()
    REASON = auto()
    REASON1 = auto()
    PROSPECT = auto()
    REPROS = auto()
    UKAREA = auto()
    ASKUK = auto()
    AREA0 = auto()
    LANGOP = auto()


# ================cs states end==============

# industry-position
ind_pos = {"ontology": {"ontindustry": ["ontconsulting", "ontfinance", "onttechnology"],
                        "ontconsulting": ["business analyst", "associate consultant", "consultant",
                                          "associate account strategist", "economic consultant", "financial consultant",
                                          "financial advisor",
                                          "compensation consultant", "human capital consultant",
                                          "human resources consultant", "advertising consultant",
                                          "marketing consultant", "sales consultant",
                                          "tax advisor", "management consultant", "strategy consultant"],
                        "ontfinance": ["investment banking", "sales and trading", "quantitative analyst",
                                       "wealth management", "asset management", "corporate banking", "capital markets",
                                       "sales manager",
                                       "credit analyst", "financial analyst", "equity research associate"],
                        "onttechnology": ["software engineer", "software developer", "swe", "sde", "data analyst",
                                          "data scientist", "full stack developer", "uiux", "ui", "ux",
                                          "ios app developer", "android app developer",
                                          "web developer", "back end", "front end", "program manager",
                                          "project manager", "product manager", "pm", "supplier development engineer",
                                          "developer advocate", "solutions architect", "supply chain manager",
                                          "technical writer", "natural language processing engineer", "nlp engineer",
                                          "language data researcher",
                                          "applied machine learning researcher", "machine learning software engineer",
                                          "nlp researcher", "nlp scientist", "ai researcher", "ai scientist", "ai engineer",
                                          "research scientist"]
                        }
           }
# industry-company
ind_comp = {"ontology": {"ontind": ["ontconsultin", "ontfinanc", "onttechnolog"],
                         "ontconsultin": ["mckinsey", "bain", "bcg", "boston consulting group", "deloitte", "pwc",
                                          "kpmg", "at kearny", "atkearny", "accenture", "ernest and young", "ey",
                                          "grant thorton", "gt"],
                         "ontfinanc": ["goldman saches", "goldman", "gs", "jp morgan", "jpm", "morgan stanley", "ms",
                                       "bank of america", "boa", "wells fargo", "citi", "citigroup", "citibank",
                                       "td bank", "capital one", "deutsche bank", "db", "barclays", "ubs",
                                       "credit suisse", "cs", "merrill lynch", "baml"],
                         "onttechnolog": ["microsoft", "apple", "google", "amazon", "ibm", "intel", "facebook",
                                          "oracle", "linkedin", "paypal", "samsung", "alphabet", "huawei", "dell", "hp",
                                          "cisco"]
                         }
            }

# dictionaries for response
pos_skill = {"business analyst": " analytical skills, communication skills, and collaboration",
             "associate consultant": "analytical skills, communication skills, and collaboration",
             "associate account strategist": "improving customer relationships, tailoring and sharing marketing strategy suggestions",
             "economic counsultant": "research skills, formualting plans to address economic problems, and processing statistical data",
             "financial consultant": "knowledge of financial topics such as taxes, investments and insurance decisions",
             "financial advisor": "knowledge of financial topics such as taxes, investments and insurance decisions",
             "compensation consultant": "knowledge of payroll procedures and labor legislation",
             "human capital consultant": "knowledge of human recources policies and procedures, and communication skills",
             "human resources consultant": "knowledge of human recources policies and procedures, and communication skills",
             "advertising consultant": "knowledge of marketing campaigns and promoting strategies",
             "marketing consultant": "knowledge of marketing campaigns and promoting strategies",
             "sales consultant": "excellent verbal and written communication skills and interpersonal skills",
             "tax advisor": "knowledge of tax management and other financial topics",
             "management consultant": "leadership, teamworking, information gathering, and solutions implementation",
             "strategy consultant": "analyzing business practices and making suggestions, defining markets and identifying trends",
             "consultant": "analytical skills, communication skills, and collaboration",

             "investment banking": "work pace, dealing with structuring and closing principals, and analytical skills",
             "ib": "work pace, dealing with structuring and closing principals, and analytical skills",
             "sales and trading": "the proficiency in modeling, writing and verbal skills, collaboration, and work pace",
             "equity research associate": "industry experience in specific fields, and strong proficiency in MS Office, Excel, Word,and other data mining tools",
             "quantitative": "problem-solving, multi-tasking, large scale data querying and analytical skills",
             "wealth management": "problem-solving skills, good understanding of the various businesses and products in the field",
             "corporate": " knowledge of accounting and finance, valuation theory, methodologies, and applications",
             "sales manager": "the proficiency in modeling, writing and verbal skills, collaboration, and work pace",
             "credit analyst": "analytical skills of financial statements, and assessment of credit requests",
             "financial analyst": "financial forecasting, reporting,operational metrics tracking, and financial data analysis",
             "capital market": "knolwdge in Fixed Income products and strong credit, financial analysis and modeling skills",

             "software": "software-developing in Java, Ruby on Rails, C++ or other programming languages, and experience with test-driven development",
             "data analyst": "strong knowledge of SQL, analytical skills, data collection and engineering",
             "data scientist": "strong knowledge of SQL, analytical skills, data collection and engineering",
             "full stack": "experience working across the full technical stack and knowledge of both frontend and backend",
             "uiux": "knowledge of wireframe tools such as Wireframe.cc and InVision and design softwares like Adobe Illustrator and Photoshop",
             "ui": "knowledge of wireframe tools such as Wireframe.cc and InVision and design softwares like Adobe Illustrator and Photoshop",
             "ux": "proficiency in visual design programs such as Adobe Photoshop, and professional writing and interpersonal skills",
             "ios": "proficiency in Objective-C, Swift, and Cocoa Touch, iOS frameworks, and experience with design patterns such as MVC, Singleton",
             "android": "knowledge of Android SDK, the open-source Android ecosystem, and familiarity with RESTful APIs",
             "web": "knowledge pf HTML, CSS, JavaScript, jQuery, and ReactJS, as well as experience in developing web applications supporting traditional web or mobile user interfaces",
             "back end": "fluency in Java, PHP, or Python, good understanding of the web development cycle, and problem solving skills",
             "front end": "HTML, CSS, JavaScript and jQuery",
             "pm": "software Development coding experience, leadership, and multi-tasking skills",
             "program manager": "software Development coding experience, leadership skills, and multi-tasking skills",
             "project manager": "software Development coding experience, leadership skills, and multi-tasking skills",
             "product manager": "software Development coding experience, leadership skills, and multi-tasking skills",
             "supplier development engineer": "familarity with supply chain, collaboration with suppliers and engineering teams",
             "supply chain manager": "developing and executing global supply chain strategies",
             "developer advocate": "familarity iwth programming language, building new product/API integrations",
             "solutions architect": "experience working in a cloud computing environment, and compiling customer requirement",
             "technical writer": "proficiency in technical writing, product documentation, and journalism",
             "research scientist": "familarity with programming language and analytical skills",
             "natural language processing engineer": "proficiency with nlp techniques and classification algorithms, model training and evaluation skills, and statistical analysis",
             "nlp engineer": "proficiency with nlp techniques and machine learning, model training and evaluation skills",
             "nlp researcher": "proficiency with nlp techniques and machine learning, model training and evaluation skills",
             "nlp scientist": "proficiency with nlp techniques and machine learning, model training and evaluation skills",
             "ai researcher": "proficiency with nlp techniques and machine learning, model training and evaluation skills",
             "ai scientist": "proficiency with nlp techniques and machine learning, model training and evaluation skills",
             "ai engineer": "proficiency with nlp techniques and machine learning, model training and evaluation skills",
             "language data researcher": "fluency in a foreign language, experience working with speech or langauge data, practical knowledge of data processing",
             "applied machine learning researcher": "deep technical skills in machinlearning, deep learning, computer vision, NLP or AI",
             "machine learning software engineer": "knowledge of extracting and processing data, proficiency in Scala, Java or C++"

             }
# city-industry dictionary
place_ind = {
    "new york": "finance and consulting",
    "ny": "finance and consulting",
    "la": "technology",
    "los angeles": "technology",
    "chicago": "technology and finance",
    "dallas": "technology and finance",
    "washington dc": "technology",
    "dc": "technology",
    "west": "technology",
    "east": "finance",
    "bay": "technology",
    "san francisco": "technology, finance and consulting",
    "sf": "technology, finance and consulting",
    "houston": "technology",
    "boston": "technology and consulting",
    "bos": "technology and consulting",
    "atl": "technology and finance",
    "atlanta": "technology and finance",
    "seattle": "technology",
    "sea": "technology",
    "san jose": "technology"
}

# industry-company
industry_company = {
    "finance": "Goldman Sachs, JP Morgan and CitiBank",
    "consulting": "McKinsey, Bain and Boston Consulting Group",
    "tech": "Facebook, LinkedIn, Apple and Google",
    "it": "Facebook, LinkedIn, Apple and Google"
}


class placeInd(Macro):
    def run(self, ngrams, vars, args):
        if 'loc' in vars:
            for key, value in place_ind.items():
                if key in vars['loc']:
                    return value


class indComp(Macro):
    def run(self, ngrams, vars, args):
        if 'industry' in vars:
            for key, value in industry_company.items():
                if key in vars['industry']:
                    return value


class posSkill(Macro):
    def run(self, ngrams, vars, args):
        if 'pos' in vars:
            for key, value in pos_skill.items():
                if key in vars['pos']:
                    return value


# ================cs dict & macro start==============
# area_tech ontology
area_tech = {"ontology":
                 {"ontmachlearning": ["machine learning", "classification", "computational intelligence",
                                      "statistical learning", "deep learning", "supervised learning",
                                      "unsupervised learning", "reinforcement learning", "transfer learning",
                                      "predictive model", "svm", "support vector machine", "vector machine",
                                      "neural network",
                                      "neural networks", "decision tree", "decision process", "random forests",
                                      "regression", "clustering", "cluster", "dimensionality reduction",
                                      "ensemble methods", "word embeddings", "neural nets", "neural network",
                                      "neural networks", "fuzzy models"],
                  "machmodel": ["svm", "support vector machine", "vector machine", "neural network", "neural networks",
                            "decision tree",
                            "decision process", "random forests", "regression",
                            "clustering", "cluster", "dimensionality reduction", "ensemble methods", "word embeddings",
                            "neural nets", "fuzzy models"],
                  "ontnlp": ["nlp", "natural language processing", "chatbot", "state machine", "ontology",
                             "lemmatization", "lemma", "parsing", "parse", "stemming", "sentence breaking",
                             "sequence tagging", "tagging", "part of speech", "parts of speech", "pos",
                             "grammar induction", "segmentation",
                             "topic modeling", "named entity recognition", "ner", "optical character recognition",
                             "ocr", "word2vec",
                             "discourse analysis", "stop words", "sentiment analysis", "wordnet"],
                  "nlptool": ["state machine", "ontology", "lemmatization", "sentence breaking",
                              "sequence tagging", "tagging", "segmentation", "part of speech", "pos", "ner",
                              "sentiment analysis", "wordnet", "ner", "word2vec"],
                  "ontai": ["ai", "artificial intelligence"],
                  "ontdb": ["database", "dbms", "db", "nosql", "mysql", "postgresql", "query",
                            "relational database", "primary key", "foreign key", "ddl",
                            "dml", "jdbc", "schema", "table", "sql", "mysql", "postgresql", "ddl", "dml"],
                  "tooldb": ["sql", "mysql", "postgresql", "ddl", "dml"],
                  "ontsecurity": ["security", "domain", "ip", "firewall", "virus", "encryption", "access control",
                                  "certification", "hacker", "inspection certificate",
                                  "intrusion prevention", "privacy", "vpn", "wifi"]
                  }
             }

tech_area = {"machine learning": "machine learning", "classification": "machine learning",
             "computational intelligence": "machine learning",
             "statistical learning": "machine learning", "deep learning": "machine learning",
             "supervised learning": "machine learning", "unsupervised learning": "machine learning",
             "reinforcement learning": "machine learning", "transfer learning": "machine learning",
             "predictive model": "machine learning", "support vector machine": "machine learning",
             "svm": "machine learning", "vector machine": "machine learning",
             "neural network": "machine learning", "neural networks": "machine learning",
             "decision tree": "machine learning",
             "decision process": "machine learning",
             "random forests": "machine learning", "regression": "machine learning", "clustering": "machine learning",
             "cluster": "machine learning", "dimensionality reduction": "machine learning",
             "ensemble methods": "machine learning", "word embeddings": "machine learning",
             "neural nets": "machine learning",
             "fuzzy models": "machine learning",

             "nlp": "nlp", "natural language processing": "nlp", "chatbot": "nlp", "state machine": "nlp",
             "ontology": "nlp", "lemmatization": "nlp", "lemma": "nlp", "parsing": "nlp", "parse": "nlp",
             "stemming": "nlp", "sentence breaking": "nlp",
             "sequence tagging": "nlp", "tagging": "nlp", "part of speech": "nlp", "parts of speech": "nlp",
             "pos": "nlp", "grammar induction": "nlp",
             "segmentation": "nlp", "topic modeling": "nlp", "named entity recognition": "nlp", "ner": "nlp",
             "optical character recognition": "nlp", "ocr": "nlp", "discourse analysis": "nlp",
             "stop words": "nlp", "sentiment analysis": "nlp", "wordnet": "nlp",

             "ai": "ai", "artificial intelligence": "ai", "word2vec":"nlp",

             "database": "database", "dbms": "database", "db": "database", "nosql": "database",
             "mysql": "database", "postgresql": "database", "query": "database", "relational database": "database",
             "primary key": "database", "foreign key": "database", "ddl": "database", "dml": "database",
             "jdbc": "database", "schema": "database", "table": "database", "sql": "database",
             "oracle database": "database",

             "cybersecurity": "cybersecurity", "security": "cybersecurity", "domain": "cybersecurity",
             "ip": "cybersecurity", "firewall": "cybersecurity", "virus": "cybersecurity",
             "encryption": "cybersecurity", "access control": "cybersecurity", "certification": "cybersecurity",
             "hacker": "cybersecurity", "inspection certificate": "cybersecurity",
             "intrusion prevention": "cybersecurity", "privacy": "cybersecurity", "vpn": "cybersecurity",
             "wifi": "cybersecurity"
             }
area_fut = {"nlp": "npl will probably be the focus of the next twenty years.",
            "machine learning": "Absolutely. Machine learning is useful in almost every area, it IS the future.",
            "database": "You are right. Though artificial intelligence is taking over the spotlight, we cannot do anything without an effective database system.",
            "cybersecurity": "AI will be the future of cybersecurity. Machines could do this task much better than human after training."
            }

lang_op = {"java": "i use java a lot too. It is the first programming language i learned",
             "javascript": "i know it is nothing like java though they sounds similar",
             "python": "i like that it is simple and straightforward",
             "c": "i wish to learn c someday",
             "c++": "i heard it is the most complicated programming language",
             "c#": "i know it has syntax similar to java",
             "php": "i have never used php before",
             "swift": "i have never used swift before",
             "go": "i have never used go before",
             "ruby": "i have never used ruby before",
             "r": "i use r to do a lot of visualizations",
             "sql": "i use it with my database project a lot too",
             "matlab": "it sounds to be complicated..."
             }


class areaFut(Macro):
    def run(self, ngrams, vars, args):
        if 'area' in vars:
            for key, value in area_fut.items():
                if key in vars['area']:
                    return value


class techArea(Macro):
    def run(self, ngrams, vars, args):
        if 'tech' in vars:
            for key, value in tech_area.items():
                if key in vars['tech']:
                    return value
        elif 'tool' in vars:
            for key, value in tech_area.items():
                if key in vars['tool']:
                    return value


class AnsCount(Macro):
    def run(self, ngrams, vars, args):
        if 'count' in vars:
            i = vars['count']
            vars['count'] = int(i) + 1
        return


class feedback(Macro):
    def run(self, ngrams, vars, args):
        fb = ""
        if len(vars['said']) > 1:
            sa = vars["said"].split()
            if len(sa)>1:
                aa = ','.join(sa[:-1]) + " and " + sa[-1]
            else:
                aa = sa[0]
            fb+="You should use more formal language in interview and avoid words such as " + aa + ". "
        if vars["count1"] > 1:
            fb+="Some of your answers for behaviroal questions are too concise. Try to elaborate more on your answers next time."
        if "count" in vars:
            if vars['count'] >= 2:
                fb+=" In terms of the technical part, you got most of the questions wrong. It seems like you need to review the basic accounting concepts before your actual interview. You can come back to practice with me again next time when you feel ready! Good luck!"
            else:
                fb+=" In terms of the technical part, you got most of the questions right, it seems like you're ready for your next interview! Good luck!"
        return fb

class wordcount(Macro):
    def run(self, ngrams, vars, args):
        if(len(vars['a'].split())<100):
            flag=1
        else:
            flag=0
        vars["flag"]=flag
        return


class check(Macro):
    def run(self, ngrams, vars, args):
        nowords=["aint", "yall", "you guys", "should", "shouldnt", "kinda", "stuff", "em", "um", "cool", "whatever"]
        for word in vars["a"].split():
            if word in nowords:
                vars["said"] += word + " "
        if (len(vars['a'].split()) < 50):
            if "count1" in vars:
                i = vars['count1']
                vars['count1'] = int(i) + 1
        return

class chooseRoute(Macro):
    def run(self, ngrams, vars, args):
        if "pos" in vars:
            position = vars["pos"]
            if position in ind_pos["ontology"]["ontfinance"]:
                route="finance"
            elif position in ind_pos["ontology"]["ontconsulting"]:
                route = "consulting"
            elif position in ind_pos["ontology"]["onttechnology"]:
                route = "tech"
            vars['route']=route
        elif "industry" in vars:
            ind = vars["industry"]
            if ind in "consulting":
                route = "consulting"
            elif ind in "finance":
                route = "finance"
            elif ind in "technology":
                route = "tech"
            vars['route'] = route
        return

class setVars(Macro):
    def run(self, ngrams, vars, args):
        vars["count1"]=0
        vars["said"]=""
        return

class setVars1(Macro):
    def run(self, ngrams, vars, args):
        vars["count"]=0
        return

class langOp(Macro):
    def run(self, ngrams, vars, args):
        if 'lang' in vars:
            for key, value in lang_op.items():
                if key in vars['lang']:
                    return value

class field(Macro):
    def run(self, ngrams, vars, args):
        a = ""
        if "area" in vars:
            a = vars["area"]
        else:
            a = "this field"
        return a
class checkposition(Macro):
    def run(self, ngrams, vars, args):
        result=""
        if "pos" in vars:
            result = "Why are you interested in " + vars["pos"]
        elif "route" in vars:
            result = "Why are you interested in working in " + vars["route"]
        return result
class setroute1(Macro):
    def run(self, ngrams, vars, args):
        vars["route"]="consulting"
        return
class setroute2(Macro):
    def run(self, ngrams, vars, args):
        vars["route"]="finance"
        return
# ================cs dict & macro end==============


knowledge = KnowledgeBase()
knowledge.load_json(ind_pos)
knowledge.load_json(ind_comp)
knowledge.load_json(area_tech)
df = DialogueFlow(State.S1, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge, macros={"placeInd": placeInd(),
"indComp":indComp(),"posSkill":posSkill(), "areaFut": areaFut(), "techArea":techArea(),
"AnsCount": AnsCount(), "feedback":feedback(),"wordcount":wordcount(),"check":check(),"chooseRoute":chooseRoute(),"langOp":langOp(),"setVars":setVars(), "field":field(),
"checkposition":checkposition(),"setroute1":setroute1(),"setroute2":setroute2(),"setVars1":setVars1()})

df.add_system_transition(State.S1, State.U1, '"Where do you want to work?"')
df.add_user_transition(State.U1, State.S2a, '[$loc={new york,ny,la,los angeles,chicago,dallas,washington dc,dc,west,east,bay,san francisco,sf,houston,boston,bos,atl,atlanta,seattle,sea,san jose}]', score=1)
df.add_user_transition(State.U1, State.S2b, '[$loc={new york,ny,la,los angeles,chicago,dallas,washington dc,dc,west,east,bay,san francisco,sf,houston,boston,bos,atl,atlanta,seattle,sea,san jose}]')
df.add_user_transition(State.U1, State.S2c, '[$comp=#ONT(ontfinanc)]', score = 2)
df.add_user_transition(State.U1, State.S2d, '[$comp=#ONT(ontconsultin)]', score = 2)
df.add_user_transition(State.U1, State.S2e, '[$comp=#ONT(onttechnolog)]', score = 2)
df.add_user_transition(State.U1, State.S2f, '[$comp=#NER(org)]', score = 1)
df.add_user_transition(State.U1, State.S2g, '[{dont know,do not know,unsure,[not,{sure,certain,considered,consider,thought}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}]}]')
df.set_error_successor(State.U1, error_successor=State.ERR1)

df.add_system_transition(State.S2a, State.U2a, '[!Sure"." $loc is a great place to work"!" There are a lot of #placeInd companies there"." What industry are you interested in"?"]')
df.add_system_transition(State.S2b, State.U2a, '[!I also think $loc is a great place to work"!" There are a lot of #placeInd companies there"." What industry are you interested in"?"]')
df.add_system_transition(State.S2g, State.U2a, '"Oh it is fine that you have not decide where to work at. Do you have an industry that you are interested in?"')
df.add_system_transition(State.S2c, State.U3a, '[!$comp is a great bank"." What position in $comp are you interested in"?"]')
df.add_system_transition(State.S2d, State.U3a, '[!$comp is a great consulting firm"." What position in $comp are you interested in"?"]')
df.add_system_transition(State.S2e, State.U3a, '[!$comp is a great technology company"." What position in $comp are you interested in"?"]')
df.add_system_transition(State.S2f, State.U3a, '[!$comp is a great company to work for"." What position in $comp are you interested in"?"]')
df.add_system_transition(State.ERR1, State.U2a, '"I am not familiar with that place. What industry do you want to work in?"')

df.add_user_transition(State.U2a, State.S3a, '[$industry={consulting,finance,tech,technology,it}]')
df.set_error_successor(State.U2a, error_successor=State.ERR2)
df.add_system_transition(State.S3a, State.U1, '[!$industry is a very promising industry to work in"." I know #indComp are famous in the $industry industry"." What company in $industry do you want to work for"?"]')
df.add_system_transition(State.ERR2, State.U3a, '"Umm...I am not very familiar with this industry. What kind of position would you like to work at?"')

df.add_user_transition(State.U3a, State.CONSULT, '[$pos=#ONT(ontconsulting)]')
df.add_user_transition(State.U3a, State.FINANCE, '[$pos=#ONT(ontfinance)]')
df.add_user_transition(State.U3a, State.TECH, '[$pos=#ONT(onttechnology)]')
df.add_user_transition(State.U3a, State.DK, '[{dont know,do not know,unsure,[not,{sure,certain,considered,consider,thought}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}]}]')
df.set_error_successor(State.U3a, error_successor=State.ERR3)
df.add_user_transition(State.U3a, State.SAME, '[{same,similar}]')

df.add_system_transition(State.CONSULT, State.U4a, '[!Many consulting companies are hiring great $pos"." Why do you want to become a $pos "?"]')
df.add_system_transition(State.FINANCE, State.U4a, '[!Many banks are looking for great $pos "." Why do you want to do $pos "?"]')
df.add_system_transition(State.TECH, State.U4a, '[!Many technology firms are looking for great $pos"." Why do you want to be a $pos "?"]')
df.add_system_transition(State.SAME, State.U4a, '[!Many firms are looking for great $pos"."Why do you want to become a $pos"?"]')
df.add_system_transition(State.ERR3, State.U4c, '"Well...I do not know much about this position, but I will look it up later. Why are you interested in this position?"')
df.add_system_transition(State.DK, State.U4b, '"Thats fine. It took me a long time to figure out what I really want to do either. I actually know a lot about different jobs now, such as business analyst, investment banking analyst, business consultant, software engineer, data analyst, wed developer, product manager… Which one are you interested in? I can tell you what I know about it."')

df.add_user_transition(State.U4a, State.S5, '[$why_posadj=#POS(adj)]')
df.set_error_successor(State.U4a, error_successor=State.ERR4)
df.add_user_transition(State.U4c, State.S5b, "/.*/")
df.add_user_transition(State.U4b, State.S6b, '[$pos={/.*/}]')

df.add_system_transition(State.S5, State.U5, '[!"Yeah for sure, it is" $why_posadj ". What kind of skills do you think that employers value for this position?"]')
df.add_system_transition(State.ERR4, State.U5, '"You have interesting insights. What kind of skills do you think that employers value for this position?"')
df.add_system_transition(State.S5b, State.U5b, '"Sounds interesting! I wish I could learn more about it. What kind of skills do you think that employers value for this position?"')

df.add_system_transition(State.S6b, State.END, '[!You know what, crucial skills for a $pos are":" #posSkill Do you feel that you are ready for this job"?" We can always talk about this anytime.]')

df.add_user_transition(State.U5, State.S6a, "/.*/")
df.add_user_transition(State.U5b, State.S6c, "/.*/")
df.add_system_transition(State.S6a, State.U6, '[!#chooseRoute #setVars Absolutely"."For a $pos","#posSkill are very important. You should try to build these skillset in order to get a job"." Do you want to practice interview with me"?"]')
df.add_system_transition(State.S6c, State.U6, '[!#chooseRoute #setVars Sounds good"!"Do you want to practice interview with me"?"]')

df.add_user_transition(State.U6, State.S77, "[{yes, yeah, yea, ye, yep, do, sure, of course, absolutely, why not}]")
df.add_user_transition(State.U6, State.END, '[{dont know,do not know,unsure,[not,{sure,certain,considered,consider,thought}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}]}]')
df.add_user_transition(State.U6, State.S2a, '[$loc={new york,ny,la,los angeles,chicago,dallas,washington dc,dc,west,east,bay,san francisco,sf,houston,boston,bos,atl,atlanta,seattle,sea,san jose}]')
df.set_error_successor(State.U6, error_successor=State.ERR6)
df.add_system_transition(State.ERR6, State.U6, '[!I dont understand". "Do you want to practice interview with me"? "I can help you to do an mock interview if you say yes"."]')
#_____________________
df.add_system_transition(State.S77, State.U01, '[!#ANY($route=finance)It seems like you are interested in $pos"."Do you want to have a mock interview in finance"?"]',score=5)
df.add_user_transition(State.U01, State.Sfin, "[{yes, yeah, yea, ye, do, sure, of course, absolutely, why not}]")
df.add_user_transition(State.U01, State.S01, '[{dont know,do not know,unsure,[not,{sure,certain,considered,consider,thought}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}]}]',score=1)
df.add_user_transition(State.U01, State.Scon, '[{consulting,#ONT(ontconsulting)}]', score=5)
df.add_user_transition(State.U01, State.Stech, '[{technology,tech,#ONT(onttechnology)}]',score=5)

df.add_system_transition(State.S77, State.U03, '[!#ANY($route=consulting)It seems like you are interested in $pos"."Do you want to have a mock interview in consulting"?"]',score=5)
df.add_user_transition(State.U03, State.Scon, "[{yes, yeah, yea, ye, do, sure, of course, absolutely, why not}]")
df.add_user_transition(State.U03, State.S01, '[{dont know,do not know,unsure,[not,{sure,certain,considered,consider,thought}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}]}]',score=1)
df.add_user_transition(State.U03, State.Sfin, '[{finance,#ONT(ontfinance)}]',score=5)
df.add_user_transition(State.U03, State.Stech, '[{technology,tech,#ONT(onttechnology)}]',score=5)

df.add_system_transition(State.S77, State.U04, '[!#ANY($route=tech)It seems like you are interested in $pos"."Do you want to have a mock interview in this field"?"]',score=5)
df.add_user_transition(State.U04, State.Stech, "[{yes, yeah, yea, ye, do,sure, of course, absolutely, why not}]")
df.add_user_transition(State.U04, State.S01, '[{dont know,do not know,unsure,[not,{sure,certain,considered,consider,thought}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}]}]',score=1)
df.add_user_transition(State.U04, State.Scon, '[{consulting,#ONT(ontconsulting)}]', score=5)
df.add_user_transition(State.U04, State.Sfin, '[{finance,#ONT(ontfinance)}]',score=5)

df.add_system_transition(State.S77, State.U05, '[!I can help you to mock consulting","finance and tech interviews"."Which one do you like to practice"?"]',score=1)
df.add_user_transition(State.U05, State.Scon, '[consulting]',score=5)
df.add_user_transition(State.U05, State.Sfin, '[finance]',score=5)
df.add_user_transition(State.U05, State.Stech, '[{technology,tech}]',score=5)
df.add_user_transition(State.U05, State.S02, '/.*/',score=1)
df.add_system_transition(State.S02, State.U05, '[!A consulting interview will consist of only behavioral questions"."Both finance and tech interviews will include behavorial and technical parts"."Which one would you like to try"?"]')


df.add_system_transition(State.S01, State.U02, '[!Then what position do you want to practice for in this mock interview"?"]')
df.add_user_transition(State.U02, State.Scon, '[$pos=#ONT(ontconsulting)]')
df.add_user_transition(State.U02, State.Sfin, '[$pos=#ONT(ontfinance)]')
df.add_user_transition(State.U02, State.Stech, '[$pos=#ONT(onttechnology)]')

df.add_system_transition(State.Scon, State.Ua, '[!Awesome"!" Lets start"."#setroute1 You will be asked only behavioral questions in this mock interview"." Tell me something about yourself first"."]')
df.add_system_transition(State.Scon, State.Ua1, 'Awesome! Lets start. #setroute1 You will be asked only behavioral questions in this mock interview. First introduce yourself please.')
df.add_system_transition(State.Scon, State.Ua2, 'Awesome! Lets start. #setroute1 You will be asked only behavioral questions in this mock interview. Walk me through your resume first.')
df.add_user_transition(State.Ua, State.Swork, '$a=<{work,worked,intern,interned,part time,internship,job},$org=#NER(org)>',score=5)
df.add_user_transition(State.Ua1, State.Swork, '$a=<{work,worked,intern,interned,part time,internship,job},$org=#NER(org)>',score=5)
df.add_user_transition(State.Ua2, State.Swork, '$a=<{work,worked,intern,interned,part time,internship,job},$org=#NER(org)>',score=5)
df.add_system_transition(State.Swork, State.Ub, '[!#check You mentioned your work experience at $org"."Could you elaborate more about your responsibility there"?"]')
df.add_user_transition(State.Ub, State.Sc, "$a=/.*/")
df.add_user_transition(State.Ua, State.Sclub, '$a=[{$club=president,vice president,chair,vp,founder,cofounder,representative,rep}]',score=5)
df.add_user_transition(State.Ua1, State.Sclub, '$a=[{$club=president,vice president,chair,vp,founder,cofounder,representative,rep}]',score=5)
df.add_user_transition(State.Ua2, State.Sclub, '$a=[{$club=president,vice president,chair,vp,founder,cofounder,representative,rep}]',score=5)
df.add_user_transition(State.Ua, State.Sne1, "$a=/.*/",score=1)
df.add_user_transition(State.Ua1, State.Sne1, "$a=/.*/",score=1)
df.add_user_transition(State.Ua2, State.Sne1, "$a=/.*/",score=1)
df.add_system_transition(State.Sne1, State.Uh, '[!#check Good"."Now tell me what are three things about you that I should take with me]')
df.add_system_transition(State.Sne1, State.Uh1, '[!#check Good"."Whats one word that describe you best]')
df.add_system_transition(State.Sne1, State.Uh2, '[!#check Good"."What do you consider your greatest accomplishment]')
df.add_system_transition(State.Sne1, State.Uh3, '[!#check Good"."What makes you different from other candidates]')
df.add_user_transition(State.Uh, State.Sc, "$a=/.*/")
df.add_user_transition(State.Uh1, State.Sc, "$a=/.*/")
df.add_user_transition(State.Uh2, State.Sc, "$a=/.*/")
df.add_user_transition(State.Uh3, State.Sc, "$a=/.*/")
df.add_system_transition(State.Sclub, State.Uclub, '[!#check You mentioned that you are a $club in your club"." Could you elaborate more about your experience with the club"?"]')
df.add_user_transition(State.Uclub, State.Sc, "$a=/.*/")
df.add_system_transition(State.Sc, State.Ud, '[!#check That sounds interesting. Do you feel more comfortable working in a team or by yourself]',score=0)
df.add_system_transition(State.Sc, State.Ud1, '[!#check That sounds interesting. What role do you like to take in a team]',score=0)
df.add_system_transition(State.Sc, State.Ud2, '[!#check That sounds interesting. Describe a time when you worked as part of a team]',score=0)
df.add_system_transition(State.Sc, State.Ud3, '[!#check That sounds interesting. Describe a time when you took a leadership position]',score=0)
df.add_user_transition(State.Ud, State.Sd, "$a=/.*/")
df.add_user_transition(State.Ud1, State.Sd, "$a=/.*/")
df.add_user_transition(State.Ud2, State.Sd, "$a=/.*/")
df.add_user_transition(State.Ud3, State.Sd, "$a=/.*/")
df.add_system_transition(State.Sd, State.Ue, '[!#check Interesting to know"." #checkposition]')
df.add_user_transition(State.Ue, State.Se, "$a=/.*/")
df.add_system_transition(State.Se, State.Uf, '[!#check Now give me an example of a big risk you have taken in your life]')
df.add_system_transition(State.Se, State.Uf1, '[!#check What is the biggest challenge you have faced and overcome in your life]')
df.add_system_transition(State.Se, State.Uf2, '[!#check What is the toughest decision you’ve made]')
df.add_system_transition(State.Se, State.Uf3, '[!#check What is an example of a big risk you have taken in your life]')
df.add_user_transition(State.Uf, State.Sf, "$a=/.*/")
df.add_user_transition(State.Uf1, State.Sf, "$a=/.*/")
df.add_user_transition(State.Uf2, State.Sf, "$a=/.*/")
df.add_user_transition(State.Uf3, State.Sf, "$a=/.*/")
df.add_system_transition(State.Sf, State.Ug, '[!#check How is your time management skill]')
df.add_system_transition(State.Sf, State.Ug1, '[!#check Give an example of your experience with multitasking]')
df.add_user_transition(State.Ug, State.Sh, "$a=/.*/")
df.add_user_transition(State.Ug1, State.Sh, "$a=/.*/")
df.add_system_transition(State.Sh, State.Ui, '[!#check Describe how you have dealt with conflict in a team situation]')
df.add_system_transition(State.Sh, State.Ui1, '[!#check Give an example of a project you enjoyed working on]')
df.add_system_transition(State.Sh, State.Ui2, '[!#check Give an example of a goal you set and how you achieved it]')
df.add_system_transition(State.Sh, State.Ui3, '[!#check Give an example of a time when you persuaded others to do something or convinced someone to see your point of view]')
df.add_user_transition(State.Ui, State.Si, "$a=/.*/")
df.add_user_transition(State.Ui1, State.Si, "$a=/.*/")
df.add_user_transition(State.Ui2, State.Si, "$a=/.*/")
df.add_user_transition(State.Ui3, State.Si, "$a=/.*/")
df.add_system_transition(State.Si, State.Uj, '[!This is the end of mock interview"."#feedback]')


df.add_system_transition(State.Sfin, State.Uaa, '[!Awesome"!" Lets start"."#setroute2 #setVars1 You will be asked both behavioral questions and technical questions in this mock interview"." Tell me something about yourself first"."]')
df.add_system_transition(State.Sfin, State.Uaa1, '[!Awesome"!" Lets start"."#setroute2 #setVars1 You will be asked both behavioral questions and technical questions in this mock interview"." Tell me something about yourself first"."]')
df.add_system_transition(State.Sfin, State.Uaa2, '[!Awesome"!" Lets start"."#setroute2 #setVars1 You will be asked both behavioral questions and technical questions in this mock interview"." Tell me something about yourself first"."]')
df.add_user_transition(State.Uaa, State.Swwork, '$a=<{work,worked,intern,interned,part time,internship,job},$org=#NER(org)>',score=5)
df.add_user_transition(State.Uaa1, State.Swwork, '$a=<{work,worked,intern,interned,part time,internship,job},$org=#NER(org)>',score=5)
df.add_user_transition(State.Uaa2, State.Swwork, '$a=<{work,worked,intern,interned,part time,internship,job},$org=#NER(org)>',score=5)
df.add_system_transition(State.Swwork, State.Ubb, '[!#check You mentioned your work experience at $org"."Could you elaborate more about your responsibility there"?"]')
df.add_user_transition(State.Ubb, State.Scc, "$a=/.*/")
df.add_user_transition(State.Uaa, State.Scclub, '$a=[{$club=president,vice president,chair,vp,founder,cofounder,representative,rep}]',score=5)
df.add_user_transition(State.Uaa1, State.Scclub, '$a=[{$club=president,vice president,chair,vp,founder,cofounder,representative,rep}]',score=5)
df.add_user_transition(State.Uaa2, State.Scclub, '$a=[{$club=president,vice president,chair,vp,founder,cofounder,representative,rep}]',score=5)
df.add_user_transition(State.Uaa, State.Sne, "$a=/.*/",score=1)
df.add_user_transition(State.Uaa1, State.Sne, "$a=/.*/",score=1)
df.add_user_transition(State.Uaa2, State.Sne, "$a=/.*/",score=1)
df.add_system_transition(State.Sne, State.Uhh, '[!#check Good"."Now tell me what are three things about you that I should take with me]')
df.add_system_transition(State.Sne, State.Uhh1, '[!#check Good"."Whats one word that describe you best]')
df.add_system_transition(State.Sne, State.Uhh2, '[!#check Good"."What do you consider your greatest accomplishment]')
df.add_system_transition(State.Sne, State.Uhh3, '[!#check Good"."What makes you different from other candidates]')
df.add_user_transition(State.Uhh, State.Scc, "$a=/.*/")
df.add_user_transition(State.Uhh1, State.Scc, "$a=/.*/")
df.add_user_transition(State.Uhh2, State.Scc, "$a=/.*/")
df.add_user_transition(State.Uhh3, State.Scc, "$a=/.*/")
##################################################################
df.add_system_transition(State.Scc, State.U99, '[!#wordcount #ANY($flag=1)Could you elaborate more"?"]',score=5)
df.add_user_transition(State.U99, State.Scc, "/.*/")
##################################################################
df.add_system_transition(State.Scclub, State.Ucclub, '[!#check You mentioned that you are a $club in your club"." Could you elaborate more about your experience with the club"?"]')
df.add_user_transition(State.Ucclub, State.Scc, "$a=/.*/")
df.add_system_transition(State.Scc, State.Udd, '[!#check Do you feel more comfortable working in a team or by yourself]',score=0)
df.add_system_transition(State.Scc, State.Udd1, '[!#check What role do you like to take in a team]',score=0)
df.add_system_transition(State.Scc, State.Udd2, '[!#check Describe a time when you worked as part of a team]',score=0)
df.add_system_transition(State.Scc, State.Udd3, '[!#check Describe a time when you took a leadership position]',score=0)
df.add_user_transition(State.Udd, State.Sdd, "$a=/.*/")
df.add_user_transition(State.Udd1, State.Sdd, "$a=/.*/")
df.add_user_transition(State.Udd2, State.Sdd, "$a=/.*/")
df.add_user_transition(State.Udd3, State.Sdd, "$a=/.*/")
df.add_system_transition(State.Sdd, State.Uee, '[!#check Interesting to know"." #checkposition]')
df.add_user_transition(State.Uee, State.See, "$a=/.*/")
df.add_system_transition(State.See, State.Uq1, '[!#check Now lets move on to the technical part","you can say next to move to the next question"."To start with","tell me what the three main financial statements are]',score=5)
df.add_user_transition(State.Uq1, State.Sy1, '<{income statement,income statements}, {balance sheet,balance sheets}, {cash flows,cash flow}>',score =5)
df.add_user_transition(State.Uq1, State.Sn1, '[$ans1={income statement,income statements,balance sheet,balance sheets,cash flows,cash flow}]',score=3)
df.add_user_transition(State.Uq1, State.Sn11, '[{<{income statement, income statements}, {balance sheet,balance sheets}>,<{balance sheet,balance sheets}, {cash flow, cash flows}>,<{cash flow, cash flows}, {income statement, income statements}>}]', score=4)
df.add_user_transition(State.Uq1, State.Sn111, "/.*/",score=0)
df.add_system_transition(State.Sy1, State.Uq2, '[!Correct"."Next","what is EBITDA]')
df.add_system_transition(State.Sy1, State.Uq6, '[!Correct"."Next","how could a company have positive EBITDA and still go bankrupt]')
df.add_system_transition(State.Sy1, State.Uq5, '[!Correct"."Now","tell me what are the three components in the statement of cash flows]')
df.add_system_transition(State.Sn1, State.Uq2, '[!You got $ans1 correct"."#AnsCount The answer is income statement","balance sheet and statement of cash flows"."Next","what is EBITDA]')
df.add_system_transition(State.Sn1, State.Uq6, '[!You got $ans1 correct"."#AnsCount The answer is income statement","balance sheet and statement of cash flows"."Next","how could a company have positive EBITDA and still go bankrupt]')
df.add_system_transition(State.Sn1, State.Uq5, '[!You got $ans1 correct"."#AnsCount The answer is income statement","balance sheet and statement of cash flows"."Now","tell me what are the three components in the statement of cash flows]')
df.add_system_transition(State.Sn11, State.Uq2, '[!You got two correct"."#AnsCount The answer is income statement"," balance sheet and statement of cash flows"." Next","what is EBITDA]')
df.add_system_transition(State.Sn11, State.Uq6, '[!You got two correct"."#AnsCount The answer is income statement"," balance sheet and statement of cash flows"." Next","how could a company have positive EBITDA and still go bankrupt]')
df.add_system_transition(State.Sn11, State.Uq5, '[!You got two correct"."#AnsCount The answer is income statement"," balance sheet and statement of cash flows"."Now","tell me what are the three components in the statement of cash flows]')
df.add_system_transition(State.Sn111, State.Uq2, '[!No"."#AnsCount The correct answer is income statement"," balance sheet and statement of cash flows"." Next"," what is EBITDA]')
df.add_system_transition(State.Sn111, State.Uq6, '[!No"."#AnsCount The correct answer is income statement"," balance sheet and statement of cash flows"." Next"," how could a company have positive EBITDA and still go bankrupt]')
df.add_system_transition(State.Sn111, State.Uq5, '[!No"."#AnsCount The correct answer is income statement"," balance sheet and statement of cash flows"." Next","Now","tell me what are the three components in the statement of cash flows]')
df.add_system_transition(State.See, State.Uq8, r'"Now lets move on to the technical part. What does the risk-free rate equal to"')
df.add_user_transition(State.Uq8, State.Sy9,'<current yield,ten year,treasury>',score=5)
df.add_user_transition(State.Uq8, State.Sn9, '/.*/',score=0)
df.add_system_transition(State.Sy9, State.Uq2,'[!You got it correct. What is EBITDA]')
df.add_system_transition(State.Sy9, State.Uq6,'[!You got it correct. How could a company have positive EBITDA and still go bankrupt]')
df.add_system_transition(State.Sy9, State.Uq5,'[!You got it correct. Now, tell me what are the three components in the statement of cash flows]')
df.add_system_transition(State.Sn9, State.Uq5,'[!#AnsCount Risk free rate is the current yield for 10 year government treasury"."Now tell me what are the three components in the statement of cash flows]')
df.add_system_transition(State.Sn9, State.Uq2,'[!#AnsCount Risk free rate is the current yield for 10 year government treasury"."What is EBITDA]')
df.add_system_transition(State.Sn9, State.Uq6,'[!#AnsCount Risk free rate is the current yield for 10 year government treasury"."How could a company have positive EBITDA and still go bankrupt]')
df.add_system_transition(State.See, State.Uq7,r'"Now lets move on to the technical part. When should a purchase be capitalized rather than expensed"')
df.add_user_transition(State.Uq7, State.Sy7,'[{more than,exceed,exceeds,over,longer},{one year,a year}]',score=5)
df.add_user_transition(State.Uq7, State.Sn7, '/.*/',score=0)
df.add_system_transition(State.Sy7, State.Uq2,'[!Great. What is EBITDA]')
df.add_system_transition(State.Sy7, State.Uq6,'[!Great. How could a company have positive EBITDA and still go bankrupt]')
df.add_system_transition(State.Sy7, State.Uq5,'[!Great. Now, tell me what are the three components in the statement of cash flows]')
df.add_system_transition(State.Sn7, State.Uq5,'[!#AnsCount When the purchase will be use for more than a year","it should be counted towards depreciation instead of expense"."Now tell me what are the three components in the statement of cash flows]')
df.add_system_transition(State.Sn7, State.Uq2,'[!#AnsCount When the purchase will be use for more than a year","it should be counted towards depreciation instead of expense"."What is EBITDA]')
df.add_system_transition(State.Sn7, State.Uq6,'[!#AnsCount When the purchase will be use for more than a year","it should be counted towards depreciation instead of expense"."How could a company have positive EBITDA and still go bankrupt]')

df.add_user_transition(State.Uq5, State.Sy5,'[cash from, <{operations,operation,operating},{finance,financing},{invest,invests,investing}>]',score=5)
df.add_user_transition(State.Uq5, State.Sn5, '/.*/',score=0)
df.add_user_transition(State.Uq6, State.Sy6,'[{[interest, {go over,goes over,too much,exceed,more than}, ebitda],[ebitda,{less than,deficit,too few,too low}, interest]}]',score=5)
df.add_user_transition(State.Uq6, State.Sn6, '/.*/',score=0)
df.add_user_transition(State.Uq2, State.Sy2, '[earnings before interest, tax, depreciation, amortization]',score=5)
df.add_user_transition(State.Uq2, State.Sn2, "/.*/",score=0)

df.add_system_transition(State.Sy2, State.Uq3,'[!Great answer"." Now explain to me how to calculate net debt]')
df.add_system_transition(State.Sy2, State.Uq4,'[!You got it right"." Next question"," when would you not want to use a DCF to value a company]')
df.add_system_transition(State.Sn2, State.Uq3,'[!#AnsCount EBITDA is earnings before interest"," tax"," depreciation and amortization"." Its a key concept in financial statement"," you shouldnt get it wrong"." Now explain to me how to calculate net debt]')
df.add_system_transition(State.Sn2, State.Uq4,'[!#AnsCount EBITDA is earnings before interest"," tax"," depreciation and amortization"." Its a key concept in financial statement"," you shouldnt get it wrong"." Next question"," when would you not want to use a DCF to value a company]')

df.add_system_transition(State.Sy5, State.Uq3,'[!Great answer"." Now explain to me how to calculate net debt]')
df.add_system_transition(State.Sy5, State.Uq4,'[!You got it right"." Next question"," when would you not want to use a DCF to value a company]')
df.add_system_transition(State.Sn5, State.Uq3,'[!#AnsCount The statement of cash flows contains cash flows from operations, investing and financing. Now explain to me how to calculate net debt]')
df.add_system_transition(State.Sn5, State.Uq4,'[!#AnsCount The statement of cash flows contains cash flows from operations, investing and financing. Next question"," when would you not want to use a DCF to value a company]')

df.add_system_transition(State.Sy6, State.Uq3,'[!Good"." Now explain to me how to calculate net debt]')
df.add_system_transition(State.Sy6, State.Uq4,'[!Nice"." Next question"," when would you not want to use a DCF to value a company]')
df.add_system_transition(State.Sn6, State.Uq3,'[!#AnsCount When interest expense exceeds EBITDA, a company would go bankrupt even when they have a positive EBITDA. Now explain to me how to calculate net debt]')
df.add_system_transition(State.Sn6, State.Uq4,'[!#AnsCount When interest expense exceeds EBITDA, a company would go bankrupt even when they have a positive EBITDA. Next question"," when would you not want to use a DCF to value a company]')

df.add_user_transition(State.Uq3, State.Sy3, '[total debt, {minus,less}, cash]',score=5)
df.add_user_transition(State.Uq3, State.Sn3, '/.*/',score=0)

df.add_user_transition(State.Uq4, State.Sy4, '<{unpredictable,unknown,no,hard to get,hard to predict,difficult to get,difficult to predict},{cash flow,cash flows}>',score=5)
df.add_user_transition(State.Uq4, State.Sn4, '/.*/',score=0)

df.add_system_transition(State.Sy3, State.rr,'[!Great"."This is the end of our mock interview"."#feedback]')
df.add_system_transition(State.Sn3, State.rr,'[!#AnsCount You got it wrong"."Net debt is just total debt minus cash"."This is the end of our mock interview"."#feedback]')

df.add_system_transition(State.Sy4, State.rr,'[!Thats correct"."This is the end of our mock interview"."#feedback]')
df.add_system_transition(State.Sn4, State.rr,'[!#AnsCount No","the correct answer is when cash flows are unpredictable"."This is the end of our mock interview"."#feedback]')



#==========================

df.add_system_transition(State.Stech, State.PROJECT, '"Tell me about an important project that you have worked on."')

# collect both tech and tool; use tech to determine the area, use tool for later questions
df.add_user_transition(State.PROJECT, State.MACHL, '<$tech=#ONT(ontmachlearning),$tool=#ONT(machmodel)>', score=6)
df.add_user_transition(State.PROJECT, State.MACHLMODEL, '[$tech=#ONT(ontmachlearning)]', score=2)
df.add_system_transition(State.MACHLMODEL, State.MLTOOL,
                         '"Could you elaborate on the tools or techniques you used, such as training models?"')
df.add_user_transition(State.MLTOOL, State.MACHL, '[$tool=#ONT(machmodel)]')
df.set_error_successor(State.MLTOOL, error_successor=State.MACHL2)

df.add_user_transition(State.PROJECT, State.NLP, '<$tech=#ONT(ontnlp),$tool=#ONT(nlptool)>', score=5)
df.add_user_transition(State.PROJECT, State.NLPTOOL, '[$tech=#ONT(ontnlp)]', score=1)
df.add_system_transition(State.NLPTOOL, State.NTOOL,
                         '"Could you elaborate on the tools or techniques you used, such as training models?"')
df.add_user_transition(State.NTOOL, State.NLP, '[$tool=#ONT(nlptool)]')
df.set_error_successor(State.NTOOL, error_successor=State.NLP2)

df.add_user_transition(State.PROJECT, State.DB, '<$tech=#ONT(ontdb),$tool=#ONT(tooldb)>',score=4)
df.add_user_transition(State.PROJECT, State.DBTOOL, '[$tech=#ONT(ontdb)]',score=0.5)
df.add_system_transition(State.DBTOOL, State.DTOOL, '"Could you elaborate on the tools or techniques you used?"')
df.add_user_transition(State.DTOOL, State.DB, '[$tool=#ONT(tooldb)]')
df.set_error_successor(State.DTOOL, error_successor=State.DB2)

df.add_user_transition(State.PROJECT, State.SEC, '[$tech=#ONT(ontsecurity)]', score=3)

# Redirect AI to more detailed categories if possible
df.add_user_transition(State.PROJECT, State.AI, '[$tech=#ONT(ontai)]')
df.add_system_transition(State.AI, State.AIELAB,
                         '"Artificial intelligence is very broad area. Could you elaborate on the techniques you used?"')
df.add_user_transition(State.AIELAB, State.MACHL, '[$tool=#ONT(machmodel)]')
df.add_user_transition(State.AIELAB, State.NLP, '[$tool=#ONT(nlptool)]')
df.add_user_transition(State.AIELAB, State.DB, '[$tool=#ONT(tooldb)]')
df.add_user_transition(State.AIELAB, State.SEC, '[$tool=#ONT(ontsecurity)]')

df.set_error_successor(State.AIELAB, error_successor=State.WHYTOOL)
df.set_error_successor(State.PROJECT, error_successor=State.UKAREA)

# with both techArea identifies, and $tool
df.add_system_transition(State.MACHL, State.AREA,
                         '[!Sounds like you are making a progress in the area of $area=#techArea"?"]')
df.add_system_transition(State.NLP, State.AREA,
                         '[!Sounds like you are making a progress in the area of $area=#techArea"?"]')
df.add_system_transition(State.DB, State.AREA,
                         '[!Sounds like you are making a progress in the area of $area=#techArea"?"]')
#df.add_system_transition(State.SEC, State.AREA, '"Sounds like you are making a progress in the area of cybersecurity?"')

df.add_user_transition(State.AREA, State.CORRECT, "[{yes, yeah, yea, ye, do, indeed, probably, of course, sure, absolutely}]")
df.set_error_successor(State.AREA, error_successor=State.WRONG)

df.add_system_transition(State.WRONG, State.ASKAREA, '[!What area does this project contribute to"?"]')
df.add_user_transition(State.ASKAREA, State.CORRECT, '/.*/')

df.add_system_transition(State.CORRECT, State.RATIONALE,
                         '[!Cool. How do you feel about using $tool"?" Why did you choose to use it"?"]')
df.add_user_transition(State.RATIONALE, State.LANG, '/.*/')

# we dont have $tool here, so ask generally
df.add_system_transition(State.MACHL2, State.RATIONALE0,
                         '[!Sounds like you are working in the area of $area={machine learning}. How do you feel about the tools and techniques you used"?"]')
df.add_system_transition(State.DB2, State.RATIONALE0,
                         '[!Sounds like you are working on a $area={database} project. How do you feel about the tools and techniques you used"?"]')
df.add_system_transition(State.NLP2, State.RATIONALE0,
                         '[!Sounds like you are working on a $area={nlp} project. How do you feel about the tools and techniques you used"?"]')
df.add_system_transition(State.SEC, State.RATIONALE0,
                         '[!Sounds like you are making progress in $area={cybersecurity}. How do you feel about the tools and techniques you used"?"]')

# dealing with UKAREA
df.add_system_transition(State.UKAREA, State.ASKUK, '"What area does this project contribute to?"')
df.add_user_transition(State.ASKUK, State.AREA0, '/.*/')
df.add_system_transition(State.AREA0, State.RATIONALE0,
                         '"Could you elaborate on the techniques you used? Why did you choose to use it?"')

# dealing with WHYTOOL(AI) - we know it is an AI project but fail to capture tool
df.add_system_transition(State.AIELAB, State.RATIONALE0, '"How do you feel about the tools and techniques you used?"')

df.add_user_transition(State.RATIONALE0, State.LANG, '/.*/')

df.add_system_transition(State.LANG, State.SKILL,
                         '"Indeed, I agree with you. I might miss this... but what programming language did you use for the project?"')  # What was your role in the project? What did you contribute to the project?
df.add_user_transition(State.SKILL, State.PREFLANG,
                       '[$lang={java, javascript, python,c, c++, c, php, swift, go, ruby, r, sql, matlab}]')
df.set_error_successor(State.SKILL, error_successor=State.UKLANG)
df.add_system_transition(State.PREFLANG, State.REASON1, '[!Why did you choose $lang"?"]')
df.add_system_transition(State.UKLANG, State.REASON, '"Why did you choose it?"')

df.add_user_transition(State.REASON1, State.LANGOP, '/.*/')

df.add_system_transition(State.LANGOP, State.FUTURE1, '[!Sounds reasonable. #langOp . What do you think about the future of #field"?"]')
df.add_user_transition(State.FUTURE1, State.REPROS, '/.*/')

df.add_user_transition(State.REASON, State.FUTURE, '/.*/')
df.add_system_transition(State.FUTURE, State.PROSPECT,
                         '[!Sounds reasonable"."Your project is very impressive"."What do you think about the future of #field"?"]')

df.add_user_transition(State.PROSPECT, State.REPROS, '/.*/')
df.add_system_transition(State.REPROS, State.END,'[!Interesting. #areaFut]')

df.run(debugging=False)
