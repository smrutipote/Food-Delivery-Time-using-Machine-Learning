# visualize.py
import plotly.express as px

def plot_distance_vs_time(df):
    fig = px.scatter(data_frame=df, 
                     x="distance",
                     y="Time_taken(min)", 
                     size="Time_taken(min)", 
                     trendline="ols", 
                     title="Relationship Between Distance and Time Taken")
    fig.show()
