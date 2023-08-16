def extract_category(text):
    # List of keywords and corresponding categories
    categories = {
        "technology": ["tech", "gadget", "software", "hardware"],
        "politics": ["politics", "government", "election", "policy"],
        "health": ["health", "wellness", "medical", "fitness"],
         "business": ["business", "economy", "finance", "startup", "market", "industry"],
        "science": ["science", "research", "discovery", "experiment", "innovation"],
        "environment": ["environment", "climate", "sustainability", "ecology", "conservation"],
        "sports": ["sports", "athlete", "competition", "tournament", "game"],
        "entertainment": ["entertainment", "celebrity", "film", "music", "arts", "culture"],
        "travel": ["travel", "destination", "adventure", "tourism", "exploration"],
        "education": ["education", "learning", "school", "university", "student"],
        "lifestyle": ["lifestyle", "fashion", "food", "home", "style"],
    }
    
    text_lower = text.lower()  # Convert text to lowercase for case-insensitive matching
    
    # Find matching categories based on keywords
    matching_categories = []
    for category, keywords in categories.items():
        if any(keyword in text_lower for keyword in keywords):
            matching_categories.append(category)
    
    if matching_categories:
        return matching_categories
    else:
        return ["unknown"]  # Default category if no match is found

