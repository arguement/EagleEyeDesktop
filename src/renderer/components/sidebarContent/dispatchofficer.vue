<template>
 <div> 
     <h3>Dispatch page</h3>
    </div>   
</template> 
<script>
import {store} from "../../store/store"
import navbar from '../navbar/navbar'
import {db} from '../../../../static/js/fire_config'
export default {
    data(){ 
        return{
        officers:[],
    }
    },
    created (){
        db.collection('Police Officer').get().then(
          querysnapshot => {
          querysnapshot.forEach (doc => {
          this.officers.push(doc.data())
          }); 
          console.log(this.officers) 
          }) 

          
    }
}
</script>