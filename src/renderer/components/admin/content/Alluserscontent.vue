<template>
   <div id="allusercontent"> 
       <router-view></router-view>
      <h1 id="report-label">REPORTS</h1> 
        <div id="user_Information">
            
       </div>
   </div>
</template> 
<script>
import {db} from '../../../../../static/js/fire_config'
export default {
    data () {
        return {
            Users : []
        }
    }, 
    created () {
        db.collection('User').get().then(
            querysnapshot => {
                querysnapshot.forEach (doc => {
                    console.log(doc.data())
                    const data ={
                        
                    }
                })
            }
        )
    } 

}
</script>