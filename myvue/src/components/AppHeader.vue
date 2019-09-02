<template>
  <div>
      <b-navbar toggleable="lg" text-variant="white" variant="warning">
        <b-navbar-brand href="#"><strong>World-Tour</strong> </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
           
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item href="#">Link</b-nav-item>
          </b-navbar-nav>
            
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav>
              <b-nav-item active>Active</b-nav-item>
              <b-nav-item>Home</b-nav-item>
              <b-nav-item>About</b-nav-item>
              <b-nav-item>Services</b-nav-item>
              <b-nav-item>Hot Tour</b-nav-item>
            </b-nav>
            <b-nav-item-dropdown text="Lang" right>
              <b-dropdown-item href="#">EN</b-dropdown-item>
              <b-dropdown-item href="#">ES</b-dropdown-item>
              <b-dropdown-item href="#">RU</b-dropdown-item>
              <b-dropdown-item href="#">FA</b-dropdown-item>
            </b-nav-item-dropdown>

            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <template slot="button-content"><em>User</em></template>
              <b-dropdown-item href="#">Profile</b-dropdown-item>
              <b-dropdown-item href="#">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>
            <b-button variant="outline-primary" squared  href="#">Sing In</b-button>
            <!-- <b-nav-form>
              <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
              <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
            </b-nav-form> -->

            
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
      <b-carousel
                  id="carousel-fade"
                  style="text-shadow: 0px 0px 2px #000"
                  fade
                  indicators
                  img-width="1024"
                  img-height="480"
                >
          <b-carousel-slide
            caption="First slide"
            img-src="https://picsum.photos/1024/480/?image=10"
          ></b-carousel-slide>
          <b-carousel-slide
            caption="Second Slide"
            img-src="https://picsum.photos/1024/480/?image=12"
          ></b-carousel-slide>
          <b-carousel-slide
            caption="Third Slide"
            img-src="https://picsum.photos/1024/480/?image=22"
          ></b-carousel-slide>
        </b-carousel>

    </div>
</template>

<script>
export default {
  name: 'app-header',
  data(){
    return {
      message: 'Hello Vue'
    }
  }
}
</script>