<template> 
<div>
    <main>
    <h3>Priority List</h3> 
    <div id="user_Information">
         <table  class="table table-borderless" style="border-collapse:separate; border-spacing:0 3px; margin-top:-3px;">
           
             <th scope="col"></th>
             <th scope="col">Crime</th>
             <th scope="col">Priority</th>
             <th scope="col">New Priority</th>
             
           
           <tbody>
            <tr id="table-data" v-for="(crimepriority,index) in CrimeList" :key='crimepriority[index]' > 
              <th scope="row" >
                <div  class="form-group form-check">
                  <input  type="checkbox" class="form-check-input" id="exampleCheck1">
                </div>
              </th> 
            <td>{{index}}</td>
            <td>{{crimepriority}}</td> 
            <td>
                <select v-model='newWeight' class="form-control" id="formrole" placeholder=crimepriority>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                </select>
            </td> 
            <td><button v-on:click="updateinfo(index,crimepriority,newWeight)"  class="btn btn-primary" id="Edit-button" >Update</button></td>
             </tr>
           </tbody>
         </table>
       </div>
    </main>
</div>
</template> 
<script> 
import {db} from '../../../../../static/js/fire_config' 
import {store} from "../../../store/store"
import navbar from '../../navbar/navbar'
export default {
    props:{},
    data () {
        return {
         priorityList:[],
         CrimeList:[],

        }
        },
    created () {
          db.collection('Crime Priorities').get().then(
          querysnapshot => {
          querysnapshot.forEach (doc => {
          this.priorityList.push(doc.data())
          });

          console.log(this.priorityList[0])
          this.CrimeList=this.priorityList[0] 
          
        })  
        this.CrimeList.sort()
        
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

        this.$router.push({ path:"/modifypriority"})
        }
       
    }
} 
</script> 
<style>

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