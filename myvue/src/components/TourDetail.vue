<template>
    <div >
      <b-card-text 
              text-variant="info"
              variant="warning"
              >
              Tour Detail:
              </b-card-text>
      <b-container>
          <b-card title=""
                border-variant="dark"
                :img-src="tour.tour_img" 
                img-alt="Image" 
                img-center 
                tag="article"
                text-variant="white"
                class="my-2"
                variant="dark"
                bg-variant="primary">
                  <b-card-text center text-variant="white">
                    {{tour.name}}
                    </b-card-text>
                    <b-card-text>
                    {{ tour.description }}
                    {{ tour.price }}
                    </b-card-text>
                      <!-- <div class="card-subtitle">{{ convertDateToTimeAgo(tour_id.created_at) }}</div> -->
                    

          </b-card>
      </b-container>
    
         <!-- <task-detail :tour="tour"></task-detail> -->
    </div>
</template>
<script>
 import TaskDetails from './TaskDetails'
import {mapGetters} from "vuex";
export default {
    name :'tour-detail',
    props:['id'],
   
   computed:{
      ...mapGetters({
        tours: 'notes'
        }),
    tour(){
        return this.tours.find(t => t.id == this.id)
        }
    },
    
    components:{
     'tasl-detail': TaskDetails
    },
    updated(){
      setInterval(() => {
      this.tour()
      }, 1000)
    }
    // beforeMount(){
    //     this.$store.dispatch("getNodes")
    // }
 }
</script>
<style scoped>

</style>