<template>
  <l-map v-if="splitCoordinates.length > 0" :center="center" :zoom="zoom">
    <l-tile-layer
        url="https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png"
        attribution='<a href="https://stadiamaps.com/">Stadia Maps</a>'
    ></l-tile-layer>
    <l-marker v-for="coordinates in splitCoordinates" :key="coordinates[0]" :lat-lng="coordinates" :icon="customMarkerIcon"></l-marker>
  </l-map>
</template>

<script>
import 'leaflet/dist/leaflet.css'
import L from 'leaflet'
import { LMap, LTileLayer, LMarker } from '@vue-leaflet/vue-leaflet'
import { store } from "@/store/store";
export default {
  name: 'StadiaMap',
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  props: {
    // wineries: Object,
  },
  data() {
    return {
      latitude: String,
      longitude: String,
      splitCoordinates: [],
    }
  },
  watch: {
    filteredWineries: 'getCoordinates',
  },
  computed: {
    customMarkerIcon() {
      return new L.Icon({
        iconUrl: require('@/assets/markerImg.png'),
        iconSize: [160, 100]
      })
    },
  },
  mounted() {
    this.getCoordinates()
  },
  methods: {
    // TODO so ako tuka praam fetch na podatocite i posle nekako so .then presmetam splitCoordinates
    // getCoordinates() {
    //   // console.log(this.filteredWineries)
    //
    //   for (let winery of this.filteredWineries) {
    //     if(winery["coords"]) {
    //       const latitude = parseFloat(winery.coords.latitude);
    //       const longitude = parseFloat(winery.coords.longitude);
    //       this.splitCoordinates.push([latitude, longitude])
    //     }
    //   }
    //
    //   // console.log(this.splitCoordinates)
    // }

    async getCoordinates() {
      const response = await fetch("https://dians-backend.onrender.com/wineries");
      this.wineries = await response.json();
      this.wineries = JSON.parse(JSON.stringify(this.wineries))["wineries"];

      this.wineries = this.filterWineries(this.wineries)

      for (let winery of this.wineries) {
        if (winery["coords"]) {
          const latitude = parseFloat(winery.coords.latitude);
          const longitude = parseFloat(winery.coords.longitude);
          this.splitCoordinates.push([latitude, longitude])
        }
      }

      console.log(this.splitCoordinates)
    },
    filterWineries(wineries) {
      let filtered = null;
      if(!store.selectedCity && store.selectedRating === 0) { // site vinarii
        filtered = wineries;
      }
      else if(store.selectedCity && store.selectedRating > 0) { // izbral i grad i rejtin
        filtered = wineries.filter(winery => winery.city.name === store.selectedCity && winery.rating >= store.selectedRating);
      }
      else if(store.selectedCity) { // izbral grad
        filtered = wineries.filter(winery => winery.city.name === store.selectedCity);
      }
      else { // izbral rejting
        filtered = wineries.filter(winery => winery.rating >= store.selectedRating);
      }

      // if(store.favoriteClicked) {
      //   filtered = filtered.filter(winery => favorites.includes(winery))
      // }

      return filtered
    }
  }
}
</script>

<style scoped>

</style>