MVP: Natural Language Query Tool for Excel/CSV Data (AI-assisted)

Summary
Project Goal
Build a minimal MVP that allows a user to ask five predefined business questions in natural language and receive deterministic, Excel-verifiable answers from a CSV dataset.
This is a proof of concept, not a production system.
________________________________________
Scope (Strictly Limited)
Data
•	Input: Single CSV file (provided)
•	Read-only
•	No database required
Supported Questions (Fixed Intents)
The system must support only the following five question types:
1.	What items are late right now?
2.	What items are required in the next 30 days but have not been received?
3.	What is the current status of item X?
4.	For workpack X, how many items are dispatched, received, and installed?
5.	Which items have a variance between forecast arrival date and received date?
No additional questions, summaries, or insights are allowed.
________________________________________
Natural Language Flexibility (Bounded)
•	Users may phrase questions slightly differently (paraphrases).
•	Each user query must map to one and only one of the five supported question types.
•	AI is used only to:
o	Classify which of the five question intents applies
o	Extract required parameters (e.g. item number, workpack ID)

Out-of-Scope Handling (Required)
If a query:
•	Does not clearly map to one of the five supported questions, or
•	Is ambiguous or outside scope
The system must refuse to answer and return a message such as:
“I can only answer these 5 question types. Try asking like: …”
There must be no attempt to guess, infer, or answer anyway.
________________________________________
Technical Requirements
•	Deterministic data processing (Python preferred)
•	AI (OpenAI or Azure OpenAI) used only for:
o	Intent classification
o	Parameter extraction
•	All calculations must be reproducible in Excel
•	No AI reasoning, analysis, or calculation over the data
•	Same input must always return the same output
No vector databases, RAG pipelines, or complex frameworks are required.
________________________________________
Output Requirements
For every successful query, return:
•	Interpreted question (which of the 5 intents)
•	Filters and rules applied (plain English)
•	Total count of matching records
•	Tabular preview of 5–10 rows
UI can be:
•	Simple web page, or
•	Streamlit app
UI quality is not important.
