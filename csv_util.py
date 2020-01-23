import pandas as pd


def print_csv_data(csv_data):
    print(csv_data)

def read_csv():
    csv_data = pd.read_csv('student_data.csv')
    print_csv_data(csv_data)


def wite_to_csv():
    # data includes student name,subject and marks
    data = [['Rohit','Maths', 80], ['Virat','Science', 90], ['Rahul','Physics', 40]]

    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['Student', 'Subject','Marks'])

    #save dataframe to a csv
    df.to_csv('student_data.csv')




#wite_to_csv()
read_csv()



