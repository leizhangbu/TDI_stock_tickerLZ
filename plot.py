from bokeh.plotting import figure, output_file, show
from bokeh.embed import components


def fig(df,title):
    inc = df['4. close'] > df['1. open']
    dec = df['1. open'] > df['4. close']
    w = 12*60*60*1000 
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

    p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=800, title = title)
    p.xaxis.major_label_orientation = 3.14/4
    p.grid.grid_line_alpha=0.3

    p.segment(df.index, df['2. high'], df.index, df['3. low'], color="black")
    p.vbar(df.index[inc], w, df['1. open'][inc], df['4. close'][inc], fill_color="#D5E1DD", line_color="black")
    p.vbar(df.index[dec], w, df['1. open'][dec], df['4. close'][dec], fill_color="#F2583E", line_color="black")

    p.yaxis.axis_label = "Price"
    p.xaxis.axis_label = "Date"

    script, div = components(p)
    return script, div

