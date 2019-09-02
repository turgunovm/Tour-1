<template>
  <div id="app">
    <!-- <div class="card" v-for="note in notes" :key="note.id">
      <div class="card-header">
        <img :src="note.tour_img" alt />
       
        <button class="btn btn-clear float-right" ></button>
        <div class="card-title"></div>
        <div class="card-subtitle">{{ convertDateToTimeAgo(note.created_at) }}</div>
      </div>
      <div class="card-body"></div>
    </div> -->
    <b-container fluid class="bv-example-row">
      <b-row>
        <b-col sm="3" v-for="note in notes" :key="note.id">
          <b-link href="#">
            <b-card title=""
                overlay
                border-variant="primary"
                :img-src="note.tour_img" 
                img-alt="Image" 
                img-top 
                tag="article"
                text-variant="white"
                class="my-2"
                variant="dark"
                bg-variant="dark">
                
                  <b-card-text center text-variant="white">
                    {{note.name}}
                    </b-card-text>
                    <b-card-text>
                    <!-- {{ note.description }} -->
                    <!-- {{ note.price }} -->
                    </b-card-text>
                      <!-- <div class="card-subtitle">{{ convertDateToTimeAgo(note.created_at) }}</div> -->
                    <b-button
                            lg=2
                            squared 
                            href="#"
                            variant="outline-primary" 
                            @click="deleteNote(note)"
                            >
                            Exit
                    </b-button>
                    <b-button
                            lg=2
                            squared 
                            href="#"
                            variant="outline-primary" 
                            
                            :to="{name:'note',params:{id:note.id}}"
                            >
                            Detail
                    </b-button>
                
          </b-card>
          </b-link>
          
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>


<script>
  import {
    mapGetters
  } from "vuex";
  import prettydate from "pretty-date";
  export default {
    name: "note-list",
    computed: mapGetters(["notes"]),
    methods: {
      convertDateToTimeAgo(date) {
        return prettydate.format(new Date(date));
      },
      deleteNote(note) {
        console.log(this.notes);
        this.$store.dispatch("deleteNote", note);
      }
    },
    beforeMount() {
      this.$store.dispatch("getNotes");
    }
  };

</script>

<style>
  header {
    margin-top: 50px;
  }

</style>
