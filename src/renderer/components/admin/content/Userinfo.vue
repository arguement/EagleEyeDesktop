<template>
    <div>
    <router-view></router-view> 
       <nav id="page-nav" class=" navbar navbar-expand-lg navbar-light bg-light">
         <li class="navbar-brand">
           <h1 id="report-label">User Information</h1> 
         </li> 
         <div id="navbar-icon">
           <ul class="navbar-nav mr-auto">
             <li class="nav-item">
               <svg id="notif" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"/></svg>
             </li> 
             <li class= "nav-item">
               <span class="dot"><div id="user-initials"></div></span>
             </li>
           </ul>
         </div>
       </nav> 
       <div v-for="personal_information in info" v-bind:key='personal_information.id'>
        <p id="offence-info"> First Name: {{personal_information['first-name']}}</p>
       </div>
    </div>
</template> 
<script>
import {db} from '../../../../../static/js/fire_config'
export default { 
    
    props:{},
    data(){
        return{
          info : []
        }
    },
    created(){
        //console.log(this.$route.params.id) 
        db.collection('User').where
        ('id-number','==',this.$route.params.id).get()
        .then(querySnapshot => {
            querySnapshot.forEach( doc => {
                //console.log(doc.data())
                this.info.push(doc.data()) 
                //console.log(this.info)
            })
        }) 
        console.log("gaza")
       for(let i=0; i < this.info.length; i++){
         console.log(this.info)
       }

    }
}
</script> 
<style>

input[type="checkbox"] {
  outline:1px solid #D5D8DC  ;
    outline-offset: -1px;
}


#user-selected {
  position: relative;
}

.report-title2 {
  position: absolute;
  right: 0;
}

#report-title {
  position: relative;
  display: flex;
  flex-direction: row;
}

#view-report {
  margin-bottom: 100px;
}

#refresh {
  margin-top: 11px;
  margin-left: 20px;
  fill: #566573;
}

.slide-fade-enter-active {
  transition: all 1s ease;
}
.slide-fade-leave-active {
  transition: all .000001s ease;
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}

#report-arrow {
    font-size: 12px;
    fill: #566573;
    color: #566573;
    letter-spacing: 1px;
}

#user-selected {
    margin-left: 50px;
}

tbody {
    background-color: white;
}

#report-data {
margin-bottom: 40px;
}

#offence-cell {
    font-weight: 600;
}

#info-label {
    font-weight: 600;
}

#offence-info {
    font-size: 12px;
    color: #566573;
    letter-spacing: 1px;
    font-weight: 400;
}

th {
    font-size: 12px;
    color: #5C6BC0;
    letter-spacing: 1px;
}

td {
    font-size: 12px;
    color: #566573;
    letter-spacing: 1px;
    font-weight: 400;
}

#reports-sidebar-content {
  background-color: #F8F9F9;
  width: 100%;
  height: 100vh;
  margin-left: 230px
}

#reports-content {
    margin-left: 50px;
    margin-right: 50px;
    margin-top: 60px;
}

#input-search {
  border: none;
  border-radius: 4px;
  background: #E5E7E9;
  height: 40px;
  font-size: 12px;
  letter-spacing: 1px;
  font-weight: 400;
  width: 100%;
  color: #85929E;
}


#reports-label {
    font-size: 16px;
}

#report-quatitiy {
    font-size: 12px;
    color: #566573;
    letter-spacing: 1px;
    font-weight: 400;
    margin-top: 14px;
    margin-right: 40px;
}

#current-page {
    font-size: 12px;
    color: #566573;
    letter-spacing: 0.5px;
    font-weight: 400;
    margin-top: 14px;
    margin-right: 10px;
}


#of {
  font-size: 12px;
    color: #566573;
    letter-spacing: 1px;
    font-weight: 400;
    margin-top: 14px;
    margin-right: 10px;
}

#report-navigations {
    margin-top: 8px;
    fill: #566573;
}

#offence {
    font-size: 20px;
    letter-spacing: 0.5px;
    font-weight: 400;
}

#offence1 {
    font-size: 15px;
    letter-spacing: 0.5px;
    font-weight: 400;
    margin-top: 50px;
    }


input:focus, input.form-control:focus {

    outline:none !important;
    outline-width: 0 !important;
    box-shadow: none;
    -moz-box-shadow: none;
    -webkit-box-shadow: none;
}

#report-info {
    margin-top: 5px;
    border: none;
    border-radius: 4px;
    height: 50px;
}

#table-data:hover {
    background-color: #E8EAF6;
}

.dot {
  height: 40px;
  width: 40px;
  background-color: #9FA8DA;
  border-radius: 50%;
  display: inline-block;
  margin-top: 5px;
}

#user-initials {
  margin-left: 9px;
  margin-top: 8px;
  font-weight: 400;
  letter-spacing: 1px;
}

#navbar-icons {
    position: absolute;
    right: 0;
}

#notif, #account, .dot {
    margin-left: 20px;
    fill: #9FA8DA;
}

#notif {
  margin-top: 13px;
}

#page-nav {
    height: 50px;
    margin: 20px;
    margin-right: 50px;
    margin-left: 50px;
    letter-spacing: 1px;
}

#report-label {
    font-size: 16px;
    margin-top: 30px;
    letter-spacing: 2px;
    font-weight: 300px;
  }
</style>