<template>
  <div class="wineries col-md-6 p-2">
    <div class="d-flex justify-content-around">
      <div class="d-flex align-items-center textDiv">
        <h5 v-if="this.selectedCity && this.selectedRating>0">Винарии - {{ this.selectedCity }} (>{{ this.selectedRating }}☆)</h5>
        <h5 v-else-if="this.selectedCity">Винарии - {{ this.selectedCity }}</h5>
        <h5 v-else-if="this.selectedRating>0">Винарии (>{{ this.selectedRating }}☆)</h5>
        <h5 v-else>Винарии</h5>
        <i class="heart fas fa-heart" @click="e => e.target.classList.toggle('active')"></i>
      </div>
    </div>
    <div class="scrollbar">
      <div v-for="winery in filteredWineries" :key="winery.name">
        <button class="btn btn-link" type="submit" @click="getWineryPage(winery)">{{ winery.name }}</button>
      </div>
    </div>
  </div>
</template>

<script>
import json from '../assets/vinarii.json'
import { store, mutations } from '@/store/store.js'
import { computed } from 'vue'
import router from "@/router"
export default {
  name: "WineriesList",
  data() {
    return {
      wineries: json
    }
  },
  setup() {
    // Use ref for reactive properties
    const selectedCity = computed(() => store.selectedCity);
    const selectedRating = computed(() => store.selectedRating);

    return {
      selectedCity,
      selectedRating,
    };
  },
  computed: {
    filteredWineries() {
      if(!store.selectedCity && store.selectedRating === 0) {
        return this.wineries;
      }
      if(!store.selectedCity) {
        return this.wineries.filter(winery => winery.ocena >= store.selectedRating);
      }
      return this.wineries.filter(winery => winery.mesto === store.selectedCity && winery.ocena >= store.selectedRating);
    }
  },
  methods: {
    getWineryPage(winery) {
      mutations.setSelectedWinery(winery);
      router.push('/winery');
    },
    clearFilters() {
      mutations.setSelectedCity(null);
      mutations.setSelectedRating(0);
    },
  }
}
</script>

<style scoped>
  .textDiv{
    justify-content: flex-end;
    width: 85%;
    gap: 7rem;
  }

  .btn-link {
    text-decoration: none;
    color: black;
  }

  .btn-link:hover {
    color: var(--primary-color);
  }

  .scrollbar {
    height: 33rem;
    overflow-y: scroll;
    overflow-x: hidden;
  }

  .scrollbar::-webkit-scrollbar {
    width: 12px;
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
</style>