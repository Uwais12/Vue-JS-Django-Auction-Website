<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <!-- <a class="navbar-brand" href="#">Navbar</a> -->
      <!-- <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor02"
        aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button> -->
      <div class="navCont" id="navbarColor02">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <router-view>
          <li class="nav-link">
            <RouterLink to="/profile">Profile</RouterLink>
          </li>
          <li class="nav-link">

            <RouterLink to="/shop">Shop</RouterLink>
          </li>
          <li class="nav-link">

            <a href="http://localhost:8000/logout">Logout</a>
          </li>
          </router-view>
          <!-- <router-link to="/login" class="nav-link">Profile</router-link> -->
          </li>
        </ul>
        <div style="width: 100%; display: flex; align-items: center;  padding-right: 1em; justify-content: end;"
          class="">
          <h1 style="color: white;" class="">Auction Site</h1>
          <!-- <button class="btn btn-secondary my-2 my-sm-0" type="submit">Filter items</button> -->
        </div>
      </div>
    </nav>
    <!-- route outlet -->
    <!-- component matched by the route will render here -->
    <router-view></router-view>
  </div>
</template>

<script lang="ts">

type Product = {
  id: number;
  title: string;
  description: string;
  picture: string;
  starting_price: number;
  finish_date: number;
}

export default {
  // need to pass the props properly and it should be fine
  props: ["product_title"],

  data() {
    return {
      search: '',
      products: [] as Product[],
    };
  },

  mounted() {
    let script1 = document.createElement('script')
    script1.setAttribute('src', 'https://unpkg.com/vue@3')
    document.head.appendChild(script1)

    let script2 = document.createElement('script')
    script2.setAttribute('src', 'https://unpkg.com/vue-router@4')
    document.head.appendChild(script2)
  },

  methods: {

    filteredList() {
      return this.products.filter(product => {
        return product.title.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  }
}
</script>