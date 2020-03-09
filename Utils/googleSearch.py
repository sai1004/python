
"""   Google Search """

# Install following two packages before executing the code below

# pip install beautifulsoup4

# pip install google

try:

    from googlesearch import search

except ImportError:

    print("No module named 'google' found")

# to search
print("getting result please be hold on")
query = "corona"

for j in search(query, tld="co.in", num=10, stop=1, pause=2):

    print(j)
