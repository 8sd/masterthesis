import matplotlib.pyplot as plt 

def read_file(path, delim="\t"):
  f = open(path)

  data = list()
  keys = f.readline().split(delim)

  for key in keys:
    if key is '':
      raise LookupError

  for line in f:
    values = line.split(delim)
    line_data = dict()
    for i in range(0, len(keys)):
      try:
        line_data[keys[i]] = values[i]
      except IndexError:
        line_data[keys[i]] = ''
    
    data.append(line_data)

  return data


foo = read_file('/tmp/pdata.csv', ',')

# line 1 points
x1 = ["1","2","grrrr","4"] 
y1 = [2,4,1,4] 
# plotting the line 1 points  
plt.plot(x1, y1, label = "line 1") 
  
# line 2 points 
y2 = [4,1,3, None] 
# plotting the line 2 points  
plt.plot(x1, y2, label = "line 2") 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
# giving a title to my graph 
plt.title('Two lines on same graph!') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show() 
