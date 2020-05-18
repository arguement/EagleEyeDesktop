<template>
    <div>
        <main>
            <div id="gaza-content">
              <prioritySidebar></prioritySidebar>
              <ModifyPriority></ModifyPriority>
            </div>
        </main>   
    </div>
</template> 
<script>
import prioritySidebar from './sidebar/prioritySidebar'
import ModifyPriority from './content/modifyprioritycontent' 
export default { 
    name: 'ModifyPrioritypage',
    components: { ModifyPriority, prioritySidebar},
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