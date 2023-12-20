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
    selectedCity() {
      return store.selectedCity;
    },
    selectedRating() {
      return store.selectedRating;
    },
    customMarkerIcon() {
      return new L.Icon({
        iconUrl: require('@/assets/markerImg.png'),
        iconSize: [160, 100]
      })
    },
  },
  mounted() {
    this.getCoordinates();
  },
  methods: {
    getCoordinates() {
      for (let winery of this.wineries) {
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