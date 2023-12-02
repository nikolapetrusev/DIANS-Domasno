<template>
  <div class="main">
    <div class="d-flex justify-content-around align-items-center">
      <HomeFilter></HomeFilter>
      <WineriesList></WineriesList>
      <div class="map col-md-3 text-center">
        <img :src="mapImg" alt="Map Image">
      </div>
    </div>
  </div>
</template>

<script>
import HomeFilter from "@/components/WineryFilter";
import WineriesList from "@/components/WineriesList";
import mapImg from "@/assets/mapImage.png";
export default {
  name: "HomePage",
  components: {WineriesList, HomeFilter},
  data() {
    return {
      mapImg: mapImg
    }
  }
}
</script>

<style scoped>
  .filters, .wineries, .map{
    background-color: var(--secondary-color);
    height: 36rem;
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }

  .filters{
    width: 24%;
  }

  .wineries {
    width: 29%;
  }

  .map {
    width: 43%;
  }

  .main {
    padding-top: .5rem;
  }

  img {
    width: 100%;
    height: 100%;
  }
</style>