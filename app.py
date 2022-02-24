#!/usr/bin/env python
# coding: utf-8

# In[1]:
from flask import Flask
app = Flask(__name__)
from flask import request, render_template
# In[2]:
from keras.models import load_model
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        income=request.form.get("income")
        age=request.form.get("age")
        loan=request.form.get("loan")
        print(income,age,loan)
        model=load_model("assignment_logreg")
        pred=model.predict([[float(income),float(age),float(loan)]])
        s = "The predicted default rate is : " + str(pred)
        return(render_template("index.html",result=s))
    else:
        return(render_template("index.html",result="2"))
# In[ ]:
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("5000"))


# In[ ]:



