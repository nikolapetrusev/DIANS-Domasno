<template>
  <l-map :center="center" :zoom="zoom">
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
    wineries: Object,
  },
  data() {
    return {
      latitude: String,
      longitude: String,
      splitCoordinates: [],
    }
  },
  computed: {
    customMarkerIcon() {
      return new L.Icon({
        iconUrl: require('@/assets/markerImg.png'),
        iconSize: [160, 100]
      })
    },
    filteredWineries() {
      let filtered = null;
      if(!store.selectedCity && store.selectedRating === 0) {
        filtered = this.wineries;
      }
      else if(store.selectedCity && store.selectedRating > 0) {
        filtered = this.wineries.filter(winery => winery.city.name === store.selectedCity && winery.rating >= store.selectedRating);
      }
      else if(store.selectedCity) {
        filtered = this.wineries.filter(winery => winery.city.name === store.selectedCity);
      }
      else {
        filtered = this.wineries.filter(winery => winery.rating >= store.selectedRating);
      }

      if(store.favoriteClicked) {
        filtered = filtered.filter(winery => sessionStorage.getItem("favorites").includes(winery))
      }

      return filtered
    },
  },
  mounted() {
    this.getCoordinates();
  },
  methods: {
    getCoordinates() {
      for (let winery of this.filteredWineries) {
        if(winery["coords"]) {
          const latitude = parseFloat(winery.coords.latitude);
          const longitude = parseFloat(winery.coords.longitude);
          this.splitCoordinates.push([latitude, longitude])
        }
      }
    },
  }
}
</script>

<style scoped>

</style>