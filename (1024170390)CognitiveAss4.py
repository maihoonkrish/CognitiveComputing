#Q1
import pandas as pd

fixed_entries = [
    {"question": "what is the annual fee", "answer": "The annual fee is Rs 500.",
     "keywords": "fee cost price charge", "category": "billing"},
    {"question": "how to reset password", "answer": "Go to Settings > Reset Password.",
     "keywords": "password reset login", "category": "account"},
    {"question": "what are your working hours", "answer": "We are open 9 AM to 5 PM.",
     "keywords": "hours timing open time", "category": "general"},
    {"question": "how can i pay the fee", "answer": "You can pay via UPI, card, or net banking.",
     "keywords": "pay payment upi fee", "category": "billing"}
]

roll_number = '1024170390'

last_two_digits_str = str(roll_number)[-2:]
digit1 = int(last_two_digits_str[0])
digit2 = int(last_two_digits_str[1])

categories = ["billing", "account", "general"]

generated_entries = []

category1 = categories[digit1 % 3]

if category1 == "billing":
    q1 = f"What is the due date for {digit1}th month's bill?"
    a1 = f"The due date for the {digit1}th month's bill is the 15th of the next month."
    k1 = "due date bill payment"
elif category1 == "account":
    q1 = f"How do I update my {digit1}th contact information?"
    a1 = f"You can update your contact information by logging into your account and navigating to the \"Profile\" section."
    k1 = "update contact profile"
else:
    q1 = f"What are the general services related to query {digit1}?"
    a1 = f"We offer a wide range of general services including support for various queries and assistance."
    k1 = "services general assistance"

generated_entries.append({"question": q1, "answer": a1, "keywords": k1, "category": category1})

category2 = categories[digit2 % 3]

if category2 == "billing":
    q2 = f"Can I get a detailed invoice for the last {digit2} months?"
    a2 = f"Yes, detailed invoices for the last {digit2} months are available in your billing history section."
    k2 = "invoice detailed history"
elif category2 == "account":
    q2 = f"How to link another account to my existing profile (digit {digit2})?"
    a2 = f"You can link another account through the 'Account Settings' page by selecting 'Link Account'."
    k2 = "link account settings"
else:
    q2 = f"Where can I find FAQs related to topic {digit2}?"
    a2 = f"All frequently asked questions related to topic {digit2} can be found in our 'Help Center'."
    k2 = "faq help topics"

generated_entries.append({"question": q2, "answer": a2, "keywords": k2, "category": category2})

all_entries = fixed_entries + generated_entries

df_faq = pd.DataFrame(all_entries)

print(df_faq)


#Q2
def score_query(query_string, df):
    query_tokens = set(query_string.lower().split())

    # Calculate scores for each FAQ entry
    scores = []
    for index, row in df.iterrows():
        faq_keywords = set(row['keywords'].lower().split())
        # Calculate the number of overlapping keywords
        matching_keywords_count = len(query_tokens.intersection(faq_keywords))
        scores.append({'entry': row.to_dict(), 'score': matching_keywords_count})

    # Sort entries by score in descending order
    ranked_entries = sorted(scores, key=lambda x: x['score'], reverse=True)

    # Filter out entries with a score of 0 (no match)
    matching_entries = [entry for entry in ranked_entries if entry['score'] > 0]

    return matching_entries


# Demonstrate the scoring function with an example query
query = "how to pay my fee"
results = score_query(query, df_faq)

print(f"\nQuery: '{query}'")
if results:
    print("Matching FAQ entries (ranked by confidence):")
    for item in results:
        print(f"  Score: {item['score']}, Question: {item['entry']['question']}")
else:
    print("No matching FAQ entries found for this query.")
