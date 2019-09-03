<template>
    <div>
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
                    {{ tour.description }}
                    {{ tour.price }}
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
                            
                            :to="{name:'note',params:{id:note.id}}"
                            >
                            Detail2
                    </b-button>

          </b-card>
    </div>
</template>
import {mapGetters} from "vuex";
export default {
   name:'tour-details',
   props:['tour']
  computed: mapGetters(["notes"]),
   beforeMount() {
      this.$store.dispatch("getNotes");
    }
}
</script>