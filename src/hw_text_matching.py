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
    U4a = auto()
    U4b = auto()
    S5 = auto()
    U5 = auto()
    S6a = auto()
    S6b = auto()
    ERR1 = auto()
    ERR2 = auto()
    ERR3 = auto()
    ERR4 = auto()
    ERR5 = auto()


#industry-position
ind_pos = {"ontology": {"ontindustry":["ontconsulting","ontfinance","onttechnology"],
                        "ontconsulting":["business analyst", "associate consultant", "consultant"],
                        "ontfinance":["investment banking","sales and trading","quantitative analyst","wealth management","asset management","corporate banking","capital markets"],
                        "onttechnology":["software engineer","software developer","swe","sde","data analyst","full stack developer","uiux","ui","ux","ios app developer","android app developer","web developer","back end","front end","program manager","project manager","product manager","pm"]
                        }
          }
#industry-company
ind_comp = {"ontology": {"ontind":["ontconsultin","ontfinanc","onttechnolog"],
                         "ontconsultin":["mckinsey","bain","bcg","boston consulting group","deloitte","pwc","kpmg","at kearny","atkearny","accenture","ernest and young","ey","grant thorton","gt"],
                         "ontfinanc":["goldman saches","goldman","gs","jp morgan","jpm","morgan stanley","ms","bank of america","boa","wells fargo","citi","citigroup","citibank","td bank","capital one","deutsche bank","db","barclays","ubs","credit suisse","cs","merrill lynch","baml"],
                         "onttechnolog":["microsoft","apple","google","amazon","ibm","intel","facebook","oracle","linkedin","paypal","samsung","alphabet","huawei","dell","hp","cisco"]
                        }
           }

