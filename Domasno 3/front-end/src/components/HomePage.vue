<template>
<!--  <AppHeader></AppHeader>-->
  <div class="main d-flex justify-content-center align-items-center">
    <div class="cont d-flex justify-content-around align-items-center gap-2">
      <WineryFilter :wineries="wineries"></WineryFilter>
      <WineriesList :wineries="wineries"></WineriesList>
      <div class="map col-md-3 text-center">
        <HomePageMap class="map" :center="[latitude, longitude]" :zoom="zoom" :wineries="wineries"></HomePageMap>
      </div>
    </div>
  </div>
<!--  <AppFooter></AppFooter>-->
</template>

<script>
import WineryFilter from "@/components/WineryFilter";
import WineriesList from "@/components/WineriesList";
import HomePageMap from "@/components/HomePageMap";
// import AppHeader from "@/components/Header";
// import AppFooter from "@/components/Footer";
import mapImg from "@/assets/mapImage.png";
import {store} from "@/store/store";
export default {
  name: "HomePage",
  components: {
    WineriesList,
    WineryFilter,
    HomePageMap,
    // AppHeader,
    // AppFooter
  },
  data() {
    return {
      wineries: store.wineries,
      mapImg: mapImg,
      latitude: 41.6086,
      longitude: 21.7453,
      zoom: 8,
    }
  },
  // mounted() {
  //   this.fetchWineries()
  // },
  // created() {
  //   const fetchWineries = async ()  => {
  //     const response = await fetch(store.api_url + "/wineries");
  //     this.wineries = await response.json();
  //     this.wineries = JSON.parse(JSON.stringify(this.wineries))["wineries"];
  //   }
  //   fetchWineries();
  // },
  methods: {
    // async fetchWineries() {
    //   const response = await fetch(store.api_url + "/wineries");
    //   this.wineries = await response.json();
    //   this.wineries = JSON.parse(JSON.stringify(this.wineries))["wineries"];
    // },
    // smeni tuka za da poceka da se zemat pod
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