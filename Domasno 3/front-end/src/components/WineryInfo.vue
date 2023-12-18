<template>
  <div class="left1">
    <div class="d-flex justify-content-start align-items-center gap-5">
      <div class="d-flex align-items-center justify-content-start gap-3">
        <h2>{{ selectedWinery.name }}</h2>
        <i class="heart fas fa-heart" @click="addToFavorites" :class="{'hide' : !userLoggedIn}"></i>
      </div>
      <div class="d-flex align-items-center">
        <i class="fas fa-star mx-2 fa-xs"></i>
        <p v-if="selectedWinery.rating!=null" class="mb-0">{{ selectedWinery.rating }}</p>
        <p v-else class="mb-0">No Info</p>
      </div>
    </div>
    <h3 v-if="selectedWinery.city">{{ selectedWinery.city.name }}</h3>
    <h4 v-if="selectedWinery.address">{{ selectedWinery.address }}</h4>
    <h5 v-if="selectedWinery.work">{{ selectedWinery.work }}</h5>
    <h5 v-if="selectedWinery.phone">{{ selectedWinery.phone }}</h5>
  </div>
</template>

<script>
import { store } from '@/store/store.js'
export default {
  name: "WineryInfo",
  computed: {
    userLoggedIn() {
      return sessionStorage.getItem("loggedIn") === "true"
    },
    selectedWinery() {
      const storedWinery = sessionStorage.getItem("selectedWinery");
      return JSON.parse(storedWinery);
    }
  },
  methods: {
    async addToFavorites() {
      const heartIcon = document.querySelector('.heart');
      if (heartIcon) {
        heartIcon.classList.toggle('active');
      }

      const requestOptions = {
        method: "POST",
        headers: {"Content-Type": "application/json", "Authorization": "Bearer " + sessionStorage.getItem("access")},
        body: JSON.stringify({"winery_id":this.selectedWinery.id})
      };
      await fetch(store.api_url + "/profiles/favorites/", requestOptions);
    }
  }
}
</script>

<style scoped>
  .left1 {
    padding-top: 2rem;
    height: 18rem;
  }

  .heart {
    font-size: 25px;
    color: darkgray;
  }

  .fa-star {
    font-size: 25px;
    color: var(--accent-color);
  }

  .active {
    font-size: 25px;
    color: var(--primary-color);
  }

  .hide {
    visibility: hidden;
  }
</style>