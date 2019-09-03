<template>
    <div>
         <b-card title=""
                overlay
                border-variant="primary"
                :img-src="tour_id.tour_img" 
                img-alt="Image" 
                img-top 
                tag="article"
                text-variant="white"
                class="my-2"
                variant="dark"
                bg-variant="dark">
                
                  <b-card-text center text-variant="white">
                    {{tour_id.name}}
                    </b-card-text>
                    <b-card-text>
                    {{ tour_id.description }}
                    {{ tour_id.price }}
                    </b-card-text>
                      <!-- <div class="card-subtitle">{{ convertDateToTimeAgo(tour_id.created_at) }}</div> -->
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
                            
                            :to="{name:'note',params:{id:note.id}}"
                            >
                            Detail2
                    </b-button>

          </b-card>
    </div>
</template>
<script>
 import TaskDetails from './TaskDetails'
 import {mapGetters} from "vuex";
export default {
    name :'tour-detail',
    props:['tour_id'],
   data(){
      
   },
    computed: mapGetters(["notes"]),
    components:{
        TaskDetails
    },
    beforeMount(){
        this.$store.dispatch("detailNotes", {id:this.id});
    }
 }
</script>
<style scoped>

</style>