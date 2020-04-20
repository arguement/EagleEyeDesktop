<template>
    <div>
        <main>
            <div id="gaza-content">
                <Allusercontent></Allusercontent>
            </div>
        </main>   
    </div>
</template> 
<script>
import Alluserscontent from './content/Alluserscontent'
export default { 
    name: 'Allusercontent-page',
    components: { reportSidebar, reportSidebarContent },
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
    margin: 0;
    padding: 0;
  }

  body { font-family: 'Source Sans Pro', sans-serif; }

  #gazaform {
    display: flex;
    flex-direction: row;
  }

</style>