from flask import Flask, render_template, request, redirect
import api_pull as ap
import plot

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:

        #request was a post
        app.vars['ticker'] = request.form['ticker']
        app.vars['results'] = ap.get_data(app.vars['ticker'])
        print("length of df: ",len(app.vars['results']))
        print(app.vars['ticker'])
        print(app.vars['results'])
        if len(app.vars['results']) == 0:
            return render_template('error.html')
        else:
            #script, div = plot.fig(app.vars['results'], app.vars['ticker'])
            html= plot.fig(app.vars['results'], app.vars['ticker'])
            Html_file= open("templates/results.html","w")
            Html_file.write(html)
            Html_file.close()
            #print(script)
            #print(div)
            #f = open('%s.txt'%(app.vars['ticker']),'w')
            #f.write('Ticker: %s\n'%(app.vars['ticker']))
            #f.close()
            
            #render_template('results.html', script=script, div=div)
            return render_template('results.html')


if __name__ == "__main__":
    app.run(debug=True)
