<template>
    <div id="add-user-form">
        <router-view></router-view> 

        <!-- NAVBAR -->
       <nav id="adduser-nav" class="navbar navbar-expand-lg navbar-light bg-light">
          <li class="navbar-brand">
            <h1 id="report-label">NEW USER</h1>
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


        <ul id="add-user-nav" class="nav">
            <li class="nav-item">
              <div id="report-arrow">
                  <router-link to="/allusers" class="nav-link" >
                  <div id="back">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
                     back </div>
                  </router-link>
              </div>
            </li>
          </ul>


       <div id="adduser_form"> 
           <form class="adduser">
            <div class="form-group">
                <label class="label">FIRST NAME</label>
                <input  v-model="FirstName" type="Text" class="form-control" id ="new-user-form"> 
            </div>    
            <div class="form-group">
                <label class="label">LAST NAME</label>
                <input v-model="LastName" type="Text" class="form-control" id ="new-user-form"> 
            </div>   
            <div class="form-group">
                <label class="label">ID NUMBER</label>
                <input  v-model="IdNumber" type="Text" class="form-control" id ="new-user-form"> 
            </div>   
            <div class="form-group">
                <label class="label">PASSWORD</label>
                <input v-model="Password" type="Text" class="form-control" id ="new-user-form"> 
            </div>  
            <div class="form-group">
                <label class="label">ROLE</label>
                <select  v-model="Role" class="form-control" id="new-user-form">
                    <option value="admin">Administrator</option>
                    <option value="user">User</option>
                </select>
            </div>        
            <button v-on:click="Adduser()" type="submit" class="btn btn-primary" id="login-button" >ADD USER</button>
          </form>
       </div>
    </div>
</template> 
<script> 
import {db} from '../../../../../static/js/fire_config'
import {store} from "../../../store/store"
export default {
    props:{},
    methods:{
    Adduser: function () {
        let FirstName = this.FirstName
        let LastName = this.LastName
        let IdNumber = this.IdNumber
        let Password=this.Password
        let role = this.Role 
        console.log("gaza")
        console.log(role) 
        db.collection("User").add({
          "first-name" : FirstName,
          "id-number" : IdNumber,
          "password" : Password,
          "role" : role,
          "surname" : LastName,
        })  
        this.$router.push({ path:"/allusers"})

    }
    },
    data () {
      return {
      electron: process.versions.electron,
      name: this.$route.name,
      node: process.versions.node,
      path: this.$route.path,
      platform: require('os').platform(),
      vue: require('vue/package.json').version,
      storeState: store.state
    }
    }
};

</script> 
<style>
#back, #back:hover{
  font-size: 12px;
  color: #566573;
  letter-spacing: 1px;
}

#add-user-nav {
  padding-left: 50px;
  padding-top: 40px;
}

#add-user-form {
  background-color: #F8F9F9;
  width: 100%;
  height: 100vh;
  margin-left: 230px;
}

.errors {
  color: red;
  margin-left: 10px;
}

#forgot-text {
  margin-top: 10px;
  letter-spacing: 1px;
  font-size: 10px;
  color: black;
}

#forgot {
  text-decoration: none;
}


#welcome {
  text-align: center;
  letter-spacing: 4px;
}

#logo-stuff {
  display: flex;
  flex-direction: row;
}

#adduser-nav {
    height: 50px;
    margin: 20px;
    margin-right: 50px;
    margin-left: 50px;
    letter-spacing: 1px;
    }

#adduser_form {
  width: 70%;
  padding-left: 100px;
  padding-top: 50px;
}

form {
  width: 400px;
}

#login-form-label {
  margin-top: 40px;
  text-align: center;
  letter-spacing: 1px;
  font-size: 15px;
  font-weight: 400;
  margin-bottom: 40px;
  color: #ABB2B9;
}

.label {
  font-size: 10px;
  letter-spacing: 1px;
  font-weight: 600;
  color: #85929E;
  display: flex;
  flex-direction: row;
}

#input-password,#input-id {
border: none;
border-radius: 4px;
height: 40px;
font-size: 12px;
letter-spacing: 1px;
font-weight: 500;
color: #ABB2B9;
background-color: #F2F3F4 ;
}

#login-button {
  margin-top: 8px;
  height: 45px;
  width: 100%;
  background-color: #7986CB;
  border: none;
  border-radius: 4px;
  color: white;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 2px
}

#login-button:hover {
  margin: 3px 0px;
  background-color: #5C6BC0;
  box-shadow: 21px 27px 54px -30px rgba(0,0,0,0.75);
}

#new-user-form {
  border: none;
  border-radius: 4px;
  height: 40px;
  font-size: 12px;
  letter-spacing: 1px;
  font-weight: 500;
  color: #ABB2B9;
  background: #E5E7E9;
}

</style>