from bs4 import BeautifulSoup
import requests
import re
import pprint
import pandas as pd




if __name__ == "__main__": 

    webpage = requests.get('https://www.yelp.com/biz/el-cortez-mexican-kitchen-tequila-bar-edmonton') 
    reviewspage = BeautifulSoup(webpage.content, 'html.parser')
    review_name = []
    reviews = reviewspage.find_all("span", class_="lemon--span__373c0__3997G text__373c0__2Kxyz fs-block text-color--black-regular__373c0__2vGEn text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--large__373c0__3t60B")
    for review in reviews: 
        review_name.append(review.text)
    #print(len(review_name))
    
    review_text = []                #reviews at index 5 to index 28
    reviewtext = reviewspage.find_all("span", class_="lemon--span__373c0__3997G raw__373c0__3rcx7")
    for reviewtexts in reviewtext:
        review_text.append(reviewtexts.text)
    review_text_final = review_text[5:25]
    #print(len(review_text_final))
        
    review_date = []
    review_dates = reviewspage.find_all("span", class_="lemon--span__373c0__3997G text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa-")
    for reviewdate in review_dates:
        review_date.append(reviewdate.text)
    reviews_date = review_date[4:]
    print(len(reviews_date))
        


    reviewer_address =[]       #address with 20 len
    reviewer_address_variable = reviewspage.find_all("div", class_="lemon--div__373c0__1mboc responsive-hidden-small__373c0__2vDff border-color--default__373c0__3-ifU")
    for revieweraddress in reviewer_address_variable:
        reviewer_address.append(revieweraddress.text)
    #print(len(reviewer_address))
    

    reviewer_friends =[]      # Friends list final len 20
    reviewer_friends_variable = reviewspage.find_all("div", class_="lemon--div__373c0__1mboc margin-r1__373c0__zyKmV border-color--default__373c0__3-ifU")
    for reviewerfriends in reviewer_friends_variable:
        reviewer_friends.append(reviewerfriends.text)
    friends_list1 = reviewer_friends[0:13:3]
    friends_list2 = [reviewer_friends[14]]
    friends_list3 = reviewer_friends[16:26:3]
    friends_list4 = reviewer_friends[27:57:3]
    friends_list = friends_list1 + friends_list2 + friends_list3 + friends_list4
    #print(len(friends_list))


    reviews_list1 = reviewer_friends[1:14:3]          #reviews_list final len 20
    reviews_list2 = [reviewer_friends[15]]
    reviews_list3 = reviewer_friends[17:27:3]
    reviews_list4 = reviewer_friends[28:57:3]
    reviews_list = reviews_list1 + reviews_list2 + reviews_list3 + reviews_list4
    #print(len(reviews_list))
    


    photos_list1 =reviewer_friends[2:12:3]         #photos list final len 20
    
    photos_list2 = reviewer_friends[18:25:3]
    photos_list3 = reviewer_friends[29:57:3]
    photos_list = photos_list1+["0 photos"]+ ["0 photos"] + photos_list2+ ["0 photos"] + photos_list3
    #print(len(photos_list))
    
    list_of_data = []
    list_of_data.append(review_name)
    list_of_data.append(reviews_date)
    list_of_data.append(friends_list)
    list_of_data.append(reviews_list)
    list_of_data.append(review_text_final)
    #print(len(list_of_data))




    reviews_df = pd.DataFrame(columns=['username', 'review_date', 'friend_count', 'reivew_count', 'review_text'])
    
    for index, data in enumerate(list_of_data):
        
        reviews_df.iloc[:, index] = data

    reviews_df.to_csv('reviewer.csv', index=False)
    
    


    



   


   