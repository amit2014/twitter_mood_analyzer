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
- Hashtags?  
- How to deal with sarcasm?  


--> Singular Tweet Mood Algorithm High-Level Idea:  
1. function takes in tweet  
2. parse input tweet to find keywords/important words  
3. for each keyword, find negative/neutral/positive (mood) value  
4. add up mood values of each word divided by total words to find total tweet mood value  
5. return total tweet mood value  


--> Over Program Ideas:  
- input collection of tweets from 1 user  
- send each tweet through tweet mood function  
- collect return value mood of each tweet in array  
- graph array over time  
- alert it high levels of negativity  


