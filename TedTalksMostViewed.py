import csv
import plotly.plotly as py
import plotly.graph_objs as go

currentFile = open('ted_main.csv', 'rt', encoding='latin1')

headline = []
viewsAsOfJune2017 = []

with currentFile as csvfile:
    readCSV = csv.DictReader(csvfile, delimiter=',')
    for row in readCSV:
        headline.append(row["title"])
        viewElement = int(row["views"])
        viewsAsOfJune2017.append(viewElement)
        #print(row)

        
        
print(headline)
print(viewsAsOfJune2017)

data = [go.Bar(
    x = headline,
    y = viewsAsOfJune2017
    )]

py.iplot(data, filename = 'Number of views per Ted Talk')

#find the top three TedTalks given by sorting the views and then associating them with the ted talk test_given_directory
#there aera 5 ted talks that do not have proper statistics and were not included in the data set.
print (sorted(viewsAsOfJune2017))
print(len(viewsAsOfJune2017))

highest = max(viewsAsOfJune2017)
print ('highest number of views: ', highest)
print ('')
