import re

# Match only the three sentences exactly
my_pattern = r"(It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.)"

# Compile the regex
my_regex = re.compile(my_pattern)

