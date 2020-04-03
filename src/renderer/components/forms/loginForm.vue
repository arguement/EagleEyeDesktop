<template>
  <div>
    <router-view></router-view>
    <h1 id="login-form-label">Log in to your account.</h1>
    <form>
  <div class="form-group">
    <label class="label" for="exampleInputEmail1">ID NUMBER</label>
    <input type="email" class="form-control" id="input-email" aria-describedby="emailHelp">
  </div>
  <div class="form-group">
    <label class="label" for="exampleInputPassword1">PASSWORD</label>
    <input type="password" class="form-control" id="input-password">
  </div>
  <router-link
  to="/home"
  >
  <button type="submit" class="btn btn-primary" id="login-button" href="/home">SUBMIT</button>
  </router-link>
</form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      electron: process.versions.electron,
      name: this.$route.name,
      node: process.versions.node,
      path: this.$route.path,
      platform: require('os').platform(),
      vue: require('vue/package.json').version
    }
  }
}
</script>

<style>
form {
  width: 400px;
}

#login-form-label {
font-size: 30px;
font-weight: 800;
}

.label {
  font-size: 11px;
  letter-spacing: 1px;
  font-weight: 600;
  color: #566573;
}

#input-password,#input-email {
border: none;
border-radius: 4px;
background:#F2F3F4;
height: 50px;
font-size: 14px;
letter-spacing: 1px;
font-weight: 600;
color: #ABB2B9;
}

#login-button {
  height: 50px;
  width: 100%;
  background-color: #3F51B5;
  border: none;
  border-radius: 4px;
  color: white;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 2px
}
</style>