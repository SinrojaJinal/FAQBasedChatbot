import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Program to measure the similarity between 
# two sentences using cosine similarity. 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import pandas

class chatbot:
    def GettingAnswers(self, ques):
        data = pandas.read_csv("FAQ.csv")
        List_Of_Questions = list(data["Questions"])
        # List_Of_Questions = ["What is Amazon S3?", "What kind of data can I store in Amazon S3?", "How much does Amazon S3 cost?"]
        List_Of_Similiarity = []
        def get_cosine_similiarity(Question):
            # X = input("Enter first string: ").lower() 
            # Y = input("Enter second string: ").lower() 
            X =Question
            Y =ques

            # tokenization 
            X_list = word_tokenize(X) 
            Y_list = word_tokenize(Y) 

            # sw contains the list of stopwords 
            sw = stopwords.words('english') 
            l1 =[];l2 =[] 

            # remove stop words from the string 
            X_set = {w for w in X_list if not w in sw} 
            Y_set = {w for w in Y_list if not w in sw} 

            # form a set containing keywords of both strings 
            rvector = X_set.union(Y_set) 
            for w in rvector: 
                if w in X_set: l1.append(1) # create a vector 
                else: l1.append(0) 
                if w in Y_set: l2.append(1) 
                else: l2.append(0) 
            c = 0

            # cosine formula 
            for i in range(len(rvector)): 
                    c+= l1[i]*l2[i] 
            cosine = c / float((sum(l1)*sum(l2))**0.5) 
            # print("similarity: ", cosine)
            List_Of_Similiarity.append(cosine)

        for i in List_Of_Questions:
            get_cosine_similiarity(i)

        data["Similiarity"] = List_Of_Similiarity
        sorted_df = data.sort_values(by = 'Similiarity', ascending = False)
        
        QuestionList = list(sorted_df.head(3)["Questions"])
        AnswersList = list(sorted_df.head(3)["Answer"])
        result = {}
        for key in QuestionList:
            for value in AnswersList:
                result[key] = value
                AnswersList.remove(value)
                break
        # print(result)
        return result

# obj = chatbot()
# result = obj.GettingAnswers("How much does amazon s3 cost?")

