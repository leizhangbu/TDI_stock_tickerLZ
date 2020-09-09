from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.embed import file_html

def fig(df,title):
    plot = figure(plot_width=800, plot_height=400, x_axis_type="datetime", title=title)
    plot.yaxis.axis_label = "Closing Price"
    plot.xaxis.axis_label = "Date"
    plot.line(df.index, df)
    print('plot')
    
    return file_html(plot, CDN, "results.html")

