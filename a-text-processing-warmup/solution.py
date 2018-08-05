# https://www.hackerrank.com/challenges/a-text-processing-warmup

import sys
import re


# '15/11/2012','15/11/12', '15th March 1999','15th March 99' or '20th of March, 1999').

# You can make the following assumptions 

# 1) In the date, year and day will always be in numeric form. 
# Which means, you don't have to worry about "fifteenth" or "twentieth" etc. 
# Month, could be either numeric form (1-12) or with its name (January-December, Jan-Dec).

# 2) This is a bit open ended, and somewhat intentionally so. 
# The aim is for you to try to write something which figures out as many common patterns as possible, in which dates are present in text.

# 3) Most of the test cases are Wikipedia articles. 
# Having a look at the common formats in which dates occur in those, will help.

# 4) Dates could either be in the form: 
# Month followed by Day followed by Year, or Day followed by Month followed by Year.

# 5) The day could be in the form of either (1,2,3,...31) or (1st, 2nd, 3rd...31st).


def count_data(line, p_a, p_an, p_the, p_date):
    count = []
    count.append(p_a.findall(line))
    count.append(p_an.findall(line))
    count.append(p_the.findall(line))
    count.append(p_date.findall(line))
    # 4T lines, four lines of output for each test case. 
    # First line -> number of occurrences of 'a'. 
    # Second line -> number of occurrences of 'an'. 
    # Third Line -> number of occurrences of 'the'. 
    # Fourth Line -> number of occurrences of date information.
    # print(count[3])
    print("\n".join(map(lambda x: str(len(x)), count)))

if __name__ == '__main__':

    s = sys.stdin.read()
    lines = list(
        filter(
            lambda x: x != " " and x != "",
            s.split("\n")))[1:]

    # print(lines)
    # print(list(map(read_data, lines)))

    p_a = re.compile(r"\ba\b", re.IGNORECASE)
    p_an = re.compile(r"\ban\b", re.IGNORECASE)
    p_the = re.compile(r"\bthe\b", re.IGNORECASE)

    months = "January|February|March|April|May|June|July|August|September|October|November|December"
    months3 = "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec"
    allmonths = months + "|" + months3 
    p1str = r"\d\d?/\d\d?/\d\d?\d?\d?"
    p2str = r"(\d\d?)(st|nd|rd|th)?\s+(of\s+)?(" + allmonths + r")(\s*,)?\s+(\d\d?\d?\d?)"
    p3str = "(" + allmonths + r")\s+(\d\d?)(st|nd|rd|th)?(\s*,)?\s+(\d\d?\d?\d?)"
    pstr = "(" + "|".join([p1str, p2str, p3str]) + ")"
    p_date = re.compile(pstr)

    for l in lines:
        count_data(l, p_a, p_an, p_the, p_date)
    # print(p.findall("December 16, 1773 10 May 1857 15/11/2012,15/11/12, 15th March 1999,15th March 99 or 20th of March, 1999"))






