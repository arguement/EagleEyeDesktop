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
//import Allusersidebar from './sidebar/Allusersidebar'
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