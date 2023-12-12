<template>
  <h2 class="pt-2">Коментари</h2>
  <div class="row d-flex">
    <div class="col-md-8 col-lg-6 cards scrollbar">
      <div class="outer-card card shadow-0 border" style="background-color: #f0f2f5; width: 32.9vw">
        <div class="card-body">
<!--          <div v-for="user in comments" :key="user.username">-->
<!--            <div v-for="comment in user.comments" :key="comment.text">-->
<!--              <CommentCard :username="user.username" :comment="comment.text" :rating="comment.rating"></CommentCard>-->
<!--            </div>-->
<!--          </div>-->
          <div v-for="review in this.reviews" :key="review.id">
            <CommentCard :username="review.user.username" :comment="review.comment" :rating="review.rating"></CommentCard>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CommentCard from "@/components/CommentCard";
import { computed } from "vue";
import { store } from "@/store/store";
export default {
  name: "CommentBox",
  components: { CommentCard },
  data() {
    return {
      reviews: Array,
    }
  },
  setup() {
    // TODO ako ne biva vaka zemi kako prop
    const selectedWinery = computed(() => store.selectedWinery);

    return {
      selectedWinery,
    }
  },
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      const response = await fetch("https://dians-backend.onrender.com/wineries");
      this.wineries = await response.json();
      this.wineries = JSON.parse(JSON.stringify(this.wineries))["wineries"]
      this.filteredWinery = this.wineries.filter(winery => winery.id === this.selectedWinery.id)
      this.reviews = this.filteredWinery[0].reviews
    },
  },
}
</script>

<style scoped>
  .cards {
    overflow-y: scroll;
    overflow-x: hidden;
  }

  .outer-card {
    height: 72vh;
  }

  .card-body {
    background-color: var(--primary-color);
    border-radius: 8px;
  }

  .scrollbar {
    height: 71.6vh;
    width: 98%;
    overflow-y: scroll;
    overflow-x: hidden;
    padding: 0 10px;
  }

  .scrollbar::-webkit-scrollbar {
    width: 12px;
  }

  .scrollbar::-webkit-scrollbar-track {
    border-radius: 8px;
    background-color: #e7e7e7;
    border: 1px solid #cacaca;
    box-shadow: inset 0 0 6px rgba(0, 0, 0, .3);
  }

  .scrollbar::-webkit-scrollbar-thumb {
    border-radius: 8px;
    background-color: var(--primary-color);
  }

</style>