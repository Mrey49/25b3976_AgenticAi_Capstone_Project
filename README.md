As we enter our second year we are now allowed to take courses apart from our core courses but that is a big headache as if we finalise the courses which we want to take based on our interests after spending a lot of time on ASC portal then we face challenges like slot clash, credits issue, we wanted to take this course as minor but it is available as elective and the prequistes required. So to solve this problem i build an AgenticAi Planner. I am myself a upcoming sophomore in elec so i created a comprehensive course database (database.py) containing all compulsory Semester 3 courses along with every hasmed elective, institute elective, department elective and minor course available to me. For each course, I included information such as:

Course code and title
Credits
Department
Course category
Time slot
Full-semester or half-semester offering
Interest tags for semantic matching

I also made (timetable.py) that is actual IITB timetable of 2025-26 year, allowing the planner to accurately detect slot clashes and generate conflict-free schedules.I then made rag.py which uses rag model to retrieve all the infoabout category of the student,credits allowed from the ugrulebook.Instead of hardcoding the ugrulebook rules i used rag as it will help just to put the new updated rulebook instead of changing the whole code.

**How the Planner Works**
The overall workflow is shown below:

Student Input-->Rulebook Validator Agent-->Eligibility Agent-->Candidate Generator Agent-->Ranking Agent-->Planner Agent-->Final Semester Plan

Rulebook Validator Agent
The first agent validates the student's registration according to the IIT Bombay Undergraduate Rulebook.
Using the RAG implemented in rag.py, the agent retrieves only the relevant sections of the rulebook related to semester registration. Based on the student's academic information, including CPI and academic standing, Gemini determines:
Academic Category (Category I–VI)
Maximum permissible registration credits
Minimum semester credits
Important registration remarks
This ensures that all subsequent planning decisions comply with the official institute regulations.

Eligibility Agent
Once the registration rules have been determined, the Eligibility Agent verifies whether the student's requested semester is valid.
The agent checks:
Maximum allowable registration credits
Minimum credit requirements
Requested semester credits
Overall registration eligibility
If the student's requested credits violate the UG Rulebook, the planner immediately informs the student instead of producing an invalid timetable.

Candidate Generator Agent
The Candidate Generator Agent prepares the pool of elective courses that can potentially be recommended.
The agent automatically removes:
Compulsory courses already included in the semester
Courses that are not available for Semester 3
Courses that are not eligible for the student
The remaining courses become the candidate list for recommendation.

Ranking Agent
The Academic Advisor Agent is responsible for recommending electives based on the student's interests.
Instead of using simple keyword matching, the planner uses Google Gemini to perform semantic understanding of the student's interests.

For example:
AI → Machine Learning, Deep Learning, Computer Vision
Mathematics → Statistics, Optimization
Finance → Financial Engineering
Security → Cryptography

Each recommended course is assigned:
A relevance score
A ranking
A short explanation describing why the course matches the student's interests

The planner also validates every recommendation against the local course database to ensure that no hallucinated course recommendations are accepted.

Planner Agent
The Planner Agent constructs the final semester schedule.
It combines:Compulsory Semester 3 courses and the AI-recommended courses

The planner then performs several constraint checks before finalizing the schedule:
Timetable slot clashes
Credit limits
Duplicate courses

**How to use**

I have created .env file just add your api key there and then run app.py
Enter your cpi,other things which it asks and your interests and then enjoy this planner instead of manually wasting so much time on Internal ASC

Ps: It contains courses of every department even of Policy Studies,Climate Change etc.
