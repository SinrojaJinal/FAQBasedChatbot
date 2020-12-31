import sqlite3
import pandas

conn = sqlite3.connect('FQA.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

# Create table - FAQ
# c.execute('''CREATE TABLE FAQ([id] INTEGER PRIMARY KEY,[Questions] text, [Answers] text)''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("1", "What is the consistency model for Amazon S3?", "Amazon S3 delivers strong read-after-write consistency automatically, without changes to performance or availability, without sacrificing regional isolation for applications, and at no additional cost.")''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("2", "Is S3 One Zone-IA available in all AWS Regions in which S3 operates?", "Yes")''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("3", "What performance does S3 One Zone-IA storage offer?", "S3 One Zone-IA storage class offers the same performance as S3 Standard and S3 Standard-Infrequent Access storage.")''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("4", "How much does Amazon S3 cost?", "With Amazon S3, you pay only for what you use. There is no minimum fee. You can estimate your monthly bill using the AWS Pricing Calculator.")''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("6", "Where is my data stored?", "You specify an AWS Region when you create your Amazon S3 bucket.")''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("5", "What is an AWS Region?", "An AWS Region is a geographic location where AWS provides multiple, physically separated and isolated Availability Zones which are connected with low latency, high throughput, and highly redundant networking.")''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("7", "What is an AWS Availability Zone (AZ)?", "An AWS Availability Zone is a physically isolated location within an AWS Region. Within each AWS Region, S3 operates in a minimum of three AZs, each separated by miles to protect against local events like fires, floods, etc.")''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("8", "How am I charged for using Versioning?", "Normal Amazon S3 rates apply for every version of an object stored or requested. For example, let’s look at the following scenario to illustrate storage costs when utilizing Versioning (let’s assume the current month is 31 days long)")''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("9", "Do your prices include taxes?", "Except as otherwise noted, our prices are exclusive of applicable taxes and duties, including VAT and applicable sales tax")''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("10", "What is IPv6?", "Every server and device connected to the Internet must have a unique address.")''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("11", "What can I do with IPv6?", "Using IPv6 support for Amazon S3, applications can connect to Amazon S3 without the need for any IPv6 to IPv4 translation software or systems.")''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("12", "Is IPv6 supported in all AWS Regions?", "Yes")''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("13", "What are Amazon S3 Event Notifications?", "Amazon S3 event notifications can be sent in response to actions in Amazon S3 like PUTs, POSTs, COPYs, or DELETEs.")''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("14", "What can I do with Amazon S3 event notifications?", "Amazon S3 event notifications enable you to run workflows, send alerts, or perform other actions in response to changes in your objects stored in S3.")''')
c.execute('''INSERT INTO FAQ("id","Questions","Answers") VALUES ("15", "What is included in an Amazon S3 event notification?", "For a detailed description of the information included in Amazon S3 event notification messages, please refer to the Configuring Amazon S3 Event Notifications topic in the Amazon S3 Developer Guide.")''')

c.execute("SELECT * FROM FAQ")
rows = c.fetchall()
conn.close()

df = pandas.DataFrame.from_records(rows)
df.columns = ["id","Questions","Answer"]
df.to_csv("FAQ.csv",index=False)
# print(df["Questions"][0])