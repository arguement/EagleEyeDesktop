<template>
     <div id="dispatch-sidebar-content">
    <router-view></router-view>
    
<!-- NAVBAR -->    
    <nav id="dispatch-nav" class="navbar navbar-expand-lg navbar-light bg-light">
      <li class="navbar-brand">
        <h1 id="report-label">DISPATCH OFFICERS</h1>
      </li>
      <div id="navbar-icons">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <svg id="notif" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"/></svg>
          </li>
          <li class="nav-item">
          <span class="dot"><div id="user-initials"></div></span>
          </li>   
        </ul>
      </div>
    </nav>

    <ul id="report-data" class="nav">
            <li class="nav-item">
                 <router-link to="/reports" class="nav-link">
              <div id="report-arrow">
                  <div>
                    <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
                    back</div>
              </div>
                 </router-link>
            </li>
          </ul>

<div id="reports-content">
      <div id="report-section">
        <div id="report-list">
    <table class="table table-borderless" style="border-collapse:separate; border-spacing:0 3px; margin-top:-3px;">
              <thead>
                <tr>
                  <th scope="col"></th>
                  <th scope="col">ID Number</th>
                  <th scope="col">First Name</th>
                  <th scope="col">Surname</th>
                  <th scope="col">Location</th>
                </tr>
              </thead>
              <tbody>
                <tr id="table-data" v-for="officer in officers" :key="officer.id">
                  <th scope="row">
                  </th>
                  <td v-on:click="dispatchofficer(officer)" id="offence-cell">{{ officer["id-number"] }}</td>
                  <td v-on:click="dispatchofficer(officer)">{{ officer["first-name"] }}</td>
                  <td v-on:click="dispatchofficer(officer)">{{ officer["surname"] }}</td>
                  <td v-on:click="dispatchofficer(officer)">{{ officer["Location"] }}</td>
                </tr>
              </tbody>
            </table>
        </div>
      </div>
    </div>
     </div>  
</template> 
<script>
import {store} from "../../store/store"
import navbar from '../navbar/navbar'
import {db} from '../../../../static/js/fire_config'
export default {
    methods:{
    dispatchofficer(officerDis){
      let officer = officerDis
        db.collection("Crime Report").doc(this.reportClicked[0]).update({
            status: "Officer Dispatched",
            officerFname: officer["first-name"],
            officerLname: officer["surname"]
        }); 
       /* db.collection("Crime Report").doc(this.reportClicked[0]).set({
            officerFname: officer["first-name"],
            officerLname: officer["last-name"]
        }, {merge: true}); */
        this.$router.push({ path:"/reports"})
    }

    },
    data(){ 
        return {
        officers:[],
        i: [],
        storeState: store.state,
        fullinfo: [],
        reportClicked: [],
      }
    },
    created (){
        this.reportClicked = this.$route.query.reportClicked
        
        db.collection('Police Officer').get().then(
          querysnapshot => {
          querysnapshot.forEach (doc => {
          this.officers.push(doc.data())
          }); 
          }) 
        
        db.collection("Crime Report").get()
        .then(snapshot => {
          snapshot.forEach(doc => {
            this.fullinfo.push( [doc.id, doc.data()])
          }); 
          
        }) 
          

          
    }
}
</script>

<style>
#dispatch-sidebar-content {
  background-color: #F8F9F9;
  width: 100%;
  height: 100vh;
  margin-left: 230px
}

#dispatch-nav {
    height: 50px;
    margin: 20px;
    margin-right: 50px;
    margin-left: 50px;
    letter-spacing: 1px;
}
</style>