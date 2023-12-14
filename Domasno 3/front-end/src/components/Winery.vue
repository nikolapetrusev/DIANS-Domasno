<template>
  <div class="container">
    <div class="row">
      <div class="col-md-7 flex-column left">
        <WineryInfo></WineryInfo>
        <AddComment></AddComment>
      </div>
      <div class="right col-md-5">
        <CommentBox :selectedWinery="selectedWinery"></CommentBox>
      </div>
    </div>
  </div>
</template>

<script>
// import { ref } from 'vue';
import AddComment from "@/components/AddComment";
import CommentBox from "@/components/CommentBox";
import WineryInfo from "@/components/WineryInfo";
// import {store} from "@/store/store";
export default {
  name: "WineryComponent",
  data() {
    return {
      wineries: "",
      selectedWinery: sessionStorage.getItem("selectedWinery"),
    }
  },
  components: {
    WineryInfo,
    CommentBox,
    AddComment
  },
  // computed: {
  //   selectedWinery() {
  //     const storedWinery = sessionStorage.getItem("selectedWinery");
  //     console.log(this.wineries.filter(winery => winery.id === storedWinery.id))
  //     const winery = this.wineries.filter(winery => winery.id === storedWinery.id)
  //     sessionStorage.setItem("selectedWinery", winery)
  //     return winery
  //   }
  // },
  mounted() {
    // this.fetchWineries();
  },
  methods: {
    // async fetchWineries() {
    //   const response = await fetch(store.api_url + "/wineries");
    //   this.wineries = await response.json();
    //   this.wineries = JSON.parse(JSON.stringify(this.wineries))["wineries"];
    //
    //   const storedWinery = JSON.parse(sessionStorage.getItem("selectedWinery"));
    //   const winery = this.wineries.filter(winery => winery.id === storedWinery.id)[0]
    //   sessionStorage.setItem("selectedWinery", JSON.stringify(winery))
    //
    //   console.log(winery)
    //   console.log(JSON.stringify(winery.reviews))
    //   sessionStorage.setItem("selectedWineryReviews", JSON.stringify(winery.reviews))
    // },
  }
}
</script>

<style scoped>
  .row {
    margin-right: 1rem;
    height: 100%;
  }

  .container {
    margin: 1rem 5rem;
    width: 100vw;
    height: 85vh;
  }

  .left {
    padding-left: 2rem;
    width:55%;
    height: 93%;
    margin-right: 2rem;
  }

  .right {
    width:  42%;
    height: 93%;
    background-color: var(--secondary-color);
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }
</style>