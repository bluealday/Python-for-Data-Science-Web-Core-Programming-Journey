#!/usr/bin/env python
# coding: utf-8

# # Week 1 - Homework
# 
# Double-click on the cells that say `ANSWER N:` (e.g. `ANSWER 1:`) to type your answer, leaving the prompt in place. For example, if the answer to question -8 were `yes` the cell should contain the text: `ANSWER -8: yes`
# 
# To lock in a cell with text, just execute it with *CTRL+ENTER* (or *CMD+ENTER* on MacOS).
# 
# When you are done with this assignment, go to *File* > *Download as...* > *Python (.py)* and save your Python file. Then submit your .py file to the assignment on Canvas.
# 
# ## Task 1
# 
# Execute the following code and answer the questions below.

# In[3]:


print(3 + 4)
print(3.0 + 4)
print(3 + 4.0)
print(3.0 + 4.0)
print()
print(3 - 4)
print(3.0 - 4)
print(3 - 4.0)
print(3.0 - 4.0)
print()
print(3 * 4)
print(3.0 * 4)
print(3 * 4.0)
print(3.0 * 4.0)


# QUESTION 1: What is the result of adding, subtracting, or multiplying two ints? (8 pts)

# ANSWER 1: An int.

# QUESTION 2: What is the result of adding, subtracting, or multiplying two floats? (8 pts)

# ANSWER 2: A float.

# QUESTION 3: What is the result of adding, subtracting, or multiplying a float and an int? Does the order matter? (9 pts)

# ANSWER 3: A float. The order does not matter.

# ## Task 2
# 
# Execute the following code and answer the questions below.

# In[4]:


print(35 / 5)
print(35.0 / 5)
print(35 / 5.0)
print(35.0 / 5.0)
print()
print(35 // 5)
print(35.0 // 5)
print(35 // 5.0)
print(35.0 // 5.0)
print()
print(35 % 5)
print(35.0 % 5)
print(35 % 5.0)
print(35.0 % 5.0)


# QUESTION 4: What is the result of \[true / regular\] division on two ints? (8 pts)

# ANSWER 4: A float.

# QUESTION 5: What is the result of \[true / regular\] division on two floats? (8 pts)

# ANSWER 5: A float.

# QUESTION 6: What is the result of \[true / regular\] division on a float and an int? Does the order matter? (9 pts)

# ANSWER 6: A float. The order does not matter.

# QUESTION 7: What is the result of floor division or modulus on two ints? (8 pts)

# ANSWER 7: An int.

# QUESTION 8: What is the result of floor division or modulus on two floats? (8 pts)

# ANSWER 8: A float.

# QUESTION 9: What is the result of floor division or modulus on a float and an int? Does the order matter? (9 pts)

# ANSWER 9: 
# A float. The order does not matter.

# ## Task 3
# 
# Write your own code to answer the question below.

# In[5]:


print('hello ' + 'world') # not using variables
text = 'hello ' + 'world' # variable with space in first string
print(text)
text = 'hello' + 'world' # variable with no spaces
print(text)



# QUESTION 10: Which of the arithmetic operators we have covered can be used on two strings? (e.g. `'hello' % 'world'`) (7 pts)

# ANSWER 10: The + operator concatenates 2 strings. If you need to have a space between the 2 strings, you can enter a space in one of the strings.

# ## Task 4
# 
# Write your own code to answer the question below.

# In[33]:


matinee_ticket_sales = 1
evening_ticket_sales = '321'
total = matinee_ticket_sales * evening_ticket_sales
print(total)
print()
total = evening_ticket_sales * matinee_ticket_sales
print(total)


# QUESTION 11: Which of the arithmetic operators we have covered can be used on a string and an int? Does the order matter? (e.g. `'hello' % 7` and `7 % 'hello'`) (9 pts)

# ANSWER 11: The multiplication operator * can be used with integers > 0 and a string.  Order does not seem to matter. If the integer is < 1, print does not display anything.

# ## Task 5
# 
# Write your own code to answer the question below.

# In[35]:


matinee_ticket_sales = 1.0
evening_ticket_sales = "3"
total = matinee_ticket_sales / evening_ticket_sales
print(total)
print()
total = evening_ticket_sales / matinee_ticket_sales
print(total)


# QUESTION 12: Which of the arithmetic operators we have covered can be used on a string and an float? Does the order matter? (e.g. `'hello' % 5.2` and `5.2 % 'hello'`) (9 pts)

# ANSWER 12: Unable to use any arithmetic operators (+, -, *, /, //, or %) to operate on a string and a float together.  Attempting to do so on lines 3 or 6 resulted in runtime errors.

# **REMINDER:** When you are done with this assignment, go to *File* > *Download as...* > *Python (.py)* and save your Python file. Then submit your .py file to the assignment on Canvas.

# In[ ]:





# In[ ]:




