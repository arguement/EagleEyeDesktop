from app import app,db,users,reports,priorities,police_officers
from flask import render_template,request,redirect,url_for,flash,jsonify
import os
import requests,json
import numpy as np
import pandas as pd 
from sklearn.cluster import KMeans
from datetime import datetime,timedelta

import geocoder  
from math import radians, cos, sin, asin, sqrt 





# reports = db.collection('User')
def changeToDate(strdate):
    fixed_date = strdate[:-1]
    iso_change = datetime.fromisoformat
    return iso_change(fixed_date)

@app.route('/addAll', methods=['POST'])
def addAll():
    

    try:
        body = request.json["gen"]
        batch = db.batch()
        
        for record in body:
            ref = reports.document()
            record.update({'birth-date': changeToDate(record['birth-date']),'date-time-commited':changeToDate(record['date-time-commited']) ,'date-time-reported':changeToDate(record['date-time-reported'])  })
            # reports.add(record)
            batch.set(ref, record)

        batch.commit()

        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
   
   
    

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
    
    
    
    return jsonify(result = allpriorities.get(cat,0))


# all of the priorities
@app.route("/allPriority",methods=["GET"])
def getAllPrority():
    
    
    allpriorities = priorities.document("Priorities").get()
    
    allpriorities = allpriorities.to_dict()
    
    
    
    
    return jsonify(priorities=allpriorities)



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
    
    clustering(other,offences)

    orient = request.args.get("orientCluster")
    orient =  orient or 'index'

    overall_offence_counts_json = crime_data.offence.value_counts().to_json()
    overall_table_with_clustering = other.to_json(orient=orient)

    #convert to dictionaries 
    overall_offence_counts_json = json.loads(overall_offence_counts_json)
    overall_table_with_clustering = json.loads(overall_table_with_clustering)
    
    return jsonify(over_counts = overall_offence_counts_json,overall_tables = overall_table_with_clustering,offences=list(offences),locations=list(location))

def clustering(other,offences):
    crimes_data_caught = other.columns[other.columns.isin(offences)].to_list()
    X = other[crimes_data_caught]
    # X = other[['Assault', 'Theft']]
    clusters = KMeans(10)  # 4 clusters!
    clusters.fit( X )
    other['Crime_clusters'] = clusters.labels_

@app.route("/dashboard",methods=["GET"])
def dashboard():
    all_reports = [doc.to_dict() for doc in reports.stream()]
    crime_data = pd.DataFrame(all_reports)

    pending_count = len(crime_data[crime_data.status == "Pending"])
    dispatch_count = len(crime_data[crime_data.status == "Officer Dispatched"])
    total_count = len(crime_data)

    #card data whcih displays overall crime counts in ja
    card_data = {"pending_count":pending_count,"dispatch_count":dispatch_count,"total_count":total_count}
    top3crimes = crime_data.offence.value_counts().sort_values(ascending=False ).head(3).to_dict() #top 3 crimes to report

    a = crime_data[["offence-location","offence"]].groupby("offence-location").agg(["count"])
    a.columns = ['offence count']
    a = a.reset_index()
    locations_with_most_crime = a.sort_values(by="offence count",ascending = False).head(6).to_dict(orient="records" )

    #dates and crime totals
    crime_data["date-time-reported"] = pd.to_datetime(crime_data["date-time-reported"]).dt.date
    start_date = datetime.now() - timedelta(30)
    crime_data["date-time-reported"] = pd.DatetimeIndex(crime_data["date-time-reported"] )

    crime_30_days = crime_data[(crime_data["date-time-reported"]> start_date) & (crime_data["date-time-reported"] <= datetime.now())]
    crime_30_days = crime_30_days.groupby("date-time-reported").agg({"offence":"count"})
    crime_30_days.columns = ['offence count']
    crime_30_days = crime_30_days.reset_index()

    crime30daysjson = crime_30_days.to_dict("records") #json(date_format="iso")



    return jsonify(card_data=card_data,top3crimes=top3crimes,locations_with_most_crime=locations_with_most_crime,crime30days=crime30daysjson)

@app.route("/location",methods=["GET"])
def get_latlngs():
    the_reports = [doc.to_dict() for doc in reports.stream()]
    #g = geocoder.arcgis(location)
    v=0
    cordinates={}
    for i in the_reports :
        try:
            v=v+1
            t=geocoder.arcgis(i['offence-location']+",Jamaica")
            
            #print(str(t.latlng[1]))
            location=str(t.latlng[1])+"," + str(t.latlng[0])
            #print(location)
        except:
            print("location execption") 
        if location in cordinates:
            cordinates[location]["count"]=cordinates[location]["count"]+1 
        else :
            cordinates[location]={"location_geo": t.latlng,"count":1, "location_name":i['offence-location']+",Jamaica"}
        
        print(cordinates)
        #print("\n")
    #print("this\n")
    #print(g.latlng) 
    #print(jsonify({"Lattitude":g.latlng[0],"Longitude":g.latlng[1]}))
    return jsonify(cordinates)  

@app.route("/locate/<location>",methods=["GET"])
def get_latlng(location):
    #the_reports = [doc.to_dict() for doc in reports.stream()]
    g = geocoder.arcgis(location)
    
    print("this/n")
    #print(g.latlng) 
    #print(jsonify({"Lattitude":g.latlng[0],"Longitude":g.latlng[1]}))
    return jsonify({"lng":g.latlng[1],"lat":g.latlng[0]})  

@app.route("/nearest/<address>",methods=["GET"])
def get_nearest(address):
    address=geocoder.arcgis(address)
    address=address.json
    #print(address)
    lat1=radians(float(address['lat']))
    long1=radians(float(address['lng'])) 
    all_officer=[doc.to_dict() for doc in police_officers.stream()]
    id=0
    distance=37573957935190097903797934
    for officer in all_officer:
        police_location_geo=geocoder.arcgis(officer["Location"])
        police_location_geo =police_location_geo.json
        lat2=radians(float(police_location_geo["lat"]))
        long2=radians(float(police_location_geo["lng"])) 
        
        dlon=long2-long1
        dlat=lat2-lat1 
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2 
        c = 2 * asin(sqrt(a))
        r = 6371

        new_distance=c*r
        if new_distance<distance:
            distance=new_distance
            id=officer["id-number"]
    return( jsonify({"id":id})) 










@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    # response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8081")