<template>
    <div>
        <main> 
            <div id="gazaform">
                <AdduserForm></AdduserForm>
                <Allusersidebar></Allusersidebar>
            </div>
        </main>
    </div>
</template> 
<script>
import AdduserForm from './forms/Adduser'
import Allusersidebar from './sidebar/Allusersidebar'
export default {
    name: 'Adduser-page',
    components: { AdduserForm,  Allusersidebar },
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
    background-color: #F8F9F9;
    display: flex;
    flex-direction: row;
    width: 100%;
    height:100%;
  }

</style>