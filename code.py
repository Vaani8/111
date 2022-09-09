import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random
import csv
df=pd.read_csv("other_data.csv")
data=df["reading_time"].tolist()
fig=ff.create_distplot([data],["reading_time"],show_hist=False)
#fig.show()
mean=st.mean(data)
median=st.median(data)
stdev=st.stdev(data)
print("Mean -> ",mean)
print("Median -> ",median)
print("Standard Diviation -> ",stdev)
def random_set_of_mean(counter): 
    dataset = [] 
    for i in range(0, counter): 
        random_index= random.randint(0,len(data)-1) 
        value = data[random_index] 
        dataset.append(value) 
    mean = st.mean(dataset) 
    return mean
mean_list = [] 
for i in range(0,1000): 
    set_of_means= random_set_of_mean(100) 
    mean_list.append(set_of_means)
mean=st.mean(mean_list)
median=st.median(mean_list)
stdev=st.stdev(mean_list)
print("Mean -> ",mean)
print("Median -> ",median)
print("Standard Diviation -> ",stdev)
fig=ff.create_distplot([mean_list],["reading_time"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="mean"))
fig.show()
first_std_start,first_std_end=mean-stdev,mean+stdev
second_std_start,second_std_end=mean-(2*stdev),mean+(2*stdev)
third_std_start,third_std_end=mean-(3*stdev),mean+(3*stdev)
fig = ff.create_distplot([mean_list], ["reading time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START")) 
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START")) 
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END")) 
fig.add_trace(go.Scatter(x=[third_std_start,third_std_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START")) 
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 
fig.show()

df = pd.read_csv("data.csv") 
data = df["reading_time"].tolist() 
mean_of_sample1 = st.mean(data) 
print("Mean of sample1:- ",mean_of_sample1) 
fig = ff.create_distplot([mean_list], ["reading time"], show_hist=False) 
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE")) 
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.show()

z_score = (mean - mean_of_sample1)/stdev
print("The z score is = ",z_score)
z_score = (mean - mean_of_sample1)/stdev
print("The z score is = ",z_score)