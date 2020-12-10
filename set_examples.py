
food = ['spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam', 'spam', 'spam', 'spam', 'spam', 'toast',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', ]

unique_foods = set(food)

print(unique_foods, '\n')

bob_countries = ['Spain', 'Bulgaria', 'UK', 'UK', 'UK', 'Israel', 'UK', 'Canada', 'Mexico', 'China']
mary_countries = ['Spain', 'Denmark', 'Japan', 'UK', 'Mexico', 'Vietnam', 'New Zealand', 'Mozambique']

bob = set(bob_countries)
mary = set(mary_countries)

print(bob)
print(mary)
print()

print("both:", bob & mary)
print("only one:", bob ^ mary)
print("either:", bob | mary)
print("just Bob:", bob - mary)
print("just Mary:", mary - bob)





