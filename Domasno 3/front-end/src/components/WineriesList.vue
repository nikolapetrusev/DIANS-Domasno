<template v-if="!loading">
  <div class="wineries col-md-6 p-2">
    <div class="d-flex justify-content-around">
      <div class="d-flex align-items-center textDiv">
        <h5 v-if="this.selectedCity && this.selectedRating>0">Винарии - {{ this.selectedCity }} (>{{ this.selectedRating }}☆)</h5>
        <h5 v-else-if="this.selectedCity">Винарии - {{ this.selectedCity }}</h5>
        <h5 v-else-if="this.selectedRating>0">Винарии (>{{ this.selectedRating }}☆)</h5>
        <h5 v-else>Винарии</h5>
        <i class="heart fas fa-heart" @click="showFavorites" :class="{'hide' : !userLoggedIn}"></i>
      </div>
    </div>
    <div class="scrollbar">
      <div v-for="winery in filteredWineries" :key="winery.id">
        <button class="btn btn-link" type="submit" @click="getWineryPage(winery)">{{ winery.name }}</button>
      </div>
    </div>
  </div>
</template>

<script>
import { store, mutations } from '@/store/store.js'
import { computed } from 'vue'
// import json from '../assets/vinarii.json'
import router from "@/router"
export default {
  name: "WineriesList",
  data() {
    return {
      favorites: "",
    }
  },
  props: {
    wineries: Object,
  },
  setup() {
    const selectedCity = computed(() => store.selectedCity);
    const selectedRating = computed(() => store.selectedRating);

    return {
      selectedCity,
      selectedRating,
    };
  },
  computed: {
    userLoggedIn() {
      console.log(sessionStorage.getItem("loggedIn"))
      return sessionStorage.getItem("loggedIn") === "true"
    },
    filteredWineries() {
      let filtered = null;

      if(!store.selectedCity && store.selectedRating === 0) { // site vinarii
        filtered = this.wineries;
      }
      else if(store.selectedCity && store.selectedRating > 0) { // izbral i grad i rejtin
        filtered = this.wineries.filter(winery => winery.city.name === store.selectedCity && winery.rating >= store.selectedRating);
      }
      else if(store.selectedCity) { // izbral grad
        filtered = this.wineries.filter(winery => winery.city.name === store.selectedCity);
      }
      else { // izbral rejting
        filtered = this.wineries.filter(winery => winery.rating >= store.selectedRating);
      }

      if (store.favoriteClicked) {
        filtered = filtered.filter(winery => {
          for (let favorite of this.favorites) {
            if (winery.id === favorite.id) {
              return true;
            }
          }
          return false;
        });
      }

      return filtered
    },
  },
  methods: {
    async showFavorites() {
      const heartIcon = document.querySelector('.heart');
      if (heartIcon) {
        heartIcon.classList.toggle('active');
      }

      mutations.toggleFavorite();

      const requestOptions = {
        method: "GET",
        headers: {"Content-Type": "application/json", "Authorization": "Bearer " + sessionStorage.getItem("access")}
      };
      const response = await fetch(store.api_url + "/profiles/favorites/", requestOptions);
      this.favorites = await response.json();4

      this.favorites = JSON.parse(JSON.stringify(this.favorites))["favorites"]
    },
    getWineryPage(winery) {
      mutations.setSelectedWinery(winery);
      sessionStorage.setItem("selectedWinery", JSON.stringify(winery))
      router.push('/winery');
    },
  }
}
</script>

<style scoped>
  .textDiv{
    justify-content: flex-end;
    width: 85%;
    min-width: 20%;;
    gap: 33%;
  }

  .btn-link {
    text-decoration: none;
    color: black;
  }

  .btn-link:hover {
    color: var(--primary-color);
  }

  .scrollbar {
    height: 95%;
    overflow-y: scroll;
    overflow-x: hidden;
  }

  .scrollbar::-webkit-scrollbar {
    width: .8rem;
  }

  .scrollbar::-webkit-scrollbar-track {
    border-radius: 8px;
    background-color: var(--secondary-color);
    border: 1px solid #cacaca;
    box-shadow: inset 0 0 6px rgba(0, 0, 0, .3);
  }

  .scrollbar::-webkit-scrollbar-thumb {
    border-radius: 8px;
    background-color: var(--primary-color);
  }

  .heart {
    font-size: 25px;
    color: darkgray;
  }

  .active {
    color: var(--primary-color)!important;
  }

  .hide{
    visibility: hidden;
  }
</style>