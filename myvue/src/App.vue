<template>
  <div id="app" variant="dark">
      <app-header></app-header>
        <b-container>
            <b-flex class="columns">
                    
                    
                    <create-note></create-note>
                   
                     <note-list></note-list> 
                <router-link to="/header">Header</router-link>
            </b-flex>
        </b-container>
      
  </div>
  
</template>

<script>
import CreateNote from './components/CreateNote'
import NoteList from './components/NoteList'
import AppHeader from './components/AppHeader'
export default {
  name: 'app',
  components: {
    'create-note': CreateNote,
    'note-list': NoteList,
    'app-header':AppHeader
  }
}
</script>

<style>
  #app{
    background-color:black;
  }
</style>
