<template> 
<div id="priority-content">
    <!-- NAVBAR -->
       <nav id="page-nav" class="navbar navbar-expand-lg navbar-light bg-light">
          <li class="navbar-brand">
            <h1 id="report-label">PRIORITY</h1>
            <p>{{ priorityList[0][0]}}</p>
          </li>
          <div id="navbar-icons">
            <ul class="navbar-nav mr-auto">
              <li class="nav-item">
                <svg id="notif" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"/></svg>
              </li>
              <li class="nav-item">
              <span class="dot"><div id="user-initials">{{ storeState.user["first-name"].charAt(0) }}{{ storeState.user["surname"].charAt(0) }}</div></span>
              </li>   
            </ul>
          </div>
        </nav>

    <div id="">
    <div id="reports-content">
        <div id="report-section">
          <div id="report-list">  
              <ul  id="report-data" class="nav">
              <ul class="nav navbar-nav mr-auto">
                <form id="search-form" class="form-inline my-2 my-lg-0">
                  <input v-model="search_item" class="form-control" id="input-search" type="search" placeholder="Find crime" aria-label="Search">
                </form>
              </ul>
              <p id="current-page">Page {{ pageNumber }} / {{ pagecount }}</p>
              <p id="of">of</p>
              <p id="report-quatitiy">{{ priorityList.length }}</p>
          
              <div id="report-navigations">
                <svg  v-on:click="prevPage" :disabled="pageNumber <= 0" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
                <svg  v-on:click="nextPage" :disabled="pageNumber  > pagecount" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
              </div>
        </ul>
    
     <div id="user_Information">
         <table  class="table table-borderless" style="border-collapse:separate; border-spacing:0 3px; margin-top:-3px;">
           
             <th scope="col"></th>
             <th scope="col">Crime</th>
             <th scope="col">Priority</th>
             <th scope="col">New Priority</th>
             
           
           <tbody>
            <tr id="table-data" v-for="crimes in sorter" :key='crimes[0]' > 
              <th scope="row" >
              </th> 
            <td>{{crimes[0]}}</td>
            <td>{{crimes[1]}}</td> 
            <td>
                <select v-model='newWeight' class="form-control" id="formrole" placeholder=crimepriority>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                </select>
            </td> 
            <td><button v-on:click="updateinfo(crimes[0],crimepriority,newWeight)"  class="btn btn-primary" id="Edit-button" >Update</button></td>
             </tr>
           </tbody>
         </table>
       </div>
          </div>
        </div>
    </div> 
    </div>
</div>
</template> 
<script> 
import {db} from '../../../../../static/js/fire_config' 
import {store} from "../../../store/store"
import navbar from '../../navbar/navbar'
export default {
    props:{
        crimes: {
      type: Array,
      required: false
    },
    size: { 
      type: Number,
      required: false,
      default: 10
    },
    pagecount: {
      type: Number,
      required: false 
    },
    paginatedData: {
      type: Array,
      required: false
    }
    },
    data () {
        return {
         priorityList:[],
         CrimeList:{},
         count: 0,
         pageNumber: 1,
         storeState: store.state,
         search_item:'',
         sorter:[]
        }
        },
    created () {
          db.collection('Crime Priorities').get().then(
          querysnapshot => {
          querysnapshot.forEach (doc => {
          this.priorityList.push(doc.data())
          });
          this.CrimeList=this.priorityList[0] 
          this.crimes = this.CrimeList
          console.log(this.CrimeList)
          
          for (let crime in this.CrimeList){
            this.sorter.push([crime,this.CrimeList[crime]])
          } 
          this.sorter.sort(function(a,b){return b[1]-a[1]})
          console.log(this.sorter) 
           
        })  
        
        
    },
    methods:{ 
        updateinfo(crime,oldweight,newWeight){ 
        console.log(crime,oldweight,newWeight)
        let modref=db.collection('Crime Priorities').doc('Priorities') 
        console.log(modref) 
        let setmod= modref.set({
            [crime]:newWeight
        },{merge:true}); 
        
        /*console.log({
            [crime]:newWeight
        })*/ 
        this.$router.push({ path:"/modifypriority"}.catch(err => {}))
        },
        // FORWARD ARROW NAV
    nextPage: function (){
      if (this.pageNumber < this.pagecount) {
         this.pageNumber++;
         this.count++
         let start = this.count * this.size
          let end = start + this.size;
          this.paginatedData = this.reportList.slice(start, end)
      } else {
        this.pageNumber = this.pageNumber
      }
      },
     // BACK ARROW NAV 
    prevPage: function (){
      if (this.pageNumber > 1) {
        this.pageNumber--;
        this.count--
        let start = this.count * this.size
        let end = start + this.size;
        this.paginatedData = this.reportList.slice(start, end)
      } else {
        this.pageNumber = this.pageNumber
      }
    }
       
    },
    computed:{
        fiter_crime:function(){
            return this.CrimeList.filter(CrimeList=>{
                return CrimeList.match(this.search_item)
            });
        }
    }
} 
</script> 
<style>
#priority_Information {
padding-left: 50px;
margin-left: 50px;
}
#priority-content {
  margin-left: 230px;
  width: 100%;
}
#add-user {
  letter-spacing: 1px;
  font-size: 12px;
  color: #5C6BC0;
  text-decoration: none;
  font-weight: 600;
}
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
  #Edit_link:hover{
    text-decoration: underline;
  }
</style>