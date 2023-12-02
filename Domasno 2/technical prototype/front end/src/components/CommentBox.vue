<template>
  <h2 class="pt-2">Коментари</h2>
  <div class="row d-flex">
    <div class="col-md-8 col-lg-6 cards scrollbar">
      <div class="card shadow-0 border" style="background-color: #f0f2f5; width: 32.9vw">
        <div class="card-body">
          <div v-for="user in comments" :key="user.username">
            <div v-for="comment in user.comments" :key="comment.text">
              <CommentCard :username="user.username" :comment="comment.text" :rating="comment.rating"></CommentCard>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import json from '../assets/comments.json'
import CommentCard from "@/components/CommentCard";
export default {
  name: "CommentBox",
  components: {CommentCard},
  data() {
    return {
      comments: json,
    }
  }
}
</script>

<style scoped>
  .cards {
    overflow-y: scroll;
    overflow-x: hidden;
  }

  .card-body {
    background-color: var(--primary-color);
    border-radius: 8px;
  }

  .scrollbar {
    height: 71.6vh;
    width: 35vw;
    overflow: auto;
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