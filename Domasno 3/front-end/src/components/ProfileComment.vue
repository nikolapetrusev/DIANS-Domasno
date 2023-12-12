<template>
  <div class="d-flex gap-2 justify-content-end pb-2 pe-3">
    <button class="btn" @click="editComment"><i class="fas fa-pen"></i></button>
    <button class="btn" @click="deleteComment"><i class="fas fa-trash"></i></button>
  </div>
  <div v-if="!isEditing">
    <CommentCard :username="username" :comment="comment" :rating="rating"></CommentCard>
  </div>
  <div v-else>
    <EditableComment :username="username" :comment="comment" :rating="rating" :id="id"></EditableComment>
  </div>
</template>

<script>
import CommentCard from "@/components/CommentCard";
import EditableComment from "@/components/EditableComment";
export default {
  name: "ProfileComment",
  components: {EditableComment, CommentCard },
  data() {
    return {
      isEditing: false,
    }
  },
  props: {
    username: String,
    comment: String,
    rating: Number,
    id: Number,
  },
  methods: {
    editComment() {
      this.isEditing = !this.isEditing
    },
    deleteComment() {
      //TODO implement
    },
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