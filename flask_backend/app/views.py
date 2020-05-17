from app import app,db,users,reports,priorities
from flask import render_template,request,redirect,url_for,flash,jsonify
import os
import requests,json
import numpy as np
import pandas as pd 
from sklearn.cluster import KMeans







# reports = db.collection('User')

@app.route('/add', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json['id']
        reports.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/list', methods=['GET'])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON.
        todo : Return document that matches query ID.
        all_todos : Return all documents.
    """
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('id')
        if todo_id:
            todo = reports.document(todo_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = [doc.to_dict() for doc in reports.stream()]
            return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/update', methods=['POST', 'PUT'])
def update():
    """
        update() : Update document in Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    try:
        id = request.json['id']
        reports.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    """
        delete() : Delete a document from Firestore collection.
    """
    try:
        # Check for ID in URL query
        todo_id = request.args.get('id')
        reports.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route("/getPriority",methods=["GET"])
def getPrority():
    # print("here")
    cat = request.args.get("category")
    
    
    allpriorities = priorities.document("Priorities").get()
    
    allpriorities = allpriorities.to_dict()
    # print(allpriorities)
    
    
    
    return allpriorities.get(cat,0)

@app.route("/CrimeAnalytics",methods=["GET"])
def getAnalytics():
    all_reports = [doc.to_dict() for doc in reports.stream()]
    crime_data = pd.DataFrame(all_reports)

    # aggregte data to be clustered

    offences = crime_data.offence.unique()
    location = crime_data["offence-location"].unique()
    # print(location)
    output = {
        "Location": location,
        "Total": []
    }
    output.update({
        i:[] for i in offences
    })

    temp = crime_data.copy()

    def testFun(x):
        lst = [x["offence-location"]]
        cols = ["offence-location"]
        cols.extend(offences)
        for i in offences:
            leng = len(crime_data.offence[(crime_data["offence-location"] == x["offence-location"]) & (crime_data.offence == i)])
            lst.append(leng)
        return pd.Series(lst,index=cols)


    other = crime_data.apply(testFun, axis=1,result_type="expand")
    other["Total"] = other.iloc[:,1:].apply(np.sum,axis=1)
    
    clustering(other)

    orient = request.args.get("orientCluster")
    orient =  orient or 'index'

    overall_offence_counts_json = crime_data.offence.value_counts().to_json()
    overall_table_with_clustering = other.to_json(orient=orient)

    #convert to dictionaries 
    overall_offence_counts_json = json.loads(overall_offence_counts_json)
    overall_table_with_clustering = json.loads(overall_table_with_clustering)
    return jsonify(over_counts = overall_offence_counts_json,overall_tables = overall_table_with_clustering)

def clustering(other):
    X = other[['Assault', 'Theft']]
    clusters = KMeans(2)  # 4 clusters!
    clusters.fit( X )
    other['Crime_clusters'] = clusters.labels_

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response





if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8081")