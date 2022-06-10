import pandas as pd
from english_words import english_words_lower_alpha_set
import pandasql as ps
import re

words = pd.DataFrame(english_words_lower_alpha_set)

url = 'https://gist.githubusercontent.com/scholtes/94f3c0303ba6a7768b47583aff36654d/raw/d9cddf5e16140df9e14f19c2de76a0ef36fd2748/wordle-La.txt'


wordle_words = pd.read_csv(url,names=["words"])

words.rename(columns = {list(words)[0]: 'words'}, inplace = True)

words_filter = (words['words'].str.len() == 5)

words_df = words.loc[words_filter]

alphabet_list = ['a','b','c','d','e','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


print('The word axiom will be used as an example.')
print('Please fill out green letters like this: -x--m')
print('If you didn\'t guess any green letters, just hit enter')
print('First Guess Green Letters >')
guess_1_green_letter = input()
guess_1_green_letter = guess_1_green_letter.replace('-', '_')

print('List yellow leters like this: a-i--')
print('If you hit enter like you would (and should) with green, this will cause the script to fail so don\'t do that.')
print('First Guess Yellow Letters >')
guess_1_yellow = input()
guess_1_yellow_df = ','.join(guess_1_yellow)
guess_1_yellow_df = guess_1_yellow_df.split(",")
guess_1_yellow_isin = '[' + guess_1_yellow.replace('-', '') + ']'
guess_1_yellow_list = guess_1_yellow.replace('-','')
guess_1_yellow_list = re.sub(r'([a-z])(?!$)', r'\1,', guess_1_yellow_list)
guess_1_yellow_list = guess_1_yellow_list.split(",")

print('List grey leters like this: xom')
print('First Guess grey Letters >')
guess_1_grey = input()
guess_1_grey = '[' + guess_1_grey + ']'


if guess_1_green_letter == '':
    q1 = f"""
        SELECT * 
        FROM wordle_words
        """
    words_df1_green = ps.sqldf(q1, locals())
    
elif guess_1_green_letter != '':
    q1 = f"""
        SELECT * 
        FROM wordle_words
        WHERE words like '{guess_1_green_letter}'
        """
    words_df1_green = ps.sqldf(q1, locals())

if re.match('[-]', guess_1_yellow_df[0]) or guess_1_yellow_df[0] == '':
    words_yellow_df1 = words_df1_green

elif re.match('[a-z]', guess_1_yellow_df[0]):
    yellow_position_1 = 'WHERE words NOT LIKE ' + "'" + guess_1_yellow_df[0] + '____' + "'"
    query1 = f"""
        SELECT * 
        FROM words_df1_green
        {yellow_position_1}
        """
    words_yellow_df1 = ps.sqldf(query1, locals())

if re.match('[-]', guess_1_yellow_df[1]) or guess_1_yellow_df[1] == '':
    words_yellow_df2 = words_yellow_df1

elif re.match('[a-z]', guess_1_yellow_df[1]):
    yellow_position_2 = 'WHERE words NOT LIKE ' + "'" + '_' + guess_1_yellow_df[1] + '___' + "'"
    query2 = f"""
        SELECT * 
        FROM words_yellow_df1
        {yellow_position_2}
        """
    words_yellow_df2 = ps.sqldf(query2, locals())

if re.match('[-]', guess_1_yellow_df[2]) or guess_1_yellow_df[2] == '':
    words_yellow_df3 = words_yellow_df2

elif re.match('[a-z]', guess_1_yellow_df[2]):
    yellow_position_3 = 'WHERE words NOT LIKE ' + "'" + '__' + guess_1_yellow_df[2] + '__' + "'"
    query3 = f"""
        SELECT * 
        FROM words_yellow_df2
        {yellow_position_3}
        """
    words_yellow_df3 = ps.sqldf(query3, locals())

if re.match('[-]', guess_1_yellow_df[3]) or guess_1_yellow_df[3] == '':
    words_yellow_df4 = words_yellow_df3

elif re.match('[a-z]', guess_1_yellow_df[3]):
    yellow_position_4 = 'WHERE words NOT LIKE ' + "'" + '___' + guess_1_yellow_df[3] + '_' + "'"
    query4 = f"""
        SELECT * 
        FROM words_yellow_df3
        {yellow_position_4}
        """
    words_yellow_df4 = ps.sqldf(query4, locals())

if re.match('[-]', guess_1_yellow_df[4]) or guess_1_yellow_df[4] == '':
    words_yellow_df5 = words_yellow_df4

elif re.match('[a-z]', guess_1_yellow_df[4]):
    yellow_position_5 = 'WHERE words NOT LIKE ' + "'" + '____' + guess_1_yellow_df[4] + "'"
    query5 = f"""
        SELECT * 
        FROM words_yellow_df4
        {yellow_position_5}
        """
    words_yellow_df5 = ps.sqldf(query5, locals())


if guess_1_grey == '':
    for letters in guess_1_yellow_list:
        words_yellow_df5 = words_yellow_df5[words_yellow_df5['words'].str.contains(letters, regex=False)]
    first_guess_df = words_yellow_df5

elif guess_1_grey  != '':
    for letters in guess_1_yellow_list:
        words_yellow_df5 = words_yellow_df5[words_yellow_df5['words'].str.contains(letters, regex=False)]
    first_guess_df = words_yellow_df5[~words_yellow_df5['words'].str.contains(guess_1_grey, regex=True)]

print(first_guess_df)


#####################################################################################################


print('The word axiom will be used as an example.')
print('Please fill out green letters like this: -x--m')
print('If you didn\'t guess any green letters, just hit enter')
print('Second Guess Green Letters >')
guess_2_green_letter = input()
guess_2_green_letter = guess_2_green_letter.replace('-', '_')

print('List yellow leters like this: a-i--')
print('If you hit enter like you would (and should) with green, this will cause the script to fail so don\'t do that.')
print('Second Guess Yellow Letters >')
guess_2_yellow = input()
guess_2_yellow_df = ','.join(guess_2_yellow)
guess_2_yellow_df = guess_2_yellow_df.split(",")
guess_2_yellow_isin = '[' + guess_2_yellow.replace('-', '') + ']'
guess_2_yellow_list = guess_2_yellow.replace('-','')
guess_2_yellow_list = re.sub(r'([a-z])(?!$)', r'\1,', guess_2_yellow_list)
guess_2_yellow_list = guess_2_yellow_list.split(",")

print('List grey leters like this: xom')
print('Second Guess grey Letters >')
guess_2_grey = input()
guess_2_grey = '[' + guess_2_grey + ']'


if guess_2_green_letter == '':
    q1 = f"""
        SELECT * 
        FROM first_guess_df
        """
    words_df1_green = ps.sqldf(q1, locals())
    
elif guess_2_green_letter != '':
    q1 = f"""
        SELECT * 
        FROM first_guess_df
        WHERE words like '{guess_2_green_letter}'
        """
    words_df1_green = ps.sqldf(q1, locals())


if re.match('[-]', guess_2_yellow_df[0]) or guess_2_yellow_df[0] == '':
    words_yellow_df1 = words_df1_green

elif re.match('[a-z]', guess_2_yellow_df[0]):
    yellow_position_1 = 'WHERE words NOT LIKE ' + "'" + guess_2_yellow_df[0] + '____' + "'"
    query1 = f"""
        SELECT * 
        FROM words_df1_green
        {yellow_position_1}
        """
    words_yellow_df1 = ps.sqldf(query1, locals())


if re.match('[-]', guess_2_yellow_df[1]) or guess_2_yellow_df[2] == '':
    words_yellow_df2 = words_yellow_df1

elif re.match('[a-z]', guess_2_yellow_df[1]):
    yellow_position_2 = 'WHERE words NOT LIKE ' + "'" + '_' + guess_2_yellow_df[1] + '___' + "'"
    query2 = f"""
        SELECT * 
        FROM words_yellow_df1
        {yellow_position_2}
        """
    words_yellow_df2 = ps.sqldf(query2, locals())


if re.match('[-]', guess_2_yellow_df[2]):
    words_yellow_df3 = words_yellow_df2

elif re.match('[a-z]', guess_2_yellow_df[2]):
    yellow_position_3 = 'WHERE words NOT LIKE ' + "'" + '__' + guess_2_yellow_df[2] + '__' + "'"
    query3 = f"""
        SELECT * 
        FROM words_yellow_df2
        {yellow_position_3}
        """
    words_yellow_df3 = ps.sqldf(query3, locals())


if re.match('[-]', guess_2_yellow_df[3]) or guess_2_yellow_df[3] == '':
    words_yellow_df4 = words_yellow_df3

elif re.match('[a-z]', guess_2_yellow_df[3]):
    yellow_position_4 = 'WHERE words NOT LIKE ' + "'" + '___' + guess_2_yellow_df[3] + '_' + "'"
    query4 = f"""
        SELECT * 
        FROM words_yellow_df3
        {yellow_position_4}
        """
    words_yellow_df4 = ps.sqldf(query4, locals())


if re.match('[-]', guess_2_yellow_df[4]) or guess_2_yellow_df[4] == '':
    words_yellow_df5 = words_yellow_df4

elif re.match('[a-z]', guess_2_yellow_df[4]):
    yellow_position_5 = 'WHERE words NOT LIKE ' + "'" + '____' + guess_2_yellow_df[4] + "'"
    query5 = f"""
        SELECT * 
        FROM words_yellow_df4
        {yellow_position_5}
        """
    words_yellow_df5 = ps.sqldf(query5, locals())

if guess_2_grey == '':
    for letters in guess_2_yellow_list:
        words_yellow_df5 = words_yellow_df5[words_yellow_df5['words'].str.contains(letters, regex=False)]
    second_guess_df = words_yellow_df5

elif guess_2_grey  != '':
    for letters in guess_2_yellow_list:
        words_yellow_df5 = words_yellow_df5[words_yellow_df5['words'].str.contains(letters, regex=False)]
    second_guess_df = words_yellow_df5[~words_yellow_df5['words'].str.contains(guess_2_grey, regex=True)]

print(second_guess_df)


#####################################################################################################


print('The word axiom will be used as an example.')
print('Please fill out green letters like this: -x--m')
print('If you didn\'t guess any green letters, just hit enter')
print('Third Guess Green Letters >')
guess_3_green_letter = input()
guess_3_green_letter = guess_3_green_letter.replace('-', '_')

print('List yellow leters like this: a-i--')
print('If you hit enter like you would (and should) with green, this will cause the script to fail so don\'t do that.')
print('Third Guess Yellow Letters >')
guess_3_yellow = input()
guess_3_yellow_df = ','.join(guess_3_yellow)
guess_3_yellow_df = guess_3_yellow_df.split(",")
guess_3_yellow_isin = '[' + guess_3_yellow.replace('-', '') + ']'
guess_3_yellow_list = guess_3_yellow.replace('-','')
guess_3_yellow_list = re.sub(r'([a-z])(?!$)', r'\1,', guess_3_yellow_list)
guess_3_yellow_list = guess_3_yellow_list.split(",")

print('List grey leters like this: xom')
print('Third Guess grey Letters >')
guess_3_grey = input()
guess_3_grey = '[' + guess_3_grey + ']'


if guess_3_green_letter == '':
    q1 = f"""
        SELECT * 
        FROM second_guess_df
        """
    words_df1_green = ps.sqldf(q1, locals())
    
elif guess_3_green_letter != '':
    q1 = f"""
        SELECT * 
        FROM second_guess_df
        WHERE words like '{guess_3_green_letter}'
        """
    words_df1_green = ps.sqldf(q1, locals())



if re.match('[-]', guess_3_yellow_df[0]) or guess_3_yellow_df[0] == '':
    words_yellow_df1 = words_df1_green

elif re.match('[a-z]', guess_3_yellow_df[0]):
    yellow_position_1 = 'WHERE words NOT LIKE ' + "'" + guess_3_yellow_df[0] + '____' + "'"
    query1 = f"""
        SELECT * 
        FROM words_df1_green
        {yellow_position_1}
        """
    words_yellow_df1 = ps.sqldf(query1, locals())

if re.match('[-]', guess_3_yellow_df[1]) or guess_3_yellow_df[1] == '':
    words_yellow_df2 = words_yellow_df1


elif re.match('[a-z]', guess_3_yellow_df[1]):
    yellow_position_2 = 'WHERE words NOT LIKE ' + "'" + '_' + guess_3_yellow_df[1] + '___' + "'"
    query2 = f"""
        SELECT * 
        FROM words_yellow_df1
        {yellow_position_2}
        """
    words_yellow_df2 = ps.sqldf(query2, locals())

if re.match('[-]', guess_3_yellow_df[2]) or guess_3_yellow_df[2] == '':
    words_yellow_df3 = words_yellow_df2


elif re.match('[a-z]', guess_3_yellow_df[2]):
    yellow_position_3 = 'WHERE words NOT LIKE ' + "'" + '__' + guess_3_yellow_df[2] + '__' + "'"
    query3 = f"""
        SELECT * 
        FROM words_yellow_df2
        {yellow_position_3}
        """
    words_yellow_df3 = ps.sqldf(query3, locals())

if re.match('[-]', guess_3_yellow_df[3]) or guess_3_yellow_df[3] == '':
    words_yellow_df4 = words_yellow_df3


elif re.match('[a-z]', guess_3_yellow_df[3]):
    yellow_position_4 = 'WHERE words NOT LIKE ' + "'" + '___' + guess_3_yellow_df[3] + '_' + "'"
    query4 = f"""
        SELECT * 
        FROM words_yellow_df3
        {yellow_position_4}
        """
    words_yellow_df4 = ps.sqldf(query4, locals())


if re.match('[-]', guess_3_yellow_df[4]) or guess_3_yellow_df[4] == '':
    words_yellow_df5 = words_yellow_df4

elif re.match('[a-z]', guess_3_yellow_df[4]):
    yellow_position_5 = 'WHERE words NOT LIKE ' + "'" + '____' + guess_3_yellow_df[4] + "'"
    query5 = f"""
        SELECT * 
        FROM words_yellow_df4
        {yellow_position_5}
        """
    words_yellow_df5 = ps.sqldf(query5, locals())


if guess_3_grey == '':
    for letters in guess_3_yellow_list:
        words_yellow_df5 = words_yellow_df5[words_yellow_df5['words'].str.contains(letters, regex=False)]
    third_guess_df = words_yellow_df5

elif guess_3_grey  != '':
    for letters in guess_3_yellow_list:
        words_yellow_df5 = words_yellow_df5[words_yellow_df5['words'].str.contains(letters, regex=False)]
    third_guess_df = words_yellow_df5[~words_yellow_df5['words'].str.contains(guess_3_grey, regex=True)]

print(third_guess_df)


#####################################################################################################


print('The word axiom will be used as an example.')
print('Please fill out green letters like this: -x--m')
print('If you didn\'t guess any green letters, just hit enter')
print('Fourth Guess Green Letters >')
guess_3_green_letter = input()
guess_3_green_letter = guess_3_green_letter.replace('-', '_')

print('List yellow leters like this: a-i--')
print('If you hit enter like you would (and should) with green, this will cause the script to fail so don\'t do that.')
print('Fourth Guess Yellow Letters >')
guess_3_yellow = input()
guess_3_yellow_df = ','.join(guess_3_yellow)
guess_3_yellow_df = guess_3_yellow_df.split(",")
guess_3_yellow_isin = '[' + guess_3_yellow.replace('-', '') + ']'
guess_3_yellow_list = guess_3_yellow.replace('-','')
guess_3_yellow_list = re.sub(r'([a-z])(?!$)', r'\1,', guess_3_yellow_list)
guess_3_yellow_list = guess_3_yellow_list.split(",")

print('List grey leters like this: xom')
print('Fourth Guess grey Letters >')
guess_3_grey = input()
guess_3_grey = '[' + guess_3_grey + ']'


if guess_3_green_letter == '':
    q1 = f"""
        SELECT * 
        FROM third_guess_df
        """
    words_df1_green = ps.sqldf(q1, locals())
    
elif guess_3_green_letter != '':
    q1 = f"""
        SELECT * 
        FROM third_guess_df
        WHERE words like '{guess_3_green_letter}'
        """
    words_df1_green = ps.sqldf(q1, locals())


if re.match('[-]', guess_3_yellow_df[0]) or guess_3_yellow_df[0] == '':
    words_yellow_df1 = words_df1_green

elif re.match('[a-z]', guess_3_yellow_df[0]):
    yellow_position_1 = 'WHERE words NOT LIKE ' + "'" + guess_3_yellow_df[0] + '____' + "'"
    query1 = f"""
        SELECT * 
        FROM words_df1_green
        {yellow_position_1}
        """
    words_yellow_df1 = ps.sqldf(query1, locals())

if re.match('[-]', guess_3_yellow_df[1]) or guess_3_yellow_df[1] == '':
    words_yellow_df2 = words_yellow_df1


elif re.match('[a-z]', guess_3_yellow_df[1]):
    yellow_position_2 = 'WHERE words NOT LIKE ' + "'" + '_' + guess_3_yellow_df[1] + '___' + "'"
    query2 = f"""
        SELECT * 
        FROM words_yellow_df1
        {yellow_position_2}
        """
    words_yellow_df2 = ps.sqldf(query2, locals())

if re.match('[-]', guess_3_yellow_df[2]) or guess_3_yellow_df[2] == '':
    words_yellow_df3 = words_yellow_df2


elif re.match('[a-z]', guess_3_yellow_df[2]):
    yellow_position_3 = 'WHERE words NOT LIKE ' + "'" + '__' + guess_3_yellow_df[2] + '__' + "'"
    query3 = f"""
        SELECT * 
        FROM words_yellow_df2
        {yellow_position_3}
        """
    words_yellow_df3 = ps.sqldf(query3, locals())

if re.match('[-]', guess_3_yellow_df[3]) or guess_3_yellow_df[3] == '':
    words_yellow_df4 = words_yellow_df3


elif re.match('[a-z]', guess_3_yellow_df[3]):
    yellow_position_4 = 'WHERE words NOT LIKE ' + "'" + '___' + guess_3_yellow_df[3] + '_' + "'"
    query4 = f"""
        SELECT * 
        FROM words_yellow_df3
        {yellow_position_4}
        """
    words_yellow_df4 = ps.sqldf(query4, locals())


if re.match('[-]', guess_3_yellow_df[4]) or guess_3_yellow_df[4] == '':
    words_yellow_df5 = words_yellow_df4

elif re.match('[a-z]', guess_3_yellow_df[4]):
    yellow_position_5 = 'WHERE words NOT LIKE ' + "'" + '____' + guess_3_yellow_df[4] + "'"
    query5 = f"""
        SELECT * 
        FROM words_yellow_df4
        {yellow_position_5}
        """
    words_yellow_df5 = ps.sqldf(query5, locals())


if guess_3_grey == '':
    for letters in guess_3_yellow_list:
        words_yellow_df5 = words_yellow_df5[words_yellow_df5['words'].str.contains(letters, regex=False)]
    fourth_guess_df = words_yellow_df5

elif guess_3_grey  != '':
    for letters in guess_3_yellow_list:
        words_yellow_df5 = words_yellow_df5[words_yellow_df5['words'].str.contains(letters, regex=False)]
    fourth_guess_df = words_yellow_df5[~words_yellow_df5['words'].str.contains(guess_3_grey, regex=True)]

print(fourth_guess_df)


#####################################################################################################


print('The word axiom will be used as an example.')
print('Please fill out green letters like this: -x--m')
print('If you didn\'t guess any green letters, just hit enter')
print('Fifth Guess Green Letters >')
guess_3_green_letter = input()
guess_3_green_letter = guess_3_green_letter.replace('-', '_')

print('List yellow leters like this: a-i--')
print('If you hit enter like you would (and should) with green, this will cause the script to fail so don\'t do that.')
print('Fifth Guess Yellow Letters >')
guess_3_yellow = input()
guess_3_yellow_df = ','.join(guess_3_yellow)
guess_3_yellow_df = guess_3_yellow_df.split(",")
guess_3_yellow_isin = '[' + guess_3_yellow.replace('-', '') + ']'
guess_3_yellow_list = guess_3_yellow.replace('-','')
guess_3_yellow_list = re.sub(r'([a-z])(?!$)', r'\1,', guess_3_yellow_list)
guess_3_yellow_list = guess_3_yellow_list.split(",")

print('List grey leters like this: xom')
print('Fifth Guess grey Letters >')
guess_3_grey = input()
guess_3_grey = '[' + guess_3_grey + ']'


if guess_3_green_letter == '':
    q1 = f"""
        SELECT * 
        FROM third_guess_df
        """
    words_df1_green = ps.sqldf(q1, locals())
    
elif guess_3_green_letter != '':
    q1 = f"""
        SELECT * 
        FROM third_guess_df
        WHERE words like '{guess_3_green_letter}'
        """
    words_df1_green = ps.sqldf(q1, locals())

if re.match('[-]', guess_3_yellow_df[0]) or guess_3_yellow_df[0] == '':
    words_yellow_df1 = words_df1_green

elif re.match('[a-z]', guess_3_yellow_df[0]):
    yellow_position_1 = 'WHERE words NOT LIKE ' + "'" + guess_3_yellow_df[0] + '____' + "'"
    query1 = f"""
        SELECT * 
        FROM words_df1_green
        {yellow_position_1}
        """
    words_yellow_df1 = ps.sqldf(query1, locals())

if re.match('[-]', guess_3_yellow_df[1]) or guess_3_yellow_df[1] == '':
    words_yellow_df2 = words_yellow_df1

elif re.match('[a-z]', guess_3_yellow_df[1]):
    yellow_position_2 = 'WHERE words NOT LIKE ' + "'" + '_' + guess_3_yellow_df[1] + '___' + "'"
    query2 = f"""
        SELECT * 
        FROM words_yellow_df1
        {yellow_position_2}
        """
    words_yellow_df2 = ps.sqldf(query2, locals())

if re.match('[-]', guess_3_yellow_df[2]) or guess_3_yellow_df[2] == '':
    words_yellow_df3 = words_yellow_df2

elif re.match('[a-z]', guess_3_yellow_df[2]):
    yellow_position_3 = 'WHERE words NOT LIKE ' + "'" + '__' + guess_3_yellow_df[2] + '__' + "'"
    query3 = f"""
        SELECT * 
        FROM words_yellow_df2
        {yellow_position_3}
        """
    words_yellow_df3 = ps.sqldf(query3, locals())

if re.match('[-]', guess_3_yellow_df[3]) or guess_3_yellow_df[3] == '':
    words_yellow_df4 = words_yellow_df3

elif re.match('[a-z]', guess_3_yellow_df[3]):
    yellow_position_4 = 'WHERE words NOT LIKE ' + "'" + '___' + guess_3_yellow_df[3] + '_' + "'"
    query4 = f"""
        SELECT * 
        FROM words_yellow_df3
        {yellow_position_4}
        """
    words_yellow_df4 = ps.sqldf(query4, locals())

if re.match('[-]', guess_3_yellow_df[4]) or guess_3_yellow_df[4] == '':
    words_yellow_df5 = words_yellow_df4

elif re.match('[a-z]', guess_3_yellow_df[4]):
    yellow_position_5 = 'WHERE words NOT LIKE ' + "'" + '____' + guess_3_yellow_df[4] + "'"
    query5 = f"""
        SELECT * 
        FROM words_yellow_df4
        {yellow_position_5}
        """
    words_yellow_df5 = ps.sqldf(query5, locals())

if guess_3_grey == '':
    for letters in guess_3_yellow_list:
        words_yellow_df5 = words_yellow_df5[words_yellow_df5['words'].str.contains(letters, regex=False)]
    fifth_guess_df = words_yellow_df5

elif guess_3_grey  != '':
    for letters in guess_3_yellow_list:
        words_yellow_df5 = words_yellow_df5[words_yellow_df5['words'].str.contains(letters, regex=False)]
    fifth_guess_df = words_yellow_df5[~words_yellow_df5['words'].str.contains(guess_3_grey, regex=True)]

print(fifth_guess_df)
print("Good luck bozo.")