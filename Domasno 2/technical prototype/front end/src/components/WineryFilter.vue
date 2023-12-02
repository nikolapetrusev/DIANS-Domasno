<template>
  <div class="filters col-md-3 p-2">
    <div class="d-flex justify-content-around align-items-center">
      <form @submit="selectRating">
        <div class="d-flex gap-4 align-items-center">
          <div class="field">
            <label for="rating">Филтрирај според оцена</label>
            <input type="text" v-model="rating" id="rating" class="form-control-sm" placeholder="Внесете оцена"/>
          </div>
          <button type="submit" class="btn btn-block btn-sm">Примени</button>
        </div>
      </form>
      <button type="submit" class="btn" @click="clearRating">✖</button>
    </div>
    <div class="bottom">
      <div class="cityFilter d-flex align-items-center">
        <h6>Филтрирај според град</h6>
        <button type="submit" class="btn" @click="clearCity">✖</button>
      </div>
      <div class="scrollbar">
        <div v-for="city in allCities" :key="city">
          <button type="submit" class="btn btn-link" @click="selectCity(city)">{{ city }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import json from '../assets/vinarii.json'
import { mutations } from '../store/store.js'
export default {
  name: "HomeFilter",
  data() {
    return {
      wineries: json,
      userRating: 0
    }
  },
  computed: {
    allCities() {
      const cities = new Set();
      this.wineries.forEach(winery => cities.add(winery.mesto));
      return Array.from(cities);
    }
  },
  methods: {
    selectCity(city) {
      mutations.setSelectedCity(city);
    },
    selectRating() {
      mutations.setSelectedRating(this.rating);
    },
    clearRating() {
      mutations.setSelectedRating(0);
    },
    clearCity() {
      mutations.setSelectedCity(0)
    }
  }
}
</script>

<style scoped>
  .field {
    display: flex;
    flex-direction: column;
  }

  .cityFilter {
    gap: 8rem;
  }

  label {
    font-weight: 500;
    line-height: 1.2;
  }

  .bottom {
    border-top: 1px solid black;
    margin-top: .5rem;
    padding-top: .5rem;
  }

  .btn {
    color: var(--secondary-color);
  }

  .btn-link {
    color: black;
    text-decoration: none;
  }

  .btn-link:hover {
    color: var(--primary-color);
  }

  .btn-sm {
    height: 10%;
    margin-left: .5rem;
    background-color: var(--primary-color);
    color: white;
  }

  .btn-sm:hover {
    background-color: var(--secondary-color);
    border: 1px solid var(--primary-color);
    color: var(--primary-color);
  }

  .form-control-sm {
    border: 1px solid lightgrey;
  }

  .scrollbar {
    height: 28.5rem;
    overflow-y: scroll;
    overflow-x: hidden;
  }

  .scrollbar::-webkit-scrollbar {
    width: 12px;
  }

  .scrollbar::-webkit-scrollbar-track {
    border-radius: 8px;
    background-color: var(--secondary-color);
    border: 1px solid #cacaca;
    box-shadow: inset 0 0 6px rgba(0, 0, 0, .3);
  }

  .scrollbar::-webkit-scrollbar-thumb {
    border-radius: 8px;
    background-color: var(--primary-color);
  }
</style>