<template>
  <div class="main d-flex justify-content-center align-items-center">
    <div class="cont d-flex justify-content-around align-items-center gap-2">
      <WineryFilter :wineries="wineries"></WineryFilter>
      <WineriesList :wineries="wineries"></WineriesList>
      <div class="map col-md-3 text-center">
        <HomePageMap class="map" :center="[latitude, longitude]" :zoom="zoom" :wineries="wineries"></HomePageMap>
      </div>
    </div>
  </div>
</template>

<script>
import WineryFilter from "@/components/WineryFilter";
import WineriesList from "@/components/WineriesList";
import HomePageMap from "@/components/HomePageMap";
import mapImg from "@/assets/mapImage.png";
export default {
  name: "HomePage",
  components: {WineriesList, WineryFilter, HomePageMap},
  data() {
    return {
      wineries: "",
      mapImg: mapImg,
      latitude: 41.6086,
      longitude: 21.7453,
      zoom: 8,
    }
  },
  mounted() {
    this.fetchWineries()
  },
  methods: {
    async fetchWineries() {
      const response = await fetch("https://dians-backend.onrender.com/wineries");
      this.wineries = await response.json();
      this.wineries = JSON.parse(JSON.stringify(this.wineries))["wineries"];
    },
  }
}
</script>

<style scoped>
  .main {
    padding: .6rem .5rem;
    height: 87.5vh;
    width: 100vw;
    margin-top: -1rem;
  }

  .cont {
    flex: 1 1 100%;
  }

  .filters, .wineries, .map{
    background-color: var(--secondary-color);
    height: 81vh;
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }

  .filters {
    flex: 1 1 25rem;
  }

  .wineries {
    flex: 1 1 28rem;
  }

  .map {
    flex: 1 1 41rem;
  }
</style>