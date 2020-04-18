<template>
    <div>
        <router-view></router-view> 
        <nav id="adduser-nav" class="navbar navbar-expand-lg navbar-light bg-light">
          <li id="logo-stuff" class="navbar-brand">
           <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="black" width="18px" height="18px"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M12 4C7 4 2.73 7.11 1 11.5 2.73 15.89 7 19 12 19s9.27-3.11 11-7.5C21.27 7.11 17 4 12 4zm0 12.5c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>
           <h1 id="logo-eye">EAGLE EYE</h1>
          </li>
       </nav> 
       <div id="adduser_form"> 
           <form class="adduser">
            <h1> Add New User</h1> 
            <div class="form-group">
                <label class="label">FirstName
                <input v-model="input.FirstName" type="Text" class="form-control" id ="Firstname"> 
            </div>    
            <div class="form-group">
                <label class="label">LastName
                <input v-model="input.LastName" type="Text" class="form-control" id ="Lastname"> 
            </div>   
            <div class="form-group">
                <label class="label">Id Number
                <input v-model="input.idnumber" type="Text" class="form-control" id ="idnumber"> 
            </div>   
            <div class="form-group">
                <label class="label">Password
                <input v-model="input.Password" type="Text" class="form-control" id ="password"> 
            </div>  
            <div class="form-group">
                <label class="label">Role
                <select v-model="input.Role" class="form-control" id="role">
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
import {db} from '../../../../static/js/fire_config'
export default {
    props:{},
    methods:{
    Adduser: function () {
        let FirstName = this.input.FirstName
        let LastName = this.input.LastName
        let IdNumber = this.input.IdNumber
        let role = this.input.Role
    }
    }
};

</script> 
<style>
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
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    top: 0;
    right: 0;
    background-color: transparent!important;
    overflow-x: hidden; /* Disable horizontal scroll */
    transition: 0.5s;
    width: 100%;
    height: 70px;
    padding-left: 50px;
    }

#logo-eye {
  font-size: 10px;
  letter-spacing: 1px;
  font-weight: 300;
  margin-top: 1.5px;
  margin-left: 10px;
}

#adduser_form {
  width: 50%;
}

form {
  width: 400px;
  margin-left: auto;
  margin-right: auto;
}

#login-form-label {
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

</style>