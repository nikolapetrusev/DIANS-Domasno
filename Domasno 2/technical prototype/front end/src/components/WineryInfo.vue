<template>
  <div class="left1">
    <div class="d-flex justify-content-start align-items-center gap-5">
      <div class="d-flex align-items-center justify-content-start gap-3">
        <h2>{{ selectedWinery.name }}</h2>
        <i class="heart fas fa-heart" @click="e => e.target.classList.toggle('active')"></i>
      </div>
      <div class="d-flex align-items-center">
        <i class="fas fa-star mx-2 fa-xs"></i>
        <p v-if="selectedWinery.ocena" class="mb-0">{{ selectedWinery.ocena }}</p>
        <p v-else class="mb-0">no info</p>
      </div>
    </div>
    <h3 v-if="selectedWinery.mesto">{{ selectedWinery.mesto }}</h3>
    <h4 v-if="selectedWinery.adresa">{{ selectedWinery.adresa }}</h4>
    <h5 v-if="selectedWinery.rab_vreme">{{ selectedWinery.rab_vreme }}</h5>
    <h5 v-if="selectedWinery.tel_br">{{ selectedWinery.tel_br }}</h5>
  </div>
</template>

<script>
import { store } from '@/store/store.js'
import {computed} from "vue";
export default {
  name: "WineryInfo",
  setup() {
    const selectedWinery = computed(() => store.selectedWinery);
    return {
      selectedWinery,
    };
  },
}
</script>

<style scoped>
  .left1 {
    padding-top: 2rem;
    height: 18rem;
  }

  .heart {
    font-size: 25px;
    color: darkgray;
  }

  .fa-star {
    font-size: 25px;
    color: var(--accent-color);
  }

  .active {
    font-size: 25px;
    color: var(--primary-color);
  }
</style>