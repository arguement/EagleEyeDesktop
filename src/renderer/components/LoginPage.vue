<template>
  <main>
  <div id="login-page">
    
    <loginForm id="the-form"></loginForm>

    <div id="shape">
      <div class='wave -one'></div>
          <div class='wave -two'></div>
          <div class='wave -three'></div>
    </div>
  </div>
  </main>
</template>

<script>
  import loginForm from './forms/loginForm'

  export default {
    name: 'login-page',
    components: { loginForm },
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      }
    }
  }
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro');

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body { font-family: 'Source Sans Pro', sans-serif; }

#the-form {
    z-index: 1; /* Sit on top */
    top: 0;
    right: 0;
    background-color: transparent!important;
    overflow-x: hidden
}

  #login-page {
    /* background-color:; */
    height: 100vh;
    width: 100vw;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

  #shape {
    z-index: -1;
  position: fixed;
  top: 0;
  transform: rotate(85deg); 
  left: 0;

  }

  .wave {
  position: absolute;
  opacity: .4;
  width: 2000px;
  height: 1300px;
  margin-left: -150px;
  margin-top: -250px;
  border-radius: 43%;
}

@keyframes rotate {
  from { transform: rotate(0deg); }
  from { transform: rotate(180deg); }
}

.wave.-one {
  animation: rotate 7000ms infinite linear;
  opacity: .1;
  background: #9FA8DA;
}

.wave.-two {
  animation: rotate 3000ms infinite linear;
  opacity: .1;
  background: #3F51B5  ;
}

.wave.-three {
  animation: rotate 7500ms infinite linear;
  background-color: #E8EAF6;
}
</style>
