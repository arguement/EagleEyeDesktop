<template>
    <div>
        <main>
            <div >
               <ModifyPriority></ModifyPriority>
            </div>
        </main>   
    </div>
</template> 
<script>
import ModifyPriority from './content/modifyprioritycontent' 
//import Allusersidebar from './sidebar/Allusersidebar'
export default { 
    name: 'ModifyPrioritypage',
    components: {ModifyPriority},
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      }
    }
    
}
</script> 