#Lambda Excercise 1

#Consider the List

prog_lang = [('Python', 3.8),
    ('Java', 13),
    ('JavaScript', 2019),
    ('Scala', 2.13)]


#1. Sort the list by each language's version in ascending order.
#[('Scala', 2.13), ('Python', 3.8), ('Java', 13), ('JavaScript', 2019)]
sort_language = sorted(prog_lang, key = lambda lang: lang[1])
print(sort_language)
#2. Sort the list by the length of the name of each language in descending order.
#[('JavaScript', 2019), ('Python', 3.8), ('Scala', 2.13), ('Java', 13)]
sort_length = sorted(prog_lang, key = lambda l: len(l[0]), reverse = True)
print(sort_length)
#3. Filter the list so that it only contains languages with 'a' in it.
#[('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]
filter_lang = list(filter(lambda l : "a" in l[0], prog_lang))
print(filter_lang)

#4. Filter the list so that it only contains languages whose version is in integer form.
#[('Java', 13), ('JavaScript', 2019)]
filter_int = list(filter(lambda v : type(v[1]) == int, prog_lang))
print(filter_int)
#5. Transform the list so that it contains the tuples in the form,
#("language in all lower case", length of the language string)
#[('python', 6), ('java', 4), ('javascript', 10), ('scala', 5)]
lang_lower = list(map(lambda l: l[0].lower(), prog_lang))
print(lang_lower)
#6. Generate a tuple in the form,
#("All languages separated by commas","All versions separated by commas")
#('Python,Java,JavaScript,Scala', '3.8,13,2019,2.13')
lang_versions = tuple(map (lambda lang : lang[0], prog_lang)), tuple(map (lambda lang : lang[1], prog_lang))
print(lang_versions)