<template>
  <div class="left1">
    <div class="d-flex justify-content-start align-items-center gap-5">
      <div class="d-flex align-items-center justify-content-start gap-3">
        <h2>{{ selectedWinery.name }}</h2>
        <i class="heart fas fa-heart" @click="addToFavorites"></i>
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
import { computed } from "vue";
export default {
  name: "WineryInfo",
  setup() {
    // TODO ako ne biva vaka zemi kako prop
    const selectedWinery = computed(() => store.selectedWinery);

    return {
      selectedWinery,
    }
  },
  methods: {
    async addToFavorites() {
      // TODO tuka dava 500 internal server error
      const heartIcon = document.querySelector('.heart');
      if (heartIcon) {
        heartIcon.classList.toggle('active');
      }

      const requestOptions = {
        method: "POST",
        headers: {"Content-Type": "application/json", "Authorization": "Bearer " + sessionStorage.getItem("access")},
        body: JSON.stringify({"winery_id":this.selectedWinery.id})
      };
      await fetch("https://dians-backend.onrender.com/profiles/favorites/", requestOptions);
      console.log("success")
      // const response = await fetch("http://192.168.43.158:8000/profiles/favorites/", requestOptions);
      //
      // if (response.status === 200) {
      //   // const data = await response.json();
      //   // sessionStorage.setItem("access", data.access);
      //   // sessionStorage.setItem("refresh", data.refresh);
      //   // Vue.http.headers.common['Authorization'] = 'Bearer ' + data.token;
      //   // router.push('/');
      // } else {
      //   console.log('Error:', response.status);
      // }
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
</style>