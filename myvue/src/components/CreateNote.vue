<template>
   <div>
    <b-form @submit="onSubmit" @reset="submitForm" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Email address:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="email"
          type="email"
          required
          placeholder="Enter email"
        ></b-form-input>
      </b-form-group>
      <b-button variant="primary">Save</b-button>
    </b-form>
    <!-- <form class="form-horizontal" @submit="submitForm">
        <div class="form-group">
            <div class="col-3"><label class="form-label">Title</label></div>
            <div class="col-9"><input class="form-input" type="text" v-model="title" placeholder="Type note title..." /></div>
        </div>
        <div class="form-group">
            <div class="col-3"><label class="form-label">Body</label></div>
            <div class="col-9"><textarea class="form-input" v-model="body" rows="8" placeholder="Type your note..."></textarea></div>
        </div>
        
            <v-btn small dark color="primary">Create</v-btn>
        
    </form> -->
  </div>
</template>

<script>
export default {
  name: 'create-note',
  data () {
    return {
      'title': '',
      'body': '',
       show: true,
       email: ''
    }
  },
  methods: {
    submitForm (event) {
      this.createNote()
      this.title = ''
      this.body = ''
      event.preventDefault()
    },
    createNote () {
      this.$store.dispatch('createNote', { title: this.title, body: this.body })
    }
  }
}
</script>