#dictionaries for response
pos_skill = {"business analyst": "1. Demonstrated aptitude for analytics 2. Proven record of leadership in a work setting and through extracurricular activities 3. Ability to work collaboratively in a team environment 4. Ability to work effectively with people at all levels in an organization 5. Ability to communicate complex ideas effectively, both verbally and in writing in English, and the local office language",
             "associate consultant": "1. Demonstrated aptitude for analytics 2. Proven record of leadership in a work setting and through extracurricular activities 3. Ability to work collaboratively in a team environment 4. Ability to work effectively with people at all levels in an organization 5. Ability to communicate complex ideas effectively, both verbally and in writing, in English and the local office language",
             "consultant": "1. Demonstrated aptitude for analytics 2. Proven record of leadership in a work setting and through extracurricular activities 3. Ability to work collaboratively in a team environment 4. Ability to work effectively with people at all levels in an organization 5. Ability to communicate complex ideas effectively, both verbally and in writing, in English and the local office language",
             "investment banking": "1. Ability to work in a fast-paced, team-based environment with minimal supervision 2. Working knowledge of deal structuring and closing principals 3. Strong communication and networking skills 4. Impeccable research, quantitative and analytical skills, especially in explaining market events 5. Ability to organize and track overlapping tasks and assignments, with frequent priority changes",
             "ib": "1. Ability to work in a fast-paced, team-based environment with minimal supervision 2. Working knowledge of deal structuring and closing principals 3. Strong communication and networking skills 4. Impeccable research, quantitative and analytical skills, especially in explaining market events 5. Ability to organize and track overlapping tasks and assignments, with frequent priority changes",
             "sales and trading": "1. Must be highly proficient in modeling and possess superior written and verbal skills in order to create effective presentations and communicate efficiently with members of the group 2. Proven analytical ability and attention to detail 3.Solid leadership and interpersonal skills 4. Superior written and oral communication skills 5. Ability to work well in a fast-paced, team oriented environment",
             "quantitative": "1. Excellent verbal, written, and interpersonal communication skills 2. Ability to identify and manage complex issues and negotiate solutions within a geographically dispersed organization 3. Strong organizational, multi-tasking, and prioritizing skills 4. Strong programming, large scale data querying and analysis skills 5. Advanced SAS, Python and R programming experience",
             "wealth management": "1. Self-starter who is analytical and creative in their thinking; ability to quickly analyze information and creatively reach solutions and execute their implementation 2. Strong quantitative skills, comfortable with formulas, performance measurement methodology and risk measures 3. Understanding of the various businesses and products within the wealth management space 4. Solid analytical ability to research and analyze complex data sets 5. Interact and communicate effectively, written and verbal, throughout all organizational levels and roles",
             "corporate": "1. Course work in accounting and finance are required 2. A fundamental understanding of valuation theory, methodologies, and applications. Strong financial and computer skills 3. Demonstrated ability to work cooperatively with all levels of staff 4. Strong analytical capabilities and excellent verbal and written communication skills",
             "capital market": "1. Must understand Fixed Income products, including bonds, credit derivatives, asset swaps, credit linked notes and equities 2. Must have experience with pricing, structuring and pitching 3. Must have excellent written, spoken and verbal communication skills, including strong interpersonal skills and the ability to articulate phone presence 4. Must have strong quantitative and analytical skills 5. Must have strong credit, financial analysis and modeling skills",
             "software": "1. Ability to develop software in Java, Ruby on Rails, C++ or other programming languages 2. Excellent knowledge of relational databases, SQL and ORM technologies such as JPA2 and Hibernate 3. Experience developing web applications using at least one popular web framework such as JSF, Wicket, GWT, Spring MVC 4. Experience with test-driven development 5. Ability to document requirements and specifications",
             "data analyst": "1. Strong knowledge of SQL and experience with reporting packages, databases, programming 2. Strong analytical skills with the ability to collect, organize, analyze, and disseminate significant amounts of information with attention to detail and accuracy 3. Technical expertise regarding data models, data mining and segmentation techniques using Python 4. Adept at queries, report writing and presenting findings 5. Excellent communication skill and ability to work with different business stakeholders to understand, identify and translate business challenges into data projects",
             "full stack": "1. Experience working across the full technical stack, delivering quality code on both frontend and backend 2. Understanding of frontend technologies and tooling. 3. Understanding of backend technologies and tooling 4. Proven REST API experience 5. Expert on Node.js or Express and MySQL 6. Knowledgeable about HTML, CSS, JavaScript, PHP and familiar with OOP, AJAX, JSON",
             "uiux": "1. Understanding of interface and interaction patterns and best practices for various platforms, as well as experience working within a responsive design framework 2. Knowledge of human centered design and UX practices. Use a range of methodologies like design research, service blueprinting, collaborative work session design and facilitation, rapid prototyping, and frameworking to strategically define ideal experiences 3. Ability to plan, conduct and synthesize user research, and develop journey maps and user flows 4. Experience creating prototypes that showcase design concepts and interaction patterns 5. Ability to quickly deliver multiple, inventive ideas that are fresh and simple while solving complex customer and business needs. Confidence in sharing in-progress work with team mates ",
             "ui":"1. Knowledge of wireframe tools such as Wireframe.cc and InVision 2. Up-to-date knowledge of design software like Adobe Illustrator and Photoshop 3. Team spirit; strong communication skills to collaborate with various stakeholders 4. Good time-management skills 5. Experience with coding and ability to troubleshoot using HTML, CSS and comparable languages",
             "ux":"1. Proficient with visual design programs such as Adobe Photoshop and others 2. Ability to work effectively in a collaborative environment to create top-performing interfaces for clients 3. Experience with coding and ability to troubleshoot using HTML, CSS and comparable languages 4. Professional written and interpersonal skills when communicating with customers and clients 5. Ability to prioritize and manage several milestones and projects efficiently",
             "ios": "1. Proficient with Objective-C and or Swift, and Cocoa Touch 2. Experience with iOS frameworks such as Core Data, Core Animation, etc. 3. Experience with Design Patterns such as MVC, Singleton, etc. 4. Experience with offline storage, threading, and performance tuning 5. Familiarity with RESTful APIs to connect iOS applications to back-end services",
             "android": "1. Strong knowledge of Android SDK, different versions of Android, and how to deal with different screen sizes 2. Experience with offline storage, threading, and performance tuning 3. Knowledge of the open-source Android ecosystem and the libraries available for common tasks 4. Familiarity with RESTful APIs to connect Android applications to backend services 5. Comfortable with Git and source control",
             "web": "1. Experience with ReactJS 2. Hands-on experience with web front end technologies such as html, CSS, JavaScript, Ajax, JSON, jquery and reactJS 3. Experience with attaching event listeners to an HTML page 4. Familiarity with debugging tools such as Firebug and Chrome DevTools 5. Experience developing web applications supporting traditional web or mobile user interfaces.",
             "back end": "1. Fluency or understanding of specific languages, such as Java, PHP, or Python, and operating systems may be required 2. Strong understanding of the web development cycle and programming techniques and tools 3. Focus on efficiency, user experience, and process improvement 4. Excellent project and time management skills 5. Strong problem solving and verbal and written communication skills",
             "front end": "1. Proficiency with HTML, CSS, JavaScript and jQuery 2. Experience with responsive and adaptive design 3. Excellent project management skills 4. Good problem solving skills 5. Excellent software engineering habits, including peer code reviews, object-oriented design, unit testing, integration testing",
             "pm": "1. Software Development coding experience in one of the following programming languages: C, C++, Java or Python 2. Internship or Teaching Assistant experience in a similar technical field 3. Experience leading entrepreneurial efforts, outreach within organizations or project management experience 4. Ability to work under pressure and function effectively in a fast-paced environment, providing leadership skills and managing multiple projects simultaneously 5. Ability to problem-solve and build relationships cross-functionally",
             "program manager": "1. Software Development coding experience in one of the following programming languages: C, C++, Java or Python 2. Internship or Teaching Assistant experience in a similar technical field 3. Experience leading entrepreneurial efforts, outreach within organizations or project management experience 4. Ability to work under pressure and function effectively in a fast-paced environment, providing leadership skills and managing multiple projects simultaneously 5. Ability to problem-solve and build relationships cross-functionally",
             "project manager": "1. Software Development coding experience in one of the following programming languages: C, C++, Java or Python 2. Internship or Teaching Assistant experience in a similar technical field 3. Experience leading entrepreneurial efforts, outreach within organizations or project management experience 4. Ability to work under pressure and function effectively in a fast-paced environment, providing leadership skills and managing multiple projects simultaneously 5. Ability to problem-solve and build relationships cross-functionally",
             "product manager": "1. Software Development coding experience in one of the following programming languages: C, C++, Java or Python 2. Internship or Teaching Assistant experience in a similar technical field 3. Experience leading entrepreneurial efforts, outreach within organizations or project management experience 4. Ability to work under pressure and function effectively in a fast-paced environment, providing leadership skills and managing multiple projects simultaneously 5. Ability to problem-solve and build relationships cross-functionally"
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

#industry-company
industry_company={
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

knowledge = KnowledgeBase()
knowledge.load_json(ind_pos)
knowledge.load_json(ind_comp)
df = DialogueFlow(State.S1, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge, macros={"placeInd": placeInd(),"indComp":indComp(),"posSkill":posSkill()})

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
df.add_system_transition(State.CONSULT, State.U4a, '[!Many consulting companies are hiring great $pos"." Why do you want to become a $pos "?"]')
df.add_system_transition(State.FINANCE, State.U4a, '[!Many banks are looking for great $pos analysts"." Why do you want to do $pos "?"]')
df.add_system_transition(State.TECH, State.U4a, '[!Many technology firms are looking for great $pos"." Why do you want to do $pos "?"]')
df.add_system_transition(State.ERR3, State.U4a, '"Well...I do not know much about this position, but I will look them up later. Why are you interested in this position?"')
df.add_system_transition(State.DK, State.U4b, '"Thats fine. It took me a long time to figure out what I really want to do either. I actually know a lot about different jobs now, such as business analyst, investment banking analyst, business consultant, software engineer, data analyst, wed developer, product manager… Which one are you interested in? I can tell you what I know about it."')

df.add_user_transition(State.U4a, State.S5, '[$why_posadj=#POS(adj)]')
df.set_error_successor(State.U4a, error_successor=State.ERR4)
df.add_user_transition(State.U4b, State.S6b, '[$pos={/.*/}]')

df.add_system_transition(State.S5, State.U5, '[!"Yeah for sure, it is" $why_posadj ". What kind of skills do you think that employees value for this position?"]')
df.add_system_transition(State.ERR4, State.U5, '"You have interesting insights. What kind of skills do you think that employees value for this position?"')

df.add_system_transition(State.S6b, State.U1, '[!You know what, top five skills for a $pos are":" #posSkill Do you feel that you are ready for this job"?" We can always talk about this anytime. For now, where else do you want to work"?"]')

df.add_user_transition(State.U5, State.S6a, "/.*/")
df.add_system_transition(State.S6a, State.U1, '[!Absolutely"." Top five skills for a $pos are":" #posSkill You should try to build these skillset in order to get a job"." Now, where else do you want to work"?"]')

df.run(debugging=True)