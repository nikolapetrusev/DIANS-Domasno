<template>
  <div class="d-flex gap-5 justify-content-end pb-2 pe-3">
    <i class="fas fa-pen"></i>
    <i class="fas fa-trash"></i>
  </div>
  <CommentCard :username="username" :comment="comment" :rating="rating"></CommentCard>
</template>

<script>
import CommentCard from "@/components/CommentCard";
export default {
  name: "ProfileComment",
  components: {CommentCard},
  props: {
    username: String,
    comment: String,
    rating: Number,
  }
}
</script>

<style scoped>
  .card {
    background-color: white;
  }

  i {
    color: var(--primary-color);
  }
</style>