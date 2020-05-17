<template>
    <div>
        <main>
            <div >
              <MpSidebar></MpSidebar>
              <ModifyPriority></ModifyPriority> 
               
            </div>
        </main>   
    </div>
</template> 
<script>
import ModifyPriority from './content/modifyprioritycontent' 
import  MpSidebar from './sidebar/modifyprioritySidebar'
export default { 
    name: 'ModifyPrioritypage',
    components: {ModifyPriority,MpSidebar},
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

  #report-page {
    background-color: #F8F9F9;
    display: flex;
    flex-direction: row;
    width: 100%;
    height:100%;
  }
  
</style>