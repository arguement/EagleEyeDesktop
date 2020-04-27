<template>
    <div>
        <main>
            <div id="gaza-content">
                <Alluserscontent></Alluserscontent>
            </div>
        </main>   
    </div>
</template> 
<script>
import Alluserscontent from './content/Alluserscontent'
export default { 
    name: 'Allusers',
    components: { Alluserscontent},
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      }
    }
    
}
</script> 

<style> /*
  @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro');

  * {
    margin: 0;
    padding: 0;
  }

  body { font-family: 'Source Sans Pro', sans-serif; }

  #gaza-content {
    display: flex;
    flex-direction: row;
  }

*/
</style>