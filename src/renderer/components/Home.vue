<template>

<div class="center">
    <h1>{{ name }}</h1>

    <!-- <button @click="temp()">
        test
    </button> -->

    <Test/>
    

</div>
    
</template>


<script>
import Test from './Test';
export default{ 

   data:function () {
    return {
      name: "jorda"
    }
  },
  components: {Test},
   methods:{
       temp(){
           let myNotification = new Notification('Title', {
           body: 'Lorem Ipsum Dolor Sit Amet'
})

       }
   },
   computed:{
       test(){
           return this.name;
       }
   }
}
</script>


<style scoped>

.center{
    display: flex; 
    justify-content: center;
    align-items: center;
    
    
}

</style>

