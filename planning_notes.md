# planning_notes.md

**Twitter API**  
https://dev.twitter.com/rest/public  
GET statuses/user_timeline  

--> Negative vs. Positive Tweets Ideas    
- Use "bag of words" (keywords with defined score of meaning on scale: negative, neutral, positive)  
    - Affective Norms for English Words
    - Self-defined?
    - Look into some machine learning
- Include emojis and emoticons  
- Hashtags? (need to skip # symbol when looking through bag)  
- How to deal with sarcasm?  


--> Singular Tweet Mood Algorithm High-Level Idea:  
1. function takes in tweet  
2. parse input tweet to find keywords/important words  
3. for each keyword, place into list: negative or positive    
4. take length of positive list and subtract length of negative list  
5. if resulting number is positive, tweet is positive; if number is negative, tweet is negative; if result is 0, tweet is neutral  

note: Make sure to save the mood number in a list to graph over time
(need to save date too)

--> Overall Program Ideas:  
- input collection of tweets from 1 user  
- send each tweet through tweet mood function  
- collect return value mood of each tweet in array  
- graph array over time  
- alert it high levels of negativity  
- alert set for "problem words" (ex: suicide, kill, etc)  

--> Resources  
- Sentiment Dictionary: http://www3.nd.edu/~mcdonald/Word_Lists.html  

**To Do List**  
[x] label y axis on graph
[ ] check for "not" and other words that discount meaning  
[x] remove # and @ symbol when checking words  
[ ] brain-storm sarcasm (research online)  
[ ] checking for extra negative flags (add alert)  
[ ] checking for danger flags (add alert)  
[ ] add more to bag of words  
[x] user input twitter screen name  

**Stretch Goals**  
[ ] machine learning to add words  
[ ] word mood ratings on scale of 1-10 instead of "neg" vs "pos"  
[ ] more graphs (frequency of word [user can choose word]), most-used words, etc  
[ ] GUI for user interaction  
