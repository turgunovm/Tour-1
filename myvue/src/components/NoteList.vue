<template>
    <div id="app2">
      
     <b-container fluid class="bv-example-row">
      
      <b-row>
        <b-col sm="3" v-for="tour in tours" :key="tour.id">
          <b-link href="#">
            <b-card title=""
                overlay
                border-variant="primary"
                :img-src="tour.tour_img" 
                img-alt="Image" 
                img-top 
                tag="article"
                text-variant="white"
                class="my-2"
                variant="dark"
                bg-variant="dark">
                
                  <b-card-text center text-variant="white">
                    {{tour.name}}
                    </b-card-text>
                    <b-card-text>
                    <!-- {{ tour.description }} -->
                    <!-- {{ tour.price }} -->
                    </b-card-text>
                      <!-- <div class="card-subtitle">{{ convertDateToTimeAgo(tour.created_at) }}</div> -->
                    <b-button
                            lg=2
                            squared 
                            href="#"
                            variant="outline-primary" 
                            @click="deleteNote(tour)"
                            >
                            Exit
                    </b-button>
                    <b-button
                            lg=2
                            squared 
                            href="#"
                            variant="outline-primary"
                            :to="{name:'tourdetail',params:{id:tour.id}}"
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
  import {mapGetters} from "vuex";
  import prettydate from "pretty-date";
  export default {
    name: "note-list",
    computed:{
      ...mapGetters({
        tours: 'notes'
        }),
    },
    
    methods: {
      convertDateToTimeAgo(date) {
        return prettydate.format(new Date(date));
      },
      deleteNote(note) {
        console.log(this.notes);
        this.$store.dispatch("deleteNote", note);
      },
      // detailNote(id) {
      //   console.log(this.id);
      //   this.$store.dispatch("detailNote", id);
      //   this.$router.push({ path: `/detail/${this.id}` })

      // }
    },
    beforeMount() {
      this.$store.dispatch("getNotes");
      // this.deleteNote()
    }
  };

</script>

<style>
  header {
    margin-top: 50px;
  }

</style>
